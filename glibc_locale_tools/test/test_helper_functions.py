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

  def test_between_quotes_multi_line_multi_value(self):
    """
    Tests BETWEEN_QUOTES_PATTERN.

    Multi line, multi value.
    """

    str = ('abday   "zo";"ma";"di";/\n'
           '	"wo";"do";"vr";/\n'
           '	"za"')

    actual = re.findall(BETWEEN_QUOTES_PATTERN, str, re.MULTILINE)
    expected = ['zo', 'ma', 'di', 'wo', 'do', 'vr', 'za']
    self.assertSequenceEqual(actual, expected)

  def test_between_quotes_multiline_multiple_single_values(self):
    """
    Tests BETWEEN_QUOTES_PATTERN.

    Multi line, multiple single values.
    """

    str = ('day     "zondag";/\n'
           '	"maandag";/\n'
           '	"dinsdag";/\n'
           '	"woensdag";/\n'
           '	"donderdag";/\n'
           '	"vrijdag";/\n'
           '	"zaterdag"')

    actual = re.findall(BETWEEN_QUOTES_PATTERN, str, re.MULTILINE)
    expected = ['zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag']
    self.assertSequenceEqual(actual, expected)

  def test_between_quotes_single_line_single_value(self):
    """
    Tests BETWEEN_QUOTES_PATTERN.

    Single line, single value
    """

    str = 'd_t_fmt "%a %d %b %Y %T %Z"'

    actual = re.findall(BETWEEN_QUOTES_PATTERN, str, re.MULTILINE)
    expected = ['%a %d %b %Y %T %Z']
    self.assertSequenceEqual(actual, expected)

  def test_between_quotes_single_line_multi_empty_value(self):
    """
    Tests BETWEEN_QUOTES_PATTERN.

    Single line, multi (empty) value.
    """

    str = 'am_pm   "";""'

    actual = re.findall(BETWEEN_QUOTES_PATTERN, str, re.MULTILINE)
    expected = ['', '']
    self.assertSequenceEqual(actual, expected)

  def test_between_quotes_single_line_single_empty_value(self):
    """
    Tests BETWEEN_QUOTES_PATTERN.

    Single line, single (empty) value.
    """

    str = 't_fmt_ampm ""'

    actual = re.findall(BETWEEN_QUOTES_PATTERN, str, re.MULTILINE)
    expected = ['']
    self.assertSequenceEqual(actual, expected)

  def test_between_quotes_multi_line_single_value(self):
    """
    Tests BETWEEN_QUOTES_PATTERN.

    Multi line, single value.
    """

    str = ('date_fmt       "%a %b %e/\n'
           ' %H:%M:%S /\n'
           '%Z %Y"')

    actual = re.findall(BETWEEN_QUOTES_PATTERN, str, re.MULTILINE)
    expected = ['%a %b %e/\n %H:%M:%S /\n%Z %Y']
    self.assertSequenceEqual(actual, expected)

  @unittest.skip("Not supported yet")
  def test_between_quotes_multi_line_single_value_with_comments(self):
    """
    Tests BETWEEN_QUOTES_PATTERN.

    Multi line, single value, with comments.
    """

    str = ('% Appropriate AM/PM time representation (%r)\n'
           '%	"%I:%M:%S %p"\n'
           't_fmt_ampm "%I:%M:%S /\n'
           '%p"')
    actual = re.findall(BETWEEN_QUOTES_PATTERN, str, re.MULTILINE)
    expected = ['%I:%M:%S /\n%p']
    self.assertSequenceEqual(actual, expected)

suite = unittest.TestLoader().loadTestsFromTestCase(TestHelperFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
