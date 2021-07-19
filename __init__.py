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

if debug:
    if "bpy" in locals():
        import importlib

        for module in modules:
            if module in locals():
                importlib.reload(locals()[module])

for mod in modules:
    try:
        exec(f"from . import {mod}")
    except Exception as e:
        print(e)

# using my addon you can rid off all try except, because it's already dealing with errors.
# but if installing a zip with blender. without any try except the error (like a wrong name of module imported)
# the error become silent. the addon is installed but you can't enable it. the console telling: addon not found :)

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
