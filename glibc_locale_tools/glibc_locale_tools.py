# -*- coding: utf-8 -*-

BETWEEN_QUOTES_PATTERN = r'"([^"]*)"'
"""
"""

UNICODE_PATTERN = r'(<U([0-9A-F]{4})>*)'
"""
"""


def unicode_decode(string):
  """
  """

  return unichr(int(string, 16))


def unicode_encode(char):
  """
  """

  return '<U%04X>' % (ord(char))
