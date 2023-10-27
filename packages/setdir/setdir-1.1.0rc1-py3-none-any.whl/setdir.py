"""
BEGIN
Path replacement
"""
from setdir import typePCS
from typing import Callable
import sys
import os.path
__location__ = os.path.dirname(os.path.realpath(sys.argv[0]))
index = 0
if not typePCS:
    with open(os.path.join(__location__,"innerdir")) as innerdir:
        opt = innerdir.read().split(",")
        assert opt[0] == "parent"
        index = int(opt[1])
        del opt
getting = {
    "child": lambda x: os.path.split(os.curdir)[1],
    "sibling": lambda x: os.path.split(os.curdir)[1 + index],
    "parent": os.pardir
}
workdir = __location__
get: Callable[[str], str] = lambda x: os.path.abspath(os.path.join(workdir, *[getting[index[0]] for _ in range(index[1])], x))
sys.path.append(workdir)
"""
END
Path replacement
"""