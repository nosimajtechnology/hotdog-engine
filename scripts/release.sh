#!/usr/bin/env bash
set -euo pipefail
: "${RELEASE_TAG:?Missing validated release tag}"
: "${GH_REPO:?Missing repository}"
: "${GH_TOKEN:?Missing workflow token}"
commit="$(git rev-parse HEAD)"
if git rev-parse -q --verify "refs/tags/$RELEASE_TAG" >/dev/null; then
  tag_commit="$(git rev-list -n 1 "$RELEASE_TAG")"
  if [ "$tag_commit" != "$commit" ]; then
    echo 'Refusing to publish different commit content under an existing tag.' >&2
    exit 1
  fi
fi
if gh release view "$RELEASE_TAG" --repo "$GH_REPO" >/dev/null 2>&1; then
  # Reruns preserve identical assets. A partial upload is repaired by uploading
  # only missing files; an existing file with different bytes is never clobbered.
  existing="$(mktemp -d)"
  trap 'rm -rf "$existing"' EXIT
  assets="$(gh release view "$RELEASE_TAG" --repo "$GH_REPO" --json assets --jq '.assets[].name')"
  for name in hotdog.zip hotdog.zip.sha256; do
    if [[ $'\n'"$assets"$'\n' == *$'\n'"$name"$'\n'* ]]; then
      gh release download "$RELEASE_TAG" --repo "$GH_REPO" --pattern "$name" --dir "$existing"
      cmp "dist/$name" "$existing/$name"
    else
      gh release upload "$RELEASE_TAG" "dist/$name" --repo "$GH_REPO"
    fi
  done
else
  gh release create "$RELEASE_TAG" dist/hotdog.zip dist/hotdog.zip.sha256 \
    --repo "$GH_REPO" --target "$commit" --title "Hotdog $RELEASE_TAG" \
    --notes-file "docs/releases/$RELEASE_TAG.md"
fi
gh release view "$RELEASE_TAG" --repo "$GH_REPO" --json url,assets
