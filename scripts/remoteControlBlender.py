import bpy
import numpy as np
import mathutils as mu
import math
import zmq
import threading
import time

def setJoint(index, angle):
    arm = bpy.data.objects['Armature']
    bone = arm.pose.bones['Bone.{:03d}'.format(index)]
    #bone.rotation_quaternion = Quaternion((1, 0, 0, -0.1))
    bone.rotation_quaternion = mu.Matrix.Rotation(math.radians(angle), 3, 'X').to_quaternion()    

def setJointByName(boneName, angle1, angle2):
    arm = bpy.data.objects['Armature']
    bone = arm.pose.bones[boneName]
    #bone.rotation_quaternion = Quaternion((1, 0, 0, -0.1))
    bone.rotation_quaternion = (mu.Matrix.Rotation(math.radians(angle1), 3, 'X') @ mu.Matrix.Rotation(math.radians(angle2), 3, 'Z')).to_quaternion()    

#for i in range(1, 25):
#    setJoint(i, np.random.random() * 10 - 5)

def threadLoop():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5555")
    doLoop = True
    while(doLoop):
        message = socket.recv()
        print(message)
        if (message == b"stop"):
            doLoop = False
        time.sleep(0.1)
        socket.send(b"ok")
    print("exit remote control loop")

t = threading.Thread(target=threadLoop)
t.start()

