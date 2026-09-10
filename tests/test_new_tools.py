# -*- coding: utf-8 -*-
"""新增工具测试: 时间戳/IP 转换、RSA 攻击套件、JWT 解码、EXIF 读取

全程离线。EXIF 测试在缺少 Pillow 时自动跳过。
"""
import base64
import json
import os
import tempfile
import unittest

import qsnctf
from qsnctf import jwt as jwt_module
from qsnctf import misc, rsa


class TimestampTests(unittest.TestCase):
    """时间戳 ↔ 日期转换"""

    def test_seconds_to_date(self):
        self.assertEqual(misc.timestamp_to_date(1700000000), '2023-11-15 06:13:20')

    def test_utc_timezone(self):
        self.assertEqual(misc.timestamp_to_date(1700000000, timezone=0),
                         '2023-11-14 22:13:20')

    def test_auto_detect_milliseconds_and_microseconds(self):
        self.assertEqual(misc.timestamp_to_date(1700000000000), '2023-11-15 06:13:20')
        self.assertEqual(misc.timestamp_to_date(1700000000000000), '2023-11-15 06:13:20')

    def test_explicit_unit(self):
        self.assertEqual(misc.timestamp_to_date(1700000000000, unit='ms'),
                         '2023-11-15 06:13:20')

    def test_custom_format(self):
        self.assertEqual(misc.timestamp_to_date(1700000000, fmt='%Y/%m/%d'), '2023/11/15')

    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            misc.timestamp_to_date(1700000000, unit='minute')

    def test_date_to_seconds(self):
        self.assertEqual(misc.date_to_timestamp('2023-11-15 06:13:20'), 1700000000)

    def test_date_to_milliseconds(self):
        self.assertEqual(misc.date_to_timestamp('2023-11-15 06:13:20', unit='ms'),
                         1700000000000)

    def test_auto_format_detection(self):
        for text in ('2023-11-15 06:13:20', '2023-11-15', '2023/11/15', '20231115'):
            self.assertEqual(misc.date_to_timestamp(text, timezone=8),
                             1699977600 if text in ('2023-11-15', '2023/11/15', '20231115')
                             else 1700000000)

    def test_round_trip(self):
        self.assertEqual(misc.date_to_timestamp(misc.timestamp_to_date(1700000000)),
                         1700000000)

    def test_unparsable_date(self):
        with self.assertRaises(ValueError):
            misc.date_to_timestamp('not-a-date')

    def test_exported_at_top_level(self):
        self.assertIs(qsnctf.timestamp_to_date, misc.timestamp_to_date)
        self.assertIs(qsnctf.date_to_timestamp, misc.date_to_timestamp)


class IpConvertTests(unittest.TestCase):
    """IP ↔ 整数转换"""

    def test_ipv4_to_int(self):
        self.assertEqual(misc.ip_to_int('192.168.1.1'), 3232235777)

    def test_int_to_ipv4(self):
        self.assertEqual(misc.int_to_ip(3232235777), '192.168.1.1')

    def test_ipv4_round_trip(self):
        for address in ('0.0.0.0', '127.0.0.1', '8.8.8.8', '255.255.255.255'):
            self.assertEqual(misc.int_to_ip(misc.ip_to_int(address)), address)

    def test_ipv6_round_trip(self):
        for address in ('::1', '2001:db8::1', 'fe80::1'):
            self.assertEqual(misc.int_to_ip(misc.ip_to_int(address), version=6), address)

    def test_int_to_ip_auto_version(self):
        # 大于 2^32 自动判定为 IPv6
        self.assertEqual(misc.int_to_ip(misc.ip_to_int('2001:db8::1')), '2001:db8::1')

    def test_invalid_version(self):
        with self.assertRaises(ValueError):
            misc.int_to_ip(1, version=5)

    def test_strips_whitespace(self):
        self.assertEqual(misc.ip_to_int(' 10.0.0.1 '), misc.ip_to_int('10.0.0.1'))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            misc.ip_to_int('999.1.1.1')
        with self.assertRaises(ValueError):
            misc.int_to_ip(-1)


class RsaAttackTests(unittest.TestCase):
    """RSA 攻击套件（使用小整数密钥，便于精确断言）"""

    def test_basic_encrypt_decrypt(self):
        p, q, e, m = 61, 53, 17, 65          # 经典示例: n=3233, c=2790
        n = p * q
        d = rsa.rsa_private_exponent(e, p, q)
        self.assertEqual((e * d) % ((p - 1) * (q - 1)), 1)   # d 为 e 模 φ(n) 的逆元
        ciphertext = rsa.rsa_encrypt(m, e, n)
        self.assertEqual(ciphertext, 2790)
        self.assertEqual(rsa.rsa_decrypt(ciphertext, d, n), m)

    def test_decrypt_with_factors(self):
        p, q, e, m = 61, 53, 17, 65
        ciphertext = rsa.rsa_encrypt(m, e, p * q)
        self.assertEqual(rsa.rsa_decrypt_with_factors(ciphertext, e, p, q), m)

    def test_decrypt_with_phi(self):
        p, q, e, m = 61, 53, 17, 65
        n = p * q
        ciphertext = rsa.rsa_encrypt(m, e, n)
        self.assertEqual(rsa.rsa_decrypt_with_phi(ciphertext, e, n, (p - 1) * (q - 1)), m)

    def test_dp_leak_attack(self):
        p, q, e = 1000003, 1000033, 65537
        n = p * q
        d = rsa.rsa_private_exponent(e, p, q)
        dp = d % (p - 1)
        m = 123456789
        self.assertEqual(rsa.rsa_decrypt_with_dp(rsa.rsa_encrypt(m, e, n), e, n, dp), m)

    def test_small_e_attack(self):
        e, m = 3, 12345678901234567890
        n = m ** 3 + 7                              # m^3 < n, k=0 即可开方
        self.assertEqual(rsa.rsa_small_e_attack(rsa.rsa_encrypt(m, e, n), e, n), m)

    def test_small_e_attack_with_k_offset(self):
        # m^3 略大于 n，需要 k>0 的情形
        e, m, n = 3, 100, 999983
        self.assertEqual(rsa.rsa_small_e_attack(rsa.rsa_encrypt(m, e, n), e, n), m)

    def test_common_modulus_attack(self):
        p, q, m = 61, 53, 65
        n = p * q
        e1, e2 = 17, 13
        c1 = rsa.rsa_encrypt(m, e1, n)
        c2 = rsa.rsa_encrypt(m, e2, n)
        self.assertEqual(rsa.rsa_common_modulus_attack(c1, c2, e1, e2, n), m)

    def test_broadcast_attack(self):
        e, m = 3, 42
        moduli = [61 * 53, 17 * 19, 23 * 29]
        ciphertexts = [rsa.rsa_encrypt(m, e, n) for n in moduli]
        self.assertEqual(rsa.rsa_broadcast_attack(ciphertexts, e, moduli), m)

    def test_wiener_attack(self):
        p, q = 1000003, 1000033
        n = p * q
        phi = (p - 1) * (q - 1)
        d = 5                                        # 极小的私钥指数
        e = pow(d, -1, phi)
        recovered_d, recovered_p, recovered_q = rsa.rsa_wiener_attack(e, n)
        self.assertEqual(recovered_d, d)
        self.assertEqual({recovered_p, recovered_q}, {p, q})

    def test_shared_factor_attack(self):
        n1, n2 = 61 * 53, 61 * 59
        p, q1, q2 = rsa.rsa_shared_factor_attack(n1, n2)
        self.assertEqual(p, 61)
        self.assertEqual(q1, 53)
        self.assertEqual(q2, 59)

    def test_factor(self):
        self.assertEqual(set(rsa.rsa_factor(3233)), {53, 61})
        self.assertEqual(set(rsa.rsa_factor(1000003 * 1000033)), {1000003, 1000033})

    def test_int_bytes_conversion(self):
        self.assertEqual(rsa.int_to_bytes(0x666c6167), b'flag')
        self.assertEqual(rsa.bytes_to_int(b'flag'), 0x666c6167)
        self.assertEqual(rsa.int_to_bytes(0).decode('latin-1'), '\x00')

    def test_attack_returns_decodable_plaintext(self):
        # 端到端: 加密 'flag' → 攻击 → 还原文本
        p, q, e = 1000003, 1000033, 65537
        n = p * q
        plaintext = rsa.bytes_to_int(b'flag')
        ciphertext = rsa.rsa_encrypt(plaintext, e, n)
        recovered = rsa.rsa_decrypt_with_factors(ciphertext, e, p, q)
        self.assertEqual(rsa.int_to_bytes(recovered).decode(), 'flag')

    def test_common_modulus_rejects_non_coprime(self):
        with self.assertRaises(ValueError):
            rsa.rsa_common_modulus_attack(1, 1, 6, 9, 3233)

    def test_shared_factor_rejects_coprime(self):
        with self.assertRaises(ValueError):
            rsa.rsa_shared_factor_attack(3233, 3599 + 1)

    def test_exported_at_top_level(self):
        self.assertIs(qsnctf.rsa_wiener_attack, rsa.rsa_wiener_attack)
        self.assertIs(qsnctf.jwt_decode, jwt_module.jwt_decode)


class JwtDecodeTests(unittest.TestCase):
    """JWT 解码"""

    @staticmethod
    def _b64(data):
        return base64.urlsafe_b64encode(json.dumps(data).encode()).rstrip(b'=').decode()

    def test_decode_header_and_payload(self):
        token = '.'.join([
            self._b64({'alg': 'HS256', 'typ': 'JWT'}),
            self._b64({'admin': True, 'user': 'moxin', 'exp': 1700000000}),
            'signature-part',
        ])
        result = qsnctf.jwt_decode(token)
        self.assertEqual(result['header'], {'alg': 'HS256', 'typ': 'JWT'})
        self.assertEqual(result['payload']['user'], 'moxin')
        self.assertTrue(result['payload']['admin'])
        self.assertEqual(result['signature'], 'signature-part')

    def test_handles_padding_variants(self):
        # 构造 base64url 长度需要补 '=' 的 payload
        payload = self._b64({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
        token = '.'.join([self._b64({'alg': 'none'}), payload, ''])
        self.assertEqual(qsnctf.jwt_decode(token)['payload'],
                         {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

    def test_rejects_malformed_token(self):
        for bad in ('', 'only.two', 'a.b.c.d', 'not-base64.@@@.sig'):
            with self.assertRaises(ValueError):
                qsnctf.jwt_decode(bad)

    def test_rejects_non_string(self):
        with self.assertRaises(ValueError):
            qsnctf.jwt_decode(None)


class ExifReadTests(unittest.TestCase):
    """EXIF 读取（无 Pillow 时跳过）"""

    def setUp(self):
        try:
            from PIL import Image
        except ImportError:
            self.skipTest("未安装 Pillow，跳过 EXIF 测试")
        self.Image = Image

    def test_read_exif_tags(self):
        from qsnctf import image as image_module
        handle, path = tempfile.mkstemp(suffix='.jpg')
        os.close(handle)
        try:
            picture = self.Image.new('RGB', (8, 8), 'white')
            exif = self.Image.Exif()
            exif[271] = 'TestMake'      # Make
            exif[272] = 'TestModel'     # Model
            exif[274] = 1               # Orientation
            picture.save(path, exif=exif)
            result = image_module.exif_read(path)
            self.assertEqual(result.get('Make'), 'TestMake')
            self.assertEqual(result.get('Model'), 'TestModel')
            self.assertEqual(result.get('Orientation'), 1)
        finally:
            os.unlink(path)

    def test_image_without_exif(self):
        from qsnctf import image as image_module
        handle, path = tempfile.mkstemp(suffix='.png')
        os.close(handle)
        try:
            self.Image.new('RGB', (4, 4), 'black').save(path)
            self.assertEqual(image_module.exif_read(path), {})
        finally:
            os.unlink(path)

    def test_exported_at_top_level(self):
        from qsnctf import image as image_module
        self.assertIs(qsnctf.exif_read, image_module.exif_read)


if __name__ == '__main__':
    unittest.main()
