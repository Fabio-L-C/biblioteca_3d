import bpy,sys,json,math
from pathlib import Path
from mathutils import Vector
src=Path(sys.argv[-2]);out=Path(sys.argv[-1]);out.mkdir(parents=True,exist_ok=True)
reports={}
for kind in ['rigged','walk','run']:
 bpy.ops.wm.read_factory_settings(use_empty=True)
 bpy.ops.import_scene.gltf(filepath=str(src/(kind+'.glb')))
 scene=bpy.context.scene;meshes=[o for o in scene.objects if o.type=='MESH' and any(m.type=='ARMATURE' for m in o.modifiers)];arms=[o for o in scene.objects if o.type=='ARMATURE']
 actions=list(bpy.data.actions);ranges=[list(a.frame_range) for a in actions]
 start=min((r[0] for r in ranges),default=0);end=max((r[1] for r in ranges),default=0)
 frames=[start] if kind=='rigged' else [start+(end-start)*.25,start+(end-start)*.75]
 details={'armatures':len(arms),'bones':sum(len(o.data.bones) for o in arms),'action_ranges':ranges,'frames':frames,'samples':[],'unweighted_vertices':sum(not any(g.weight>0 for g in v.groups) for o in meshes for v in o.data.vertices)}
 scene.frame_set(round(start))
 points=[o.matrix_world@Vector(c) for o in meshes for c in o.bound_box];lo=Vector(tuple(min(p[i] for p in points) for i in range(3)));hi=Vector(tuple(max(p[i] for p in points) for i in range(3)))
 center=(lo+hi)/2;height=hi.z-lo.z
 scene.render.engine='CYCLES';scene.cycles.samples=8;scene.render.resolution_x=720;scene.render.resolution_y=900;scene.render.resolution_percentage=100
 scene.world=bpy.data.worlds.new('review_world');scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.65,.65,.65,1);scene.world.node_tree.nodes['Background'].inputs[1].default_value=.6
 for offset,power,size in [((2,-3,3),500,4),((-3,-1,1),250,3),((0,3,2),400,3)]:
  lamp=bpy.data.lights.new('review_light','AREA');lamp.energy=power;lamp.shape='DISK';lamp.size=size;obj=bpy.data.objects.new('review_light',lamp);scene.collection.objects.link(obj);obj.location=center+Vector(offset)*height;obj.rotation_euler=(center-obj.location).to_track_quat('-Z','Y').to_euler()
 data=bpy.data.cameras.new('review_camera');data.type='ORTHO';data.ortho_scale=height*1.3;cam=bpy.data.objects.new('review_camera',data);scene.collection.objects.link(cam);scene.camera=cam
 for i,frame in enumerate(frames):
  scene.frame_set(int(frame),subframe=frame-int(frame));deps=bpy.context.evaluated_depsgraph_get();pts=[]
  for o in meshes:
   ev=o.evaluated_get(deps);me=ev.to_mesh();pts.extend(o.matrix_world@v.co for v in me.vertices);ev.to_mesh_clear()
  vmin=Vector(tuple(min(p[j] for p in pts) for j in range(3)));vmax=Vector(tuple(max(p[j] for p in pts) for j in range(3)));target=(vmin+vmax)/2
  cam.location=target+Vector((1.7,-4,.1))*height;cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler()
  scene.render.filepath=str(out/(kind+'_'+str(i)+'.png'));bpy.ops.render.render(write_still=True)
  details['samples'].append({'frame':frame,'min':list(vmin),'max':list(vmax),'finite':all(math.isfinite(c) for p in pts for c in p)})
 reports[kind]=details
 (out/'deformation_report.json').write_text(json.dumps(reports,indent=2),encoding='utf8')
