import bpy

fileName = 'd:/dev/hand/landscape.jpg'

obj = bpy.data.objects['Plane']

# Get material
mat = bpy.data.materials.get("Material")
if mat is None:
    # create material
    mat = bpy.data.materials.new(name="Material")

mat.use_nodes = True
bsdf = mat.node_tree.nodes['Principled BSDF']
texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load(fileName)
mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

obj.data.materials.append(mat)

