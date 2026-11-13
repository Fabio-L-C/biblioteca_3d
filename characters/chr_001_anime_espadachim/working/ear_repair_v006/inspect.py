import bpy,json,sys
from mathutils import Vector
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=sys.argv[-2])
result=[]
for o in [o for o in bpy.context.scene.objects if o.type=='MESH']:
 m=o.data
 adj=[[] for v in m.vertices]
 for e in m.edges:
  a,b=e.vertices;adj[a].append(b);adj[b].append(a)
 seen=set();cs=[]
 for v in m.vertices:
  if v.index in seen:continue
  seen.add(v.index);stack=[v.index];ids=[]
  while stack:
   k=stack.pop();ids.append(k)
   for n in adj[k]:
    if n not in seen:seen.add(n);stack.append(n)
  pts=[o.matrix_world@m.vertices[k].co for k in ids]
  cs.append({'count':len(ids),'seed':ids[0],'min':[min(p[i] for p in pts) for i in range(3)],'max':[max(p[i] for p in pts) for i in range(3)]})
 result.append({'name':o.name,'vertices':len(m.vertices),'components':sorted(cs,key=lambda c:-c['count'])})
open(sys.argv[-1],'w').write(json.dumps(result))
