# Git Practice Missions

Work inside this folder. Do not use your real Astrid repository for experiments.

## Mission 0 — Inspect the project

```bash
pwd
ls -la
git status
```

Expected: `git status` says this is not a Git repository yet.

## Mission 1 — Start tracking

1. Initialize a repository on `main`.
2. Check the status.
3. Stage only `README.md`.
4. Check the status again.
5. Unstage `README.md` without deleting it.
6. Stage all project files.
7. Inspect what is staged.
8. Create your first commit with a meaningful message.
9. View the commit history.

Useful commands to learn: `git init`, `git status`, `git add`, `git restore --staged`, `git diff --cached`, `git commit`, `git log`.

## Mission 2 — Make and inspect a change

1. Edit `notes/ideas.md` and add one idea.
2. Run `git status`.
3. Run `git diff` and read the change.
4. Stage the file.
5. Run `git diff --cached`.
6. Commit the change.

## Mission 3 — Ignore a file

1. Create a file named `local-secret.txt`.
2. Put fake text in it (never use a real password or API key).
3. Check whether Git sees it.
4. Add `local-secret.txt` to `.gitignore`.
5. Check `git status`.
6. Confirm the file still exists on disk.

## Mission 4 — Create a feature branch

1. Create and switch to a branch named `feature/greeting`.
2. Change the greeting in `app.py`.
3. Commit the change on that branch.
4. Switch back to `main`.
5. Confirm the greeting on `main` has not changed.
6. Switch back to your feature branch.

Useful commands: `git switch -c`, `git switch`, `git branch`, `git log --oneline --all`.

## Mission 5 — Merge a branch

1. Switch to `main`.
2. Merge `feature/greeting` into `main`.
3. Inspect the history.
4. Delete the feature branch after the merge.

Useful commands: `git merge`, `git branch -d`.

## Mission 6 — Practice a merge conflict

This mission is deliberately designed to create a conflict.

1. On `main`, edit the line beginning `PROJECT_STATUS=` in `notes/ideas.md` to say `PROJECT_STATUS=stable`.
2. Commit that change.
3. Create a branch named `feature/status-message` from `main`.
4. On that branch, change the same line to `PROJECT_STATUS=feature-ready`.
5. Commit the change.
6. Switch back to `main`.
7. Change the same line to `PROJECT_STATUS=main-ready`.
8. Commit the change.
9. Merge `feature/status-message` into `main`. Git should report a conflict.
10. Open `notes/ideas.md`. Find the conflict markers: `<<<<<<<`, `=======`, and `>>>>>>>`.
11. Edit the file so only the line you choose remains. Remove all conflict markers.
12. Stage the resolved file and finish the merge with a commit.
13. Run `git status` and confirm the working tree is clean.

Do not panic when you see a conflict. Git is asking you to choose how the competing edits should be combined.

## Mission 7 — Undo safely

Use a disposable edit; do not experiment on important work.

1. Change a line in `notes/ideas.md` but do not stage it.
2. Inspect it with `git diff`.
3. Discard that unstaged change with `git restore notes/ideas.md`.
4. Make another change and stage it.
5. Unstage it with `git restore --staged notes/ideas.md` (this keeps the edit in your working folder).

Learn the difference:
- `git restore <file>` discards unstaged edits in that file.
- `git restore --staged <file>` removes it from staging but keeps the edit.

## Mission 8 — Tags and remote practice

Optional: create a separate empty **private** GitHub repository for this lab. Do not reuse your Astrid repository.

1. Create a version tag: `git tag -a v1.0 -m "Practice lab version 1.0"`.
2. Add your new GitHub repository as `origin`.
3. Push the branch: `git push -u origin main`.
4. Push the tag: `git push origin v1.0`.
5. Check the remote: `git remote -v`.

Never paste a personal access token into a file or share it in chat. When Git prompts for an HTTPS password, use your token privately.

## Final challenge

Without looking at the earlier missions, do this from memory:

1. Check status.
2. Create a branch.
3. Make a change.
4. Review the diff.
5. Stage and commit it.
6. Merge it into `main`.
7. Push your changes (if you configured a remote).

When stuck, run `git status` first. It is your Git dashboard.
