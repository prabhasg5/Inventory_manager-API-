#!/bin/bash

# Start rebase from root
git rebase -i --root

# After marking all commits as 'edit', run this script:
# OR copy-paste each section manually during each pause

# === Commit 1 ===
GIT_COMMITTER_DATE="2025-05-11T20:02:18" git commit --amend --no-edit --date "2025-05-11T20:02:18"
git rebase --continue

# === Commit 2 ===
GIT_COMMITTER_DATE="2025-05-11T21:01:43" git commit --amend --no-edit --date "2025-05-11T21:01:43"
git rebase --continue

# === Commit 3 ===
GIT_COMMITTER_DATE="2025-05-11T21:17:05" git commit --amend --no-edit --date "2025-05-11T21:17:05"
git rebase --continue

# === Commit 4 ===
GIT_COMMITTER_DATE="2025-05-12T10:08:29" git commit --amend --no-edit --date "2025-05-12T10:08:29"
git rebase --continue

# === Commit 5 ===
GIT_COMMITTER_DATE="2025-05-13T19:34:52" git commit --amend --no-edit --date "2025-05-13T19:34:52"
git rebase --continue

# === Commit 6 ===
GIT_COMMITTER_DATE="2025-05-14T07:57:11" git commit --amend --no-edit --date "2025-05-14T07:57:11"
git rebase --continue

echo "✅ All commit dates updated naturally!"chmod +x rebase_dates.sh



