import bpy, sys, json, math
from pathlib import Path
from mathutils import Vector
args = sys.argv[sys.argv.index('--') + 1:]
model, prefix = args[:2]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(Path(model).resolve()))
meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH']
points = [o.matrix_world @ Vector(c) for o in meshes for c in o.bound_box]
lo = Vector(tuple(min(v[i] for v in points) for i in range(3)))
hi = Vector(tuple(max(v[i] for v in points) for i in range(3)))
center = (lo + hi) / 2
height = hi.z - lo.z
for obj in meshes:
    if not obj.data.materials:
        mat = bpy.data.materials.new('neutral_review')
        mat.diffuse_color = (0.52, 0.57, 0.65, 1)
        obj.data.materials.append(mat)
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.samples = 12
scene.render.resolution_x = 900
scene.render.resolution_y = 900
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.world = bpy.data.worlds.new('review_world')
scene.world.use_nodes = True
scene.world.node_tree.nodes['Background'].inputs[0].default_value = (0.65, 0.65, 0.65, 1)
scene.world.node_tree.nodes['Background'].inputs[1].default_value = 0.6
for offset, power, size in [((2,-3,3),500,4),((-3,-1,1),250,3),((0,3,2),400,3)]:
    lamp = bpy.data.lights.new('review_light','AREA')
    lamp.energy = power
    lamp.shape = 'DISK'
    lamp.size = size
    obj = bpy.data.objects.new('review_light',lamp)
    scene.collection.objects.link(obj)
    obj.location = center + Vector(offset) * height
    obj.rotation_euler = (center - obj.location).to_track_quat('-Z','Y').to_euler()
cam_data = bpy.data.cameras.new('review_camera')
cam_data.type = 'ORTHO'
cam_data.ortho_scale = max(height, hi.x-lo.x, hi.y-lo.y) * 1.15
cam = bpy.data.objects.new('review_camera',cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
Path(prefix).parent.mkdir(parents=True,exist_ok=True)
for name, direction in [('front',(0,-4,0)),('side',(-4,0,0)),('back',(0,4,0))]:
    cam.location = center + Vector(direction) * height
    cam.rotation_euler = (center - cam.location).to_track_quat('-Z','Y').to_euler()
    scene.render.filepath = prefix + '_' + name + '.png'
    bpy.ops.render.render(write_still=True)
head_center = Vector((center.x, center.y, lo.z + height * 0.9))
cam_data.ortho_scale = height * 0.27
scene.render.resolution_x = 900
scene.render.resolution_y = 900
for name, direction in [('head_front',(0,-4,0)),('head_threequarter',(2,-4,0)),('head_left',(-2,-4,0)),('ear_right',(4,0,0)),('ear_left',(-4,0,0))]:
    cam.location = head_center + Vector(direction) * height
    cam.rotation_euler = (head_center - cam.location).to_track_quat('-Z','Y').to_euler()
    scene.render.filepath = prefix + '_' + name + '.png'
    bpy.ops.render.render(write_still=True)
hand_points = [o.matrix_world @ v.co for o in meshes for v in o.data.vertices if (o.matrix_world @ v.co).x < lo.x + (hi.x-lo.x)*0.15]
hand_center = Vector(tuple((min(p[i] for p in hand_points)+max(p[i] for p in hand_points))/2 for i in range(3))) if hand_points else Vector((lo.x,center.y,lo.z+height*0.8))
cam_data.ortho_scale = height * 0.22
cam.location = hand_center + Vector((0,-4,0)) * height
cam.rotation_euler = (hand_center - cam.location).to_track_quat('-Z','Y').to_euler()
scene.render.filepath = prefix + '_hand.png'
bpy.ops.render.render(write_still=True)
print(json.dumps({'meshes':len(meshes),'polygons':sum(len(o.data.polygons) for o in meshes),'bounds_min':list(lo),'bounds_max':list(hi),'rigs':sum(o.type=='ARMATURE' for o in scene.objects)}))
