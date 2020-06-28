import bpy
import math
import mathutils as mu
import random
import numpy as np
import time

print('Hello Hand!')

arm = bpy.data.objects['Armature']

def setJoint(index, angle):
    bone = arm.pose.bones['Bone.{:03d}'.format(index)]
    #bone.rotation_quaternion = Quaternion((1, 0, 0, -0.1))
    bone.rotation_quaternion = mu.Matrix.Rotation(math.radians(angle), 3, 'X').to_quaternion()    

def setJointByName(boneName, angle1, angle2):
    bone = arm.pose.bones[boneName]
    #bone.rotation_quaternion = Quaternion((1, 0, 0, -0.1))
    bone.rotation_quaternion = (mu.Matrix.Rotation(math.radians(angle1), 3, 'X') @ mu.Matrix.Rotation(math.radians(angle2), 3, 'Z')).to_quaternion()    

setZero = False
saveImages = False
numPoses = 1

ranges = [
[-15, 15],
[-25, 60], 
[-45, 0], 
[-45, 0], 

[0, 0],
[-5, 5], 
[-45, 30], 
[-45, 30], 
[-45, 15], 

[0, 0], 
[-5, 5], 
[-45, 30], 
[-45, 30], 
[-45, 15],
 
[0, 0], 
[-5, 5], 
[-30, 15], 
[-30, 15], 
[-30, 10], 

[0, 0], 
[-15, 5], 
[-30, 15], 
[-30, 15], 
[-30, 15]
]

enabled = [ 
1,
1,
1,
1, # <- end of thumb

1,
1,
1,
1,
1, # <- end of pointer finger

1,
1,
1,
1,
1, # <- end of middle finger

1,
1,
1,
1,
1,

1,
1,
1,
1, 
1]



ranges = np.array(ranges)

for k in range(0, numPoses):
    for i in range(1, 25):
        idx = i - 1
        if ((enabled[idx] < 0.5) or setZero):
            angle = 0
        else:
            r = ranges[idx, 1] - ranges[idx, 0]
            angle = (random.random()) * r + ranges[idx, 0]
        setJoint(i, angle)

    rootAngle1 = (random.random() - 0.5) * 80
    rootAngle2 = (random.random() - 0.5) * 40
    if (setZero):
        rootAngle1 = 0
        rootAngle2 = 0
    #rootAngle1 = rootAngle2 = 0
    setJointByName('Bone.HandRoot', (random.random()-0.5) * rootAngle1, (random.random() - 0.5) * rootAngle2)

    x = (random.random() - 0.5) * 5
    y = (random.random() - 0.5) * 5
    z = (random.random() - 0.5) * 5
    #x = y = z = 0
    bpy.data.objects['HandFrame'].location = mu.Vector((x, y, z))

    if saveImages:
        bpy.context.scene.render.filepath = 'c:\\tmp\\image_{:06d}.jpg'.format(k)
        bpy.ops.render.render(write_still = True)
