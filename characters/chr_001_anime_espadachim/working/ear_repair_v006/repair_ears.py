import bpy,bmesh,sys,json,numpy as np
from pathlib import Path
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=sys.argv[-2])
out=Path(sys.argv[-1]);out.mkdir(parents=True,exist_ok=True)
o=next(o for o in bpy.context.scene.objects if o.type=='MESH');m=o.data
before=len(m.polygons)
bm=bmesh.new();bm.from_mesh(m)
# Unir apenas duplicatas de posição na região das orelhas; preservar UVs por loop.
near=[v for v in bm.verts if .065<abs(v.co.x)<.115 and -.03<v.co.y<.045 and .74<v.co.z<.815]
bmesh.ops.remove_doubles(bm,verts=near,dist=.000002)
old_boundary=set(e for e in bm.edges if e.is_boundary)
def roi(v):
 p=v.co
 return .071<abs(p.x)<.105 and -.018<p.y<.025 and .745<p.z<.795
faces=[f for f in bm.faces if all(roi(v) for v in f.verts)]
edges=list({e for f in faces for e in f.edges});verts=list({v for f in faces for v in f.verts})
res=bmesh.ops.bisect_plane(bm,geom=faces+edges+verts,dist=.0000001,plane_co=(0,0,.781),plane_no=(0,0,1),clear_inner=True,clear_outer=False)
new_boundary=[e for e in bm.edges if e.is_boundary and e not in old_boundary]
bound_stats={'old_boundary':len(old_boundary),'new_boundary':len(new_boundary),'points':[[float(c) for c in v.co] for e in new_boundary for v in e.verts]}
(out/'boundary.json').write_text(json.dumps(bound_stats))
uv=bm.loops.layers.uv.active
im=next(n.image for mat in m.materials for n in mat.node_tree.nodes if n.type=='TEX_IMAGE');w,h=im.size
pix=np.empty(w*h*4,dtype=np.float32);im.pixels.foreach_get(pix);pix=pix.reshape(h,w,4)
def skin_uv(u):
 rgb=pix[min(h-1,max(0,int(u.y*h))),min(w-1,max(0,int(u.x*w))),:3]
 return rgb[0]>.35 and rgb[0]>rgb[2]*1.5

# UV de pele adjacente para cada tampa; sem alterar a textura original.
cap_faces=[]
while new_boundary:
 seed=new_boundary.pop();group={seed};stack=[seed]
 while stack:
  e=stack.pop()
  for v in e.verts:
   for n in v.link_edges:
    if n in new_boundary:
     new_boundary.remove(n);group.add(n);stack.append(n)
 uvs=[l[uv].uv.copy() for e in group for f in e.link_faces for l in f.loops if l.vert in e.verts]
 skin=[u for u in uvs if skin_uv(u)]
 avg=skin[0] if skin else (uvs[0] if uvs else None)
 caps=bmesh.ops.holes_fill(bm,edges=list(group),sides=0)['faces'];cap_faces.extend(caps)
 for f in caps:
  f.material_index=0;f.smooth=True
  for l in f.loops:
   if avg is not None:l[uv].uv=avg
cap_original_verts={v for f in cap_faces for v in f.verts}
cap_edges=list({e for f in cap_faces for e in f.edges})
sub=bmesh.ops.subdivide_edges(bm,edges=cap_edges,cuts=1,use_grid_fill=True)
local_verts=list(cap_original_verts|{g for g in sub['geom_inner'] if isinstance(g,bmesh.types.BMVert)})
local_verts=[v for v in local_verts if v.is_valid]
for _ in range(6):bmesh.ops.smooth_vert(bm,verts=local_verts,factor=.45,use_axis_x=True,use_axis_y=True,use_axis_z=True)
local_set=set(local_verts)
bmesh.ops.recalc_face_normals(bm,faces=[f for f in bm.faces if any(v in local_set for v in f.verts)])
report={'source':'source/attempt_005/textured_n1.glb','method':'Local bisect and capped removal of bilateral ear appendages','cut_z':.781,'roi':{'abs_x':[.071,.105],'y':[-.018,.025],'z':[.745,.795]},'source_triangles':before,'caps':len(cap_faces),'smoothing_passes':6,'uv_strategy':'Sample adjacent skin UV; never average across UV islands','remaining_new_boundary_edges':sum(e.is_boundary and e not in old_boundary for e in bm.edges)}
bm.to_mesh(m);bm.free();m.update()
bpy.ops.wm.save_as_mainfile(filepath=str(out/'ear_repaired.blend'))
bpy.ops.export_scene.gltf(filepath=str(out/'ear_repaired.glb'),export_format='GLB',export_yup=True,export_normals=True,export_materials='EXPORT')
report['polygons_after']=len(m.polygons)
(out/'repair_report.json').write_text(json.dumps(report,indent=2),encoding='utf8')
