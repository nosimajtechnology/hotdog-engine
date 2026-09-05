# Release Hotdog

The Release action validates the skill, runs package-integrity tests, builds a
deterministic ZIP and SHA-256 file, then attaches both to the GitHub release.
It uses the repository's automatic GITHUB_TOKEN with contents:write for that job;
no personal token, API key or stored secret is needed.

## Normal release

1. Make changes in `hotdog/` and validate them.
2. Update `hotdog/VERSION` and the `SKILL.md` title to the same stable version.
3. Add `docs/releases/v<version>.md` describing changes and actual validation.
4. Push/merge to `main`. A VERSION change triggers the release automatically.
5. Wait for Release to succeed. Confirm `hotdog.zip` and `hotdog.zip.sha256`.

Documentation-only pushes do not publish another version. Existing assets are
compared on reruns, not overwritten. Different bytes or a tag at a different
commit cause failure; use a new version instead. Partial uploads can be rerun.

## Alternative triggers

- Push a matching `v<version>` tag to release that commit.
- Run Actions > Release > Run workflow on main or a matching version tag.
- Create/publish a GitHub release with a tag matching the checked-out package.
  The published event builds that exact tag and attaches assets.

These triggers are alternatives, not steps to perform together. Workflows
serialize release writes. Release creation by GITHUB_TOKEN does not need to
trigger a second workflow: the same job uploads the assets.

If Actions or workflow writes are restricted by repository/organization policy,
the owner must enable the permitted release action. Do not broaden unrelated
permissions. The local package can still be built with `python3 scripts/package.py`.

## Verify downloads

Download both release assets into one folder, then run `sha256sum -c
hotdog.zip.sha256` on Linux or compare `Get-FileHash hotdog.zip -Algorithm SHA256`
to the checksum on PowerShell. The character-sheet checksum is also validated
inside the package. ZIP and repository snapshots are distinct artifacts.

## Installed skill parity

Install the exact `hotdog/` package from the released commit using the host's
current skill workflow. Compare relative file SHA-256 values to the repo copy.
A repository push does not automatically update an already-installed skill.
