#binary and source dist
python setup.py bdist_wheel sdist
#upload
twine upload -r testpypi dist/*
twine upload dist/*
