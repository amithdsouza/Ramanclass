import os
import subprocess


def main():
    cmd = ['pgrep', '-fla', 'top' ]
    output = subprocess.check_output(cmd)
    lines = output.split('\n')
    for line in lines:
        line.strip()
        words = line.split()
        if len(words) <= 1:
           continue
        if words[1] == 'top':
           print words[0], words[1]
           ps_cmd = ['pstree', '-aps', words[0]]
           ps_output = subprocess.check_output(ps_cmd)
           print ps_output


main()
