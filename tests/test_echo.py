#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo

# Your test case class goes here
class TestEcho(unittest.TestCase):

    def setUp(self):
        pass

    def test_upper_short(self):
        args = ["-u", "hello world"]
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_lower_short(self):
        args = ['-l', "HeLlo WOrLd"]
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_title_short(self):
        args = ['-t', "HeLlo WOrLd"]
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_upper_long(self):
        args = ["--upper", "hello world"]
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_lower_long(self):
        args = ['--lower', "HeLlo WOrLd"]
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_title_long(self):  
        args = ['--title', "HeLlo WOrLd"]
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
