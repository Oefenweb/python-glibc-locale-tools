# -*- coding: utf-8 -*-

import unittest
from glibc_locale_tools.glibc_locale_tools import *


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

suite = unittest.TestLoader().loadTestsFromTestCase(TestHelperFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
