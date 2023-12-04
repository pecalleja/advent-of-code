import glob
import os

import requests


for generated_file in glob.glob("./*.py.template"):
    new_file_name = generated_file.replace(".template", "")
    os.rename(generated_file, new_file_name)

day = "{{ cookiecutter.day }}"
r = requests.get(f"https://adventofcode.com/2023/day/{day}/input", timeout=30)
with open("input.txt", "wb") as f:
    f.write(r.content)
