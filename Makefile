#!/usr/bin/env make
#
# Make file for matmod-python-exercises

# target: help             - displays this help text
# target:
.PHONY:  help
help:
	@echo 'help             - displays this help text'
	@echo 'clear-cache      - clearing the cache'
	@echo 'test             - running python unittest\n'


# target: clear-cache             - clearing the cache
.PHONY:  clear-cache
clear-cache:
	@echo "removing ./*/__pycache__"
	@rm -rf ./*/__pycache__
	@echo "All done!"


# target: test                    - running python unittest
.PHONY:  test
test:
	coverage run 01/exercises01test.py
