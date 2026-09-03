# -*- coding: utf-8 -*-
"""纯 Python 实现的 JS 相关编解码器 (替代 execjs/exejs 执行)

- aaencode / aadecode : AAEncode 颜文字编码 (原 aaencode.js)
- jsfuck_encode       : JSFuck 编码 (原 jsfuck_encode.js 0.4.0 算法移植)

jsfuck_decode 需要执行 JS (eval), 无法纯 Python 实现, 保留 exejs 可选依赖。
"""
import re

# ============ AAEncode ============

_AA_B = [
    "(c^_^o)", "(ﾟΘﾟ)", "((o^_^o) - (ﾟΘﾟ))", "(o^_^o)", "(ﾟｰﾟ)",
    "((ﾟｰﾟ) + (ﾟΘﾟ))", "((o^_^o) +(o^_^o))", "((ﾟｰﾟ) + (o^_^o))",
    "((ﾟｰﾟ) + (ﾟｰﾟ))", "((ﾟｰﾟ) + (ﾟｰﾟ) + (ﾟΘﾟ))", "(ﾟДﾟ) .ﾟωﾟﾉ",
    "(ﾟДﾟ) .ﾟΘﾟﾉ", "(ﾟДﾟ) ['c']", "(ﾟДﾟ) .ﾟｰﾟﾉ", "(ﾟДﾟ) .ﾟДﾟﾉ",
    "(ﾟДﾟ) [ﾟΘﾟ]",
]

_AA_PREFIX = (
    "ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻   //*´∇｀*/ ['_']; o=(ﾟｰﾟ)  =_=3; c=(ﾟΘﾟ) =(ﾟｰﾟ)-(ﾟｰﾟ); "
    "(ﾟДﾟ) =(ﾟΘﾟ)= (o^_^o)/ (o^_^o);"
    "(ﾟДﾟ)={ﾟΘﾟ: '_' ,ﾟωﾟﾉ : ((ﾟωﾟﾉ==3) +'_') [ﾟΘﾟ] "
    ",ﾟｰﾟﾉ :(ﾟωﾟﾉ+ '_')[o^_^o -(ﾟΘﾟ)] "
    ",ﾟДﾟﾉ:((ﾟｰﾟ==3) +'_')[ﾟｰﾟ] }; (ﾟДﾟ) [ﾟΘﾟ] =((ﾟωﾟﾉ==3) +'_') [c^_^o];"
    "(ﾟДﾟ) ['c'] = ((ﾟДﾟ)+'_') [ (ﾟｰﾟ)+(ﾟｰﾟ)-(ﾟΘﾟ) ];"
    "(ﾟДﾟ) ['o'] = ((ﾟДﾟ)+'_') [ﾟΘﾟ];"
    "(ﾟoﾟ)=(ﾟДﾟ) ['c']+(ﾟДﾟ) ['o']+(ﾟωﾟﾉ +'_')[ﾟΘﾟ]+ ((ﾟωﾟﾉ==3) +'_') [ﾟｰﾟ] + "
    "((ﾟДﾟ) +'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ ((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+"
    "((ﾟｰﾟ==3) +'_') [(ﾟｰﾟ) - (ﾟΘﾟ)]+(ﾟДﾟ) ['c']+"
    "((ﾟДﾟ)+'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ (ﾟДﾟ) ['o']+"
    "((ﾟｰﾟ==3) +'_') [ﾟΘﾟ];(ﾟДﾟ) ['_'] =(o^_^o) [ﾟoﾟ] [ﾟoﾟ];"
    "(ﾟεﾟ)=((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟДﾟ) .ﾟДﾟﾉ+"
    "((ﾟДﾟ)+'_') [(ﾟｰﾟ) + (ﾟｰﾟ)]+((ﾟｰﾟ==3) +'_') [o^_^o -ﾟΘﾟ]+"
    "((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟωﾟﾉ +'_') [ﾟΘﾟ]; "
    "(ﾟｰﾟ)+=(ﾟΘﾟ); (ﾟДﾟ)[ﾟεﾟ]='\\\\'; "
    "(ﾟДﾟ).ﾟΘﾟﾉ=(ﾟДﾟ+ ﾟｰﾟ)[o^_^o -(ﾟΘﾟ)];"
    "(oﾟｰﾟo)=(ﾟωﾟﾉ +'_')[c^_^o];"
    "(ﾟДﾟ) [ﾟoﾟ]='\\\"';"
    "(ﾟДﾟ) ['_'] ( (ﾟДﾟ) ['_'] (ﾟεﾟ+"
)

_AA_SUFFIX = "(ﾟДﾟ)[ﾟoﾟ]) (ﾟΘﾟ)) ('_');"


def aaencode(text: str) -> str:
    """AAEncode 编码 (与 aaencode.js 输出一致)"""
    r = _AA_PREFIX + "(ﾟДﾟ)[ﾟoﾟ]+ "
    for ch in text:
        n = ord(ch)
        t = "(ﾟДﾟ)[ﾟεﾟ]+"
        if n <= 127:
            octal = oct(n)[2:]
            t += "".join(_AA_B[int(d)] + "+ " for d in octal)
        else:
            hex4 = "%04x" % n
            t += "(oﾟｰﾟo)+ " + "".join(_AA_B[int(c, 16)] + "+ " for c in hex4)
        r += t
    r += _AA_SUFFIX
    return r


# 反向表: token -> index (按长度降序, 长 token 优先匹配)
_AA_REV = sorted(
    [(tok, i) for i, tok in enumerate(_AA_B)],
    key=lambda x: -len(x[0]),
)


def _aa_decode_segment(seg: str) -> list:
    """解析一段 b-token 序列, 返回 token 索引列表"""
    digits = []
    i = 0
    while i < len(seg):
        matched = False
        for tok, idx in _AA_REV:
            if seg.startswith(tok, i):
                digits.append(idx)
                i += len(tok)
                # 跳过 "+ "
                while i < len(seg) and seg[i] in "+ ":
                    i += 1
                matched = True
                break
        if not matched:
            i += 1  # 跳过无法识别字符
    return digits


def aadecode(text: str) -> str:
    """AAEncode 解码 (纯 Python, 解析 b-token 序列还原字符)"""
    if not text or not text.strip():
        return ""
    # 定位编码主体: 从固定前缀后的 "(ﾟДﾟ)[ﾟoﾟ]+ " 开始, 到后缀前
    start = text.find("(ﾟДﾟ)[ﾟoﾟ]+ ")
    if start < 0:
        raise ValueError("Given code is not encoded as aaencode.")
    body = text[start + len("(ﾟДﾟ)[ﾟoﾟ]+ "):]
    end = body.rfind(_AA_SUFFIX)
    if end >= 0:
        body = body[:end]
    # 按字符段分割: "(ﾟДﾟ)[ﾟεﾟ]+" 为 ASCII 段前缀, "(oﾟｰﾟo)+" 为 unicode 段前缀
    result = []
    # 分割字符段
    segments = re.split(r"\(ﾟДﾟ\)\[ﾟεﾟ\]\+", body)
    for seg in segments:
        seg = seg.strip()
        if not seg:
            continue
        if seg.startswith("(oﾟｰﾟo)+"):
            inner = seg[len("(oﾟｰﾟo)+"):]
            idxs = _aa_decode_segment(inner)
            if idxs:
                # 每个 idx 是一个 hex 位 (0-15)
                result.append(chr(int("".join(hex(v)[2:] for v in idxs), 16)))
        else:
            idxs = _aa_decode_segment(seg)
            if idxs:
                # 每个 idx 是一个 8 进制位 (0-7)
                result.append(chr(int("".join(str(v) for v in idxs), 8)))
    return "".join(result)


# ============ JSFuck ============

from qsnctf.jsfuck_py import jsfuck_encode  # noqa: E402  (纯 Python, 与原 JS 版逐字节一致)