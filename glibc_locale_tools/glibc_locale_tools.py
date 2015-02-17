# -*- coding: utf-8 -*-

BETWEEN_QUOTES_PATTERN = r'^[^%].*"([^"]*)"'
"""
"""

UNICODE_PATTERN = r'(<U([0-9A-F]{4})>*)'
"""
"""

TO_DECODE_PATTERN = r'[^\/\n]{1}'
"""
"""

POSSIBLE_LC_SECTIONS = ['LC_CTYPE', 'LC_NUMERIC', 'LC_TIME', 'LC_COLLATE', 'LC_MONETARY', 'LC_MESSAGES', 'LC_PAPER',
                        'LC_NAME', 'LC_ADDRESS', 'LC_TELEPHONE', 'LC_MEASUREMENT', 'LC_IDENTIFICATION', 'LC_ALL']
"""
"""

LC_SECTION_PATTERN = r'\n{0}(.*?)END\s+{0}'
"""
"""


def unicode_decode(unicode_char):
  """
  """

  return unichr(int(unicode_char, 16))


def unicode_encode(char):
  """
  """

  return '<U%04X>' % (ord(char))


def replace_positional(original, start, replacement, end):
  """
  """

  return original[:start] + replacement + original[end:]


def reverse_iter(iterator):
  """
  """

  return reversed(list(iterator))
