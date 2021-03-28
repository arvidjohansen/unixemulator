# unixemulator
**unixemulator** is a poor attempt to emulate the unix bourne again shell (BASH)

just for fun

```python
C:\Users\arvidj\Desktop\git\unixemulator3>bash.py
'Welcome to unix emulator'
arvidj@DEK7:unixemulator3$ls
['.git',
 '.vscode',
 'bash.py',
 'echo',
 'emulator.py',
 'README.md',
 'setup.py',
 'somefolder',
 '__init__.py',
 '__pycache__']
arvidj@DEK7:unixemulator3$cd ..
arvidj@DEK7:git$cd ..
arvidj@DEK7:Desktop$mkdir mydir
'Successfully created folder: mydir'
None
arvidj@DEK7:Desktop$cd mydir
arvidj@DEK7:mydir$echo sometext somefile
None
arvidj@DEK7:mydir$ls
['somefile']
arvidj@DEK7:mydir$cp somefile somefile2
'somefile2'
arvidj@DEK7:mydir$cat somefile2
'sometext'
arvidj@DEK7:mydir$pwd
'C:\\Users\\arvidj\\Desktop\\mydir'
arvidj@DEK7:mydir$mv somefile helloface
'helloface'
arvidj@DEK7:mydir$ls
['helloface', 'somefile2']
arvidj@DEK7:mydir$
 ```

