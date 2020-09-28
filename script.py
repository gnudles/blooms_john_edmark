import bpy,math;
phiang=2.0*math.pi*(1-(5**0.5-1)/2)
def edmark(frame_count,num_objects):
    SR=5
    R=0
    a=0
    b=0
    for i in range(frame_count):
        s=(i/2.0+5.0)/50.0
        for j in range(num_objects):
            c=bpy.context.active_object.copy();
            x = R*math.cos(a+2.0*math.pi*j/num_objects)
            y = R*math.sin(a+2.0*math.pi*j/num_objects)
            z = SR*math.cos(b)-SR
            c.location=(x,y,z)
            c.rotation_euler[2]=a;
            c.scale=(s,s,s);
            bpy.context.collection.objects.link(c)
        a+=phiang;
        b+=math.pi*0.5/frame_count
        R=SR*math.sin(b)
edmark(60,6)

