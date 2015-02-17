# -*- coding: utf-8 -*-

BETWEEN_QUOTES_PATTERN = r'^[^%].*"([^"]*)"'
"""
A re pattern to match a between quotes section, that is not a comment.
"""

UNICODE_PATTERN = r'(<U([0-9A-F]{4})>*)'
"""
A re pattern to match a unicode char (e.g. <U002D>).
"""

TO_DECODE_PATTERN = r'[^\/\n]{1}'
"""
A re pattern to match a string section that needs decoding.
"""

POSSIBLE_LC_SECTIONS = ['LC_CTYPE', 'LC_NUMERIC', 'LC_TIME', 'LC_COLLATE', 'LC_MONETARY', 'LC_MESSAGES', 'LC_PAPER',
                        'LC_NAME', 'LC_ADDRESS', 'LC_TELEPHONE', 'LC_MEASUREMENT', 'LC_IDENTIFICATION', 'LC_ALL']
"""
A list of possible LC sections (categories)
"""

LC_SECTION_PATTERN = r'\n{0}(.*?)END\s+{0}'
"""
A re pattern to match a LC_* section (category, e.g. LC_TIME) in a locale file (e.g. nl_NL).
"""

COMMENT_CHAR_PATTERN = r'^(comment_char\s+(.*))$'
"""
A re pattern to match a comment_char line.
"""

ESCAPE_CHAR_PATTERN = r'^(escape_char\s+(.*))$'
"""
A re pattern to match a escape_char line.
"""


def unicode_decode(unicode_char):
  """
  Decodes an unicode char (e.g. 20AC to €).

  :param unicode_char: An unicode char
  :return: A (decoded) unicode char
  """

  return unichr(int(unicode_char, 16))


def unicode_encode(char):
  """
  Encodes an char (e.g. € to <U20AC>).

  :param char: A char
  :return: An (encoded) char
  """

  return '<U%04X>' % (ord(char))


def replace_positional(original, start, replacement, end):
  """
  Replaces a substring in a string between a start and end position.

  :param original: An original string
  :param start: A start position
  :param replacement: A replacement string
  :param end: An end position
  :return: A (replaced) string
  """

  return original[:start] + replacement + original[end:]


def reverse_iter(iterator):
  """
  Reverses an iterator.

  :param iterator: An iterator
  :return: A reversed iterator
  """

  return reversed(list(iterator))
