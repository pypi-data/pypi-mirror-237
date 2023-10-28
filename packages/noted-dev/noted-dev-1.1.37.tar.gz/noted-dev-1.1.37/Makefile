# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file "LICENCE.txt". In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

# Create virtual environment:
# python3 -m venv venv-noted
# . venv-noted/bin/activate
# ./venv-noted/bin/python3 -m pip install --upgrade pip

# Install on CentOS:
# sudo yum install -y python3
# sudo yum install python-pip
# sudo yum install -y wget
# wget https://test-files.pythonhosted.org/packages/b9/30/109c8fb7a9a69572d080308fecf53000f5ee7b537714944355a2f457c4dc/noted-dev-1.1.62.tar.gz
# tar -xf noted-dev-1.1.62.tar.gz
# pip install noted-dev-1.1.62/
# noted -h

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install wheel
	python3 -m pip install build

clean:
	sudo rm -rf build/
	sudo rm -rf dist/
	sudo rm -rf .eggs/
	sudo rm -rf src/noted_dev.egg-info/

run:
	sudo python3 setup.py bdist_wheel
	sudo python3 setup.py install

build:
	sudo python3 setup.py sdist

build_centos:
	sudo python3 setup.py bdist_rpm

check:
	python3 -m twine check dist/*

upload_testpypi:
	python3 -m twine upload --repository testpypi dist/*

upload_pypi:
	python3 -m twine upload dist/*

generate_uml:
	pyreverse -o png /Users/carmen/cernbox/gitlab_workspace/noted/src/noted --all-ancestors --all-associated --show-builtin --module-names y --project noted