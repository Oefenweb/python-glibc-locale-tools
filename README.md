# glibc-locale-tools

[![Build Status](https://travis-ci.org/Oefenweb/glibc-locale-tools.svg)](https://travis-ci.org/Oefenweb/glibc-locale-tools)

`glibc-locale-tools` provides some tools to work with (glibc) locale files (e.g. `LC_MONETARY`, `LC_NUMERIC`, `LC_TIME`)

## Usage

### locale-extract-lc

Extracts a given `LC_*` section from a locale file.

```sh
bin/locale-extract-lc < glibc_locale_tools/test/data/nl_NL LC_TIME > glibc_locale_tools/test/data/nl_NL.LC_TIME.actual;
```

### locale-decode-lc

Decodes a given `LC_*` file.

```sh
bin/locale-decode-lc < glibc_locale_tools/test/data/nl_NL.LC_TIME.expected > glibc_locale_tools/test/data/nl_NL.LC_TIME.decoded;
```

### locale-encode-lc

(Re)encodes a given `LC_*` file.

```sh
bin/locale-encode-lc < glibc_locale_tools/test/data/nl_NL.LC_TIME.decoded > glibc_locale_tools/test/data/nl_NL.LC_TIME.encoded;
```

## References

* [Glibc locale files](http://localization-guide.readthedocs.org/en/latest/guide/locales/glibc.html)
