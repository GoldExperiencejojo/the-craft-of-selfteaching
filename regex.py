import re

str = 'achroiocythaemia achroiocythemia a|e'
pttn = r'[a|ae]'
print(re.findall(pttn, str))

pttn = r'[a|e]'
print(re.findall(pttn, str))

pttn = r'[ae]'
print(re.findall(pttn, str))

pttn = r'[(ae)]'
print(re.findall(pttn, str))

pttn = r'[a|ae|(ae)]'
print(re.findall(pttn, str))