del /f /s /q "dist/"
python setup.py sdist bdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*