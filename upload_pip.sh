python setup.py register
python setup.py build
python setup.py sdist
python setup.py sdist upload
sleep 10
pip uninstall -y appinstance
pip install -U appinstance