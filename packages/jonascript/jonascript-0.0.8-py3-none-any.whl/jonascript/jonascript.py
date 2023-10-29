import subprocess
from dataclasses import dataclass
from typing import Any, Union

@dataclass(frozen=True)
class Output:
    args: Any
    data: str
    returncode: int

    def list(self) -> list[str]:
        return self.data.split("\n")

def cmd(command: Union[str, 'Command']) -> Output:
    # if i try to capture stderr as well by doing stderr=subropcess.PIPE as well
    # or using capture_output=True, fzf is not shown in the terminal
    output = subprocess.run(command.command if type(command) is Command else command, shell=True, stdout=subprocess.PIPE)
    return Output(output.args, output.stdout.decode().strip(), output.returncode)

@dataclass(frozen=True)
class Command:
    command: str

    def aand(self, command: str) -> 'Command':
        return Command(f"{self.command} && {command}")

    def oor(self, command: str) -> 'Command':
        return Command(f"{self.command} || {command}")

    def pipe(self, command: str) -> 'Command':
        return Command(f"{self.command} | {command}")

    def exec(self) -> Output:
        return cmd(self)


HOME = cmd("echo $HOME").data
"""
equivalent to bash's $HOME, e.g. '/home/dev'
"""

WINDOW = Command("xprop -root")\
    .pipe("awk 'NR==1{print $NF}'")\
    .exec()\
    .data
"""
id of the focused window, e.g. '0x2000001'
"""