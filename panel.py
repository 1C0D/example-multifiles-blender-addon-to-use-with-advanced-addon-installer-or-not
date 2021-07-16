import bpy

class Test_PT_Panel(bpy.types.Panel):
    #bl_idname = "Test_PT_Panel"
    bl_label = "Test Panel"
    bl_category = "Test Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.label(text='toto')  # try to change text there to see direct changes after reinstalling it with advanced addon installer
        col = layout.column(align=True)
        col.operator('object.simple_operator')


def register():
    bpy.utils.register_class(Test_PT_Panel)

def unregister():
    bpy.utils.unregister_class(Test_PT_Panel)
