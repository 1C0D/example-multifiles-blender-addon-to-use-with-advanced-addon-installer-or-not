import sys

bl_info = {
    "name": "bbb",
    "author": "bbb",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "category": "Object"
}

debug = 0 # 0 (ON) / 1 (OFF) or any value

modules = ("op", "panel") # "modules" you need to import/reload(debug ON)/register/unregister 

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

