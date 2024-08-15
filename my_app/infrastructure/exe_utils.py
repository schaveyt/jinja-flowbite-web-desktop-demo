
import subprocess
from pathlib import Path
from dataclasses import dataclass

@dataclass
class ExeResult:
    stdout: str = ""
    stderr: str = ""
    return_code: int = -1


def execute_external_cmd(cmd_array: list[str]) -> ExeResult:
    print(cmd_array)
    cmd_results = subprocess.run(cmd_array, capture_output=True, text=True)

    return ExeResult(cmd_results.stdout, cmd_results.stderr, cmd_results.returncode)

