import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    # shlex split la string en syntaxe shell-like
    output = subprocess.run(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output



if __name__=='__main__':
    response = execute('ls')
    print(response.stdout)