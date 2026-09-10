# -*- coding: utf-8 -*-
"""新增功能测试: word_freq (词频统计) 与 SMTPMail (SMTP 邮件发送)

全程离线: SMTP 通过 mock 校验报文与连接行为, 不产生真实网络请求。
"""
import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

import qsnctf
import qsnctf.api as api
from qsnctf import misc


class WordFreqTests(unittest.TestCase):
    """word_freq: 英文单词提取与频率统计"""

    def test_basic_count_and_order(self):
        result = misc.word_freq("the quick brown fox jumps over the lazy dog the fox")
        self.assertEqual(result['the'], 3)
        self.assertEqual(result['fox'], 2)
        self.assertEqual(list(result)[0], 'the')  # 降序排列

    def test_case_insensitive_by_default(self):
        self.assertEqual(misc.word_freq("Flag flag FLAG"), {'flag': 3})

    def test_case_sensitive(self):
        result = misc.word_freq("Flag flag FLAG", case_sensitive=True)
        self.assertEqual(result, {'Flag': 1, 'FLAG': 1, 'flag': 1})

    def test_top_limit(self):
        result = misc.word_freq("a b b c c c d d d d", top=2)
        self.assertEqual(list(result.items()), [('d', 4), ('c', 3)])

    def test_min_length_filters_noise(self):
        result = misc.word_freq("I am a CTF player", min_length=2)
        self.assertNotIn('i', result)
        self.assertNotIn('a', result)
        self.assertIn('ctf', result)

    def test_ignores_punctuation(self):
        result = misc.word_freq("hello, world! hello-world")
        self.assertEqual(result['hello'], 2)
        self.assertEqual(result['world'], 2)

    def test_apostrophe_is_part_of_word(self):
        self.assertEqual(misc.word_freq("don't don't do")["don't"], 2)

    def test_tie_break_is_alphabetical(self):
        self.assertEqual(list(misc.word_freq("bb aa cc aa bb").items()),
                         [('aa', 2), ('bb', 2), ('cc', 1)])

    def test_empty_input(self):
        self.assertEqual(misc.word_freq(""), {})
        self.assertEqual(misc.word_freq(None), {})

    def test_exported_at_top_level(self):
        self.assertIs(qsnctf.word_freq, misc.word_freq)


class SMTPMailTests(unittest.TestCase):
    """SMTPMail: 安全默认行为 + 报文正确性 + 三种连接方式"""

    def test_construction_performs_no_network(self):
        with patch.object(api.smtplib, 'SMTP_SSL') as ssl_cls, \
                patch.object(api.smtplib, 'SMTP') as smtp_cls:
            api.SMTPMail('smtp.example.com', 465, 'u@example.com', 'pw')
        ssl_cls.assert_not_called()
        smtp_cls.assert_not_called()

    def test_ssl_send_builds_message_and_recipients(self):
        server = MagicMock()
        with patch.object(api.smtplib, 'SMTP_SSL', return_value=server) as ssl_cls:
            ok = api.SMTPMail('smtp.example.com', 465, 'u@example.com', 'pw').send(
                'a@example.com, b@example.com', '主题标题', '正文内容',
                cc='c@example.com', bcc='d@example.com')
        self.assertTrue(ok)
        ssl_cls.assert_called_once()
        server.login.assert_called_once_with('u@example.com', 'pw')
        message = server.send_message.call_args[0][0]
        self.assertEqual(message['Subject'], '主题标题')
        self.assertEqual(message['From'], 'u@example.com')
        self.assertIsNone(message['Bcc'])           # 密送不写入邮件头
        self.assertIn('a@example.com', message['To'])
        self.assertEqual(server.send_message.call_args[1]['to_addrs'],
                         ['a@example.com', 'b@example.com', 'c@example.com', 'd@example.com'])
        server.quit.assert_called_once()

    def test_starttls_path(self):
        server = MagicMock()
        with patch.object(api.smtplib, 'SMTP', return_value=server) as smtp_cls:
            api.SMTPMail('smtp.example.com', 587, 'u@example.com', 'pw',
                         use_starttls=True).send('a@example.com', 's', 'c')
        smtp_cls.assert_called_once()
        server.starttls.assert_called_once()
        self.assertGreaterEqual(server.ehlo.call_count, 2)

    def test_plain_smtp_without_auth(self):
        server = MagicMock()
        with patch.object(api.smtplib, 'SMTP', return_value=server), \
                patch.object(api.smtplib, 'SMTP_SSL') as ssl_cls:
            api.SMTPMail('smtp.example.com', 25, use_ssl=False).send(
                'a@example.com', 's', 'c', sender='noreply@example.com')
        ssl_cls.assert_not_called()
        server.login.assert_not_called()            # 无用户名则不登录
        message = server.send_message.call_args[0][0]
        self.assertEqual(message['From'], 'noreply@example.com')

    def test_html_content_and_custom_headers(self):
        server = MagicMock()
        with patch.object(api.smtplib, 'SMTP_SSL', return_value=server):
            api.SMTPMail('h', 465, 'u', 'p').send(
                'a@example.com', 's', '<b>hi</b>', content_type='html',
                headers={'X-Test': '1'})
        message = server.send_message.call_args[0][0]
        self.assertEqual(message.get_content_type(), 'text/html')
        self.assertEqual(message['X-Test'], '1')

    def test_attachments_from_file_and_bytes(self):
        server = MagicMock()
        with tempfile.NamedTemporaryFile('wb', suffix='.txt', delete=False) as f:
            f.write(b'hello attachment')
            path = f.name
        try:
            with patch.object(api.smtplib, 'SMTP_SSL', return_value=server):
                api.SMTPMail('h', 465, 'u', 'p').send(
                    'a@example.com', 's', 'c',
                    attachments=[path, ('data.bin', b'\x00\x01')])
            message = server.send_message.call_args[0][0]
            names = [part.get_filename() for part in message.iter_attachments()]
            self.assertIn(os.path.basename(path), names)
            self.assertIn('data.bin', names)
        finally:
            os.unlink(path)

    def test_requires_recipient(self):
        with self.assertRaises(ValueError):
            api.SMTPMail('h', 465, 'u', 'p').send('', 's', 'c')

    def test_requires_sender(self):
        with self.assertRaises(ValueError):
            api.SMTPMail('h', 465).send('a@example.com', 's', 'c')

    def test_invalid_content_type(self):
        with self.assertRaises(ValueError):
            api.SMTPMail('h', 465, 'u', 'p').send('a@example.com', 's', 'c',
                                                  content_type='xml')

    def test_exported_at_top_level(self):
        self.assertIs(qsnctf.SMTPMail, api.SMTPMail)


if __name__ == '__main__':
    unittest.main()
