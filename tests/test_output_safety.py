import contextlib
import io
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

from main import process_acrostic  # noqa: E402


def _run(words, text):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        process_acrostic(words, text)
    return buf.getvalue()


class OutputSafetyTest(unittest.TestCase):
    def test_control_sequences_are_escaped(self):
        out = _run(['ski'], 'Soft kittens inspire m\x1b]52;c;AAAA\x07\x1b[2Jore quietly. Tigers hunt.')
        self.assertIn('ski ->', out)
        self.assertNotIn('\x1b', out)
        self.assertNotIn('\x07', out)
        self.assertIn('\\x1b', out)

    def test_control_in_word_and_acrostic_escaped(self):
        out = _run(['s\x1bk'], '\x1bsk is ok. Another one.')
        self.assertNotIn('\x1b', out)

    def test_plain_text_unchanged(self):
        out = _run(['ski'], 'Soft kittens inspire café. Tigers hunt.')
        self.assertIn('ski -> Skic ||| Full sentence: Soft kittens inspire café', out)


if __name__ == '__main__':
    unittest.main()
