from pathlib import Path
print(type(Path('README.md').read_text()))
print(Path('README.md').read_text())