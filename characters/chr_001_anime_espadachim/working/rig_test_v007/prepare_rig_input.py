import bpy,sys,json,math
from pathlib import Path
from mathutils import Vector
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=sys.argv[-2])
out=Path(sys.argv[-1]);out.mkdir(parents=True,exist_ok=True)
o=next(o for o in bpy.context.scene.objects if o.type=='MESH');bpy.context.view_layer.objects.active=o;o.select_set(True)
original=len(o.data.polygons)
mod=o.modifiers.new('rig_limit_copy','DECIMATE');mod.decimate_type='COLLAPSE';mod.ratio=299000/original;mod.use_collapse_triangulate=True
bpy.ops.object.modifier_apply(modifier=mod.name)
mesh=o.data
tris=sum(len(p.vertices)-2 for p in mesh.polygons)
pts=[o.matrix_world@v.co for v in mesh.vertices]
report={'source':'exports/v006/chr_001_anime_espadachim_v006.glb','tool':'Blender 5.2','method':'Local collapse decimation in separate copy; no new generation','source_triangles':original,'triangles':tris,'vertices':len(mesh.vertices),'target_triangles':299000,'under_rig_limit':tris<=300000,'rig':False,'pose':'T-pose','height_uncalibrated':True,'bounds_min':[min(v[i] for v in pts) for i in range(3)],'bounds_max':[max(v[i] for v in pts) for i in range(3)],'meshy_credits_consumed':0,'status':'prepared_locally_not_uploaded','pending':['Explicit approval to upload corrected derivative to Meshy and start rig (5 credits)','Rig and deformation tests']}
bpy.ops.wm.save_as_mainfile(filepath=str(out/'rig_input.blend'))
bpy.ops.export_scene.gltf(filepath=str(out/'rig_input.glb'),export_format='GLB',export_yup=True,export_normals=True)
(out/'preparation_report.json').write_text(json.dumps(report,indent=2),encoding='utf8')
