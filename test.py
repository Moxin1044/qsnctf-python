from qsnctf import *


a = WebShellCracking('http://localhost/shell.php', threadline=50,mode="GET")
print(a.results)