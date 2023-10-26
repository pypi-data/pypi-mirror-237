# Release

Create and activate a fresh virtual environment:

```bash
python -m venv env
source env/bin/activate
```

Upgrade pip and build:

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade build
```

- Update version number in `setup.py`.
- Update `CHANGELOG.md`.
- Commit the changes and create a tag:

```bash
git add -p
git commit -m "Release N.N.N"
git tag N.N.N
git push
git push origin N.N.N
```

Create a build and upload it to PyPi:

```bash
rm -rf dist
python -m build
python -m twine upload dist/*
```

Done! 🎉, notify the community.
