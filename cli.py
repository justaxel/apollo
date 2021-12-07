import subprocess as subp
from typing import List, Tuple


def comm(cmd: str) -> Tuple[str, str]:
    """Executes a shell command using `subp.Popen` interface."""

    with subp.Popen(f"{cmd}", shell=True, stdout=subp.PIPE) as proc:
        stdout_, stderr_ = proc.communicate()

    dec_stdout = stdout_.decode()
    if stderr_:
        return dec_stdout, stderr_.decode()
    else:
        return dec_stdout, None


def cmd_concat(cmds: List[str]) -> str:
    """Concatenates cli commands with the `&&` operator."""

    return " && ".join(cmds)

