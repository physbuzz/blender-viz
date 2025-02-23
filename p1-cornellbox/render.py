import bpy
bpy.data.scenes["Scene"].render.filepath = "p01_0001.png"
bpy.ops.render.render(write_still=True)

