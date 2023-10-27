import os
import subprocess

CONFIG_FILE_NAME = "commit-msg.config.json"
GIT_HOOKS_DIRECTORY = "./.github/git-hooks"

if not os.path.exists(CONFIG_FILE_NAME):
    config_file = open(CONFIG_FILE_NAME, "w")
    config_file.writelines([
        "{",
        "    \"enabled\": true,",
        "    \"revert\": true,",
        "    \"max_length\": 72,",
        "    \"types\": [",
        "        \"build\",",
        "        \"ci\",",
        "        \"docs\",",
        "        \"feat\",",
        "        \"fix\",",
        "        \"perf\",",
        "        \"refactor\",",
        "        \"style\",",
        "        \"test\",",
        "        \"chore\"",
        "    ],",
        "    \"scopes\": []",
        "}",
    ])
    config_file.close()

subprocess.run(["mkdir", "-p", GIT_HOOKS_DIRECTORY], shell=True)
subprocess.run(["touch", f"{GIT_HOOKS_DIRECTORY}/commit-msg"], shell=True)

commit_msg_hook_file = open(f"{GIT_HOOKS_DIRECTORY}/commit-msg", "w")
commit_msg_hook_file.writelines([
    "#!/usr/bin/env python3",
    "",
    "from commit_msg_git_hook import commit_msg as cm",
    "",
    "cm.main()",
])
commit_msg_hook_file.close()

subprocess.run(["chmod", "+x", f"{GIT_HOOKS_DIRECTORY}/commit-msg"])
subprocess.run(["git", "config", "core.hooksPath", GIT_HOOKS_DIRECTORY])