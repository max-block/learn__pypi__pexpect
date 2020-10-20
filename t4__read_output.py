import pexpect

child = pexpect.spawn("ls -l /", encoding="utf-8")
out = child.read()

print(out)
