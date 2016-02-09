all: check source deb

init:
	pip install -r requirements.txt

dist: source deb

source:
	python setup.py sdist

deb:
	python setup.py --command-packages=stdeb.command bdist_deb

check:
	find . -name \*.py | xargs pep8 --first
	find bin -type f | xargs pep8 --first

test:
	nosetests -v

	glibc_locale_tools/test/test-category-extract da_DK
	glibc_locale_tools/test/test-category-extract nl_NL
	glibc_locale_tools/test/test-category-extract en_US
	glibc_locale_tools/test/test-category-extract tr_TR
	glibc_locale_tools/test/test-category-decode-encode da_DK
	glibc_locale_tools/test/test-category-decode-encode nl_NL
	glibc_locale_tools/test/test-category-decode-encode en_US
	glibc_locale_tools/test/test-category-decode-encode tr_TR

clean:
	python setup.py clean
	rm -rf build deb_dist debian dist MANIFEST *.egg-info deb_dist
	find . -name '*.pyc' -print0 | xargs --no-run-if-empty -0 rm
	find . -name '*.decoded' -print0 | xargs --no-run-if-empty -0 rm
	find . -name '*.encode' -print0 | xargs --no-run-if-empty -0 rm
	find . -name '*.actual' -print0 | xargs --no-run-if-empty -0 rm
