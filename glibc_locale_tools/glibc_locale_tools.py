# -*- coding: utf-8 -*-

import re


BETWEEN_QUOTES_PATTERN = r'"([^"]*)"'
"""
A re pattern to match a between quotes section, that is not a comment.
"""

UNICODE_PATTERN = r'(<U([0-9A-F]{4})>*)'
"""
A re pattern to match a unicode char (e.g. <U002D>).
"""

TO_DECODE_PATTERN = r'(/(?!\n)|[^/\n]){1}'
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

COMMENT_LINE_WITH_QUOTES_PATTERN = r'^%.*"[^"]*"'
"""
A re pattern to match a comment line with a between quotes section.
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


def between_range(range1, range2):
  """
  Checks whether or not range 2 is between range 1.

  :param range1: A range
  :param range2: A range
  :return: Whether or not range 2 is between range 1
  """

  return range1['start'] <= range2['start'] <= range1['end'] and range1['start'] <= range2['end'] <= range1['end']


def in_unsafe_spans(match_start, match_end, unsafe_spans):
  """
  Checks whether not a range (match start and end) is in unsafe ranges.

  :param match_start: A match start position
  :param match_end: A match end position
  :param unsafe_spans: A list of unsafe spans
  :return: Whether not a range is in unsafe ranges
  """

  for unsafe_span in unsafe_spans:
    if between_range(unsafe_span, {'start': match_start, 'end': match_end}):
      return True

  return False


def get_unsafe_spans(lines, lines_joined):
  """
  Generates a list of unsafe spans.

  Unsafe span are comment lines that contain double quotes (that should not be (en|de)coded).

  :param lines: A list of lines
  :param lines_joined: A string of lines
  :return: A list of unsafe spans
  """

  unsafe_lines = []
  for line in lines:
    if re.search(COMMENT_LINE_WITH_QUOTES_PATTERN, line):
      unsafe_lines.append(line)

  unsafe_lines_pattern = '({0})'.format('|'.join(map(re.escape, unsafe_lines)))

  unsafe_spans = []
  for unsafe_line in re.finditer(unsafe_lines_pattern, lines_joined):
    unsafe_spans.append({'start': unsafe_line.start(0), 'end': unsafe_line.end(0)})

  return unsafe_spans
