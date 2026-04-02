import shlex

READ_ONLY_CMDS = {
    "ls", "find", "du", "pwd", "whoami", "date", "head", "tail", "cat", "open", "echo", "ps"
}

WRITE_CMDS = {
    "mv", "cp", "mkdir", "zip", "touch", "chmod", "chown", "ln", "tar"
}

def classify_command(cmd: str) -> str:
    """
    Returns "read" or "write".
    Heuristic-based: looks at the first command token and presence of redirection.
    """
    s = cmd.strip()

    # If command uses output redirection, treat as write (creates/overwrites files)
    if ">" in s or ">>" in s:
        return "write"

    # Try to parse first token safely
    try:
        parts = shlex.split(s)
    except Exception:
        # If we can't parse, be conservative
        return "write"

    if not parts:
        return "write"

    first = parts[0]

    if first in WRITE_CMDS:
        return "write"

    if first in READ_ONLY_CMDS:
        return "read"

    # Unknown commands: be conservative
    return "write"
