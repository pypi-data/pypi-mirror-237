# Commit Message Git Hook

A set of tools to validate git Conventional Commit messages.

See the [Conventional Commits Specification](https://www.conventionalcommits.org/en/v1.0.0/).

## Installation Instructions

### Install from PyPI (Python Package Index)

Run the script below to install the latest version of this package:

```bash
pip install commit-msg-git-hook --upgrade
```

### Setup the Local Git Hook `commit-msg`

Run the script below to scaffold the hook:

```bash
python3 -m commit_msg_git_hook.setup
```

It does the following steps:

- Create a directory for git-hooks, by default `./.github/git-hooks`.
- Set the hooks path to the current repository as the created directory.
- Create the `commit-msg` hook file.
- Fill it with a basic script to call `commit_msg.main()`, from this package.
- Make the hook file executable.
- Create a configuration file `commit-msg.config.json` if it doesn't exist.

## Configuration Instructions

Customize the configuration file `commit-msg.config.json` to fit your project's needs.

Probably you will want to add **scopes**, to fully utilize the [Conventional Commits Specification](https://www.conventionalcommits.org/en/v1.0.0/).

## Basic Usage

After setting up and adding the new files to your git remote repository, your collaborators will
need to run the **installation** and **setup** steps again.
But, this time, the setup will only set the hooks path and make sure the file `commit-msg` is
executable.

Every time you make a commit, the hook will check if its message is in accordance to the
specification and the project's customization.

## How To Edit Commits

If your branch is not shared yet (not merged into `develop`, for example), you can edit your commits
with the command below. Git will list the last `n` commits and ask you whether you want to keep or
edit each one of them.

```bash
git rebase -i HEAD~n
```

More information here: https://docs.github.com/pt/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/changing-a-commit-message