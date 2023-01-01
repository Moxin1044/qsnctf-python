import hashlib
import hmac


def md5(input_string):
    # MD5
    m = hashlib.md5()
    # 将输入字符串转换为字节并计算散列值
    m.update(input_string.encode())
    # 输出散列值
    return m.hexdigest()


def sha512(input_string):
    # SHA256
    m = hashlib.sha512()
    # 将输入字符串转换为字节并计算散列值
    m.update(input_string.encode())
    # 输出散列值
    return m.hexdigest()


def sha384(input_string):
    # SHA384
    m = hashlib.sha384()
    # 将输入字符串转换为字节并计算散列值
    m.update(input_string.encode())
    # 输出散列值
    return m.hexdigest()


def sha256(input_string):
    # 创建一个SHA-256对象
    m = hashlib.sha256()
    # 将输入字符串转换为字节并计算散列值
    m.update(input_string.encode())
    # 输出散列值
    return m.hexdigest()


def sha224(input_string):
    # SHA224
    m = hashlib.sha224()
    # 将输入字符串转换为字节并计算散列值
    m.update(input_string.encode())
    # 输出散列值
    return m.hexdigest()


def sha1(input_string):
    # 创建一个SHA1对象
    m = hashlib.sha1()
    # 将输入字符串转换为字节并计算散列值
    m.update(input_string.encode())
    # 输出散列值
    return m.hexdigest()


def shake_128(input_string, bits):
    # 创建一个Shake128对象
    m = hashlib.new('shake_128')
    # 将输入字符串转换为字节并计算散列值
    m.update(input_string.encode())
    # 输出散列值
    return m.hexdigest(int(bits))


def shake_256(input_string, bits):
    # 创建一个Shake128对象
    m = hashlib.new('shake_256')
    # 将输入字符串转换为字节并计算散列值
    m.update(input_string.encode())
    # 输出散列值
    return m.hexdigest(int(bits))


def HMAC_SHA256_HEX(secret, data):
    # 使用 HMAC-SHA256 算法和密钥对数据进行签名
    secret = str(secret)
    data = str(data)
    signature = hmac.new(secret.encode("utf-8"), data.encode("utf-8"), hashlib.sha256).hexdigest()
    return signature


def sha3_512(input_string):
    # sha3-256
    h = hashlib.sha3_512()
    h.update(input_string.encode())
    return h.hexdigest()


def sha3_384(input_string):
    # sha3-384
    h = hashlib.sha3_384()
    h.update(input_string.encode())
    return h.hexdigest()


def sha3_256(input_string):
    # sha3-256
    h = hashlib.sha3_256()
    h.update(input_string.encode())
    return h.hexdigest()


def sha3_224(input_string):
    # sha3-224
    h = hashlib.sha3_224()
    h.update(input_string.encode())
    return h.hexdigest()