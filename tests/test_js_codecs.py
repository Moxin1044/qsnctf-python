# -*- coding: utf-8 -*-
"""JS 编解码器纯 Python 实现测试 (jsfuck_py / js_codecs)

无需 JS 引擎与 exejs, CI 可直接运行。
黄金样本与 plugin/js 原版 (node) 输出逐字节一致 (已交叉验证)。
"""
import unittest

from qsnctf.js_codecs import aaencode, aadecode, jsfuck_encode
from qsnctf import misc


class JSFuckEncodeTests(unittest.TestCase):
    """jsfuck_encode: 与 jsfuck_encode.js 输出逐字节一致"""

    GOLDEN_TEST123 = (
    '[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+'
    '[]+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+'
    '(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]'
    '])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]])[+!+[]+[+[]]]+([][['
    ']]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][['
    ']]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]'
    ']+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])['
    '+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]])[+'
    '!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+'
    '[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[!+[]+!+[]+!+[]])'
    )

    def test_golden_sample_matches_js_original(self):
        # node: JSFuck('test123') 长度 756, 与本黄金样本逐字节一致
        self.assertEqual(jsfuck_encode('test123'), self.GOLDEN_TEST123)

    def test_output_is_pure_jsfuck(self):
        cases = ['alert(1)', '1+1', 'constructor', '"hi"', '[]', '中文',
                 'true', 'false', 'undefined', 'NaN', 'Infinity', 'a.b.c',
                 'document.cookie', "x=1;y=2;x+y", "'a'"]
        for text in cases:
            out = jsfuck_encode(text)
            self.assertTrue(out, 'empty output for %r' % text)
            self.assertTrue(set(out) <= set('[]()!+'),
                            'non-JSFuck chars in output of %r' % text)
            self.assertTrue(out.startswith('[][]') or out.startswith('[][('))
            self.assertTrue(out.endswith(')'))

    def test_empty_input(self):
        self.assertEqual(jsfuck_encode(''), '')

    def test_misc_jsfuck_encode_is_pure_python(self):
        # misc.jsfuck_encode 已切换纯 Python, 不应要求 exejs
        out = misc.jsfuck_encode('misc-test')
        self.assertTrue(set(out) <= set('[]()!+'))


class AAEncodeTests(unittest.TestCase):
    """aaencode/aadecode: 与原 aaencode.js 输出逐字节一致"""

    def test_round_trip(self):
        cases = ['hello', 'alert(1)', 'test123', '中文测试', 'flag{aa_bb_cc}',
                 "console.log('hi')", '~!@#$%%^&*()']
        for text in cases:
            self.assertEqual(aadecode(aaencode(text)), text)

    def test_structure(self):
        out = aaencode('qsnctf')
        self.assertTrue(out.startswith(u'ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻'))
        self.assertTrue(out.endswith("('_');"))

    def test_reject_non_aaencode(self):
        with self.assertRaises(ValueError):
            aadecode('this is not aaencode at all')

    def test_misc_aaencode_is_pure_python(self):
        out = misc.aaencode('misc-aa')
        self.assertEqual(misc.aadecode(out), 'misc-aa')


if __name__ == '__main__':
    unittest.main()
