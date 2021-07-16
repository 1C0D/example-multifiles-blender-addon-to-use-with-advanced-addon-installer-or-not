import sys

bl_info = {
    "name": "bbb",
    "author": "bbb",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "category": "Object"
}

debug = 0 # 0 (ON) or 1 (OFF)

modules = ("op", "panel") # the "modules" there you need to import/reload (if debug ON)/register/unregister 

for mod in modules:
    try:
        exec("from . import {mod}".format(mod=mod))
    except Exception as e:
        print(e)


def register():
   
    import importlib
    for mod in modules:
        try:
            if debug:
                exec("importlib.reload({mod})".format(mod=mod))
            exec("{mod}.register()".format(mod=mod))
        except Exception as e:
            print(e)

def unregister():

    for mod in modules:
        try:
            exec("{mod}.unregister()".format(mod=mod))
        except Exception as e:
            print(e)

