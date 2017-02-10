#!/usr/bin/env python

from cmd_pkg import commands 
import threading
import sys

def run_command(cmd,args=None,flags=None):

    if args:
        c = threading.Thread(target=cmd, args=(args,))
    else:
        c = threading.Thread(target=cmd)
        
    c.start()
    c.join()

if __name__ == '__main__':
   
   while True:	
    if len(sys.argv) < 2:
        print("usage: python driver.py cmd where cmd = 'ls' or 'pwd', etc.")
        sys.exit(0) 
    cmd = sys.argv[1]    
    if cmd == 'cat':
        run_command(commands.cat,sys.argv[2])
    elif cmd == 'mv':
        run_command(commands.mv,sys.argv[2])
    elif cmd == 'pwd':
        run_command(commands.pwd,sys.argv[2])	
    elif cmd =='exit':
		break
		
		