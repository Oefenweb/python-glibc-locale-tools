all: check source deb

init:
	pip install -r requirements.txt --use-mirrors

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

	glibc_locale_tools/test/test-category-extract nl_NL
	glibc_locale_tools/test/test-category-extract en_US
	glibc_locale_tools/test/test-category-decode-encode nl_NL

clean:
	python setup.py clean
	rm -rf build deb_dist debian dist MANIFEST *.egg-info deb_dist
	find . -name '*.pyc' -print0 | xargs --no-run-if-empty -0 rm
