# jelloow-names

Package for maintaining centralized governance of data for company data extraction

## Deployment to PyPi

Add credential to `~/.pypirc` file.

```bash
echo "[pypi]
username = __token__
password = $PIPY_TOKEN" >> ~/.pypirc
```

Create and activate a virtual environment.

```bash
python -m venv venv
python.exe -m pip install --upgrade pip

#linux / mac
source venv/bin/activate

#windows
venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

Build the package and then upload it to PyPi.

```bash
python -m build
python -m twine upload --repository pypi dist/*
```
