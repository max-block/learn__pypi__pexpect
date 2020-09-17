import sys
import time

import pexpect

child = pexpect.spawn("builder node", encoding="utf-8", timeout=300)
child.logfile = sys.stdout

child.expect(pexpect.EOF, async_=True)

print("zz1")
time.sleep(3)
out = child.read()
print("out", out)
