# Development and release flow

This repository follows a lightweight GitFlow model.

## Branches

- `master`: production-ready code. Tags and PyPI releases are created from this branch.
- `develop`: integration branch for the next version.
- `feature/*`: feature work branched from and merged back into `develop`.
- `release/*`: release stabilization branched from `develop`, then merged into both `master` and `develop`.
- `hotfix/*`: urgent fixes branched from `master`, then merged into both `master` and `develop`.

Pull requests and branch pushes run the CI workflow across supported Python versions.

## Automated release

1. Update the package version in `setup.py`.
2. Merge the release branch into `master`.
3. Create and push an annotated tag that exactly matches the package version:

   ```bash
   git tag -a v0.0.9.4 -m "Release v0.0.9.4"
   git push origin master
   git push origin v0.0.9.4
   ```

4. The release workflow validates the version, runs tests, builds and checks the wheel and source distribution, publishes them to PyPI, and creates a GitHub Release with both files attached.

The workflow can also be run manually for an existing tag from GitHub Actions.

## Required repository configuration

PyPI Trusted Publishing must authorize:

- Owner: `Moxin1044`
- Repository: `qsnctf-python`
- Workflow: `python-publish.yml`
- Environment: `pypi`

The `pypi` GitHub Environment may use required reviewers when a manual publishing gate is desired. Protect `v*` tags so only maintainers can create release tags.
