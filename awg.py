import json
import subprocess
from subprocess import CompletedProcess
from pathlib import Path
import sys
import os

cfg_path = "/path/to/cfg/config.conf"

AWG_INTERFACE = Path(cfg_path).stem


def run_command(command: str) -> CompletedProcess:
    result = subprocess.run(command.split(), capture_output=True, text=True)

    return result


def awg_status() -> bool:
    command = "ip link"
    run_command(command)

    return AWG_INTERFACE in run_command(command).stdout


def print_awg_status() -> None:
    data = {}

    if awg_status() is True:
        data['text'] = " "
        print(json.dumps(data))
    else:
        data['text'] = " "
        print(json.dumps(data))


def awg_toggle(cfg_path: str) -> None:
    data = {}
    abs_path = os.path.expanduser(cfg_path)

    if awg_status() is True:
        command = f"awg-quick down {abs_path}"
        run_command(command)
        data['text'] = " "
        print(json.dumps(data))
    else:
        command = f"awg-quick up {abs_path}"
        run_command(command)
        data['text'] = " "
        print(json.dumps(data))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_awg_status()
    else:
        awg_toggle(cfg_path)
