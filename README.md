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

__NOTE__: This can be useful because some (web) framework, for instance [CakePHP](http://book.cakephp.org/2.0/en/core-libraries/internationalization-and-localization.html), use `LC_TIME` files to provide localisation.

### locale-decode-category

Decodes a given `LC_*` (category) file to a human readable format.

```sh
bin/locale-decode-category < \
  glibc_locale_tools/test/data/nl_NL.LC_TIME.expected > \
  glibc_locale_tools/test/data/nl_NL.LC_TIME.decoded;
```

__NOTE__: This can be useful when you want to make changes in for instance `LC_TIME`. Use `locale-encode-category` to re-encode.

### locale-encode-category

(Re)encodes a given `LC_*` (category) file to a machine readable format.

```sh
bin/locale-encode-category < \
  glibc_locale_tools/test/data/nl_NL.LC_TIME.decoded > \
  glibc_locale_tools/test/data/nl_NL.LC_TIME.encoded;
```

__NOTE__: This can be useful when you want to re-encode for instance `LC_TIME`.

## References

* [Glibc locale files](http://localization-guide.readthedocs.org/en/latest/guide/locales/glibc.html)
