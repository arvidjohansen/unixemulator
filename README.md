# unixemulator
**unixemulator** is a poor attempt to emulate the unix bourne again shell (BASH)

just for fun

```python
>>> python emulator.py
C:\Users\arvidj\Desktop\git\unixemulator>python emulator.py
'Welcome to unix emulator'
arvidj@DESKTOP-K1:unixemulator$ls
['.git',
 '.vscode',
 'emulator.py',
 'README.md',
 'setup.py',
 '__init__.py',
 '__pycache__']
arvidj@DESKTOP-K1:unixemulator$mkdir('somefolder')
'Successfully created folder: somefolder'
None
arvidj@DESKTOP-K1:unixemulator$cd('somefolder')
'Changed dir: C:\\Users\\arvidj\\Desktop\\git\\unixemulator\\somefolder'
arvidj@DESKTOP-K1:somefolder$echo('some content','some filename')
None
arvidj@DESKTOP-K1:somefolder$ls
['some filename']
arvidj@DESKTOP-K1:somefolder$cat('some filename')
'some content'
arvidj@DESKTOP-K1:somefolder$
 ```

