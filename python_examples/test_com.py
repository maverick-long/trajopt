

"""Loads up an environment, attaches a viewer, loads a scene, and requests information about the robot.
"""
from openravepy import *
# import array
import time
from numpy import *
from numpy.linalg import inv

def draw_ax(T, size, env, handles):
    p0 = T[:3,3]
    xax, yax, zax = T[:3,:3].T*size
    width = size/20.
    handles.append(env.drawarrow(p0, p0+xax, width, [1,0,0]))
    handles.append(env.drawarrow(p0, p0+yax, width, [0,1,0]))
    handles.append(env.drawarrow(p0, p0+zax, width, [0,0,1]))

env = Environment() # create openrave environment
env.SetViewer('qtcoin') # attach viewer (optional)
# viewer = trajoptpy.GetViewer(env)
env.Load('../val_motionplanning/valkyrie_description/valkyrie_C.dae') # load a simple scene
# env.Load('../data/door.xml') # load a simple scene
robot = env.GetRobots()[0] # get the first robot
kinbody = env.GetBodies()
activejoint = [robot.GetJoint("leftHipYaw").GetDOFIndex(),robot.GetJoint("leftHipRoll").GetDOFIndex(),
               robot.GetJoint("leftHipPitch").GetDOFIndex(),robot.GetJoint("leftKneePitch").GetDOFIndex(),
               robot.GetJoint("leftAnklePitch").GetDOFIndex(),robot.GetJoint("leftAnkleRoll").GetDOFIndex(),
               robot.GetJoint("rightHipYaw").GetDOFIndex(),robot.GetJoint("rightHipRoll").GetDOFIndex(),
               robot.GetJoint("rightHipPitch").GetDOFIndex(),robot.GetJoint("rightKneePitch").GetDOFIndex(),
               robot.GetJoint("rightAnklePitch").GetDOFIndex(),robot.GetJoint("rightAnkleRoll").GetDOFIndex(),
               robot.GetJoint("torsoYaw").GetDOFIndex(),robot.GetJoint("torsoPitch").GetDOFIndex(),
               robot.GetJoint("torsoRoll").GetDOFIndex(),robot.GetJoint("leftShoulderPitch").GetDOFIndex(),
               robot.GetJoint("leftShoulderRoll").GetDOFIndex(),robot.GetJoint("leftShoulderYaw").GetDOFIndex(),
               robot.GetJoint("leftElbowPitch").GetDOFIndex(),robot.GetJoint("leftForearmYaw").GetDOFIndex(),
               robot.GetJoint("leftWristRoll").GetDOFIndex(),robot.GetJoint("leftWristPitch").GetDOFIndex(),
               robot.GetJoint("lowerNeckPitch").GetDOFIndex(),robot.GetJoint("neckYaw").GetDOFIndex(),
               robot.GetJoint("upperNeckPitch").GetDOFIndex(),robot.GetJoint("rightShoulderPitch").GetDOFIndex(),
               robot.GetJoint("rightShoulderRoll").GetDOFIndex(),robot.GetJoint("rightShoulderYaw").GetDOFIndex(),
               robot.GetJoint("rightElbowPitch").GetDOFIndex(),robot.GetJoint("rightForearmYaw").GetDOFIndex(),
               robot.GetJoint("rightWristRoll").GetDOFIndex(),robot.GetJoint("rightWristPitch").GetDOFIndex()]

robot.SetActiveDOFs(activejoint)
# robot.SetActiveDOFValues([0, 0, -0.62, 1.34, -0.72, 0,
#                                   0, 0, -0.62, 1.34, -0.72, 0,
#                                   0, 0, 0,
#                                   -0.2,-1.2, 0.70, -1.5, 1.3, 0.024, 0.0454, 
#                                   0, 0, 0, 
#                                   -0.2, 1.2, 0.70, 1.5, 1.3, -0.024, -0.0454])

robot.SetActiveDOFValues([-0.040029726922512054, -0.03369460999965668, -0.44156399369239807, 1.0303349494934082, -0.67119961977005, 0.05691482871770859, 
                          -0.01733711175620556, 0.07575292885303497, -0.4435535967350006, 1.0348072052001953, -0.6449311375617981, -0.07128202170133591, 
                          -0.030195342376828194, -0.03811405599117279, 0.008478663861751556, 
                          -0.16961249709129333, -1.1993234157562256, 0.6941242814064026, -1.5178706645965576, 0.0, 0.0, 0.0, 
                          0.014572739601135254, -0.0004940032958984375, 0.0, 
                          -0.19163087010383606, 1.2046902179718018, 0.6956586837768555, 1.506352424621582, 0.0, 0.0, 0.0])

# Set transparency of the robot
for link in robot.GetLinks():
            for geom in link.GetGeometries():
                geom.SetTransparency(0.8)

# Set up robot in initial transform
# init_transform = numpy.eye(4)
# init_transform[:3,3] = [-0.4, -0.2, .08]
# robot.SetTransform(init_transform)

# Tz = matrixFromAxisAngle([0,0,numpy.pi/3])
# robot.SetTransform(numpy.dot(Tz,robot.GetTransform()))

robot.SetTransform(inv(robot.GetLink("leftFoot").GetTransform()))

handles = []
# T = robot.GetLink("l_hand").GetTransform()
# # handles.append(drawTransform(T,length=0.2))
# draw_ax(T, 0.1, env, handles)

# # T = (kinbody[1].GetLinks())[2].GetTransform()
# # T[:3,3] = T[:3,3]+[-0.12, -0.34, 0.95]
# # draw_ax(T, 0.1, env, handles)

# T = robot.GetLink("l_palm").GetTransform()
# Tz = numpy.dot(matrixFromAxisAngle([-numpy.pi/2,0,0]),matrixFromAxisAngle([0,0,numpy.pi/2]))
# Tz[:3,3] = Tz[:3,3]+[0, 0.12, 0]
# T = numpy.dot(T,Tz)
# draw_ax(T, 0.1, env, handles)

# T = robot.GetLink("l_foot").GetTransform()
# T[:3,3] = T[:3,3]+[0.25, 0.4, 0]
# draw_ax(T, 0.1, env, handles)

for link in robot.GetLinks():
	compoint = link.GetGlobalCOM()
	handles.append(env.plot3(points=array(compoint),
                                           pointsize=0.02,
                                           colors=array(((0,0,1))),
                                           drawstyle=1))

# handles.append(env.plot3(points=[0,0, 0],
#                           pointsize=0.02,
#                           colors=array(((0,1,0))),
#                           drawstyle=1))

compoint = robot.GetCenterOfMass()
handles.append(env.plot3(points=[compoint[0],compoint[1],0],
                          pointsize=0.02,
                          colors=array(((1,0,0))),
                          drawstyle=1))

print "com: %f, %f, %f" % (compoint[0],compoint[1],compoint[2])
compoint = robot.GetLink("rightFoot").GetGlobalCOM()
print "com: %f, %f, %f" % (compoint[0],compoint[1],compoint[2])
newrobots = []
newrobot = RaveCreateRobot(env,robot.GetXMLId())
newrobot.Clone(robot,0)
newrobots.append(newrobot)

with env:
  env.Add(newrobot,True)
  # hand = newrobot.GetLink("l_palm")
  # T = (kinbody[1].GetLinks())[2].GetTransform()
  # T[:3,3] = T[:3,3]+[-0.12, -0.34, 0.95]
  # Tz = numpy.dot(matrixFromAxisAngle([0,-numpy.pi/2,0]),matrixFromAxisAngle([0,0,-numpy.pi/2]))
  # Tz[:3,3] = Tz[:3,3]+[0, 0, -0.12]
  # T = numpy.dot(T,Tz)
  # hand.SetTransform(T)
  
  # T = hand.GetTransform()
  # T[:3,3] = T[:3,3]+[-0.12, 0, 0]
  # draw_ax(T, 0.1, env, handles)

wait = input("PRESS ENTER TO CONTINUE.")


