NAMESPACE=llimllib
APP=slackbot-raspbian

.PHONY: testall
testall: requirements
	tox

# to run a single file, with debugger support:
# pytest -s test/test_plugins/test_image.py
.PHONY: test
test: install
	LANG=en_US.UTF-8 pytest --cov=limbo --cov-report term-missing test

.PHONY: clean
clean:
	rm -rf build dist slackbot_raspbian.egg-info

.PHONY: run
run:
	python setup.py install
	make clean
	bin/limbo

.PHONY: repl
repl: install
	bin/limbo -t

.PHONY: requirements
requirements:
	ansible-playbook deploy-slackbot-raspbian.yml

.PHONY: install
install: requirements
	python setup.py install
	make clean

.PHONY: publish
publish:
	pandoc -s -w rst README.md -o README.rst
	python setup.py sdist upload
	rm README.rst

.PHONY: flake8
flake8:
	flake8 limbo test
