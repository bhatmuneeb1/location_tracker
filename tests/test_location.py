import unittest

from track_location import parse_ip


class ParseIpTests(unittest.TestCase):
    def test_ipv4(self):
        self.assertEqual(parse_ip("8.8.8.8"), "8.8.8.8")

    def test_ipv6_is_normalized(self):
        self.assertEqual(parse_ip("2001:4860:4860:0:0:0:0:8888"), "2001:4860:4860::8888")

    def test_whitespace_is_ignored(self):
        self.assertEqual(parse_ip(" 1.1.1.1 \n"), "1.1.1.1")

    def test_hostname_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_ip("example.com")

    def test_malformed_address_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_ip("999.999.1.1")


if __name__ == "__main__":
    unittest.main()
