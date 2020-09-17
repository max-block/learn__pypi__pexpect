import sys

import pexpect

child = pexpect.spawn("cat /not/existing/path", encoding="utf-8", timeout=300)
child.logfile = sys.stdout  # it caches stderr also
child.expect(pexpect.EOF)
# cat: /not/existing/path: No such file or directory
