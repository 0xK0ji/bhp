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
    output = subprocess.run(shlex.split(cmd), capture_output=True)
    return output



if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )