

.PHONY: clean test

clean:
	rm -fR *.egg-info build dist

install:
	pip install tox

test: install
	tox -r
