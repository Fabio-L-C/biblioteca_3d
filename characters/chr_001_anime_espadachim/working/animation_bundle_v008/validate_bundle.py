import bpy,sys,json,math
from pathlib import Path
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=sys.argv[-2])
out=Path(sys.argv[-1]);arms=[o for o in bpy.context.scene.objects if o.type=='ARMATURE'];arm=arms[0]
meshes=[o for o in bpy.context.scene.objects if o.type=='MESH' and any(m.type=='ARMATURE' for m in o.modifiers)]
for tr in arm.animation_data.nla_tracks:tr.mute=True
report={'armatures':len(arms),'bones':len(arm.data.bones),'unweighted_vertices':sum(not any(g.weight>0 for g in v.groups) for o in meshes for v in o.data.vertices),'clips':[]}
for action in list(bpy.data.actions):
 action.use_fake_user=True;arm.animation_data.action=action
 if len(action.slots):arm.animation_data.action_slot=action.slots[0]
 start,end=action.frame_range;samples=[]
 for t in [0,.125,.25,.375,.5,.625,.75,.875,1]:
  frame=start+(end-start)*t;bpy.context.scene.frame_set(int(frame),subframe=frame-int(frame));deps=bpy.context.evaluated_depsgraph_get();pts=[]
  for o in meshes:
   ev=o.evaluated_get(deps);m=ev.to_mesh();pts.extend(o.matrix_world@v.co for v in m.vertices);ev.to_mesh_clear()
  samples.append({'fraction':t,'finite':all(math.isfinite(c) for p in pts for c in p),'min':[min(p[i] for p in pts) for i in range(3)],'max':[max(p[i] for p in pts) for i in range(3)]})
 report['clips'].append({'name':action.name,'frame_range':[start,end],'samples':samples})
arm.animation_data.action=None;bpy.context.scene.frame_set(0)
for o in bpy.context.selected_objects:o.select_set(False)
for o in meshes:o.select_set(True)
bpy.context.view_layer.objects.active=meshes[0]
bpy.ops.file.pack_all();bpy.ops.wm.save_as_mainfile(filepath=str(out/'chr_001_anime_espadachim_v008.blend'))
(out/'blender_validation.json').write_text(json.dumps(report,indent=2),encoding='utf8')
