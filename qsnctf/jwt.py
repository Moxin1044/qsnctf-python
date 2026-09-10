# -*- coding: utf-8 -*-
"""JWT（JSON Web Token）解码

纯 Python 实现，不校验签名，用于 CTF 中快速查看 token 的 header / payload 内容。
"""

import base64
import json

__all__ = ['jwt_decode']


def _base64url_decode(segment):
    """base64url 解码（自动补齐 = 填充）"""
    if isinstance(segment, str):
        segment = segment.encode('utf-8')
    padding = b'=' * (-len(segment) % 4)
    return base64.urlsafe_b64decode(segment + padding)


def jwt_decode(token):
    """解码 JWT（不校验签名）

    :param token: JWT 字符串，形如 ``header.payload.signature``
    :return: 字典 ``{'header': dict, 'payload': dict, 'signature': str, 'raw': [三段原文]}``

    示例::

        >>> jwt_decode('eyJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6dHJ1ZX0.xxx')
        {'header': {'alg': 'HS256'}, 'payload': {'admin': True}, ...}
    """
    if not token or not isinstance(token, str):
        raise ValueError("token 不能为空")
    parts = token.strip().split('.')
    if len(parts) != 3:
        raise ValueError("JWT 格式错误：应为 header.payload.signature 三段")
    header_segment, payload_segment, signature_segment = parts
    try:
        header = json.loads(_base64url_decode(header_segment))
        payload = json.loads(_base64url_decode(payload_segment))
    except Exception as exc:
        raise ValueError("JWT 解码失败：%s" % exc)
    return {
        'header': header,
        'payload': payload,
        'signature': signature_segment,
        'raw': parts,
    }
