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

```bash
#!/usr/bin/env python3

import commit_msg as cm

cm.main()

```

4. Now run the command below in the repository root to set your repository git hooks path:

```bash
git config core.hooksPath .github/git-hooks
```

> **NOTE**: The configuration is local to this repository. Each repo can have its own hooks path.


### 2. Using the Server-Side Scan
