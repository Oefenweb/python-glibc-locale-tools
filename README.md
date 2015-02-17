# glibc-locale-tools

[![Build Status](https://travis-ci.org/Oefenweb/glibc-locale-tools.svg)](https://travis-ci.org/Oefenweb/glibc-locale-tools)

`glibc-locale-tools` provides some tools to work with (glibc) locale files (e.g. `LC_MONETARY`, `LC_NUMERIC`, `LC_TIME`)

## Usage

### locale-extract-category

Extracts a given `LC_*` section (category) from a locale file.

```sh
bin/locale-extract-category < \
  glibc_locale_tools/test/data/nl_NL LC_TIME > \
  glibc_locale_tools/test/data/nl_NL.LC_TIME.actual;
```

### locale-decode-category

Decodes a given `LC_*` (category) file.

```sh
bin/locale-decode-category < \
  glibc_locale_tools/test/data/nl_NL.LC_TIME.expected > \
  glibc_locale_tools/test/data/nl_NL.LC_TIME.decoded;
```

### locale-encode-category

(Re)encodes a given `LC_*` (category) file.

```sh
bin/locale-encode-category < \
  glibc_locale_tools/test/data/nl_NL.LC_TIME.decoded > \
  glibc_locale_tools/test/data/nl_NL.LC_TIME.encoded;
```

## References

* [Glibc locale files](http://localization-guide.readthedocs.org/en/latest/guide/locales/glibc.html)
