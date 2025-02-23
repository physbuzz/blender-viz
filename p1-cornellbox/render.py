import bpy
bpy.data.scenes["Scene"].render.filepath = "p1_0001.png"
bpy.ops.render.render(write_still=True)

