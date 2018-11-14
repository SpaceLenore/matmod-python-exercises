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
clean-cache:
	@echo "removing ./*/__pycache__"
	@rm -rf ./*/__pycache__
	@echo "All done!"


# target: test                    - running python unittest
.PHONY:  test
test:
	@cd 01 && python3 -m unittest -v exercises01test
