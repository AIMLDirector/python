import re

textone = "we are learning python"

output = re.findall("we", textone)
output1 = re.findall(r"\S+", textone)
output2 = re.findall(r"\b\w{6}\b", textone)
output3 = re.findall(r"\Awe\Z", textone )
print(output)
print(output1)
print(output2)
print(output3)
