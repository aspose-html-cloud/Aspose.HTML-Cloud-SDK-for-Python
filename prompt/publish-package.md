# Prompt: Publish a new release of `asposehtmlcloud` to PyPI

> Paste this prompt to an AI coding assistant (e.g. GitHub Copilot Chat)
> inside the [aspose-html-cloud-python](https://github.com/aspose-html-cloud/aspose-html-cloud-python)
> repository when you need to cut a new PyPI release.

---

## Context

You are working in the `aspose-html-cloud-python` repository, which is the
official Aspose.HTML Cloud SDK for Python. Its authoritative publish
procedure lives in [`.github/PUBLISHING.md`](../.github/PUBLISHING.md).
Follow it precisely.

## Task

Publish version **`<NEW_VERSION>`** of the `asposehtmlcloud` package to
PyPI (<https://pypi.org/project/asposehtmlcloud/>).

Replace `<NEW_VERSION>` with the target version, e.g. `26.7.1`.
Use PEP 440 form only — **no leading zeros** (`26.7.1`, not `26.07.1`).

## Inputs the user will provide

- `<NEW_VERSION>` — e.g. `26.7.1`
- `<PYPI_TOKEN>` — a project-scoped PyPI API token starting with `pypi-`
  (never commit it, never print it back in a summary)

## Steps to perform

1. **Bump the version in both source files:**
   - `setup.py` → `VERSION = "<NEW_VERSION>"`
   - `asposehtmlcloud/api_client.py` → `self.default_headers['x-aspose-client-version'] = "<NEW_VERSION>"`
2. **Clean previous build artifacts:**
   ```powershell
   Remove-Item -Recurse -Force build, dist, asposehtmlcloud.egg-info -ErrorAction SilentlyContinue
   ```
3. **Build sdist and wheel:**
   ```powershell
   python setup.py sdist bdist_wheel
   ```
   Confirm two files appear under `dist/`:
   - `asposehtmlcloud-<NEW_VERSION>-py3-none-any.whl`
   - `asposehtmlcloud-<NEW_VERSION>.tar.gz`
4. **Verify metadata:**
   ```powershell
   python -m twine check dist/*
   ```
5. **Upload to PyPI:**
   ```powershell
   python -m twine upload dist/* -u __token__ -p "<PYPI_TOKEN>"
   ```
6. **Report** the release URL: `https://pypi.org/project/asposehtmlcloud/<NEW_VERSION>/`.

## Guardrails

- Do **not** re-use an existing PyPI version — PyPI rejects duplicate
  uploads. If the version already exists, ask the user for a new one.
- Do **not** echo, log, or store the PyPI token in files, git history,
  the terminal transcript summary, or the chat response.
- If `twine` or `setuptools`/`wheel` is missing, install them via
  `python -m pip install --upgrade twine setuptools wheel` first.
- If setuptools warns *"Normalizing 'X.0Y.Z' to 'X.Y.Z'"*, stop and ask the
  user to confirm the normalized form; update both source files to the
  normalized value.
- Do **not** create additional summary markdown files — the changes and
  a short chat summary are enough.
- If PyPI returns `403` with *"Username/Password authentication is no longer
  supported"*, the caller passed a real password instead of an API token.
  Stop and ask for a token starting with `pypi-`.

## Expected outcome

- `setup.py` and `asposehtmlcloud/api_client.py` show the new version.
- `dist/` contains the two freshly built artifacts.
- The package is visible at
  `https://pypi.org/project/asposehtmlcloud/<NEW_VERSION>/`.
- `pip install --upgrade asposehtmlcloud` installs the new version
  (may take a few minutes to propagate).
