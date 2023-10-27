# Commit Message Git Hook

## Installation Instructions

### 1. Using the Local Git Hook `commit-msg`

1. Create a folder called `git-hooks` in your project repository. For example, inside the `.github` directory:

```bash
mkdir -p ./.github/git-hooks
```

2. Create the `commit-msg` git-hook file:

```bash
touch ./.github/git-hooks/commit-msg
```

3. And then paste this content in it:

```python
#!/usr/bin/env python3

from commit_msg_git_hook import commit_msg as cm

cm.main()

```

4. You must make it executable:

```bash
chmod +x ./.github/git-hooks/commit-msg
```

5. Now run the command below in the repository root to set your repository git hooks path:

```bash
git config core.hooksPath .github/git-hooks
```

> **NOTE**: The configuration is local to this repository. Each repo can have its own hooks path.

6. Finally, create a configuration file called `commit-msg.config.json` in your project's root directory:

```json
{
    "enabled": true,
    "revert": true,
    "max_length": 72,
    "types": [
        "build",
        "ci",
        "docs",
        "feat",
        "fix",
        "perf",
        "refactor",
        "style",
        "test",
        "chore"
    ],
    "scopes": []
}

```

### 2. Using the Server-Side Scan
