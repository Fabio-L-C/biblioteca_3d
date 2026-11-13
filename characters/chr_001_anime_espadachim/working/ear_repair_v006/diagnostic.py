import bpy,sys,json,numpy as np
from mathutils import Vector
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=sys.argv[-2])
o=next(o for o in bpy.context.scene.objects if o.type=='MESH');m=o.data
im=next(n.image for mat in m.materials for n in mat.node_tree.nodes if n.type=='TEX_IMAGE');w,h=im.size
pix=np.empty(w*h*4,dtype=np.float32);im.pixels.foreach_get(pix);pix=pix.reshape(h,w,4)
uv=m.uv_layers.active.data
mask=[];samples=[]
for f in m.polygons:
 p=o.matrix_world@f.center
 if .07<abs(p.x)<.112 and .745<p.z<.803:
  u=sum((uv[i].uv for i in f.loop_indices),Vector((0,0)))/len(f.loop_indices)
  rgb=pix[min(h-1,max(0,int(u.y*h))),min(w-1,max(0,int(u.x*w))),:3]
  if rgb[0]>.3 and rgb[0]>rgb[2]*1.5:
   mask.append(f.index);samples.append([*p,*[float(c) for c in rgb]])
mat=bpy.data.materials.new('selected_appendages');mat.diffuse_color=(1,0,0,1);m.materials.append(mat)
for k in mask:m.polygons[k].material_index=len(m.materials)-1
open(sys.argv[-1]+'/selection.json','w').write(json.dumps({'faces':mask,'samples':samples}))
bpy.ops.wm.save_as_mainfile(filepath=sys.argv[-1]+'/diagnostic.blend')
