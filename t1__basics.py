import sys

import pexpect

child = pexpect.spawn("bash", ["questions.sh"], encoding="utf-8", timeout=300)
child.logfile = sys.stdout

child.expect("first")
child.sendline("foo")
child.expect("second")
child.sendline("bar")
child.expect(pexpect.EOF)
