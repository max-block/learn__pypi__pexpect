import sys

import pexpect

child = pexpect.spawn("bash", ["password.sh"], encoding="utf-8", timeout=300)
child.logfile_read = sys.stdout
child.expect("input password:")
child.sendline("secret")
child.expect(pexpect.EOF)

# it' doesn't work here. Check mm-cli: p login
