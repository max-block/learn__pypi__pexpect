import os

import pexpect
from dotenv import load_dotenv

load_dotenv()

ssh_key = os.getenv("SSH_KEY")
host = os.getenv("HOST")

command = "ls -l /"

child = pexpect.spawn(
    f"ssh -o 'StrictHostKeyChecking=no' -i {ssh_key} {host} '{command}'",
    encoding="utf-8",
    timeout=300,
)
out = child.read()
# There are some problems with it inside of docker :(
# Don't use pexpect with docker, use plain subprocess

print(out)
