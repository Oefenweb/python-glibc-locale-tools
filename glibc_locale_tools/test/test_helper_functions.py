# -*- coding: utf-8 -*-

import unittest
from glibc_locale_tools.glibc_locale_tools import *
import re


class TestHelperFunctions(unittest.TestCase):

  def test_unicode_decode(self):
    """
    Tests `unicode_decode`.
    """

    # Ascii char
    unicode_char = '002D'
    actual = unicode_decode(unicode_char)
    expected = u'-'
    self.assertEqual(actual, expected)

    # Non-ascii char
    unicode_char = '20AC'
    actual = unicode_decode(unicode_char)
    expected = u'€'
    self.assertEqual(actual, expected)

    # Empty char
    unicode_char = ''
    self.assertRaises(ValueError, unicode_decode, unicode_char)

  def test_unicode_encode(self):
    """
    Tests `unicode_encode`.
    """

    # Ascii char
    char = u'-'
    actual = unicode_encode(char)
    expected = '<U002D>'
    self.assertEqual(actual, expected)

    # Non-ascii char
    char = u'€'
    actual = unicode_encode(char)
    expected = '<U20AC>'
    self.assertEqual(actual, expected)

    # Empty char
    char = u''
    self.assertRaises(TypeError, unicode_encode, char)

  def test_replace_positional(self):
    """
    Tests `replace_positional`.
    """

    original = 'quisquam'
    start = 3
    replacement = 'ct'
    end = 5
    actual = replace_positional(original, start, replacement, end)
    expected = 'quictuam'
    self.assertEqual(actual, expected)

  def test_reverse_iter(self):
    """
    Tests `reverse_iter`.
    """

    actual = reverse_iter(iter([1, 2, 3]))
    expected = iter([3, 2, 1])

    self.assertSequenceEqual(list(actual), list(expected))

  def test_between_quotes(self):
    """
    Tests BETWEEN_QUOTES_PATTERN.
    """

    # Multiline, multi value
    str1 = ('abday   "zo";"ma";"di";/\n'
            '	"wo";"do";"vr";/\n'
            '	"za"')

    actual1 = re.findall(BETWEEN_QUOTES_PATTERN, str1)
    expected1 = ['zo', 'ma', 'di', 'wo', 'do', 'vr', 'za']
    self.assertSequenceEqual(actual1, expected1)

    # Multiline, multiple single values
    str2 = ('day     "zondag";/\n'
            '	"maandag";/\n'
            '	"dinsdag";/\n'
            '	"woensdag";/\n'
            '	"donderdag";/\n'
            '	"vrijdag";/\n'
            '	"zaterdag"')

    actual2 = re.findall(BETWEEN_QUOTES_PATTERN, str2)
    expected2 = ['zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag']
    self.assertSequenceEqual(actual2, expected2)

    # Single line, single value
    str3 = 'd_t_fmt "%a %d %b %Y %T %Z"'

    actual3 = re.findall(BETWEEN_QUOTES_PATTERN, str3)
    expected3 = ['%a %d %b %Y %T %Z']
    self.assertSequenceEqual(actual3, expected3)

    # Single line, multi (empty) value
    str4 = 'am_pm   "";""'

    actual4 = re.findall(BETWEEN_QUOTES_PATTERN, str4)
    expected4 = ['', '']
    self.assertSequenceEqual(actual4, expected4)

    # Single line, single (empty) value
    str5 = 't_fmt_ampm ""'

    actual5 = re.findall(BETWEEN_QUOTES_PATTERN, str5)
    expected5 = ['']
    self.assertSequenceEqual(actual5, expected5)

    # Multi line, single value
    str6 = ('date_fmt       "%a %b %e/\n'
            ' %H:%M:%S /\n'
            '%Z %Y"')

    actual6 = re.findall(BETWEEN_QUOTES_PATTERN, str6)
    expected6 = ['%a %b %e/\n %H:%M:%S /\n%Z %Y']
    self.assertSequenceEqual(actual6, expected6)

suite = unittest.TestLoader().loadTestsFromTestCase(TestHelperFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
