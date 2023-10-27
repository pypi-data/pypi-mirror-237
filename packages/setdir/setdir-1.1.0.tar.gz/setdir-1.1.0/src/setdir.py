from typing import Callable
import sys
import os.path
import atexit
__location__ = os.path.dirname(os.path.realpath(sys.argv[0]))
index = 0
typePCS = False
def get(PCS, folder, depth):
    global typePCS
    if PCS != "parent" and PCS != "sibling" and PCS != "child":
        return False
    typePCS = [PCS, depth]
    return get_path(folder)

def get_path(folder: str) -> Callable[[str], str]:
    global typePCS
    def do(sI, folder):
        getting = {
            "child": lambda x: os.path.split(os.curdir)[1],
            "sibling": lambda x: os.path.split(os.curdir)[1 + index],
            "parent": os.pardir
        }
        workdir = __location__
        sys.path.append(workdir)
        return os.path.abspath(os.path.join(workdir, *[getting[sI[0]] for _ in range(sI[1])], folder))
    if not typePCS:
        sI = typePCS
        with open(os.path.join(__location__,"innerdir")) as innerdir:
            opt = innerdir.read().split(",")
            assert opt[0] == "parent"
            index = int(opt[1])
            del opt
        return atexit.register(lambda: do(sI, folder))
    return do(typePCS, folder)
    