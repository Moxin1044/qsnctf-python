# -*- coding: utf-8 -*-
"""RSA 攻击套件（纯 Python 实现，覆盖 CTF 中最常见的 RSA 攻击方式）

包含：
- 基础加解密、由 p/q/e 求私钥指数
- 已知 p、q 解密；phi 已知解密
- dp 泄漏攻击
- 小公钥指数攻击（e 很小且明文较短）
- 共模攻击（同一 n、同一明文、两个互素公钥指数）
- 广播攻击 / Håstad（同一明文、相同小指数、多组互素模数）
- Wiener 攻击（私钥指数 d 过小）
- 公因子攻击（两个模数共享素因子）
- 因数分解（Pollard rho 本地 / factordb 在线）
- 整数与字节串互转（拿到 m 后还原明文）

所有攻击函数均返回整数形式的明文 m（可用 int_to_bytes 还原为文本）。
"""

import math
import time

try:
    import requests
except ImportError:
    requests = None

__all__ = [
    'rsa_encrypt', 'rsa_decrypt', 'rsa_private_exponent',
    'rsa_decrypt_with_factors', 'rsa_decrypt_with_phi', 'rsa_decrypt_with_dp',
    'rsa_small_e_attack', 'rsa_common_modulus_attack', 'rsa_broadcast_attack',
    'rsa_wiener_attack', 'rsa_shared_factor_attack', 'rsa_factor', 'rsa_factordb',
    'int_to_bytes', 'bytes_to_int',
]


# ---------------- 基础运算 ----------------

def rsa_encrypt(message, e, n):
    """RSA 加密：c = m^e mod n"""
    return pow(int(message), int(e), int(n))


def rsa_decrypt(ciphertext, d, n):
    """RSA 解密：m = c^d mod n"""
    return pow(int(ciphertext), int(d), int(n))


def rsa_private_exponent(e, p, q):
    """由 p、q、e 计算私钥指数 d = e^-1 mod φ(n)"""
    p, q, e = int(p), int(q), int(e)
    phi = (p - 1) * (q - 1)
    return pow(e, -1, phi)


def rsa_decrypt_with_factors(ciphertext, e, p, q):
    """已知 p、q（或已分解出因子）时解密，返回 m"""
    p, q, e = int(p), int(q), int(e)
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return pow(int(ciphertext), d, p * q)


def rsa_decrypt_with_phi(ciphertext, e, n, phi):
    """已知 φ(n) 时解密，返回 m"""
    d = pow(int(e), -1, int(phi))
    return pow(int(ciphertext), d, int(n))


# ---------------- 常见攻击 ----------------

def rsa_decrypt_with_dp(ciphertext, e, n, dp):
    """dp 泄漏攻击：dp ≡ d mod (p-1)，用 gcd(a^(e·dp) − a, n) 恢复 p 后解密"""
    e, n, dp = int(e), int(n), int(dp)
    p = None
    for a in range(2, 1000):
        candidate = math.gcd(pow(a, e * dp, n) - a, n)
        if 1 < candidate < n:
            p = candidate
            break
    if p is None:
        raise ValueError("dp 泄漏攻击失败：未能分解 n")
    return rsa_decrypt_with_factors(ciphertext, e, p, n // p)


def rsa_small_e_attack(ciphertext, e, n, max_k=1000000):
    """小公钥指数攻击：e 很小且明文较短（m^e < n）时直接开方

    在 c + k·n（k = 0,1,2,...）中寻找完全 e 次方数。
    """
    e, n, c = int(e), int(n), int(ciphertext)
    if e < 2:
        raise ValueError("公钥指数 e 必须大于 1")
    for k in range(max_k):
        root, exact = _perfect_nth_root(c + k * n, e)
        if exact:
            return root
    raise ValueError("小指数攻击失败：未找到完全 e 次方（可增大 max_k）")


def rsa_common_modulus_attack(ciphertext1, ciphertext2, e1, e2, n):
    """共模攻击：同一模数 n、同一明文 m，两个互素的公钥指数 e1/e2"""
    c1, c2, e1, e2, n = (int(ciphertext1), int(ciphertext2),
                         int(e1), int(e2), int(n))
    g, s1, s2 = _extended_gcd(e1, e2)
    if g != 1:
        raise ValueError("e1 与 e2 不互素，共模攻击不适用")

    def _pow_signed(base, exponent):
        if exponent < 0:
            base = pow(base, -1, n)
            exponent = -exponent
        return pow(base, exponent, n)

    return (_pow_signed(c1, s1) * _pow_signed(c2, s2)) % n


def rsa_broadcast_attack(ciphertexts, e, moduli):
    """广播攻击（Håstad）：同一明文用相同小指数 e 加密给 e 个互素模数

    :param ciphertexts: e 组密文
    :param moduli: e 个两两互素的模数
    """
    e = int(e)
    ciphertexts = [int(c) for c in ciphertexts]
    moduli = [int(m) for m in moduli]
    if len(ciphertexts) != e or len(moduli) != e:
        raise ValueError("广播攻击需要收齐 %d 组密文与模数" % e)
    combined, _ = _crt(ciphertexts, moduli)
    root, exact = _integer_nth_root(combined, e)
    if not exact:
        raise ValueError("广播攻击失败：CRT 结果不是完全 e 次方")
    return root


def rsa_wiener_attack(e, n):
    """Wiener 攻击（d 过小）：连分数逼近 e/n，返回 (d, p, q)"""
    e, n = int(e), int(n)
    for k, d in _convergents(_continued_fraction(e, n)):
        if k == 0 or (e * d - 1) % k:
            continue
        phi = (e * d - 1) // k
        summary = n - phi + 1
        discriminant = summary * summary - 4 * n
        if discriminant < 0:
            continue
        root, exact = _integer_sqrt(discriminant)
        if not exact or (summary + root) % 2:
            continue
        p, q = (summary + root) // 2, (summary - root) // 2
        if p * q == n:
            return d, p, q
    raise ValueError("Wiener 攻击失败：d 不满足小解密指数条件")


def rsa_shared_factor_attack(n1, n2):
    """公因子攻击：两个模数共享素因子，返回 (p, q1, q2)

    p 为公共素因子，q1 = n1 // p、q2 = n2 // p。
    """
    n1, n2 = int(n1), int(n2)
    p = math.gcd(n1, n2)
    if p in (1, n1, n2):
        raise ValueError("两个模数无公共素因子")
    return p, n1 // p, n2 // p


# ---------------- 因数分解 ----------------

def rsa_factor(n, timeout=10):
    """本地因数分解（Pollard rho），返回 (p, q)"""
    n = int(n)
    if n < 4:
        raise ValueError("n 过小，无需分解")
    factor = _pollard_rho(n, timeout)
    return factor, n // factor


def rsa_factordb(n, timeout=15):
    """在线因数分解（factordb.com），返回素因子列表，需要可选依赖 requests"""
    if requests is None:
        raise ImportError("rsa_factordb 需要可选依赖 'requests'")
    response = requests.get("http://factordb.com/api",
                            params={"query": int(n)}, timeout=timeout)
    response.raise_for_status()
    data = response.json()
    factors = []
    for base, exponent in data.get("factors", []):
        factors.extend([int(base)] * int(exponent))
    if data.get("status") != "FF" or len(factors) < 2:
        raise ValueError("factordb 未给出完整分解（status=%s）" % data.get("status"))
    return factors


# ---------------- 整数 / 字节串 ----------------

def int_to_bytes(value, length=None, byteorder='big'):
    """整数 → 字节串（RSA 得到 m 后还原明文用）"""
    value = int(value)
    if length is None:
        length = max(1, (value.bit_length() + 7) // 8)
    return value.to_bytes(length, byteorder)


def bytes_to_int(data, byteorder='big'):
    """字节串 → 整数"""
    if isinstance(data, str):
        data = data.encode()
    return int.from_bytes(data, byteorder)


# ---------------- 内部工具 ----------------

def _extended_gcd(a, b):
    """扩展欧几里得：返回 (gcd, x, y) 使 a·x + b·y = gcd"""
    old_r, r = int(a), int(b)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t


def _integer_nth_root(value, degree):
    """整数 n 次方根（牛顿迭代）：返回 (floor(root), 是否整除)"""
    value, degree = int(value), int(degree)
    if value < 0:
        raise ValueError("仅支持非负整数开方")
    if degree < 1:
        raise ValueError("次方数必须大于 0")
    if value < 2 or degree == 1:
        return value, True
    x = 1 << ((value.bit_length() + degree - 1) // degree)   # 上界起点
    while True:
        y = ((degree - 1) * x + value // x ** (degree - 1)) // degree
        if y >= x:
            break
        x = y
    while (x + 1) ** degree <= value:
        x += 1
    return x, x ** degree == value


def _perfect_nth_root(value, degree):
    """快速判断完全 n 次方：返回 (root, True) 或 (None, False)"""
    value, degree = int(value), int(degree)
    if value < 0:
        return None, False
    if value < 2:
        return value, True
    if value.bit_length() <= 1023:           # 浮点可安全表示时先做快速判断
        estimate = int(round(value ** (1.0 / degree)))
        if estimate > 0 and estimate ** degree == value:
            return estimate, True
    # 浮点精度不足时用整数牛顿迭代兜底
    root, exact = _integer_nth_root(value, degree)
    return (root, True) if exact else (None, False)


def _integer_sqrt(value):
    """整数平方根：返回 (floor(sqrt), 是否整除)"""
    value = int(value)
    if value < 0:
        raise ValueError("负数没有整数平方根")
    root = math.isqrt(value)
    return root, root * root == value


def _continued_fraction(numerator, denominator):
    """连分数展开系数列表"""
    coefficients = []
    numerator, denominator = int(numerator), int(denominator)
    while denominator:
        quotient = numerator // denominator
        coefficients.append(quotient)
        numerator, denominator = denominator, numerator - quotient * denominator
    return coefficients


def _convergents(coefficients):
    """由连分数系数生成渐近分数 (分子, 分母)"""
    if not coefficients:
        return
    h_prev, h = 1, coefficients[0]
    k_prev, k = 0, 1
    yield h, k
    for coefficient in coefficients[1:]:
        h_prev, h = h, coefficient * h + h_prev
        k_prev, k = k, coefficient * k + k_prev
        yield h, k


def _crt(remainders, moduli):
    """中国剩余定理：返回 (解, 模数乘积)"""
    total = 1
    for modulus in moduli:
        total *= modulus
    result = 0
    for remainder, modulus in zip(remainders, moduli):
        partial = total // modulus
        result += remainder * partial * pow(partial, -1, modulus)
    return result % total, total


def _pollard_rho(n, timeout=10):
    """Pollard rho（Brent 变体）求 n 的一个非平凡因子"""
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    deadline = time.monotonic() + max(timeout, 0.1)
    constant = 1
    while time.monotonic() < deadline:
        x = y = 2
        divisor = 1
        while divisor == 1:
            x = (x * x + constant) % n
            y = (y * y + constant) % n
            y = (y * y + constant) % n
            divisor = math.gcd(abs(x - y), n)
            if time.monotonic() > deadline:
                break
        if divisor != n:
            return divisor
        constant += 1
    raise TimeoutError("因数分解超时，可增大 timeout 或改用 rsa_factordb()")
