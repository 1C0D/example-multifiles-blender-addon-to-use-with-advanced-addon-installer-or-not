import sys

bl_info = {
    "name": "bbb",
    "author": "bbb",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "category": "Object"
}

debug = 1 # 1 (ON) / 0 (OFF) or any value

modules = ("op", "panel") # "modules" you need to import/reload(debug ON)/register/unregister 

for mod in modules:
    try:
        exec(f"from . import {mod}")
    except Exception as e:
        print(e)


def register():
   
    import importlib
    for mod in modules:
        try:
            if debug:
                exec(f"importlib.reload({mod})")
            exec(f"{mod}.register()")
        except Exception as e:
            print(e)

def unregister():

    for mod in modules:
        try:
            exec(f"{mod}.unregister()")
        except Exception as e:
            print(e)
