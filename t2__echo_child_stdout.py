import sys

import pexpect

child = pexpect.spawn("brew upgrade", encoding="utf-8", timeout=300)
child.logfile = sys.stdout

child.expect(pexpect.EOF)
