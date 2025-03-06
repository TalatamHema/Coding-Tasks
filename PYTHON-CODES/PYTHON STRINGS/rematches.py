import re

pattern = r"Hello"
string = "Hello, World!"

match = re.match(pattern, string)
print(bool(match))
