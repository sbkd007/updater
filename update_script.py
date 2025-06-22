import re

file_path = "main.py"

with open(file_path, "r") as file:
    content = file.read()

match = re.search(r'helloworld(\d+)', content)
if match:
    number = int(match.group(1)) + 1
else:
    number = 1

new_content = f'print("helloworld{number}")\n'

with open(file_path, "w") as file:
    file.write(new_content)
