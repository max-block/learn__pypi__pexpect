import sys

import pexpect

shell_cmd = "echo 1 && echo 2"

child = pexpect.spawn("bash", ["-c", shell_cmd], encoding="utf-8")
child.logfile = sys.stdout

child.expect(pexpect.EOF)
