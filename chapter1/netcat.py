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
    # capture_output permet de capturer l'output sous variable.stdout
    output = subprocess.run(shlex.split(cmd), capture_output=True)
    return output



if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        # RawDescriptionHelpFormater garde le formatage de la description et de l'épilogue
        formatter_class=argparse.RawDescriptionHelpFormatter,
        #textwrap.dedent() enlève l'indentation par défaut des triple quote (multi ligne)
        epilog=textwrap.dedent('''Example:
            netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
            netcat.py -t 192.168.1.108 -u=mytest.txt # upload file
            netcat.py -t 192.168.1.108 -l 5555 -l -e=\"cat /etc/passwd\" # execute command
            echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
            netcat.py -t 192.168.1.108 -p 5555 # connect to server
            '''))
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
        
    nc = NetCat(args, buffer.encode())
    nc.run()
        

            