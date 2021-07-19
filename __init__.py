bl_info = {
    "name": "bbb",
    "author": "bbb",
    "blender": (2, 93, 0),
    "version": (0, 1, 1),
    "category": "Object"
}


debug = 1 # 1 (ON) / 0 (OFF) or any value

modules = ("op", "panel") # "modules" you need to import/reload/register/unregister 
#"utils" is imported in "op" module, see the reload there

for mod in modules:
    exec(f"from . import {mod}")


def register():

    import importlib
    for mod in modules:
        if debug:
        # if mod in locals(): # not working there
            exec(f"importlib.reload({mod})")
        exec(f"{mod}.register()")


def unregister():

    for mod in modules:
        exec(f"{mod}.unregister()".format(mod=mod))
