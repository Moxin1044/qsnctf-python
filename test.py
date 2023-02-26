from qsnctf import *

a = DomainScan("qsnctf.com", threadline=100, echo=True)
print(a.results_title)
print(a.results)
