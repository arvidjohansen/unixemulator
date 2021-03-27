#*encoding: utf-8
import os
import shutil
import sys
import types

from getpass import getuser
from socket import gethostname
from varinfo import *

DEBUG = False

settings = {
    'smallcwd' : True #changes the cwd to only the last dir
}

def ls(path=None):
    if path == None:
        path = '.'
    if os.path.exists(path):
        return os.listdir(path)
    else:#search file or directory
        content = os.listdir()
        return [c for c in content if path in c]

def cd(path):
    """Change directory to path"""
    os.chdir(path)
    return f'Changed dir: {os.getcwd()}'

def cp(target, destination):
    """Copy file to destination"""
    return shutil.copyfile(target, destination)

def mv(target, destination):
    """Move (or rename) file to destination"""
    return shutil.move(target, destination)

def mkdir(name):
    """Creates a new directory with name"""
    try:
        os.mkdir(name)
        print(f'Successfully created folder: {name}')
    except FileExistsError as e:
        print(e)
def cwd():
    """Current working directory
    returns the current working directory"""
    return os.getcwd()

def pwd():
    """Print working directory
    returns the current working directory"""
    cwd = os.getcwd()
    return cwd

def cat(input_):
    """cat (concatenate)
    returns the content of a file"""

    if isinstance(input_,str):
        return open(input_,encoding='utf-8').read()

def grep(input_, find):
    """grep - Global Regular Expression Print
    returns lines of the input content 
    that matches the find string"""
    if isinstance(input_, str):
        return [l for l in input_.split('\n') if find in l] 
    elif isinstance(input_,list):
        return [l for l in input_ if find in l]
    raise Exception('grep needs a string or a list to search in')

def echo(text, filename):
    """Echos text into a file"""
    with open(filename,'w') as file:
        file.write(text)

def exec_command(cmd):
    """Executes a command
    Returns the result"""
    if DEBUG: print(f'exec_commmand: {cmd}')
    
    exec('global i; i = %s' % cmd)
    global i
    return i

def getattri(name):
    """getattr in current module
    Returns the named attribute of the current module"""
    return getattr(sys.modules[__name__], name)

def _setup():
    """Sets up the necessary variables 
    for the program to work"""

    global USER
    global HOSTNAME 
    USER = getuser()
    HOSTNAME = gethostname()
def main():
    _setup()
    print('Welcome to unix emulator')

    shell = True

    if not shell:
        print('Falling back to python shell...')
        return 

    while(True):
        cwd = pwd() #current working dir = print working dir
        if not settings['smallcwd']:
            bottom_str = f'{USER}@{HOSTNAME}:{cwd}$'
        else:
            cwd = cwd.split('\\')[-1]
            bottom_str = f'{USER}@{HOSTNAME}:{cwd}$'

        cmd = input(bottom_str)

        if DEBUG: print(f'cmd: {cmd}')

        try:
            res = exec_command(cmd)
        except SyntaxError as e:
            res = e
        except Exception as e:
            res = e
        if isinstance(res,types.FunctionType) or \
        isinstance(res,types.BuiltinFunctionType):
            res = res()
            print(res)
        else:
            if DEBUG: print(f'Else - cmd: {cmd}\nres:{res}')
            print(res)
                

if __name__ == '__main__':
    main()