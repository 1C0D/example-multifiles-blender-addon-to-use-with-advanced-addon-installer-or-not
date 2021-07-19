import bpy
from .utils import ChangeName
from .__init__ import debug #to get the value of debug

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"
    bl_options = {'UNDO'}    

    def execute(self, context):

        print('aaaa')
        ChangeName.print_name() # try a change in utils

        return {'FINISHED'}


def register():
    
    if debug:
        import importlib
        from . import utils # doing from .utils import ChangeName, the module is not imported, so we couldn't reload it
        importlib.reload(utils) ## 
    
    bpy.utils.register_class(SimpleOperator)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
