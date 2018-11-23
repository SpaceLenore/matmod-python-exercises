#!/usr/bin/env make
#
# Make file for matmod-python-exercises

# target: help             - displays this help text
# target:
.PHONY:  help
help:
	@echo 'help             - displays this help text'
	@echo 'clear-cache      - clearing the cache'
	@echo 'install          - install dependencies for test environment'
	@echo 'test             - running python unittest\n'


# target: clear-cache           - clearing the cache
.PHONY:  clear-cache
clear-cache:
	@echo "removing ./*/__pycache__"
	@rm -rf ./*/__pycache__
	@echo "All done!"

# target: dependencies - prepare test environment
.PHONY: install
install:
	pip install coverage

# target: test                    - running python unittest
.PHONY:  test
test:
	cd 01 && coverage run exercises01test.py
	cd 02 && coverage run exercises02test.py
	coverage combine 01/.coverage 02/.coverage
