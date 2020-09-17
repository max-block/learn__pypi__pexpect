import pexpect

child = pexpect.spawn("bash", ["questions.sh"], encoding="utf-8", timeout=300)

child.expect("first")
child.sendline("foo")

child.interact()
