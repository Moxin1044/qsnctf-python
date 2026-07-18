import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import qsnctf
import qsnctf.api as api
import qsnctf.base as base
import qsnctf.misc as misc
import qsnctf.web as web


class CoreCodecTests(unittest.TestCase):
    def test_custom_base64_round_trip(self):
        standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        custom = standard[::-1]
        encoded = qsnctf.base64_encode_custom("hello CTF", custom)
        self.assertEqual(qsnctf.base64_decode_custom(encoded, custom), "hello CTF")

    def test_atbash_preserves_non_ascii_letters(self):
        self.assertEqual(qsnctf.atbash_cipher("Abc-\u4e2d"), "Zyx-\u4e2d")

    def test_arithmetic_sequence_value_is_numeric(self):
        self.assertEqual(qsnctf.differential_sequence_ask_n_value(1, 3, 4), 10)

    def test_missing_base58_has_actionable_error(self):
        if base.base58 is None:
            with self.assertRaisesRegex(ImportError, "base58"):
                qsnctf.base58_encode("test")


class SideEffectTests(unittest.TestCase):
    def test_network_clients_do_not_run_during_construction(self):
        with patch.object(api, "_request") as request:
            api.quipqiup("ciphertext")
            api.FeishuWebhook("title", "message", "token")
            api.DingTalk("title", "message", "token")
            api.FOFA("email", "key")
        request.assert_not_called()

    def test_scanner_only_runs_when_requested(self):
        response = SimpleNamespace(status_code=200, text="<title>ok</title>")
        scanner = web.DirScan(
            "https://example.com",
            threadline=16,
            dirlist=["/one"],
            auto_run=False,
        )
        with patch.object(web, "_request", return_value=response) as request:
            request.assert_not_called()
            scanner.run()
        self.assertEqual(scanner.results, ["https://example.com/one"])
        self.assertEqual(scanner.errors, [])

    def test_web_request_uses_secure_defaults(self):
        response = Mock()
        fake_requests = SimpleNamespace(request=Mock(return_value=response))
        with patch.object(web, "requests", fake_requests):
            self.assertIs(web._request("GET", "https://example.com"), response)
        _, _, kwargs = fake_requests.request.mock_calls[0]
        self.assertEqual(kwargs["timeout"], web.DEFAULT_TIMEOUT)
        self.assertTrue(kwargs["verify"])


    def test_api_request_sets_timeout_and_checks_status(self):
        response = Mock()
        fake_requests = SimpleNamespace(request=Mock(return_value=response))
        with patch.object(api, "requests", fake_requests):
            self.assertIs(api._request("GET", "https://example.com"), response)
        _, _, kwargs = fake_requests.request.mock_calls[0]
        self.assertEqual(kwargs["timeout"], api.DEFAULT_TIMEOUT)
        response.raise_for_status.assert_called_once_with()

    def test_fofa_credentials_are_sent_as_params(self):
        payload = {
            "error": False,
            "email": "user@example.com",
            "username": "user",
            "isvip": False,
            "vip_level": 0,
            "avatar": "",
            "fcoin": 0,
        }
        client = api.FOFA("user@example.com", "secret-key")
        with patch.object(
            qsnctf.plugin.python.operation,
            "send_get_json",
            return_value=payload,
        ) as send:
            client.get_userinfo()
        url = send.call_args.args[0]
        params = send.call_args.kwargs["params"]
        self.assertNotIn("secret-key", url)
        self.assertEqual(params["key"], "secret-key")
        self.assertNotIn("secret-key", client.check_fofa_config())
class ArchiveTests(unittest.TestCase):
    def test_unprotected_rar_is_detected_without_cracking(self):
        fake_archive = Mock()
        fake_archive.needs_password.return_value = False
        fake_rarfile = SimpleNamespace(
            RarFile=Mock(return_value=fake_archive),
            Error=Exception,
        )
        with patch.object(misc, "rarfile", fake_rarfile):
            cracker = misc.RarPasswordCracking("archive.rar", auto_run=True)
        self.assertEqual(
            cracker.results,
            "No password is required to decompress this package.",
        )


if __name__ == "__main__":
    unittest.main()
