#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo

# Your test case class goes here
class TestEcho(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()


    def test_upper_short(self):
        args = ["-u", "hello world"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_lower_short(self):
        args = ['-l', "HeLlo WOrLd"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_title_short(self):
        args = ['-t', "HeLlo WOrLd"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_upper_long(self):
        args = ["--upper", "hello world"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_lower_long(self):
        args = ['--lower', "HeLlo WOrLd"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_title_long(self):  
        args = ['--title', "HeLlo WOrLd"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
