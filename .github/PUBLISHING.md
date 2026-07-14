# Publishing `asposehtmlcloud` to PyPI

This document describes how to build and publish the
[`asposehtmlcloud`](https://pypi.org/project/asposehtmlcloud/) Python
package to the Python Package Index (PyPI).

> Audience: package maintainers with access to the `asposecloud` PyPI account.

---

## 1. Prerequisites

### 1.1 Local tooling

Install the build and upload tools (one-time setup):

```powershell
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel twine
```

### 1.2 PyPI account

- PyPI profile: <https://pypi.org/user/asposecloud/>
- Package page: <https://pypi.org/project/asposehtmlcloud/>

### 1.3 API token (required)

PyPI **no longer accepts username/password uploads** — you must use an API
token.

1. Sign in at <https://pypi.org/manage/account/>.
2. Go to **Account settings → API tokens → Add API token**.
3. Give it a descriptive name (e.g. `aspose-html-cloud-python-release`).
4. Scope: prefer **"Project: asposehtmlcloud"** over "Entire account".
5. Copy the token (starts with `pypi-`) and store it in a password manager.
   It will not be shown again.

Optional — store it in [`~/.pypirc`](https://packaging.python.org/en/latest/specifications/pypirc/)
so you don't need to paste it each time:

```ini
[pypi]
username = __token__
password = pypi-<your-token-here>
```

Windows path: `C:\Users\<you>\.pypirc` (protect its ACL).

---

## 2. Version bump

PyPI does not allow re-uploading the same version, so each release **must**
bump the version.

### 2.1 Version format

- Follow [PEP 440](https://peps.python.org/pep-0440/).
- Segments **cannot have leading zeros** — setuptools normalizes them.
  Example: `26.07.1` is silently normalized to `26.7.1`.
- The `asposehtmlcloud` project uses a `YY.M.PATCH` scheme
  (e.g. `25.10.1`, `26.7.1`).

### 2.2 Files to update

Update the version in **both** places so the SDK reports the version it
actually is on PyPI:

| File | What to change |
|------|----------------|
| [`setup.py`](../setup.py) | `VERSION = "YY.M.PATCH"` |
| [`asposehtmlcloud/api_client.py`](../asposehtmlcloud/api_client.py) | `self.default_headers['x-aspose-client-version'] = "YY.M.PATCH"` |

Commit and push the bump on `master` before publishing.

---

## 3. Build the distributions

From the repo root:

```powershell
# Clean any previous build artifacts to avoid uploading stale files
Remove-Item -Recurse -Force build, dist, asposehtmlcloud.egg-info -ErrorAction SilentlyContinue

# Build source distribution (.tar.gz) and wheel (.whl)
python setup.py sdist bdist_wheel
```

You should end up with two files in `dist/`, e.g.:

```
dist/asposehtmlcloud-26.7.1-py3-none-any.whl
dist/asposehtmlcloud-26.7.1.tar.gz
```

> Setuptools may print deprecation warnings about `setup.py` and license
> classifiers. They are informational and do not block the build.

### Sanity check (optional)

```powershell
python -m twine check dist/*
```

---

## 4. Upload to PyPI

### 4.1 With inline token

```powershell
python -m twine upload dist/* -u __token__ -p "pypi-<your-token-here>"
```

Username is literally the string `__token__` — the token itself goes in the
password position.

### 4.2 With `.pypirc`

If you stored credentials in `.pypirc`:

```powershell
python -m twine upload dist/*
```

### 4.3 Expected success output

```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading asposehtmlcloud-26.7.1-py3-none-any.whl
Uploading asposehtmlcloud-26.7.1.tar.gz

View at:
https://pypi.org/project/asposehtmlcloud/26.7.1/
```

Open the URL to confirm the release is live. It usually appears within a
minute; installation via `pip` may take a few minutes to propagate to
mirrors.

---

## 5. Post-release verification

In a clean environment:

```powershell
python -m pip install --upgrade asposehtmlcloud
python -c "import asposehtmlcloud, importlib.metadata; print(importlib.metadata.version('asposehtmlcloud'))"
```

The printed version should match the one you just released.

Tag the release in git:

```powershell
git tag -a v26.7.1 -m "Release 26.7.1"
git push origin v26.7.1
```

---

## 6. Test releases (recommended for risky changes)

Use [TestPyPI](https://test.pypi.org/) before hitting production:

1. Create a separate token at <https://test.pypi.org/manage/account/>.
2. Upload:

   ```powershell
   python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u __token__ -p "pypi-<test-token>"
   ```

3. Install to verify:

   ```powershell
   python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ asposehtmlcloud==<version>
   ```

---

## 7. Troubleshooting

| Symptom | Cause / Fix |
|---------|-------------|
| `403 Forbidden` / *"Username/Password authentication is no longer supported"* | You used a plain username/password. Switch to an API token; username must be `__token__`. |
| `400 File already exists` | You are trying to re-upload the same version. Bump the version in `setup.py` and `api_client.py`, rebuild, and retry. |
| `Normalizing 'YY.MM.P' to 'YY.M.P'` warning | PEP 440 does not allow leading zeros. Use the normalized form (`26.7.1`, not `26.07.1`) in the source to avoid a mismatch between the SDK header and the PyPI version. |
| `ModuleNotFoundError: No module named 'setuptools'` | `python -m pip install --upgrade setuptools wheel` |
| `ModuleNotFoundError: No module named 'twine'` | `python -m pip install --upgrade twine` |
| Upload hangs behind a corporate proxy | Configure `HTTPS_PROXY` env var or use `.pypirc` with `repository = https://upload.pypi.org/legacy/`. |

---

## 8. Security notes

- **Never commit** the PyPI token to git. Keep it in a password manager,
  in `.pypirc` (locked-down permissions), or in a CI secret.
- If a token leaks, revoke it immediately at
  <https://pypi.org/manage/account/token/> and issue a new one.
- Prefer **project-scoped tokens** over account-wide tokens.
- Consider migrating to
  [PyPI Trusted Publishers](https://docs.pypi.org/trusted-publishers/) for
  CI-driven releases — no long-lived secrets required.

---

## 9. Quick reference (copy/paste)

```powershell
# 1. Bump version in setup.py + asposehtmlcloud/api_client.py, commit, push.

# 2. Clean & build
Remove-Item -Recurse -Force build, dist, asposehtmlcloud.egg-info -ErrorAction SilentlyContinue
python setup.py sdist bdist_wheel

# 3. Verify
python -m twine check dist/*

# 4. Publish
python -m twine upload dist/* -u __token__ -p "pypi-<token>"

# 5. Tag
git tag -a vYY.M.P -m "Release YY.M.P"
git push origin vYY.M.P
```
