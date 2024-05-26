'''from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)'''

from pathlib import Path
path = Path('name.txt')
name = input('Please provide your name: ')
path.write_text(name)