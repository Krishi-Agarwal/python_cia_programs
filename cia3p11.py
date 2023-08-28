import re
krishi="Student in Christ Deemed to Be university reg no 2141119 name KRISHI reg no 2141113 name AYUSH reg no 2141133 name roshan reg no 2141132 name ROSHAN"
res=re.findall("reg no",krishi)
print(res)
comp=re.compile("['2141119','2141133']")
res=re.findall(comp,krishi)

print(res)
res=re.search("name",krishi)
print(res)
