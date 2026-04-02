from pathlib import Path
from datetime import datetime
from typing import Optional

LOG_PATH = Path(__file__).parent / "logs" / "history.log"


def log_run(
    user_request: str,
    command: str,
    safe: bool,
    exit_code: Optional[int],
    output: str,
    router_info: Optional[str] = None,
) -> None:
    """
    Logs each run to the 'history.log' file in the logs/ folder.
    """
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # keep logs readable (don’t dump giant outputs)
    output = (output or "").strip()
    if len(output) > 800:
        output = output[:800] + " ... [truncated]"

    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write(f"TIME: {ts}\n")
        f.write(f"REQUEST: {user_request}\n")
        if router_info:
            f.write(f"ROUTER: {router_info}\n")
        f.write(f"COMMAND: {command}\n")
        f.write(f"SAFE: {safe}\n")
        if exit_code is not None:
            f.write(f"EXIT_CODE: {exit_code}\n")
        if output:
            f.write("OUTPUT:\n")
            f.write(output + "\n")
        f.write("\n")

