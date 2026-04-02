from safety import is_safe_command

tests = [
    "ls ~/Desktop",
    "find ~/Downloads -type f -name '*.pdf'",
    "rm -rf ~/",
    "sudo ls",
    "shutdown -h now",
]

for t in tests:
    print(t, "=>", "SAFE" if is_safe_command(t) else "BLOCKED")
