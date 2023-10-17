# This file is in module_3 which doesn't take any inputs
# The code just sets a relative path that can be used by another module
# It outputs the relative path as filename
from pathlib import Path
def rel_D():
    root_dir = Path(__file__).resolve().parent.parent
    filename = root_dir / "Data"/ "raw" / "output.txt"
    return filename