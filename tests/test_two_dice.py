#!/usr/bin/env python3

import contextlib
import io
import re
import unittest

from src.two_dice import main


class TwoDice(unittest.TestCase):

    def test_lines(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main()
        result = buf.getvalue().strip().split('\n')
        self.assertEqual(
            len(result), 4,
            msg="The output should contain exactly four lines! Got %d "
                "line(s)." % len(result))

    def test_content(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main()
        result = buf.getvalue().strip().split('\n')
        pattern = r'\((\d),\s*(\d)\)'
        s = set()
        for line in result:
            self.assertRegex(
                line, pattern,
                msg="The output %s was not in the requested format!" % line)
            m = re.match(pattern, line)
            a = int(m.group(1))
            b = int(m.group(2))
            self.assertEqual(
                a + b, 5,
                msg="The pair (%d, %d) does not sum to 5!" % (a, b))
            self.assertTrue(
                a in range(1, 7),
                msg="The value of a dice should be between 1 and 6!")
            self.assertTrue(
                b in range(1, 7),
                msg="The value of a dice should be between 1 and 6!")
            s.add((a, b))
        self.assertEqual(
            len(s), 4,
            msg="Are you sure you printed correct number of pairs? Got "
                "%d distinct pair(s): %s." % (len(s), s))


if __name__ == '__main__':
    unittest.main()
