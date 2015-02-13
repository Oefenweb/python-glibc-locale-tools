# glibc-locale-tools

`glibc-locale-tools` provides some tools to work with (glibc) locale files (e.g. `LC_MONETARY`, `LC_NUMERIC`, `LC_TIME`)

## Usage

### locale-extract-lc_time

Extracts a given LC section from a locale file.

```sh
./locale-extract-lc_time < test/data/nl_NL LC_TIME > test/data/LC_TIME;
```

## References

* [Glibc locale files](http://localization-guide.readthedocs.org/en/latest/guide/locales/glibc.html)
