# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-18.57.30 176069
# Run by ltiaulas2019 on Thu Oct 24 15:01:56 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=398.0, 
    height=244.533340454102)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(pathName='C:/temp/g13-umero.cae')
#: The model database "C:\temp\g13-umero.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.071, 
    farPlane=223.677, width=217.814, height=105.383, viewOffsetX=6.1887, 
    viewOffsetY=1.0844)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=171.474, 
    farPlane=205.65, width=252.502, height=122.165, cameraPosition=(22.0872, 
    -11.4307, 188.562), cameraTarget=(22.0872, -11.4307, 0))
session.Image(name='osso-protese', fileName='C:/temp/osso-protese.png')
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    showImage=True, imageName='osso-protese')
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.4326, 
    farPlane=349.691, width=2380.97, height=1151.96, cameraPosition=(235.764, 
    -254.079, 188.562), cameraTarget=(235.764, -254.079, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.1478, 
    farPlane=359.976, cameraPosition=(472.182, 139.238, 188.562), 
    cameraTarget=(472.182, 139.238, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.1479, 
    farPlane=359.976, cameraPosition=(505.756, 130.84, 188.562), cameraTarget=(
    505.756, 130.84, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.1479, 
    farPlane=359.976, cameraPosition=(540.729, 193.827, 188.562), 
    cameraTarget=(540.729, 193.827, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.1479, 
    farPlane=359.976, cameraPosition=(483.373, 165.833, 188.562), 
    cameraTarget=(483.373, 165.833, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=116.478, 
    farPlane=260.646, width=941.179, height=455.36, cameraPosition=(190.103, 
    216.513, 188.562), cameraTarget=(190.103, 216.513, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=120.803, 
    farPlane=256.321, cameraPosition=(184.02, 182.762, 188.562), cameraTarget=(
    184.02, 182.762, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=111.877, 
    farPlane=265.247, width=1133.15, height=548.241, cameraPosition=(219.55, 
    176.729, 188.562), cameraTarget=(219.55, 176.729, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=106.983, 
    farPlane=270.141, cameraPosition=(217.553, 138.092, 188.562), 
    cameraTarget=(217.553, 138.092, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=101.775, 
    farPlane=275.349, width=1282.43, height=620.462, cameraPosition=(245.882, 
    133.924, 188.562), cameraTarget=(245.882, 133.924, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=96.2358, 
    farPlane=280.888, cameraPosition=(255.677, 168.603, 188.562), 
    cameraTarget=(255.677, 168.603, 0))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    sheetSize=1000.0, sheetAuto=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=144.622, 
    farPlane=232.502, width=649.291, height=314.139, cameraPosition=(174.965, 
    172.062, 188.562), cameraTarget=(174.965, 172.062, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(185.265, 
    159.848, 188.562), cameraTarget=(185.265, 159.848, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=128.69, 
    farPlane=248.434, width=884.708, height=428.038, cameraPosition=(219.568, 
    155.165, 188.562), cameraTarget=(219.568, 155.165, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=124.869, 
    farPlane=252.255, cameraPosition=(213.33, 218.097, 188.562), cameraTarget=(
    213.33, 218.097, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=120.803, 
    farPlane=256.321, width=1001.25, height=484.426, cameraPosition=(229.901, 
    223.475, 188.562), cameraTarget=(229.901, 223.475, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=116.478, 
    farPlane=260.646, cameraPosition=(269.316, 220.532, 188.562), 
    cameraTarget=(269.316, 220.532, 0))
session.viewports['Viewport: 1'].view.setValues(width=941.179, height=455.36, 
    cameraPosition=(258.374, 218.007, 188.562), cameraTarget=(258.374, 218.007, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=120.803, 
    farPlane=256.321, cameraPosition=(267.775, 215.794, 188.562), 
    cameraTarget=(267.775, 215.794, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=132.283, 
    farPlane=244.841, width=734.825, height=355.522, cameraPosition=(232.094, 
    201.907, 188.562), cameraTarget=(232.094, 201.907, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=135.66, 
    farPlane=241.464, cameraPosition=(221.301, 173.828, 188.562), 
    cameraTarget=(221.301, 173.828, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=124.869, 
    farPlane=252.255, width=941.179, height=455.36, cameraPosition=(254.29, 
    179.447, 188.562), cameraTarget=(254.29, 179.447, 0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=890.728, 
    farPlane=994.89, cameraPosition=(226.969, 68.0437, 942.809), cameraTarget=(
    226.969, 68.0437, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=890.728, 
    farPlane=994.89, cameraPosition=(256.297, 197.752, 942.809), cameraTarget=(
    256.297, 197.752, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=880.105, 
    farPlane=1005.51, width=926.561, height=448.288, cameraPosition=(304.279, 
    208.202, 942.809), cameraTarget=(304.279, 208.202, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=876.103, 
    farPlane=1009.52, cameraPosition=(293.936, 227.266, 942.809), 
    cameraTarget=(293.936, 227.266, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=871.845, 
    farPlane=1013.77, width=1048.62, height=507.342, cameraPosition=(321.403, 
    235.626, 942.809), cameraTarget=(321.403, 235.626, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=867.315, 
    farPlane=1018.3, cameraPosition=(314.626, 232.543, 942.809), cameraTarget=(
    314.626, 232.543, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=871.845, 
    farPlane=1013.77, cameraPosition=(314.626, 232.543, 942.809), 
    cameraTarget=(314.626, 232.543, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=867.315, 
    farPlane=1018.3, cameraPosition=(311.545, 214.666, 942.809), cameraTarget=(
    311.545, 214.666, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=867.315, 
    farPlane=1018.3, width=1115.55, height=539.726, cameraPosition=(332.98, 
    206.077, 942.809), cameraTarget=(332.98, 206.077, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(276.613, 
    203.454, 942.809), cameraTarget=(276.613, 203.454, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=851.917, 
    farPlane=1033.7, width=1186.76, height=574.177, cameraPosition=(287.97, 
    185.338, 942.809), cameraTarget=(287.97, 185.338, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(126.9, 188.826, 
    942.809), cameraTarget=(126.9, 188.826, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(168.039, 
    200.686, 942.809), cameraTarget=(168.039, 200.686, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(172.92, 
    200.686, 942.809), cameraTarget=(172.92, 200.686, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(172.92, 
    201.384, 942.809), cameraTarget=(172.92, 201.384, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(186.865, 
    205.57, 942.809), cameraTarget=(186.865, 205.57, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=934.608, 
    farPlane=951.01, width=113.917, height=55.1153, cameraPosition=(120.973, 
    318.591, 942.809), cameraTarget=(120.973, 318.591, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=941.773, 
    farPlane=943.845, width=14.3902, height=6.96227, cameraPosition=(126.227, 
    328.234, 942.809), cameraTarget=(126.227, 328.234, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=784.658, 
    farPlane=1100.96, width=2336.96, height=1130.66, cameraPosition=(527.004, 
    -72.6484, 942.809), cameraTarget=(527.004, -72.6484, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(443.247, 
    88.0899, 942.809), cameraTarget=(443.247, 88.0899, 0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=806.525, 
    farPlane=1079.09, width=2013.84, height=974.334, cameraPosition=(-85.9473, 
    -54.9442, 942.809), cameraTarget=(-85.9473, -54.9442, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(474.899, 
    74.0989, 942.809), cameraTarget=(474.899, 74.0989, 0))
s.resetView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=851.545, 
    farPlane=1034.07, width=1191.61, height=576.525, cameraPosition=(21.0893, 
    76.3227, 942.809), cameraTarget=(21.0893, 76.3227, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=1000.0)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=1.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=832.93, 
    farPlane=1052.69, width=1623.66, height=785.56, cameraPosition=(41.9654, 
    40.8097, 942.809), cameraTarget=(41.9654, 40.8097, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=825.916, 
    farPlane=1059.7, cameraPosition=(351.053, 172.532, 942.809), cameraTarget=(
    351.053, 172.532, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=851.545, 
    farPlane=1034.07, width=1191.61, height=576.525, cameraPosition=(299.014, 
    178.247, 942.809), cameraTarget=(299.014, 178.247, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=857.021, 
    farPlane=1028.6, cameraPosition=(280.811, 210.471, 942.809), cameraTarget=(
    280.811, 210.471, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=862.168, 
    farPlane=1023.45, width=1052.91, height=509.418, cameraPosition=(266.223, 
    208.555, 942.809), cameraTarget=(266.223, 208.555, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=867.006, 
    farPlane=1018.61, cameraPosition=(264.368, 219.077, 942.809), 
    cameraTarget=(264.368, 219.077, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=867.006, 
    farPlane=1018.61, cameraPosition=(251.377, 188.128, 942.809), 
    cameraTarget=(251.377, 188.128, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=879.849, 
    farPlane=1005.77, width=822.059, height=397.727, cameraPosition=(228.868, 
    182.132, 942.809), cameraTarget=(228.868, 182.132, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=883.626, 
    farPlane=1001.99, cameraPosition=(229.351, 177.783, 942.809), 
    cameraTarget=(229.351, 177.783, 0))
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].view.setValues(width=874.531, height=423.114, 
    cameraPosition=(229.889, 170.547, 942.809), cameraTarget=(229.889, 170.547, 
    0))
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=True, 
    imageName='osso-protese')
session.viewports['Viewport: 1'].view.setValues(nearPlane=169.223, 
    farPlane=207.901, width=285.765, height=138.258, cameraPosition=(11.8398, 
    6.13766, 188.562), cameraTarget=(11.8398, 6.13766, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(15.8693, 
    8.99354, 188.562), cameraTarget=(15.8693, 8.99354, 0))
s1.Spot(point=(-8.75, 35.0))
s1.Spot(point=(-5.0, 40.0))
s1.Spot(point=(-2.5, 37.5))
session.viewports['Viewport: 1'].view.setValues(nearPlane=168.182, 
    farPlane=208.942, width=283.078, height=136.959)
session.viewports['Viewport: 1'].view.setValues(nearPlane=180.861, 
    farPlane=196.263, width=106.972, height=51.7549, cameraPosition=(10.7965, 
    43.4413, 188.562), cameraTarget=(10.7965, 43.4413, 0))
s1.undo()
s1.undo()
s1.undo()
s1.undo()
#* Nothing to undo.
session.viewports['Viewport: 1'].view.setValues(nearPlane=173.351, 
    farPlane=203.773, width=224.769, height=108.747, cameraPosition=(13.9971, 
    40.3735, 188.562), cameraTarget=(13.9971, 40.3735, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(13.733, 
    42.4877, 188.562), cameraTarget=(13.733, 42.4877, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=171.347, 
    farPlane=205.777, width=254.378, height=123.073, cameraPosition=(13.9244, 
    41.1387, 188.562), cameraTarget=(13.9244, 41.1387, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=170.248, 
    farPlane=206.876, cameraPosition=(15.12, 42.0359, 188.562), cameraTarget=(
    15.12, 42.0359, 0))
session.viewports['Viewport: 1'].view.setValues(width=239.116, height=115.689, 
    cameraPosition=(14.9048, 42.5877, 188.562), cameraTarget=(14.9048, 42.5877, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=171.347, 
    farPlane=205.777, cameraPosition=(13.9213, 44.8368, 188.562), 
    cameraTarget=(13.9213, 44.8368, 0))
session.viewports['Viewport: 1'].view.setValues(width=254.378, height=123.073, 
    cameraPosition=(14.0558, 44.4286, 188.562), cameraTarget=(14.0558, 44.4286, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=170.248, 
    farPlane=206.876, cameraPosition=(14.3547, 48.0176, 188.562), 
    cameraTarget=(14.3547, 48.0176, 0))
session.viewports['Viewport: 1'].view.setValues(width=270.615, height=130.929, 
    cameraPosition=(14.2975, 51.0291, 188.562), cameraTarget=(14.2975, 51.0291, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=169.079, 
    farPlane=208.044, cameraPosition=(15.5694, 51.6655, 188.562), 
    cameraTarget=(15.5694, 51.6655, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(15.4104, 
    36.5522, 188.562), cameraTarget=(15.4104, 36.5522, 0))
s1.Spot(point=(2.5, 70.0))
s1.Spot(point=(18.75, 53.75))
s1.Spot(point=(27.5, 63.75))
s1.Spot(point=(11.25, 78.75))
s1.Spot(point=(16.25, 83.75))
s1.Spot(point=(13.75, 86.25))
s1.Spot(point=(-3.75, 67.5))
s1.Spot(point=(-1.25, 63.75))
s1.delete(objectList=(v[7], ))
s1.Spot(point=(-1.25, 66.25))
s1.Line(point1=(-3.75, 67.5), point2=(13.75, 86.25))
s1.Line(point1=(13.75, 86.25), point2=(16.25, 83.75))
s1.Line(point1=(16.25, 83.75), point2=(11.25, 78.75))
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.Line(point1=(11.25, 78.75), point2=(27.5, 63.75))
s1.Line(point1=(27.5, 63.75), point2=(18.75, 53.75))
s1.Line(point1=(18.75, 53.75), point2=(2.5, 70.0))
s1.Line(point1=(2.5, 70.0), point2=(-1.25, 66.25))
s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s1.Line(point1=(-1.25, 66.25), point2=(-3.75, 67.5))
p = mdb.models['Model-1'].Part(name='implant', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['implant']
p.BaseSolidExtrude(sketch=s1, depth=20.0)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['implant']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['implant']
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=167.989, 
    farPlane=209.135, width=304.005, height=147.083, cameraPosition=(-6.11963, 
    24.8329, 188.562), cameraTarget=(-6.11963, 24.8329, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(2.27536, 
    26.7988, 188.562), cameraTarget=(2.27536, 26.7988, 0))
session.viewports['Viewport: 1'].view.setValues(width=285.765, height=138.258, 
    cameraPosition=(2.66117, 26.7934, 188.562), cameraTarget=(2.66117, 26.7934, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=167.989, 
    farPlane=209.135, cameraPosition=(6.01917, 29.1453, 188.562), 
    cameraTarget=(6.01917, 29.1453, 0))
s.Spot(point=(-13.75, 61.25))
s.Spot(point=(5.0, 80.0))
s.Spot(point=(7.5, 76.25))
s.undo()
s.Spot(point=(-11.25, 58.75))
s.Spot(point=(-7.5, 63.75))
s.Spot(point=(10.0, 47.5))
s.Spot(point=(18.75, 57.5))
s.Spot(point=(1.25, 73.75))
s.Spot(point=(7.5, 77.5))
s.delete(objectList=(v[6], ))
s.Spot(point=(2.5, 73.75))
s.Line(point1=(-13.75, 61.25), point2=(5.0, 80.0))
s.Line(point1=(5.0, 80.0), point2=(7.5, 77.5))
s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.Line(point1=(7.5, 77.5), point2=(2.5, 73.75))
s.Line(point1=(2.5, 73.75), point2=(18.75, 57.5))
s.Line(point1=(18.75, 57.5), point2=(10.0, 47.5))
s.Line(point1=(10.0, 47.5), point2=(-7.5, 63.75))
s.Line(point1=(-7.5, 63.75), point2=(-11.25, 58.75))
s.Line(point1=(-11.25, 58.75), point2=(-13.75, 61.25))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=83.2651, 
    farPlane=100.583, width=127.223, height=61.5527, viewOffsetX=-0.586374, 
    viewOffsetY=-2.8708)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.131, 
    farPlane=223.617, width=217.882, height=105.415, viewOffsetX=-2.52173, 
    viewOffsetY=-3.19484)
session.viewports['Viewport: 1'].view.setValues(nearPlane=248.316, 
    farPlane=286.306, width=246.962, height=119.485, viewOffsetX=1.59611, 
    viewOffsetY=-9.87239)
session.viewports['Viewport: 1'].view.setValues(nearPlane=252.356, 
    farPlane=282.265, width=195.953, height=94.8055, viewOffsetX=-0.283465, 
    viewOffsetY=-6.60099)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.203, 
    farPlane=281.418, width=196.61, height=95.1238, viewOffsetX=2.83456, 
    viewOffsetY=-20.3774)
session.viewports['Viewport: 1'].view.setValues(nearPlane=252.255, 
    farPlane=282.366, width=221.678, height=107.252, viewOffsetX=3.47585, 
    viewOffsetY=-23.2515)
session.viewports['Viewport: 1'].view.setValues(nearPlane=251.351, 
    farPlane=283.27, width=220.883, height=106.868, viewOffsetX=3.07406, 
    viewOffsetY=-21.8697)
session.viewports['Viewport: 1'].view.setValues(nearPlane=254.691, 
    farPlane=279.93, width=185.901, height=89.9423, viewOffsetX=2.37984, 
    viewOffsetY=-17.6559)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.927, 
    farPlane=280.694, width=185.343, height=89.6725, viewOffsetX=42.5558, 
    viewOffsetY=-18.4746)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.967, 
    farPlane=280.654, width=185.372, height=89.6867, viewOffsetX=48.2261, 
    viewOffsetY=-19.0224)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.965, 
    farPlane=280.656, width=185.371, height=89.686, viewOffsetX=44.8494, 
    viewOffsetY=-21.4197)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.965, 
    farPlane=280.656, width=185.371, height=89.686, viewOffsetX=43.6514, 
    viewOffsetY=-19.8941)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.965, 
    farPlane=280.656, width=185.371, height=89.686, viewOffsetX=47.1367, 
    viewOffsetY=-19.4582)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.965, 
    farPlane=280.656, width=185.371, height=89.686, viewOffsetX=51.6022, 
    viewOffsetY=-19.8941)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.965, 
    width=185.371, height=89.686, viewOffsetX=54.434, viewOffsetY=-19.1313)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.965, 
    width=185.371, height=89.686, viewOffsetX=53.9984, viewOffsetY=-20.439)
session.viewports['Viewport: 1'].view.setValues(nearPlane=252.258, 
    farPlane=282.363, width=195.878, height=94.7692, viewOffsetX=54.6159, 
    viewOffsetY=-19.7731)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.209, 
    farPlane=281.412, width=196.616, height=95.1265, viewOffsetX=-0.628022, 
    viewOffsetY=-15.9177)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.156, 
    farPlane=281.466, width=196.574, height=95.1064, viewOffsetX=0.527064, 
    viewOffsetY=-18.5722)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.159, 
    farPlane=281.463, width=196.576, height=95.1073, viewOffsetX=1.79754, 
    viewOffsetY=25.8033)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.158, 
    width=196.576, height=95.1071, viewOffsetX=0.642567, viewOffsetY=-19.6124)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.158, 
    width=196.576, height=95.1072, viewOffsetX=3.53, viewOffsetY=-17.3012)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.158, 
    width=196.576, height=95.1073, viewOffsetX=3.18352, viewOffsetY=-17.7635)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.158, 
    width=196.576, height=95.1074, viewOffsetX=3.64552, viewOffsetY=-11.7543)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.158, 
    width=196.576, height=95.1075, viewOffsetX=16.1192, viewOffsetY=19.2163)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.158, 
    farPlane=281.463, width=196.577, height=95.1076, viewOffsetX=6.99492, 
    viewOffsetY=-12.7944)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.158, 
    farPlane=281.463, width=196.577, height=95.1077, viewOffsetX=2.49052, 
    viewOffsetY=-15.3368)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.158, 
    farPlane=281.463, width=196.577, height=95.1078, viewOffsetX=4.45399, 
    viewOffsetY=-18.3414)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.158, 
    farPlane=281.463, width=196.577, height=95.1079, viewOffsetX=9.18941, 
    viewOffsetY=-19.7282)
session.viewports['Viewport: 1'].view.setValues(nearPlane=253.158, 
    farPlane=281.463, width=196.578, height=95.108, viewOffsetX=0.873556, 
    viewOffsetY=-18.1103)
session.viewports['Viewport: 1'].view.setValues(nearPlane=244.75, 
    farPlane=289.871, width=331.677, height=160.471, viewOffsetX=1.48821, 
    viewOffsetY=-34.1502)
session.viewports['Viewport: 1'].view.setValues(nearPlane=243.432, 
    farPlane=291.189, width=329.891, height=159.607, viewOffsetX=9.62084, 
    viewOffsetY=-44.6326)
session.viewports['Viewport: 1'].view.setValues(nearPlane=243.697, 
    farPlane=290.924, width=310.435, height=150.194, viewOffsetX=9.15399, 
    viewOffsetY=-41.3089)
session.viewports['Viewport: 1'].view.setValues(nearPlane=244.961, 
    farPlane=289.66, width=312.046, height=150.974, viewOffsetX=7.5514, 
    viewOffsetY=-41.5232)
session.viewports['Viewport: 1'].view.setValues(nearPlane=244.856, 
    farPlane=289.765, width=311.913, height=150.909, viewOffsetX=7.73143, 
    viewOffsetY=-41.5054)
p1 = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['Part-2']
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=185.592, 
    farPlane=232.156, width=341.714, height=165.328, viewOffsetX=1.62142, 
    viewOffsetY=-7.95904)
session.viewports['Viewport: 1'].view.setValues(nearPlane=184.448, 
    farPlane=233.3, width=339.607, height=164.308, viewOffsetX=10.79, 
    viewOffsetY=-33.4646)
session.viewports['Viewport: 1'].view.setValues(nearPlane=184.634, 
    farPlane=233.114, width=319.553, height=154.606, viewOffsetX=10.693, 
    viewOffsetY=-31.6338)
session.viewports['Viewport: 1'].view.setValues(nearPlane=185.868, 
    farPlane=231.88, width=321.689, height=155.639, viewOffsetX=9.06345, 
    viewOffsetY=-29.5759)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=169.223, 
    farPlane=207.901, width=285.765, height=138.258, cameraPosition=(12.0858, 
    11.7757, 188.562), cameraTarget=(12.0858, 11.7757, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(15.4438, 
    14.1276, 188.562), cameraTarget=(15.4438, 14.1276, 0))
session.viewports['Viewport: 1'].view.setValues(width=304.005, height=147.083, 
    cameraPosition=(17.33, 11.9991, 188.562), cameraTarget=(17.33, 11.9991, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(15.9011, 
    13.0714, 188.562), cameraTarget=(15.9011, 13.0714, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    imageName='osso-protese')
s1.Spot(point=(-6.25, 46.25))
s1.Spot(point=(-3.75, 43.75))
s1.undo()
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=156.837, 
    farPlane=220.287, width=468.798, height=226.813, cameraPosition=(25.1858, 
    27.7617, 188.562), cameraTarget=(25.1858, 27.7617, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(12.5156, 
    -2.00233, 188.562), cameraTarget=(12.5156, -2.00233, 0))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    sheetSize=400.0, sheetAuto=OFF)
session.viewports['Viewport: 1'].view.setValues(width=498.722, height=241.291, 
    cameraPosition=(10.8981, 0.768265, 188.562), cameraTarget=(10.8981, 
    0.768265, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=152.657, 
    farPlane=224.467, cameraPosition=(8.84699, -5.6818, 188.562), 
    cameraTarget=(8.84699, -5.6818, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=150.366, 
    farPlane=226.758, width=564.42, height=273.077, cameraPosition=(6.14613, 
    5.7299, 188.562), cameraTarget=(6.14613, 5.7299, 0))
s1.Line(point1=(-33.75, 67.5), point2=(-28.75, 61.25))
s1.Line(point1=(-28.75, 61.25), point2=(-23.3362044359092, 65.5810364513891))
s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s1.Line(point1=(-23.3362044359092, 65.5810364513891), point2=(
    -26.9932330063311, 70.1523221643874))
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.Line(point1=(-26.9932330063311, 70.1523221643874), point2=(
    -21.2479807226919, 74.7485239913221))
s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s1.Line(point1=(-21.2479807226919, 74.7485239913221), point2=(15.0, 42.5))
s1.Line(point1=(15.0, 42.5), point2=(32.5, 62.1703471702233))
s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s1.Line(point1=(32.5, 62.1703471702233), point2=(-3.79466303484514, 
    94.4604027359746))
s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s1.Line(point1=(-3.79466303484514, 94.4604027359746), point2=(1.91062435647473, 
    100.873258947395))
s1.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(width=530.555, height=256.693, 
    cameraPosition=(5.34334, 10.9364, 188.562), cameraTarget=(5.34334, 10.9364, 
    0))
s1.Line(point1=(1.91062435647473, 100.873258947395), point2=(7.01642029173672, 
    96.3308160465676))
s1.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s1.Line(point1=(7.01642029173672, 96.3308160465676), point2=(11.2587381129852, 
    101.099265438388))
s1.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s1.Line(point1=(11.2587381129852, 101.099265438388), point2=(3.75, 
    107.779519519841))
s1.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s1.Line(point1=(3.75, 107.779519519841), point2=(-33.75, 67.5))
p = mdb.models['Model-1'].Part(name='implant', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['implant']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['implant']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=167.742, 
    farPlane=204.29, width=268.436, height=129.874, viewOffsetX=-4.09443, 
    viewOffsetY=3.45617)
session.viewports['Viewport: 1'].view.setValues(nearPlane=166.811, 
    farPlane=205.22, width=266.947, height=129.154, viewOffsetX=-4.38543, 
    viewOffsetY=-29.5185)
session.viewports['Viewport: 1'].view.setValues(nearPlane=161.932, 
    farPlane=210.1, width=353.097, height=170.835, viewOffsetX=-5.21095, 
    viewOffsetY=-36.9254)
p1 = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=190.195, 
    farPlane=227.553, width=274.528, height=132.822, viewOffsetX=3.31973, 
    viewOffsetY=-3.65337)
p1 = mdb.models['Model-1'].parts['implant']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=168.741, 
    farPlane=203.29, width=253.833, height=122.809, viewOffsetX=9.25494, 
    viewOffsetY=1.35753)
p1 = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Model-1'].parts['implant']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['implant']
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=190.265, 
    farPlane=227.483, width=273.51, height=132.329, viewOffsetX=-16.621, 
    viewOffsetY=6.06364)
session.viewports['Viewport: 1'].view.setValues(nearPlane=189.295, 
    farPlane=228.453, width=272.116, height=131.655, viewOffsetX=4.88759, 
    viewOffsetY=-20.8421)
session.viewports['Viewport: 1'].view.setValues(nearPlane=188.034, 
    farPlane=229.714, width=305.912, height=148.006, viewOffsetX=5.31531, 
    viewOffsetY=-24.9213)
session.viewports['Viewport: 1'].view.setValues(nearPlane=186.85, 
    farPlane=230.898, width=303.986, height=147.074, viewOffsetX=6.71068, 
    viewOffsetY=-25.6579)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.867315, 
    farPlane=1.0183, width=1.11555, height=0.539726, cameraPosition=(
    -0.0263466, 0.00171075, 0.942809), cameraTarget=(-0.0263466, 0.00171075, 
    0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.00183714, 
    -0.029112, 0.942809), cameraTarget=(0.00183714, -0.029112, 0))
s.Line(point1=(-0.08, 0.095), point2=(-0.07, 0.085))
s.Line(point1=(-0.07, 0.085), point2=(-0.060133922248724, 0.0948660777512487))
s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
#: Warning: Coincident point selected.
#: Warning: Coincident point selected.
#: Warning: Coincident point selected.
s.Spot(point=(-0.060133922248724, 0.0948660777512487))
s.CoincidentConstraint(entity1=v[3], entity2=g[3], addUndoState=False)
s.Spot(point=(-0.060133922248724, 0.0948660777512487))
s.CoincidentConstraint(entity1=v[4], entity2=g[3], addUndoState=False)
s.Spot(point=(-0.060133922248724, 0.0948660777512487))
s.CoincidentConstraint(entity1=v[5], entity2=g[3], addUndoState=False)
s.Spot(point=(-0.060133922248724, 0.0948660777512487))
s.CoincidentConstraint(entity1=v[6], entity2=g[3], addUndoState=False)
s.Spot(point=(-0.055, 0.11))
s.undo()
s.undo()
s.undo()
s.undo()
s.delete(objectList=(c[6], ))
s.delete(objectList=(g[3], ))
s.delete(objectList=(g[2], ))
s.delete(objectList=(v[3], ))
s.Spot(point=(-0.08, 0.095))
s.Spot(point=(-0.07, 0.085))
s.Spot(point=(-0.06, 0.09))
s.Spot(point=(0.015, 0.045))
s.Spot(point=(0.05, 0.08))
s.Spot(point=(-0.01, 0.14))
s.Spot(point=(0.0, 0.175))
s.Spot(point=(0.01, 0.165))
s.Spot(point=(0.0, 0.155))
s.Spot(point=(-0.065, 0.1))
s.delete(objectList=(v[12], ))
s.Spot(point=(0.005, 0.155))
s.Spot(point=(-0.005, 0.165))
s.Line(point1=(-0.08, 0.095), point2=(0.0, 0.175))
s.Line(point1=(0.0, 0.175), point2=(0.01, 0.165))
s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s.Line(point1=(0.01, 0.165), point2=(0.005, 0.155))
s.Line(point1=(0.005, 0.155), point2=(-0.005, 0.165))
s.undo()
s.undo()
s.undo()
s.undo()
s.Spot(point=(-0.02, 0.15))
s.Spot(point=(-0.055, 0.11))
s.Line(point1=(-0.08, 0.095), point2=(0.0, 0.175))
s.Line(point1=(0.0, 0.175), point2=(0.01, 0.165))
s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s.Line(point1=(0.01, 0.165), point2=(0.005, 0.155))
s.Line(point1=(0.005, 0.155), point2=(-0.005, 0.165))
s.Line(point1=(-0.005, 0.165), point2=(-0.02, 0.15))
s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s.Line(point1=(-0.02, 0.15), point2=(-0.01, 0.14))
s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s.Line(point1=(-0.01, 0.14), point2=(0.05, 0.08))
s.ParallelConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s.Line(point1=(0.05, 0.08), point2=(0.015, 0.045))
s.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s.Line(point1=(0.015, 0.045), point2=(-0.055, 0.11))
s.Line(point1=(-0.055, 0.11), point2=(-0.065, 0.1))
s.Line(point1=(-0.065, 0.1), point2=(-0.06, 0.09))
s.Line(point1=(-0.06, 0.09), point2=(-0.07, 0.085))
s.PerpendicularConstraint(entity1=g[14], entity2=g[15], addUndoState=False)
s.Line(point1=(-0.07, 0.085), point2=(-0.08, 0.095))
#: Warning: Coincident point selected.
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.317121, 
    farPlane=0.41827, width=0.741115, height=0.358565, viewOffsetX=-0.0122296, 
    viewOffsetY=0.0332722)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.314808, 
    farPlane=0.420583, width=0.735709, height=0.35595, viewOffsetX=0.0103373, 
    viewOffsetY=-0.0846113)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.319689, 
    farPlane=0.415702, width=0.70229, height=0.339781, viewOffsetX=0.0109717, 
    viewOffsetY=-0.0812193)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.317135, 
    farPlane=0.418256, width=0.696679, height=0.337067, viewOffsetX=0.00679073, 
    viewOffsetY=-0.0822087)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.317539, 
    farPlane=0.417852, width=0.697567, height=0.337497, 
    viewOffsetX=0.000651626, viewOffsetY=-0.00685858)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.317475, 
    farPlane=0.417916, width=0.697427, height=0.337429, 
    viewOffsetX=-0.00262667, viewOffsetY=-0.0130072)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.317484, 
    farPlane=0.417907, width=0.697447, height=0.337438, viewOffsetX=-0.0263941, 
    viewOffsetY=-0.00685737)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.317484, 
    farPlane=0.417907, height=0.337438, viewOffsetX=-0.0329506, 
    viewOffsetY=-0.0113675)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.317484, 
    farPlane=0.417907, width=0.697447, height=0.337438, viewOffsetX=-0.0567179, 
    viewOffsetY=-0.00685739)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-0.0263941, 
    viewOffsetY=-0.0171076)
del mdb.models['Model-1'].parts['Part-2']
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('osso-4', 'Partition edge-6', 'Partition edge-5', 
    'Partition edge-4', 'Partition edge-3', 'Partition edge-2', 
    'Partition edge-1', 'FH2-part-left', 'FH2-part-right', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Datum csys-1', 'Datum pt-1', 'RP-1', 'RP-2', 'RP-3', ))
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('s_Surf-1', 
    's_Surf-2', 's_Surf-3', 's_Surf-4', ))
mdb.models['Model-1'].rootAssembly.deleteSets(setNames=('test-points', 'Set-2', 
    'Set-4', 'base-osso', 'm_Set-3', 'm_Set-5', 'm_Set-7', 'm_Set-8', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
del mdb.models['Model-1'].steps['step-1']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].constraints.delete(('Constraint-1', 'Constraint-2', 
    'Constraint-3', 'Constraint-4', ))
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=False)
session.Image(name='imp', fileName='C:/temp/imp.jpeg')
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=True, 
    imageName='imp')
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.85737, 
    farPlane=1.02825, width=1.06902, height=0.539726, cameraPosition=(
    0.0317714, 0.00760752, 0.942809), cameraTarget=(0.0317714, 0.00760752, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.00296672, 
    -0.0363313, 0.942809), cameraTarget=(-0.00296672, -0.0363313, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.871845, 
    farPlane=1.01377, width=0.887909, height=0.448288, cameraPosition=(
    -0.00693178, -0.0683595, 0.942809), cameraTarget=(-0.00693178, -0.0683595, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.876103, 
    farPlane=1.00952, cameraPosition=(0.00068972, -0.0590996, 0.942809), 
    cameraTarget=(0.00068972, -0.0590996, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887404, 
    farPlane=0.998214, width=0.693234, height=0.35, cameraPosition=(0.0249253, 
    -0.101078, 0.942809), cameraTarget=(0.0249253, -0.101078, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.890728, 
    farPlane=0.99489, cameraPosition=(0.0402266, -0.101503, 0.942809), 
    cameraTarget=(0.0402266, -0.101503, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.737483, 
    height=0.372341, cameraPosition=(0.0361978, -0.0920158, 0.942809), 
    cameraTarget=(0.0361978, -0.0920158, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887404, 
    farPlane=0.998214, cameraPosition=(0.0407195, -0.0924682, 0.942809), 
    cameraTarget=(0.0407195, -0.0924682, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.784556, 
    height=0.396107, cameraPosition=(0.0367222, -0.0824043, 0.942809), 
    cameraTarget=(0.0367222, -0.0824043, 0))
s1.ArcByCenterEnds(center=(0.08, -0.025), point1=(-0.005, -0.08), point2=(
    0.125, 0.06), direction=CLOCKWISE)
s1.Spot(point=(0.015, -0.06))
s1.Spot(point=(0.03, -0.075))
s1.Spot(point=(0.035, -0.065))
s1.delete(objectList=(v[4], v[5]))
s1.Spot(point=(0.03, -0.07))
s1.Spot(point=(0.05, -0.05))
s1.Spot(point=(0.135, -0.125))
s1.Spot(point=(0.18, -0.075))
s1.Spot(point=(0.105, 0.0))
s1.delete(objectList=(v[3], v[6], v[7]))
s1.delete(objectList=(v[8], v[9], v[10]))
s1.Spot(point=(0.02, -0.055))
s1.Spot(point=(0.035, -0.065))
s1.Spot(point=(0.05, -0.05))
s1.Spot(point=(0.11, -0.1))
s1.Spot(point=(0.15, -0.065))
s1.Spot(point=(0.09, -0.015))
s1.Spot(point=(0.105, 0.0))
s1.Spot(point=(0.09, 0.015))
s1.delete(objectList=(v[18], ))
s1.Spot(point=(0.09, 0.015))
s1.delete(objectList=(v[19], ))
s1.Spot(point=(0.085, 0.015))
s1.Line(point1=(-0.005, -0.08), point2=(0.02, -0.055))
s1.Line(point1=(0.02, -0.055), point2=(0.035, -0.065))
s1.Line(point1=(0.035, -0.065), point2=(0.05, -0.05))
s1.Line(point1=(0.05, -0.05), point2=(0.11, -0.1))
s1.Line(point1=(0.11, -0.1), point2=(0.15, -0.065))
s1.Line(point1=(0.15, -0.065), point2=(0.09, -0.015))
s1.Line(point1=(0.09, -0.015), point2=(0.105, 0.0))
s1.Line(point1=(0.105, 0.0), point2=(0.085, 0.015))
s1.Line(point1=(0.085, 0.015), point2=(0.127370021310096, 0.0644767069190696))
p = mdb.models['Model-1'].Part(name='implant', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['implant']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['implant']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.460299, 
    farPlane=0.522638, width=0.439687, height=0.221989, viewOffsetX=0.0195698, 
    viewOffsetY=0.0154316)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.458569, 
    farPlane=0.524367, width=0.438035, height=0.221155, viewOffsetX=0.0938897, 
    viewOffsetY=-0.0109608)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.45856, 
    farPlane=0.524377, width=0.438026, height=0.221151, viewOffsetX=0.0560204, 
    viewOffsetY=0.00865544)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.458561, 
    farPlane=0.524376, width=0.438027, height=0.221151, 
    viewOffsetX=-0.00252631, viewOffsetY=-0.00639252)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.436436, 
    farPlane=0.5465, width=0.774009, height=0.390782, viewOffsetX=-0.000436321, 
    viewOffsetY=-0.0366964)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.433319, 
    farPlane=0.549618, width=0.768481, height=0.387991, viewOffsetX=-0.0235206, 
    viewOffsetY=-0.0609489)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.440004, 
    farPlane=0.542933, width=0.648135, height=0.327231, viewOffsetX=-0.0191175, 
    viewOffsetY=-0.0476008)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.442776, 
    farPlane=0.540161, width=0.652218, height=0.329292, viewOffsetX=-0.0220371, 
    viewOffsetY=-0.0511015)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.442469, 
    farPlane=0.540468, width=0.651766, height=0.329064, viewOffsetX=-0.0248191, 
    viewOffsetY=-0.0522656)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.442503, 
    farPlane=0.540434, width=0.651816, height=0.329089, viewOffsetX=0.0047525, 
    viewOffsetY=-0.0438724)
del mdb.models['Model-1'].parts['implant']
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ArcByCenterEnds(center=(0.035, 0.05), point1=(-0.04, 0.0), point2=(0.08, 
    0.125), direction=CLOCKWISE)
s.Spot(point=(0.06, 0.1))
s.Spot(point=(-0.015, 0.025))
s.Spot(point=(0.0, 0.01))
s.Spot(point=(0.075, 0.085))
s.Spot(point=(0.06, 0.07))
s.Spot(point=(0.095, 0.035))
s.Spot(point=(0.05, -0.005))
s.Spot(point=(0.01, 0.03))
s.delete(objectList=(v[10], ))
s.Spot(point=(0.015, 0.03))
s.Line(point1=(-0.04, 0.0), point2=(-0.015, 0.025))
s.Line(point1=(-0.015, 0.025), point2=(0.0, 0.01))
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s.Line(point1=(0.0, 0.01), point2=(0.015, 0.03))
s.Line(point1=(0.015, 0.03), point2=(0.05, -0.005))
s.Line(point1=(0.05, -0.005), point2=(0.095, 0.035))
s.Line(point1=(0.095, 0.035), point2=(0.06, 0.07))
s.Line(point1=(0.06, 0.07), point2=(0.075, 0.085))
s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s.Line(point1=(0.075, 0.085), point2=(0.06, 0.1))
s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s.Line(point1=(0.06, 0.1), point2=(0.0813760206800632, 0.127293367800105))
p = mdb.models['Model-1'].Part(name='implant', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['implant']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['implant']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.385238, 
    farPlane=0.450053, width=0.456755, height=0.230606, viewOffsetX=0.00371649, 
    viewOffsetY=0.0186602)
del mdb.models['Model-1'].parts['implant']
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.880105, 
    farPlane=1.00551, width=0.784556, height=0.396107, cameraPosition=(
    -0.0223977, 0.017115, 0.942809), cameraTarget=(-0.0223977, 0.017115, 0))
s1.undo()
#* Nothing to undo.
#: Warning: Coincident point selected
#: Warning: Coincident point selected
s1.undo()
#* Nothing to undo.
#: Warning: Coincident point selected
#: Warning: Coincident point selected
s1.undo()
#* Nothing to undo.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.871845, 
    farPlane=1.01377, width=0.887909, height=0.448288, cameraPosition=(
    -0.0899878, 0.0502708, 0.942809), cameraTarget=(-0.0899878, 0.0502708, 0))
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.Image(name='imp2', fileName='C:/temp/imp2.jpeg')
session.viewports['Viewport: 1'].imageOptions.setValues(imageName='imp2')
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.80725, 
    farPlane=4.12095, width=1.96965, height=0.994439)
p1 = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ArcByCenterEnds(center=(0.035, 0.05), point1=(-0.04, 0.0), point2=(0.08, 
    0.125), direction=CLOCKWISE)
s.Spot(point=(-0.02, 0.02))
s.Spot(point=(-0.005, 0.005))
s.Spot(point=(-0.005, 0.005))
s.Spot(point=(0.0, 0.015))
s.delete(objectList=(v[4], v[5], v[6]))
s.Spot(point=(-0.005, 0.005))
s.Spot(point=(0.0, 0.01))
s.Spot(point=(-0.005, 0.015))
s.Spot(point=(0.01, 0.025))
s.Spot(point=(0.06, -0.02))
s.delete(objectList=(v[10], ))
s.Spot(point=(0.01, 0.025))
s.Spot(point=(0.095, 0.015))
s.Spot(point=(0.05, 0.06))
s.Spot(point=(0.065, 0.075))
s.delete(objectList=(v[12], v[14], v[15]))
s.Spot(point=(0.005, 0.03))
s.Spot(point=(0.045, 0.065))
s.Spot(point=(0.06, 0.08))
s.Spot(point=(0.065, 0.075))
s.Spot(point=(0.07, 0.08))
s.Spot(point=(0.055, 0.095))
s.Line(point1=(-0.04, 0.0), point2=(-0.02, 0.02))
s.Line(point1=(-0.02, 0.02), point2=(-0.005, 0.005))
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s.Line(point1=(-0.005, 0.005), point2=(0.0, 0.01))
s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s.Line(point1=(0.0, 0.01), point2=(-0.005, 0.015))
s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s.Line(point1=(-0.005, 0.015), point2=(0.005, 0.03))
s.Line(point1=(0.005, 0.03), point2=(0.06, -0.02))
s.Line(point1=(0.06, -0.02), point2=(0.095, 0.015))
s.Line(point1=(0.095, 0.015), point2=(0.045, 0.065))
s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s.Line(point1=(0.045, 0.065), point2=(0.06, 0.08))
s.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s.Line(point1=(0.06, 0.08), point2=(0.065, 0.075))
s.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s.Line(point1=(0.065, 0.075), point2=(0.07, 0.08))
s.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
s.Line(point1=(0.07, 0.08), point2=(0.055, 0.095))
s.PerpendicularConstraint(entity1=g[13], entity2=g[14], addUndoState=False)
s.Line(point1=(0.055, 0.095), point2=(0.0813760206800632, 0.127293367800105))
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.928607, 
    farPlane=0.957012, width=0.177702, height=0.0897183, cameraPosition=(
    0.0316034, 0.0332422, 0.942809), cameraTarget=(0.0316034, 0.0332422, 0))
s.delete(objectList=(g[7], g[8], v[16], c[24], c[27]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.920908, 
    farPlane=0.96471, width=0.27403, height=0.138352, cameraPosition=(
    0.0449883, 0.0405597, 0.942809), cameraTarget=(0.0449883, 0.0405597, 0))
s.Spot(point=(0.005, 0.025))
s.Line(point1=(-0.005, 0.015), point2=(0.005, 0.025))
s.Line(point1=(0.005, 0.025), point2=(0.06, -0.02))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.911062, 
    farPlane=0.974556, width=0.449547, height=0.226967, cameraPosition=(
    0.0582373, 0.0626865, 0.942809), cameraTarget=(0.0582373, 0.0626865, 0))
s.Spot(point=(0.01, 0.03))
s.delete(objectList=(g[17], ))
s.delete(objectList=(c[64], ))
s.Line(point1=(0.06, -0.02), point2=(0.01, 0.03))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.935618, 
    farPlane=0.95, width=0.0899703, height=0.0454242, cameraPosition=(
    0.0611019, 0.108317, 0.942809), cameraTarget=(0.0611019, 0.108317, 0))
s.Spot(point=(0.0530757196247578, 0.0966362878680229))
s.delete(objectList=(g[15], ))
s.Line(point1=(0.0813760206800632, 0.127293367800105), point2=(
    0.0530757196247578, 0.0966362878680229))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.926462, 
    farPlane=0.959157, width=0.231486, height=0.116873, cameraPosition=(
    0.0876611, 0.113638, 0.942809), cameraTarget=(0.0876611, 0.113638, 0))
s.delete(objectList=(g[14], ))
s.delete(objectList=(v[21], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.935935, 
    farPlane=0.949684, width=0.0860142, height=0.0434268, cameraPosition=(
    0.0781409, 0.0935737, 0.942809), cameraTarget=(0.0781409, 0.0935737, 0))
s.Line(point1=(0.0530757196247578, 0.0966362878680229), point2=(
    0.071786068379879, 0.0819315016269684))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.869746, 
    farPlane=1.01587, width=1.03461, height=0.522352, cameraPosition=(0.405864, 
    0.098143, 0.942809), cameraTarget=(0.405864, 0.098143, 0))
s.autoConstrain(objectList=(g[2], g[3], g[4], g[5], g[6], g[9], g[10], g[11], 
    g[12], g[13], g[16], g[18], g[19], g[20]))
#: 3 constraints added
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.934933, 
    farPlane=0.950685, width=0.0985448, height=0.0497533, cameraPosition=(
    0.0910189, 0.0937888, 0.942809), cameraTarget=(0.0910189, 0.0937888, 0))
s.dragEntity(entity=g[20], points=((0.0610895581178795, 0.0903380737858597), (
    0.0610204041004181, 0.09), (0.06, 0.09), (0.06, 0.09), (0.06, 0.09), (
    0.0607787221670151, 0.09), (0.0612016618251801, 0.09), (0.0615037605166435, 
    0.0906754285097122), (0.0612016618251801, 0.09), (0.0612016618251801, 
    0.09), (0.0615037605166435, 0.0906754285097122)))
s.redo()
#* Nothing to redo.
s.dragEntity(entity=v[57], points=((0.0721081198039639, 0.0823412793933999), (
    0.0721081198039639, 0.0823412793933999), (0.0710501000285149, 
    0.0817282944917679), (0.0707480013370514, 0.0813655704259872), (
    0.0713521987199783, 0.0819701105356216), (0.0715334564447403, 
    0.0826350972056389), (0.0718959793448448, 0.0831187218427658), (
    0.0725605934858322, 0.0837837159633636), (0.0728022754192352, 
    0.0840859860181808), (0.0717147141695023, 0.0833605378866196), (0.07, 
    0.0822723731398582), (0.0686333030462265, 0.0814260244369507), (
    0.0671832263469696, 0.0813051164150238), (0.065, 0.0813051164150238), (
    0.0632559359073639, 0.0813051164150238), (0.0633163601160049, 
    0.0811237543821335), (0.0658539906144142, 0.0811237543821335), (0.07, 
    0.0810028463602066), (0.07, 0.0813051164150238), (0.0711709409952164, 
    0.081607386469841), (0.0708688423037529, 0.0816678404808044), (
    0.0708688423037529, 0.0817887485027313), (0.0711105167865753, 
    0.0819096565246582)))
s.dragEntity(entity=v[57], points=((0.0711105167865754, 0.0819096565246582), (
    0.0711105167865754, 0.0819096565246582), (0.0716542974114418, 
    0.0824537351727486)))
s.dragEntity(entity=v[57], points=((0.0716542974114418, 0.0824537351727486), (
    0.0716542974114418, 0.0824537351727486), (0.0722585022449493, 
    0.0828769132494926)))
s.dragEntity(entity=v[57], points=((0.0722585022449493, 0.0828769132494926), (
    0.0722585022449493, 0.0828769132494926), (0.0718959793448448, 
    0.0820910185575485), (0.0717147141695023, 0.0818492025136948), (
    0.0717147141695023, 0.0817887485027313), (0.0718355625867844, 
    0.0820910185575485), (0.0718959793448448, 0.0820910185575485)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.930261, 
    farPlane=0.955358, width=0.177692, height=0.0897132, cameraPosition=(
    0.110462, 0.120756, 0.942809), cameraTarget=(0.110462, 0.120756, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0995674, 
    0.0998265, 0.942809), cameraTarget=(0.0995674, 0.0998265, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.929459, 
    farPlane=0.956159, cameraPosition=(0.0952095, 0.0943761, 0.942809), 
    cameraTarget=(0.0952095, 0.0943761, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.936456, 
    farPlane=0.949162, width=0.0794932, height=0.0401346, cameraPosition=(
    0.084449, 0.0857315, 0.942809), cameraTarget=(0.084449, 0.0857315, 0))
s.delete(objectList=(g[13], v[20], c[51]))
s.Line(point1=(0.0718959793448448, 0.0820910185575485), point2=(0.065, 0.075))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.938856, 
    farPlane=0.946762, width=0.049456, height=0.0249693, cameraPosition=(
    0.0776793, 0.0774119, 0.942809), cameraTarget=(0.0776793, 0.0774119, 0))
s.Spot(point=(0.06, 0.08))
s.dragEntity(entity=v[18], points=((0.06, 0.08), (0.06, 0.08), (
    0.059500940144062, 0.08), (0.0595615841448307, 0.0795508623123169), (
    0.0596525520086288, 0.0793688297271729), (0.059500940144062, 
    0.0793991684913635)))
s.delete(objectList=(v[59], ))
s.delete(objectList=(g[11], ))
s.dragEntity(entity=v[18], points=((0.059500940144062, 0.0793991684913635), (
    0.059500940144062, 0.0793991684913635), (0.0591977164149284, 
    0.0791564509272575), (0.0590764246881008, 0.0788833945989609), (
    0.0590461045503616, 0.0788833945989609)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.925071, 
    farPlane=0.960547, width=0.221943, height=0.112055, cameraPosition=(
    0.159985, 0.0733448, 0.942809), cameraTarget=(0.159985, 0.0733448, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.113175, 
    0.0816502, 0.942809), cameraTarget=(0.113175, 0.0816502, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.931306, 
    farPlane=0.954312, width=0.143925, height=0.0726651, cameraPosition=(
    0.0897838, 0.0847404, 0.942809), cameraTarget=(0.0897838, 0.0847404, 0))
s.dragEntity(entity=v[18], points=((0.0590461045503616, 0.0788833945989609), (
    0.0590461045503616, 0.0788833945989609), (0.058854453265667, 0.08), (
    0.058854453265667, 0.0788689330220222), (0.0583249889314175, 0.08), (
    0.0584132336080074, 0.08)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.940507, 
    farPlane=0.945111, width=0.0288046, height=0.0145429, cameraPosition=(
    0.0647001, 0.0807064, 0.942809), cameraTarget=(0.0647001, 0.0807064, 0))
s.dragEntity(entity=v[18], points=((0.0584132336080074, 0.08), (
    0.0584132336080074, 0.08), (0.0583157911896706, 0.0797433629631996)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.911084, 
    farPlane=0.974534, width=0.449236, height=0.22681, cameraPosition=(
    0.175436, 0.110631, 0.942809), cameraTarget=(0.175436, 0.110631, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.14018, 
    0.0888596, 0.942809), cameraTarget=(0.14018, 0.0888596, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.934158, 
    farPlane=0.95146, width=0.108247, height=0.0546517, cameraPosition=(
    0.0736015, 0.0749969, 0.942809), cameraTarget=(0.0736015, 0.0749969, 0))
s.Line(point1=(0.0583157911896706, 0.0797433629631996), point2=(
    0.0434370189905167, 0.0664585903286934))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.926681, 
    farPlane=0.958937, width=0.228378, height=0.115304, cameraPosition=(
    0.116787, 0.0776322, 0.942809), cameraTarget=(0.116787, 0.0776322, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.120568, 
    0.0524139, 0.942809), cameraTarget=(0.120568, 0.0524139, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.933568, 
    farPlane=0.95205, width=0.115627, height=0.058378, cameraPosition=(
    0.0787549, 0.0646114, 0.942809), cameraTarget=(0.0787549, 0.0646114, 0))
s.dragEntity(entity=v[61], points=((0.0434370189905167, 0.0664585903286934), (
    0.0434370189905167, 0.0664585903286934), (0.0439107120037079, 
    0.06599460542202), (0.0441233888268471, 0.06599460542202)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.925652, 
    farPlane=0.959966, width=0.242955, height=0.122663, cameraPosition=(
    0.102985, 0.068563, 0.942809), cameraTarget=(0.102985, 0.068563, 0))
s.delete(objectList=(g[10], ))
s.delete(objectList=(v[17], ))
s.Line(point1=(0.0441233888268471, 0.06599460542202), point2=(0.095, 0.015))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.927649, 
    farPlane=0.957969, width=0.189687, height=0.0957693, cameraPosition=(
    0.101396, 0.109494, 0.942809), cameraTarget=(0.101396, 0.109494, 0))
s.delete(objectList=(v[54], ))
s.dragEntity(entity=g[19], points=((0.0567064010422025, 0.100569323428493), (
    0.0565617121756077, 0.1), (0.0586551353335381, 0.105), (0.06, 0.105), (
    0.06, 0.105), (0.06, 0.103035598993301), (0.06, 0.101755574345589), (0.06, 
    0.102221041917801), (0.06, 0.102686502039433), (0.06, 0.103151962161064), (
    0.0587714314460754, 0.103384703397751), (0.06, 0.103268332779408)))
s.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.9285, 
    farPlane=0.957118, width=0.20262, height=0.102299, cameraPosition=(
    0.101566, 0.114297, 0.942809), cameraTarget=(0.101566, 0.114297, 0))
s.dragEntity(entity=v[57], points=((0.0718959793448448, 0.0820910185575485), (
    0.0718959793448448, 0.0820910185575485), (0.07, 0.08), (0.071315623819828, 
    0.0817929357290268), (0.0715640857815742, 0.08), (0.07, 
    0.0814200341701508), (0.07, 0.08)))
s.dragEntity(entity=v[57], points=((0.07, 0.08), (0.07, 0.08), (0.07, 
    0.0817929357290268), (0.0720610171556473, 0.0815443322062492), (
    0.0714398622512817, 0.0821658298373222), (0.07, 0.0819172337651253), (
    0.071315623819828, 0.0820415318012238), (0.0714398622512817, 
    0.0815443322062492), (0.07, 0.0817929357290268)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.92544, 
    farPlane=0.960178, width=0.217321, height=0.109721, cameraPosition=(
    0.100657, 0.116326, 0.942809), cameraTarget=(0.100657, 0.116326, 0))
s.dragEntity(entity=v[57], points=((0.07, 0.0817929357290268), (0.07, 
    0.0817929357290268), (0.07, 0.08), (0.07, 0.0815966352820396), (0.07, 
    0.0814633145928383)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.920104, 
    farPlane=0.965514, width=0.28409, height=0.143431, cameraPosition=(
    0.0355266, 0.0817492, 0.942809), cameraTarget=(0.0355266, 0.0817492, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.921466, 
    farPlane=0.964152, cameraPosition=(0.0417972, 0.0461964, 0.942809), 
    cameraTarget=(0.0417972, 0.0461964, 0))
s.delete(objectList=(g[3], g[4], g[5], g[6], g[16], g[18], v[3], v[7], v[8], 
    v[9], v[46], c[5], c[8], c[9], c[12], c[13], c[14], c[17], c[18], c[19], 
    c[22], c[63], c[81], c[83]))
s.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.917113, 
    farPlane=0.968505, width=0.321514, height=0.162326, cameraPosition=(
    0.0383061, 0.0437321, 0.942809), cameraTarget=(0.0383061, 0.0437321, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0590045, 
    0.0896883, 0.942809), cameraTarget=(0.0590045, 0.0896883, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.932003, 
    farPlane=0.953615, width=0.135204, height=0.0682619, cameraPosition=(
    0.0650966, 0.0933502, 0.942809), cameraTarget=(0.0650966, 0.0933502, 0))
s.delete(objectList=(v[19], ))
s.delete(objectList=(v[18], ))
s.dragEntity(entity=v[40], points=((0.0644577229377877, 0.0744423856976378), (
    0.065, 0.075), (0.0632314383983612, 0.0758078545331955), (
    0.0640604048967361, 0.075), (0.0641433000564575, 0.075), (
    0.063811719417572, 0.075)))
s.dragEntity(entity=v[58], points=((0.0644577229377877, 0.0744423856976378), (
    0.065, 0.075), (0.0634801313281059, 0.075), (0.0638946071267128, 0.075)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.928855, 
    farPlane=0.956763, width=0.174592, height=0.0881481, cameraPosition=(
    -0.00466585, 0.0502866, 0.942809), cameraTarget=(-0.00466585, 0.0502866, 
    0))
s.delete(objectList=(c[8], ))
s.delete(objectList=(v[9], ))
s.delete(objectList=(v[46], ))
s.delete(objectList=(v[51], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.907219, 
    farPlane=0.978399, width=0.503962, height=0.25444, cameraPosition=(
    -0.0369094, 0.0165588, 0.942809), cameraTarget=(-0.0369094, 0.0165588, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0106749, 
    0.0663338, 0.942809), cameraTarget=(0.0106749, 0.0663338, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.934233, 
    farPlane=0.951385, width=0.107299, height=0.0541729, cameraPosition=(
    -0.0176298, 0.0272195, 0.942809), cameraTarget=(-0.0176298, 0.0272195, 0))
s.delete(objectList=(g[4], ))
s.dragEntity(entity=v[3], points=((-0.02, 0.02), (-0.02, 0.02), (
    -0.0191100165247917, 0.0211966261267662), (-0.0186495035886765, 
    0.020867507904768), (-0.01897843927145, 0.02), (-0.02, 0.02)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.934233, 
    farPlane=0.951385, width=0.121433, height=0.0613093, cameraPosition=(
    -0.0179375, 0.0278308, 0.942809), cameraTarget=(-0.0179375, 0.0278308, 0))
s.dragEntity(entity=v[3], points=((-0.02, 0.02), (-0.02, 0.02), (
    -0.0189425870776176, 0.0210890248417854), (-0.0184214115142822, 
    0.0216104909777641), (-0.017825786024332, 0.021982965990901), (
    -0.0168578922748566, 0.0225789230316877), (-0.0164856240153313, 
    0.0231003891676664), (-0.0161878131330013, 0.0237708427011967), (-0.015, 
    0.025), (-0.015, 0.025), (-0.015, 0.025), (-0.0139542110264301, 
    0.0260056890547276), (-0.0139542110264301, 0.0260801836848259)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.920757, 
    farPlane=0.96486, width=0.275911, height=0.139302, cameraPosition=(
    -0.0298497, 0.0075041, 0.942809), cameraTarget=(-0.0298497, 0.0075041, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.00652106, 
    0.048296, 0.942809), cameraTarget=(0.00652106, 0.048296, 0))
s.dragEntity(entity=v[3], points=((-0.0139542110264301, 0.0260801836848259), (
    -0.015, 0.025), (-0.0120026702061296, 0.03), (-0.01, 0.0279000513255596), (
    -0.0123410010710359, 0.03), (-0.011664324440062, 0.0280693136155605), (
    -0.01, 0.03), (-0.01, 0.03), (-0.01, 0.03), (-0.0069276699796319, 
    0.0317930579185486), (-0.00726600084453821, 0.0333164036273956), (
    -0.00709683541208506, 0.0324700996279716), (-0.00811183545738459, 0.03), (
    -0.01, 0.03), (-0.01, 0.03), (-0.01, 0.03), (-0.011664324440062, 
    0.0279000513255596)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.90385, 
    farPlane=0.981768, width=0.551672, height=0.278528, cameraPosition=(
    0.00446358, 0.0308663, 0.942809), cameraTarget=(0.00446358, 0.0308663, 0))
s.delete(objectList=(v[11], ))
s.dragEntity(entity=v[33], points=((0.06, -0.02), (0.06, -0.02), (0.065, 
    -0.015)))
s.undo()
s.dragEntity(entity=v[33], points=((0.06, -0.02), (0.06, -0.02), (0.065, 
    -0.015), (0.065, -0.015)))
s.undo()
s.undo()
s.delete(objectList=(g[5], g[6], v[7], v[8], c[13], c[14], c[18], c[22]))
s.delete(objectList=(g[16], c[81]))
s.delete(objectList=(v[3], ))
s.dragEntity(entity=v[22], points=((-0.011664324440062, 0.0279000513255596), (
    -0.01, 0.03), (-0.01, 0.03)))
s.Line(point1=(0.005, 0.015), point2=(-0.01, 0.03))
s.undo()
s.Line(point1=(0.005, 0.015), point2=(-0.01, 0.03))
s.Line(point1=(-0.01, 0.03), point2=(0.005, 0.015))
s.ParallelConstraint(entity1=g[24], entity2=g[25], addUndoState=False)
#: Warning: Coincident point selected.
s.dragEntity(entity=v[63], points=((0.005, 0.015), (0.005, 0.015), (0.005, 
    0.02), (0.005, 0.015), (0.01, 0.02), (0.005, 0.015), (0.01, 0.015), (0.005, 
    0.02), (0.01, 0.015), (0.005, 0.02), (0.005, 0.02), (0.0, 0.02), (0.005, 
    0.02), (0.005, 0.015)))
s.Line(point1=(0.005, 0.015), point2=(0.0118136730889091, 0.0218136730836704))
s.Line(point1=(0.0118136730889091, 0.0218136730836704), point2=(
    0.0061522275311745, 0.0274751186458388))
s.PerpendicularConstraint(entity1=g[26], entity2=g[27], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.939098, 
    farPlane=0.94652, width=0.052546, height=0.0265295, cameraPosition=(
    0.00800603, 0.0283079, 0.942809), cameraTarget=(0.00800603, 0.0283079, 0))
s.delete(objectList=(g[27], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.92909, 
    farPlane=0.956528, width=0.194268, height=0.0980821, cameraPosition=(
    -0.00497752, 0.0254086, 0.942809), cameraTarget=(-0.00497752, 0.0254086, 
    0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0130081, 
    0.0429275, 0.942809), cameraTarget=(0.0130081, 0.0429275, 0))
s.dragEntity(entity=v[64], points=((0.0118136730889091, 0.0218136730836704), (
    0.0118136730889091, 0.0218136730836704), (0.00782683212310076, 0.025), (
    0.0069930674508214, 0.0271366462111473), (0.00639752019196749, 
    0.0283284075558186), (0.00758861470967531, 0.0266599394381046), (0.01, 
    0.025), (0.01, 0.0229654777795076), (0.0112810106948018, 
    0.0218928903341293), (0.0112810106948018, 0.0217737145721912)))
s.undo()
s.undo()
s.dragEntity(entity=v[53], points=((0.01, 0.03), (0.01, 0.03), (0.01, 
    0.0330954566597939), (0.00854149181395769, 0.0314269885420799), (0.01, 
    0.03), (0.00854149181395769, 0.0313078165054321), (0.01, 0.03), (
    0.00854149181395769, 0.03), (0.00842237938195467, 0.03)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.923962, 
    farPlane=0.961656, width=0.235811, height=0.119056, cameraPosition=(
    -0.012502, 0.0562724, 0.942809), cameraTarget=(-0.012502, 0.0562724, 0))
s.dragEntity(entity=v[53], points=((0.00842237938195467, 0.03), (
    0.00842237938195467, 0.03), (0.00665497034788132, 0.0327649265527725), (
    0.005, 0.0321862809360027), (0.00679955631494522, 0.0321862809360027), (
    0.00708872824907303, 0.0323309414088726)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.921305, 
    farPlane=0.964313, width=0.269063, height=0.135845, cameraPosition=(
    -0.0495717, 0.0622416, 0.942809), cameraTarget=(-0.0495717, 0.0622416, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.0187226, 
    0.0336862, 0.942809), cameraTarget=(-0.0187226, 0.0336862, 0))
s.dragEntity(entity=v[53], points=((0.00708872824907303, 0.0323309414088726), (
    0.00708872824907303, 0.0323309414088726), (0.01, 0.03), (0.01, 
    0.0317880064249039), (0.00824972428381443, 0.03), (0.01, 
    0.0317880064249039), (0.00791978277266026, 0.031622938811779), (
    0.00791978277266026, 0.0321181267499924)))
s.dragEntity(entity=v[53], points=((0.00791978277266026, 0.0321181267499924), (
    0.00791978277266026, 0.0321181267499924), (0.00808475352823734, 
    0.0326133072376251), (0.01, 0.031622938811779), (0.01, 0.03), (
    0.00808475352823734, 0.03), (0.01, 0.03)))
s.dragEntity(entity=v[65], points=((0.0061522275311745, 0.0274751186458388), (
    0.00709494389593601, 0.0270012505352497)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.900335, 
    farPlane=0.985282, width=0.60144, height=0.303655, cameraPosition=(
    -0.12784, -0.0163588, 0.942809), cameraTarget=(-0.12784, -0.0163588, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.881862, 
    farPlane=1.02951, cameraPosition=(-0.0657097, -0.295367, 0.898434), 
    cameraUpVector=(0.0423411, 0.954978, 0.29364))
s.undo()
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.00372712, 
    -0.216967, 0.918495), cameraTarget=(-0.0658574, 0.0620411, 0.0200607))
s.undo()
s.undo()
s.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.882042, 
    farPlane=1.03331, cameraPosition=(-0.0300483, -0.263262, 0.90427), 
    cameraUpVector=(0.0114291, 0.938829, 0.344193), cameraTarget=(-0.0662121, 
    0.0614173, 0.019869))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.88329, 
    farPlane=1.02941, cameraPosition=(-0.0106976, -0.214332, 0.919767), 
    cameraUpVector=(0.0405485, 0.955781, 0.291269), cameraTarget=(-0.0659117, 
    0.0621769, 0.0201096))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.393191, 
    farPlane=0.484813, cameraPosition=(0.00566646, -0.0414196, 0.426873), 
    cameraUpVector=(-0.0131827, 0.972899, 0.230853))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.397551, 
    farPlane=0.480454, cameraPosition=(-0.0027884, -0.00958604, 0.432846), 
    cameraUpVector=(-0.000166469, 0.987301, 0.158859), cameraTarget=(0.0199338, 
    0.0600639, -4.65661e-09))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.376252, 
    farPlane=0.501752, width=0.653672, height=0.330026, cameraPosition=(
    0.0976649, -0.0745897, 0.427659), cameraTarget=(0.120387, -0.00493976, 
    -0.00518654))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.00199448, 
    -0.000178248, 0.434611), cameraTarget=(0.0247167, 0.0694716, 0.0017649))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.394276, 
    farPlane=0.483729, width=0.352078, height=0.177757, cameraPosition=(
    -0.0147615, -0.017037, 0.431019), cameraTarget=(0.00796071, 0.0526129, 
    -0.00182746))
s.dragEntity(entity=v[53], points=((0.00842237938195467, 0.03), (0.01, 0.03), (
    0.01, 0.03), (0.01, 0.035), (0.01, 0.03), (0.0078095830976963, 
    0.0320830494165421), (0.01, 0.0323018506169319), (0.01, 
    0.0320831164717674)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.401763, 
    farPlane=0.476242, width=0.258391, height=0.130457, cameraPosition=(
    -0.0141949, -0.0216527, 0.430306), cameraTarget=(0.00852729, 0.0479971, 
    -0.00254044))
s.dragEntity(entity=v[53], points=((0.01, 0.0320831164717674), (0.01, 
    0.0320831164717674), (0.00786841940134764, 0.0316133052110672), (
    0.00818829704076052, 0.0319344699382782), (0.01, 0.0317739956080914), (
    0.00802835915237665, 0.0317738875746727), (0.00818700063973665, 
    0.0317739136517048)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.406159, 
    farPlane=0.471846, width=0.203393, height=0.102689, cameraPosition=(
    0.00770242, -0.0242139, 0.431043), cameraTarget=(0.0304246, 0.045436, 
    -0.00180307))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0276315, 
    -0.0432227, 0.42903), cameraTarget=(0.0503538, 0.0264272, -0.00381562))
session.viewports['Viewport: 1'].view.setValues(width=0.191189, 
    height=0.0965276, cameraPosition=(0.0321635, -0.0438099, 0.429173), 
    cameraTarget=(0.0548858, 0.02584, -0.0036722))
s.dragEntity(entity=v[65], points=((0.0061522275311745, 0.0274751186458388), (
    0.0061522275311745, 0.0274751186458388), (0.005, 0.0286264084279537), (
    0.005, 0.028269961476326), (0.005, 0.03), (0.005, 0.03), (
    0.00371510349214077, 0.0281509906053543), (0.005, 0.0287450700998306), (
    0.005, 0.0288640819489956), (0.005, 0.0287452898919582)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.386078, 
    farPlane=0.491926, width=0.514538, height=0.25978, cameraPosition=(
    0.062588, -0.0770019, 0.42543), cameraTarget=(0.0853103, -0.00735201, 
    -0.00741605))
s.delete(objectList=(v[11], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.375873, 
    farPlane=0.502131, width=0.659032, height=0.332732, cameraPosition=(
    0.0751107, -0.0950826, 0.423178), cameraTarget=(0.097833, -0.0254327, 
    -0.00966807))
s.dragEntity(entity=v[33], points=((0.06, -0.02), (0.06, -0.02), (0.065, 
    -0.015), (0.07, -0.01), (0.07, -0.01)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.388258, 
    farPlane=0.489746, width=0.427367, height=0.215769, cameraPosition=(
    0.0275484, -0.0755729, 0.42382), cameraTarget=(0.0502707, -0.00592297, 
    -0.0090255))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0330358, 
    -0.029284, 0.431557), cameraTarget=(0.0557581, 0.0403659, -0.00128901))
s.dragEntity(entity=g[18], points=((0.0305814907345414, 0.0093963170879438), (
    0.03, 0.01), (0.035, 0.01), (0.04, 0.015), (0.04, 0.015), (0.04, 0.015), (
    0.04, 0.015), (0.04, 0.02)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.412787, 
    farPlane=0.466805, width=0.140315, height=0.0708421, cameraPosition=(
    0.0659946, -0.0496996, 0.430002), cameraTarget=(0.0887169, 0.0199503, 
    -0.00284395))
s.dragEntity(entity=g[18], points=((0.0636094727756168, -0.00359166270896317), 
    (0.0635279044508934, -0.0036592110991478), (0.065, -0.00409494340419769), (
    0.0639544129371643, -0.005), (0.065, -0.00409499555826187), (
    0.0640426725149155, -0.00392067432403564), (0.065, -0.00400783121585846)))
s.dragEntity(entity=g[18], points=((0.0637934242915838, -0.00280216570115964), 
    (0.0634459853172302, -0.00313610583543777), (0.0630166605114937, 
    -0.00296181440353394)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.408658, 
    farPlane=0.470933, width=0.217261, height=0.109691, cameraPosition=(
    0.0642809, -0.0431398, 0.430968), cameraTarget=(0.0870032, 0.0265101, 
    -0.00187835))
s.dragEntity(entity=v[52], points=((0.0700322727097517, -0.00997213429721339), 
    (0.07, -0.01), (0.0713525488972664, -0.00842117518186569), (0.07, -0.01), (
    0.07, -0.01)))
s.undo()
session.viewports['Viewport: 1'].view.setValues(width=0.204225, 
    height=0.103109, cameraPosition=(0.0602179, -0.0421718, 0.43091), 
    cameraTarget=(0.0829402, 0.0274781, -0.00193587))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0339557, 
    -0.0282299, 0.431775), cameraTarget=(0.056678, 0.04142, -0.0010711))
s.Line(point1=(0.0182192733494884, 0.0418017793544914), point2=(0.005, 
    0.0287452898919582))
#: Warning: Coincident point selected.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41333, 
    farPlane=0.466262, width=0.133521, height=0.0674122, cameraPosition=(
    0.029885, -0.0101335, 0.434473), cameraTarget=(0.0526073, 0.0595164, 
    0.00162713))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41397, 
    farPlane=0.465621, cameraPosition=(0.0385479, 0.00815414, 0.437871), 
    cameraTarget=(0.0612702, 0.077804, 0.00502458))
s.dragEntity(entity=v[40], points=((0.063811719417572, 0.075), (
    0.063811719417572, 0.075), (0.0636724904179573, 0.075), (
    0.0636704862117767, 0.0741743147373199), (0.063673160970211, 0.075), (
    0.0633419156074524, 0.0740912929177284), (0.0637564808130264, 0.075), (
    0.0639204233884811, 0.075), (0.0640843659639359, 0.075), (
    0.0635078772902489, 0.075), (0.063669815659523, 0.0740913450717926)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.418254, 
    farPlane=0.461338, width=0.0719165, height=0.0363092, cameraPosition=(
    0.0400221, 0.00378067, 0.437245), cameraTarget=(0.0627444, 0.0734305, 
    0.00439823))
s.dragEntity(entity=v[40], points=((0.063669815659523, 0.0740913450717926), (
    0.063669815659523, 0.0740913450717926), (0.0634010583162308, 0.075), (
    0.0633113086223602, 0.075), (0.063529908657074, 0.0744734779000282), (
    0.0635751485824585, 0.075), (0.0637068822979927, 0.0745181888341904)))
s.dragEntity(entity=v[58], points=((0.0638946071267128, 0.075), (
    0.0638946071267128, 0.075), (0.0638389885425568, 0.0744735300540924), (
    0.0637513995170593, 0.0745628848671913)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.391784, 
    farPlane=0.487809, width=0.403113, height=0.203524, cameraPosition=(
    -0.0116333, -0.0111637, 0.432128), cameraTarget=(0.011089, 0.0584861, 
    -0.000718138))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=True)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.890728, 
    farPlane=0.99489, width=0.737483, height=0.37234, cameraPosition=(
    -0.000613681, 0.00810771, 0.942809), cameraTarget=(-0.000613681, 
    0.00810771, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.000742831, 
    0.00810771, 0.942809), cameraTarget=(0.000742831, 0.00810771, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.76751, 
    farPlane=1.11111, cameraPosition=(-0.276421, -0.37317, 0.816515), 
    cameraUpVector=(-0.752738, 0.656344, 0.05097), cameraTarget=(0.000742831, 
    0.00810771, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.266593, 
    -0.371855, 0.820465), cameraTarget=(0.010571, 0.00942242, 0.00395007))
session.viewports['Viewport: 1'].view.setValues(farPlane=1.11111, 
    cameraPosition=(-0.268414, -0.371828, 0.81986), cameraTarget=(0.00875032, 
    0.00944928, 0.00334459))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.76751, 
    farPlane=1.11111, cameraPosition=(-0.267008, -0.370973, 0.820736), 
    cameraTarget=(0.0101562, 0.0103043, 0.0042211))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.269466, 
    -0.368309, 0.821145), cameraTarget=(0.00769813, 0.0129678, 0.00463046))
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883868, 
    farPlane=1.00175, width=0.834634, height=0.42139, cameraPosition=(
    -0.00820292, 0.029771, 0.942809), cameraTarget=(-0.00820292, 0.029771, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.000496559, 
    0.030795, 0.942809), cameraTarget=(0.000496559, 0.030795, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.890728, 
    farPlane=0.99489, width=0.65164, height=0.329, cameraPosition=(0.00302101, 
    0.0196251, 0.942809), cameraTarget=(0.00302101, 0.0196251, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.893853, 
    farPlane=0.991765, cameraPosition=(0.00102336, 0.0112302, 0.942809), 
    cameraTarget=(0.00102336, 0.0112302, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887404, 
    farPlane=0.998214, width=0.784556, height=0.396107, cameraPosition=(
    -0.0127083, 0.0402174, 0.942809), cameraTarget=(-0.0127083, 0.0402174, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883867, 
    farPlane=1.00175, cameraPosition=(-0.00260675, 0.0392548, 0.942809), 
    cameraTarget=(-0.00260675, 0.0392548, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.737483, height=0.37234, 
    cameraPosition=(0.00162148, 0.0290754, 0.942809), cameraTarget=(0.00162148, 
    0.0290754, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887404, 
    farPlane=0.998214, cameraPosition=(0.000264972, 0.0295278, 0.942809), 
    cameraTarget=(0.000264972, 0.0295278, 0))
s.ArcByCenterEnds(center=(0.035, 0.085), point1=(-0.04, 0.03), point2=(0.085, 
    0.165), direction=CLOCKWISE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.763973, 
    farPlane=1.00453, cameraPosition=(0.108301, 0.752261, 0.595713), 
    cameraUpVector=(-0.411424, 0.615548, -0.672184), cameraTarget=(0.000264972, 
    0.0295278, 0))
s.undo()
s.undo()
#* Nothing to undo.
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.890728, 
    farPlane=0.99489, width=0.737483, height=0.37234, cameraPosition=(
    -0.00400167, 0.000556472, 0.942809), cameraTarget=(-0.00400167, 
    0.000556472, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887404, 
    farPlane=0.998214, cameraPosition=(6.7804e-05, -0.010754, 0.942809), 
    cameraTarget=(6.7804e-05, -0.010754, 0))
s1.ArcByCenterEnds(center=(0.035, 0.045), point1=(-0.04, -0.01), point2=(0.09, 
    0.12), direction=CLOCKWISE)
s1.undo()
s1.ArcByCenterEnds(center=(0.04, 0.04), point1=(-0.04, -0.01), point2=(0.085, 
    0.125), direction=CLOCKWISE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887404, 
    farPlane=0.998214, width=0.693234, height=0.35, cameraPosition=(0.00435802, 
    -0.0036174, 0.942809), cameraTarget=(0.00435802, -0.0036174, 0))
s1.Spot(point=(0.06, 0.095))
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.997, 
    farPlane=222.75, width=174.194, height=87.947, viewOffsetX=18.5835, 
    viewOffsetY=37.0809)
session.Image(name='imp3', fileName='C:/temp/imp3.jpeg')
session.viewports['Viewport: 1'].imageOptions.setValues(imageName='imp3')
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.876103, 
    farPlane=1.00952, width=0.834634, height=0.42139, cameraPosition=(
    -0.0142614, 0.0165247, 0.942809), cameraTarget=(-0.0142614, 0.0165247, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.0224491, 
    0.0129406, 0.942809), cameraTarget=(-0.0224491, 0.0129406, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.887909, 
    height=0.448288, cameraPosition=(-0.0320686, 0.0166173, 0.942809), 
    cameraTarget=(-0.0320686, 0.0166173, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.876103, 
    farPlane=1.00952, cameraPosition=(-0.0467672, 0.0247878, 0.942809), 
    cameraTarget=(-0.0467672, 0.0247878, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.871845, 
    farPlane=1.01377, width=0.887909, height=0.448288, cameraPosition=(
    -0.0467672, 0.0247878, 0.942809), cameraTarget=(-0.0467672, 0.0247878, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.876103, 
    farPlane=1.00952, cameraPosition=(-0.0418676, 0.022609, 0.942809), 
    cameraTarget=(-0.0418676, 0.022609, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.880105, 
    farPlane=1.00551, width=0.784556, height=0.396107, cameraPosition=(
    -0.0313169, 0.0104039, 0.942809), cameraTarget=(-0.0313169, 0.0104039, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883867, 
    farPlane=1.00175, cameraPosition=(-0.0250635, -0.000184588, 0.942809), 
    cameraTarget=(-0.0250635, -0.000184588, 0))
s.ArcByCenterEnds(center=(0.02, 0.055), point1=(-0.065, 0.0), point2=(0.07, 
    0.14), direction=CLOCKWISE)
session.viewports['Viewport: 1'].view.setValues(width=0.737483, 
    height=0.372341, cameraPosition=(-0.0360002, -0.010631, 0.942809), 
    cameraTarget=(-0.0360002, -0.010631, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.0210787, 
    0.00791818, 0.942809), cameraTarget=(-0.0210787, 0.00791818, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.784556, 
    height=0.396107, cameraPosition=(-0.0232866, 0.0102717, 0.942809), 
    cameraTarget=(-0.0232866, 0.0102717, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883867, 
    farPlane=1.00175, cameraPosition=(-0.0228056, 0.00160839, 0.942809), 
    cameraTarget=(-0.0228056, 0.00160839, 0))
s.Line(point1=(-0.04, 0.02), point2=(-0.065, 0.0))
s.delete(objectList=(g[3], ))
s.Line(point1=(-0.065, 0.0), point2=(0.0713318754731277, 0.142264188304317))
s.Line(point1=(-0.04, 0.0260878440589565), point2=(-0.0249999999898137, 
    0.0117133331174406))
s.CoincidentConstraint(entity1=v[4], entity2=g[4], addUndoState=False)
s.Line(point1=(-0.0249999999898137, 0.0117133331174406), point2=(0.065, 
    0.105629571816771))
s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s.Line(point1=(0.065, 0.105629571816771), point2=(0.05, 0.120004082710919))
s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s.CoincidentConstraint(entity1=v[7], entity2=g[4], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.890728, 
    farPlane=0.99489, width=0.737483, height=0.372341, cameraPosition=(
    -0.0211109, 0.00294341, 0.942809), cameraTarget=(-0.0211109, 0.00294341, 
    0))
s.Line(point1=(-0.0170588810771032, 0.02), point2=(-0.0215006496873684, 
    0.0242565500957426))
s.PerpendicularConstraint(entity1=g[6], entity2=g[8], addUndoState=False)
s.CoincidentConstraint(entity1=v[8], entity2=g[6], addUndoState=False)
s.Line(point1=(-0.0215006496873684, 0.0242565500957426), point2=(
    0.0510525771939001, 0.0999668409382366))
s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.924618, 
    farPlane=0.961, width=0.227605, height=0.114913, cameraPosition=(0.0312525, 
    0.0665965, 0.942809), cameraTarget=(0.0312525, 0.0665965, 0))
s.Line(point1=(0.0510525771939001, 0.0999668409382366), point2=(
    0.0554943458098652, 0.0957102908382109))
s.CoincidentConstraint(entity1=v[11], entity2=g[6], addUndoState=False)
s.delete(objectList=(g[6], ))
s.Line(point1=(-0.0249999999898137, 0.0117133331174406), point2=(
    -0.0170588810771032, 0.02))
s.PerpendicularConstraint(entity1=g[5], entity2=g[11], addUndoState=False)
s.undo()
s.undo()
s.undo()
s.undo()
s.undo()
s.undo()
s.undo()
s.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.893853, 
    farPlane=0.991765, width=0.693235, height=0.35, cameraPosition=(0.12789, 
    0.0876222, 0.942809), cameraTarget=(0.12789, 0.0876222, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.0166225, 
    0.017452, 0.942809), cameraTarget=(-0.0166225, 0.017452, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.880105, 
    farPlane=1.00551, width=0.784557, height=0.396107, cameraPosition=(
    -0.0237341, 0.0121779, 0.942809), cameraTarget=(-0.0237341, 0.0121779, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883867, 
    farPlane=1.00175, cameraPosition=(-0.0256583, 0.00303328, 0.942809), 
    cameraTarget=(-0.0256583, 0.00303328, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883867, 
    farPlane=1.00175, cameraPosition=(-0.0246963, 0.00640235, 0.942809), 
    cameraTarget=(-0.0246963, 0.00640235, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.737484, 
    height=0.372341, cameraPosition=(-0.0197754, 0.00176562, 0.942809), 
    cameraTarget=(-0.0197754, 0.00176562, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887404, 
    farPlane=0.998214, cameraPosition=(-0.0238449, -0.000948898, 0.942809), 
    cameraTarget=(-0.0238449, -0.000948898, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887404, 
    farPlane=0.998214, cameraPosition=(-0.0233927, 0.000860781, 0.942809), 
    cameraTarget=(-0.0233927, 0.000860781, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887404, 
    farPlane=0.998214, cameraPosition=(-0.02701, 0.0035753, 0.942809), 
    cameraTarget=(-0.02701, 0.0035753, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.880105, 
    farPlane=1.00551, width=0.784557, height=0.396107, cameraPosition=(
    -0.025437, 0.000239912, 0.942809), cameraTarget=(-0.025437, 0.000239912, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883867, 
    farPlane=1.00175, cameraPosition=(-0.024475, 0.000721205, 0.942809), 
    cameraTarget=(-0.024475, 0.000721205, 0))
s.undo()
s.Line(point1=(-0.065, 0.0), point2=(0.0713318754731277, 0.142264188304317))
s.Line(point1=(0.0713318754731277, 0.142264188304317), point2=(
    -0.042100444543805, 0.023896001270425))
s.ParallelConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s.CoincidentConstraint(entity1=v[4], entity2=g[4], addUndoState=False)
s.Line(point1=(-0.042100444543805, 0.023896001270425), point2=(
    -0.0275997759790458, 0.01))
s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s.Line(point1=(-0.0275997759790458, 0.01), point2=(0.0634387933652212, 0.105))
s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s.Line(point1=(0.0634387933652212, 0.105), point2=(0.0489381247902761, 
    0.11889600127754))
s.CoincidentConstraint(entity1=v[7], entity2=g[4], addUndoState=False)
s.Line(point1=(0.0489381247902761, 0.11889600127754), point2=(
    -0.042100444543805, 0.023896001270425))
s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s.Line(point1=(-0.042100444543805, 0.023896001270425), point2=(
    -0.0275997759790458, 0.01))
s.Line(point1=(-0.0275997759790458, 0.01), point2=(-0.0212241435783653, 
    0.016653060152521))
s.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.890728, 
    farPlane=0.99489, width=0.651641, height=0.329, cameraPosition=(-0.0250862, 
    0.00429705, 0.942809), cameraTarget=(-0.0250862, 0.00429705, 0))
s.Line(point1=(-0.0212241435783653, 0.016653060152521), point2=(
    -0.0273360606491906, 0.0225101147429996))
s.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.880105, 
    farPlane=1.00551, width=0.784557, height=0.396107, cameraPosition=(
    -0.024312, 0.000913164, 0.942809), cameraTarget=(-0.024312, 0.000913164, 
    0))
s.Line(point1=(-0.0273360606491906, 0.0225101147429996), point2=(
    0.0502639101297291, 0.103486752193248))
s.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.912967, 
    farPlane=0.972651, width=0.373387, height=0.188516, cameraPosition=(
    0.0135287, 0.0495942, 0.942809), cameraTarget=(0.0135287, 0.0495942, 0))
s.Line(point1=(0.0502639101297291, 0.103486752193248), point2=(
    0.0563758271987625, 0.0976296976040597))
s.PerpendicularConstraint(entity1=g[13], entity2=g[14], addUndoState=False)
s.CoincidentConstraint(entity1=v[11], entity2=g[7], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.851917, 
    farPlane=1.0337, width=1.28707, height=0.649816, cameraPosition=(0.0468305, 
    0.0701367, 0.942809), cameraTarget=(0.0468305, 0.0701367, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.413232, 
    0.0290791, 0.942809), cameraTarget=(-0.413232, 0.0290791, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.89679, 
    farPlane=0.988828, width=0.57579, height=0.290705, cameraPosition=(
    -0.16422, 0.0590216, 0.942809), cameraTarget=(-0.16422, 0.0590216, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.899551, 
    farPlane=0.986067, cameraPosition=(-0.204466, 0.0519571, 0.942809), 
    cameraTarget=(-0.204466, 0.0519571, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.612543, 
    height=0.309261, cameraPosition=(-0.219304, 0.0505705, 0.942809), 
    cameraTarget=(-0.219304, 0.0505705, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.89679, 
    farPlane=0.988828, cameraPosition=(-0.236205, 0.0479401, 0.942809), 
    cameraTarget=(-0.236205, 0.0479401, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.89679, 
    farPlane=0.988828, cameraPosition=(-0.220056, 0.0400489, 0.942809), 
    cameraTarget=(-0.220056, 0.0400489, 0))
s.delete(objectList=(g[7], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.93026, 
    farPlane=0.955358, width=0.157018, height=0.0792752, cameraPosition=(
    -0.00292318, 0.0925414, 0.942809), cameraTarget=(-0.00292318, 0.0925414, 
    0))
s.Line(point1=(0.0634387933652212, 0.105), point2=(0.0563758271987625, 
    0.0976296976040597))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.906733, 
    farPlane=0.978885, width=0.51085, height=0.257918, cameraPosition=(
    -0.0938742, 0.0822792, 0.942809), cameraTarget=(-0.0938742, 0.0822792, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.178128, 
    0.0449861, 0.942809), cameraTarget=(-0.178128, 0.0449861, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.890515, 
    farPlane=0.995103, width=0.654307, height=0.330347, cameraPosition=(
    -0.217089, 0.027355, 0.942809), cameraTarget=(-0.217089, 0.027355, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.893653, 
    farPlane=0.991965, cameraPosition=(-0.234339, 0.0297634, 0.942809), 
    cameraTarget=(-0.234339, 0.0297634, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.893653, 
    farPlane=0.991965, cameraPosition=(-0.0261321, 0.0197286, 0.942809), 
    cameraTarget=(-0.0261321, 0.0197286, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883626, 
    farPlane=1.00199, width=0.838051, height=0.423115, cameraPosition=(
    -0.039144, 0.0175306, 0.942809), cameraTarget=(-0.039144, 0.0175306, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.879848, 
    farPlane=1.00577, cameraPosition=(-0.0355472, 0.0113612, 0.942809), 
    cameraTarget=(-0.0355472, 0.0113612, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.787768, 
    height=0.397728, cameraPosition=(-0.0322639, 0.0105746, 0.942809), 
    cameraTarget=(-0.0322639, 0.0105746, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883626, 
    farPlane=1.00199, cameraPosition=(-0.0226039, 0.0202399, 0.942809), 
    cameraTarget=(-0.0226039, 0.0202399, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883626, 
    farPlane=1.00199, cameraPosition=(-0.0250189, 0.00187577, 0.942809), 
    cameraTarget=(-0.0250189, 0.00187577, 0))
s.Line(point1=(-0.005, 0.04581810142265), point2=(0.0532469570303427, -0.01))
s.PerpendicularConstraint(entity1=g[13], entity2=g[16], addUndoState=False)
s.CoincidentConstraint(entity1=v[12], entity2=g[13], addUndoState=False)
s.Line(point1=(0.0532469570303427, -0.01), point2=(0.0850019748895647, 
    0.0231367981405128))
s.PerpendicularConstraint(entity1=g[16], entity2=g[17], addUndoState=False)
s.Line(point1=(0.0850019748895647, 0.0231367981405128), point2=(
    0.0267550178617113, 0.0789548995785157))
s.PerpendicularConstraint(entity1=g[17], entity2=g[18], addUndoState=False)
s.CoincidentConstraint(entity1=v[15], entity2=g[13], addUndoState=False)
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.914643, 
    farPlane=0.970975, width=0.35242, height=0.17793, cameraPosition=(
    -0.0124004, 0.0488051, 0.942809), cameraTarget=(-0.0124004, 0.0488051, 0))
s.delete(objectList=(g[13], ))
s.Line(point1=(-0.0273360606491906, 0.0225101147429996), point2=(-0.005, 
    0.04581810142265))
s.PerpendicularConstraint(entity1=g[12], entity2=g[19], addUndoState=False)
s.Line(point1=(0.0267550178617113, 0.0789548995785157), point2=(
    0.0502639101297291, 0.103486752193248))
s.PerpendicularConstraint(entity1=g[18], entity2=g[20], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.906733, 
    farPlane=0.978885, width=0.51085, height=0.257918, cameraPosition=(
    -0.0286403, 0.0335746, 0.942809), cameraTarget=(-0.0286403, 0.0335746, 0))
s.delete(objectList=(g[4], ))
s.delete(objectList=(g[5], ))
s.delete(objectList=(g[9], ))
s.Line(point1=(-0.065, 0.0), point2=(-0.042100444543805, 0.023896001270425))
s.Line(point1=(0.0489381247902761, 0.11889600127754), point2=(
    0.0713318754731277, 0.142264188304317))
s.PerpendicularConstraint(entity1=g[8], entity2=g[22], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.887177, 
    farPlane=0.998441, width=0.787768, height=0.397728, cameraPosition=(
    0.0189257, 0.0479379, 0.942809), cameraTarget=(0.0189257, 0.0479379, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.03517, 
    0.0406889, 0.942809), cameraTarget=(-0.03517, 0.0406889, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.890515, 
    farPlane=0.995103, width=0.654307, height=0.330347, cameraPosition=(
    -0.0411706, 0.055525, 0.942809), cameraTarget=(-0.0411706, 0.055525, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.893653, 
    farPlane=0.991965, cameraPosition=(0.0470867, 0.053518, 0.942809), 
    cameraTarget=(0.0470867, 0.053518, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.883626, 
    farPlane=1.00199, width=0.838051, height=0.423115, cameraPosition=(
    0.0616758, 0.0365537, 0.942809), cameraTarget=(0.0616758, 0.0365537, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.879848, 
    farPlane=1.00577, cameraPosition=(0.0282771, 0.0509488, 0.942809), 
    cameraTarget=(0.0282771, 0.0509488, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.914296, 
    farPlane=0.971322, width=0.403761, height=0.203851, cameraPosition=(
    0.0495894, 0.0495468, 0.942809), cameraTarget=(0.0495894, 0.0495468, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.00428708, 
    0.0626745, 0.942809), cameraTarget=(0.00428708, 0.0626745, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.910539, 
    farPlane=0.975079, width=0.45695, height=0.230705, cameraPosition=(
    0.00935812, 0.0566544, 0.942809), cameraTarget=(0.00935812, 0.0566544, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.90848, 
    farPlane=0.977138, cameraPosition=(-0.00633113, 0.0586166, 0.942809), 
    cameraTarget=(-0.00633113, 0.0586166, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.90848, 
    farPlane=0.977138, cameraPosition=(-0.0141758, 0.0566544, 0.942809), 
    cameraTarget=(-0.0141758, 0.0566544, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.90848, 
    farPlane=0.977138, cameraPosition=(-0.0183783, 0.0591773, 0.942809), 
    cameraTarget=(-0.0183783, 0.0591773, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.936738, 
    farPlane=0.94888, width=0.0759585, height=0.0383499, cameraPosition=(
    -0.04501, 0.011109, 0.942809), cameraTarget=(-0.04501, 0.011109, 0))
s.delete(objectList=(g[6], ))
s.delete(objectList=(g[10], ))
s.Line(point1=(-0.042100444543805, 0.023896001270425), point2=(
    -0.0275997759790458, 0.01))
s.PerpendicularConstraint(entity1=g[21], entity2=g[23], addUndoState=False)
p = mdb.models['Model-1'].Part(name='implante', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['implante']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.426244, 
    farPlane=0.51417, width=0.619021, height=0.312531, viewOffsetX=0.0625355, 
    viewOffsetY=0.0177079)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.423979, 
    farPlane=0.516435, width=0.615732, height=0.310871, viewOffsetX=-0.0151879, 
    viewOffsetY=-0.0307354)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.423949, 
    farPlane=0.516465, width=0.615688, height=0.310849, 
    viewOffsetX=-0.00990196, viewOffsetY=-0.0122258)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.448386, 
    farPlane=0.492028, width=0.273835, height=0.138254, viewOffsetX=-0.0139911, 
    viewOffsetY=-0.0154561)
p = mdb.models['Model-1'].parts['implante']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1000 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.0757209562577325)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.435068, 
    farPlane=0.505346, width=0.495324, height=0.250079, viewOffsetX=0.0884447, 
    viewOffsetY=-0.0405744)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.433172, 
    farPlane=0.507242, width=0.493165, height=0.248989, viewOffsetX=0.0351445, 
    viewOffsetY=-0.0258757)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.440882, 
    farPlane=0.499532, width=0.368377, height=0.185986, viewOffsetX=0.0174212, 
    viewOffsetY=-0.0082691)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.442532, 
    farPlane=0.497882, width=0.369756, height=0.186683, viewOffsetX=0.00592445, 
    viewOffsetY=-0.012383)
p = mdb.models['Model-1'].parts['implante']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
    -0.004123, 0.077909, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=0.47, gridSpacing=0.01, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['implante']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.Line(point1=(-0.037977444543805, -0.054012998729575), point2=(
    0.0547568010061789, 0.0427564627452171))
s1.ParallelConstraint(entity1=g[2], entity2=g[17], addUndoState=False)
p = mdb.models['Model-1'].parts['implante']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Material(name='Co-Cr')
mdb.models['Model-1'].materials['Co-Cr'].Elastic(table=((230000.0, 0.3), ))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['osso']
a1.Instance(name='osso-1', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['implante']
a1.Instance(name='implante-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.997, 
    farPlane=222.75, width=174.194, height=87.947, viewOffsetX=-12.2822, 
    viewOffsetY=1.06862)
session.viewports['Viewport: 1'].view.setValues(nearPlane=195.787, 
    farPlane=221.961, width=174.9, height=88.3034, viewOffsetX=-7.61364, 
    viewOffsetY=-5.9012)
session.viewports['Viewport: 1'].view.setValues(nearPlane=192.267, 
    farPlane=225.481, width=234.03, height=118.157, viewOffsetX=-4.62148, 
    viewOffsetY=-14.0721)
session.viewports['Viewport: 1'].view.setValues(nearPlane=191.292, 
    farPlane=226.456, width=232.843, height=117.558, viewOffsetX=-0.600733, 
    viewOffsetY=-9.28699)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['implante']
a1.Instance(name='implante-2', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'osso-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'implante-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'implante-2', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('implante-2', 'osso-1', 'implante-1', ))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.435069, 
    farPlane=0.505345, width=0.43767, height=0.220971, viewOffsetX=0.0242811, 
    viewOffsetY=-0.0225839)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p=mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p=mdb.models['Model-1'].parts['implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.442515, 
    farPlane=0.497899, width=0.39174, height=0.197782, viewOffsetX=0.0197164, 
    viewOffsetY=-0.00844809)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['implante']
s = p.features['Shell planar-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.427589, 
    farPlane=0.512807, width=0.603358, height=0.304624, cameraPosition=(
    0.0657371, 0.0636526, 0.470198), cameraTarget=(0.0657371, 0.0636526, 0))
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=True)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.418898, 
    farPlane=0.521498, width=0.726426, height=0.366758, cameraPosition=(
    0.0857706, 0.0573486, 0.470198), cameraTarget=(0.0857706, 0.0573486, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0679551, 
    0.0470989, 0.470198), cameraTarget=(0.0679551, 0.0470989, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.415624, 
    farPlane=0.524772, cameraPosition=(0.0599382, 0.0448707, 0.470198), 
    cameraTarget=(0.0599382, 0.0448707, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, width=0.822121, height=0.415073, cameraPosition=(
    0.0625491, 0.0550561, 0.470198), cameraTarget=(0.0625491, 0.0550561, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.408434, 
    farPlane=0.531962, cameraPosition=(0.0635573, 0.0666559, 0.470198), 
    cameraTarget=(0.0635573, 0.0666559, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.772794, 
    height=0.390168, cameraPosition=(0.0621812, 0.0606795, 0.470198), 
    cameraTarget=(0.0621812, 0.0606795, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(0.057443, 0.0564127, 0.470198), 
    cameraTarget=(0.057443, 0.0564127, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(-0.0240534, 0.00426384, 0.470198), 
    cameraTarget=(-0.0240534, 0.00426384, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.269964, 
    0.00378977, 0.470198), cameraTarget=(-0.269964, 0.00378977, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.292707, 
    -0.000951034, 0.470198), cameraTarget=(-0.292707, -0.000951034, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.0316343, 
    -0.00284737, 0.470198), cameraTarget=(-0.0316343, -0.00284737, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.0240532, 
    0.00331569, 0.470198), cameraTarget=(-0.0240532, 0.00331569, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.024527, 
    0.00284161, 0.470198), cameraTarget=(-0.024527, 0.00284161, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.0221579, 
    0.00284161, 0.470198), cameraTarget=(-0.0221579, 0.00284161, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.822121, 
    height=0.415073, cameraPosition=(-0.0223545, -0.00198494, 0.470198), 
    cameraTarget=(-0.0223545, -0.00198494, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.408434, 
    farPlane=0.531962, cameraPosition=(-0.0314276, -0.00551532, 0.470198), 
    cameraTarget=(-0.0314276, -0.00551532, 0))
session.viewports['Viewport: 1'].view.setValues(width=0.772794, 
    height=0.390168, cameraPosition=(-0.030233, -0.000688776, 0.470198), 
    cameraTarget=(-0.030233, -0.000688776, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(-0.0226519, 0.00405203, 0.470198), 
    cameraTarget=(-0.0226519, 0.00405203, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(-0.0240734, 0.00310387, 0.470198), 
    cameraTarget=(-0.0240734, 0.00310387, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.408434, 
    farPlane=0.531962, cameraPosition=(-0.0244061, 0.00322491, 0.470198), 
    cameraTarget=(-0.0244061, 0.00322491, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(-0.0244061, 0.00275083, 0.470198), 
    cameraTarget=(-0.0244061, 0.00275083, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(-0.0239323, 0.00417307, 0.470198), 
    cameraTarget=(-0.0239323, 0.00417307, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(-0.0253538, 0.00275083, 0.470198), 
    cameraTarget=(-0.0253538, 0.00275083, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(-0.0253538, 0.00796571, 0.470198), 
    cameraTarget=(-0.0253538, 0.00796571, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(-0.0244062, 0.00464715, 0.470198), 
    cameraTarget=(-0.0244062, 0.00464715, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(-0.0239324, 0.00369899, 0.470198), 
    cameraTarget=(-0.0239324, 0.00369899, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.41214, 
    farPlane=0.528256, cameraPosition=(0.187863, -0.00151585, 0.470198), 
    cameraTarget=(0.187863, -0.00151585, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.418898, 
    farPlane=0.521498, width=0.726426, height=0.366758, cameraPosition=(
    0.176256, 0.00361844, 0.470198), cameraTarget=(0.176256, 0.00361844, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.415624, 
    farPlane=0.524772, cameraPosition=(-0.00724298, 0.0276827, 0.470198), 
    cameraTarget=(-0.00724298, 0.0276827, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.415624, 
    farPlane=0.524772, cameraPosition=(-0.0192685, 0.0152049, 0.470198), 
    cameraTarget=(-0.0192685, 0.0152049, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.408434, 
    farPlane=0.531962, width=0.874597, height=0.441567, cameraPosition=(
    -0.0253836, 0.00140745, 0.470198), cameraTarget=(-0.0253836, 0.00140745, 
    0))
s2.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.428661, 
    farPlane=0.511753, width=0.585179, height=0.295445, viewOffsetX=0.0102096, 
    viewOffsetY=0.0180944)
session.Image(name='protese-grid-overlay', 
    fileName='C:/temp/protese-grid-overlay.png')
session.viewports['Viewport: 1'].imageOptions.setValues(
    imageName='protese-grid-overlay')
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.39032, 
    farPlane=0.550094, width=1.1196, height=0.565262, viewOffsetX=0.0178191, 
    viewOffsetY=0.0255477)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.387005, 
    farPlane=0.553409, width=1.11009, height=0.560462, viewOffsetX=0.0088197, 
    viewOffsetY=-0.157858)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.376896, 
    farPlane=0.563518, width=1.1548, height=0.583038, viewOffsetX=0.00987682, 
    viewOffsetY=-0.164839)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.374878, 
    farPlane=0.559301, width=1.14862, height=0.579916, cameraPosition=(
    -0.0213214, 0.0787102, 0.466535), cameraUpVector=(-0.0343168, 0.999309, 
    -0.01428), cameraTarget=(-0.00516286, 0.0725504, -0.00335429), 
    viewOffsetX=0.00982394, viewOffsetY=-0.163957)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.376397, 
    farPlane=0.557782, width=1.15328, height=0.582266, viewOffsetX=0.0169348, 
    viewOffsetY=-0.162499)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.376502, 
    farPlane=0.557678, width=1.1536, height=0.582428, viewOffsetX=0.0155249, 
    viewOffsetY=-0.161837)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.871845, 
    farPlane=1.01377, width=1.00488, height=0.507342, cameraPosition=(
    0.00152585, 0.0203638, 0.942809), cameraTarget=(0.00152585, 0.0203638, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.0034031, 
    0.0135828, 0.942809), cameraTarget=(-0.0034031, 0.0135828, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.862497, 
    farPlane=1.02312, width=1.13725, height=0.574176, cameraPosition=(
    -0.0114788, 0.025561, 0.942809), cameraTarget=(-0.0114788, 0.025561, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.85737, 
    farPlane=1.02825, cameraPosition=(0.0219904, 0.0220727, 0.942809), 
    cameraTarget=(0.0219904, 0.0220727, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.20984, height=0.610826, 
    cameraPosition=(0.0195203, 0.0281067, 0.942809), cameraTarget=(0.0195203, 
    0.0281067, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.851917, 
    farPlane=1.0337, cameraPosition=(0.0195203, 0.0273645, 0.942809), 
    cameraTarget=(0.0195203, 0.0273645, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.28707, height=0.649815, 
    cameraPosition=(0.0175554, 0.0290463, 0.942809), cameraTarget=(0.0175554, 
    0.0290463, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.846115, 
    farPlane=1.0395, cameraPosition=(0.0199227, 0.0337837, 0.942809), 
    cameraTarget=(0.0199227, 0.0337837, 0))
s.ArcByCenterEnds(center=(0.025, 0.195), point1=(-0.055, 0.155), point2=(0.07, 
    0.27), direction=CLOCKWISE)
s.Line(point1=(-0.055, 0.155), point2=(0.0710178993308422, 0.271696498884737))
s.Line(point1=(-0.02, 0.16), point2=(-0.035, 0.173520622785238))
s.CoincidentConstraint(entity1=v[4], entity2=g[3], addUndoState=False)
s.delete(objectList=(g[4], ))
s.Line(point1=(-0.035311791100291, 0.173231894517425), point2=(
    -0.0219062237447361, 0.158755526717869))
s.CoincidentConstraint(entity1=v[5], entity2=g[3], addUndoState=False)
s.Line(point1=(0.0511991391191403, 0.253343709787135), point2=(
    0.0637457857519621, 0.239794870985861))
s.PerpendicularConstraint(entity1=g[3], entity2=g[6], addUndoState=False)
s.CoincidentConstraint(entity1=v[7], entity2=g[3], addUndoState=False)
s.Line(point1=(0.0637457857519621, 0.239794870985861), point2=(
    -0.0219062237447361, 0.158755526717869))
s.Line(point1=(0.000547460249744787, 0.18), point2=(0.0653470744673541, 
    0.111512067103831))
s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s.CoincidentConstraint(entity1=v[9], entity2=g[7], addUndoState=False)
s.Line(point1=(0.0653470744673541, 0.111512067103831), point2=(0.11, 
    0.153760273846748))
s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s.delete(objectList=(g[9], ))
s.Line(point1=(0.045, 0.222058612443254), point2=(0.108447267752085, 0.155))
s.PerpendicularConstraint(entity1=g[7], entity2=g[10], addUndoState=False)
s.CoincidentConstraint(entity1=v[12], entity2=g[7], addUndoState=False)
s.Line(point1=(0.108447267752085, 0.155), point2=(0.0653470744673541, 
    0.111512067103831))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.911062, 
    farPlane=0.974556, width=0.39722, height=0.200548, cameraPosition=(
    0.0396039, 0.179588, 0.942809), cameraTarget=(0.0396039, 0.179588, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.178424, 
    0.180319, 0.942809), cameraTarget=(0.178424, 0.180319, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.033272, 
    0.182512, 0.942809), cameraTarget=(0.033272, 0.182512, 0))
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=False)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0310801, 
    0.188604, 0.942809), cameraTarget=(0.0310801, 0.188604, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0327849, 
    0.189335, 0.942809), cameraTarget=(0.0327849, 0.189335, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.879849, 
    farPlane=1.00577, width=0.891542, height=0.450122, cameraPosition=(
    0.195225, 0.108308, 0.942809), cameraTarget=(0.195225, 0.108308, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.87583, 
    farPlane=1.00979, cameraPosition=(0.074968, 0.138389, 0.942809), 
    cameraTarget=(0.074968, 0.138389, 0))
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=True)
session.viewports['Viewport: 1'].view.setValues(width=0.948449, 
    height=0.478853, cameraPosition=(0.0855574, 0.135509, 0.942809), 
    cameraTarget=(0.0855574, 0.135509, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.871555, 
    farPlane=1.01406, cameraPosition=(0.0431069, 0.112817, 0.942809), 
    cameraTarget=(0.0431069, 0.112817, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.867006, 
    farPlane=1.01861, width=1.07339, height=0.541934, cameraPosition=(
    0.0604579, 0.102201, 0.942809), cameraTarget=(0.0604579, 0.102201, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.862168, 
    farPlane=1.02345, cameraPosition=(0.0176802, 0.0765203, 0.942809), 
    cameraTarget=(0.0176802, 0.0765203, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.14191, height=0.576526, 
    cameraPosition=(0.0240023, 0.0692279, 0.942809), cameraTarget=(0.0240023, 
    0.0692279, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.857021, 
    farPlane=1.0286, cameraPosition=(0.0191015, 0.0601212, 0.942809), 
    cameraTarget=(0.0191015, 0.0601212, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.21479, height=0.613325, 
    cameraPosition=(0.0249334, 0.0519609, 0.942809), cameraTarget=(0.0249334, 
    0.0519609, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.851545, 
    farPlane=1.03407, cameraPosition=(0.0204645, 0.0474895, 0.942809), 
    cameraTarget=(0.0204645, 0.0474895, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.29233, height=0.652474, 
    cameraPosition=(0.024767, 0.0388083, 0.942809), cameraTarget=(0.024767, 
    0.0388083, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.845719, 
    farPlane=1.0399, cameraPosition=(0.0208053, 0.032466, 0.942809), 
    cameraTarget=(0.0208053, 0.032466, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.851545, 
    farPlane=1.03407, width=1.29233, height=0.652474, cameraPosition=(
    0.0208053, 0.032466, 0.942809), cameraTarget=(0.0208053, 0.032466, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.845719, 
    farPlane=1.0399, cameraPosition=(0.0215977, 0.032466, 0.942809), 
    cameraTarget=(0.0215977, 0.032466, 0))
s.Line(point1=(-0.0148619773907407, 0.165420415361398), point2=(
    -0.0212102282494016, 0.172130001277765))
s.CoincidentConstraint(entity1=v[14], entity2=g[7], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.917921, 
    farPlane=0.967697, width=0.352419, height=0.17793, cameraPosition=(
    -0.0319584, 0.161064, 0.942809), cameraTarget=(-0.0319584, 0.161064, 0))
s.Line(point1=(-0.0212102282494016, 0.172130001277765), point2=(
    0.0574694718859142, 0.246572519813128))
s.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
s.CoincidentConstraint(entity1=v[16], entity2=g[6], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.836961, 
    farPlane=1.04866, width=1.49885, height=0.756738, cameraPosition=(0.160948, 
    0.0363675, 0.942809), cameraTarget=(0.160948, 0.0363675, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0203444, 
    0.00602436, 0.942809), cameraTarget=(0.0203444, 0.00602436, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.40892, height=0.711334, 
    cameraPosition=(0.00752471, 0.0255267, 0.942809), cameraTarget=(0.00752471, 
    0.0255267, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.836961, 
    farPlane=1.04866, cameraPosition=(0.0239376, 0.0134262, 0.942809), 
    cameraTarget=(0.0239376, 0.0134262, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.32438, height=0.668654, 
    cameraPosition=(0.0107986, 0.0303582, 0.942809), cameraTarget=(0.0107986, 
    0.0303582, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.843312, 
    farPlane=1.04231, cameraPosition=(0.0205427, 0.0295457, 0.942809), 
    cameraTarget=(0.0205427, 0.0295457, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.24492, height=0.628535, 
    cameraPosition=(0.00819209, 0.0448768, 0.942809), cameraTarget=(0.00819209, 
    0.0448768, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.849282, 
    farPlane=1.03634, cameraPosition=(0.0204047, 0.0387671, 0.942809), 
    cameraTarget=(0.0204047, 0.0387671, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.843312, 
    farPlane=1.04231, cameraPosition=(0.0201611, 0.0383284, 0.942809), 
    cameraTarget=(0.0201611, 0.0383284, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.849282, 
    farPlane=1.03634, cameraPosition=(0.0232142, 0.0444381, 0.942809), 
    cameraTarget=(0.0232142, 0.0444381, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.849282, 
    farPlane=1.03634, cameraPosition=(0.0201611, 0.0406195, 0.942809), 
    cameraTarget=(0.0201611, 0.0406195, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.843312, 
    farPlane=1.04231, cameraPosition=(0.0201611, 0.0406195, 0.942809), 
    cameraTarget=(0.0201611, 0.0406195, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0178713, 
    0.0398558, 0.942809), cameraTarget=(0.0178713, 0.0398558, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.929896, 
    farPlane=0.955722, width=0.16157, height=0.0815734, cameraPosition=(
    0.0469356, 0.214742, 0.942809), cameraTarget=(0.0469356, 0.214742, 0))
s.Line(point1=(0.0505228518869595, 0.24), point2=(0.0568711027374226, 
    0.23329041409319))
s.PerpendicularConstraint(entity1=g[13], entity2=g[14], addUndoState=False)
s.CoincidentConstraint(entity1=v[17], entity2=g[13], addUndoState=False)
s.CoincidentConstraint(entity1=v[18], entity2=g[7], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.900968, 
    farPlane=0.98465, width=0.592483, height=0.299133, cameraPosition=(
    0.0351112, 0.163045, 0.942809), cameraTarget=(0.0351112, 0.163045, 0))
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.917304, 
    farPlane=0.968314, width=0.31912, height=0.161117, cameraPosition=(
    0.0421262, 0.186088, 0.942809), cameraTarget=(0.0421262, 0.186088, 0))
s.delete(objectList=(g[7], ))
s.Line(point1=(-0.0219062237447361, 0.158755526717869), point2=(
    -0.0148619773907407, 0.165420415361398))
s.Line(point1=(0.000547460249744787, 0.18), point2=(-0.00580079061739462, 
    0.186709585905726))
s.CoincidentConstraint(entity1=v[19], entity2=g[13], addUndoState=False)
s.Line(point1=(0.045, 0.222058612443254), point2=(0.0386517491545238, 
    0.228768198349416))
s.ParallelConstraint(entity1=g[10], entity2=g[17], addUndoState=False)
s.CoincidentConstraint(entity1=v[20], entity2=g[13], addUndoState=False)
s.Line(point1=(0.0568711027374226, 0.23329041409319), point2=(
    0.0637457857519621, 0.239794870985861))
s.PerpendicularConstraint(entity1=g[14], entity2=g[18], addUndoState=False)
s.delete(objectList=(g[13], ))
s.Line(point1=(-0.0212102282494016, 0.172130001277765), point2=(
    -0.00580079061739462, 0.186709585905726))
s.PerpendicularConstraint(entity1=g[12], entity2=g[19], addUndoState=False)
s.Line(point1=(0.0386517491545238, 0.228768198349416), point2=(
    0.0505228518869595, 0.24))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.912102, 
    farPlane=0.973516, width=0.434825, height=0.219535, cameraPosition=(
    0.0554861, 0.175464, 0.942809), cameraTarget=(0.0554861, 0.175464, 0))
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=True)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.895456, 
    farPlane=0.990162, width=0.670533, height=0.338539, cameraPosition=(
    0.145148, 0.161666, 0.942809), cameraTarget=(0.145148, 0.161666, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0345573, 
    0.161254, 0.942809), cameraTarget=(0.0345573, 0.161254, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.865126, 
    farPlane=1.02049, width=1.10001, height=0.555374, cameraPosition=(
    0.0510149, 0.102039, 0.942809), cameraTarget=(0.0510149, 0.102039, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.860168, 
    farPlane=1.02545, cameraPosition=(0.0253862, 0.0743718, 0.942809), 
    cameraTarget=(0.0253862, 0.0743718, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.860168, 
    farPlane=1.02545, cameraPosition=(0.0199907, 0.0682984, 0.942809), 
    cameraTarget=(0.0199907, 0.0682984, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.860168, 
    farPlane=1.02545, cameraPosition=(0.0193163, 0.0635747, 0.942809), 
    cameraTarget=(0.0193163, 0.0635747, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.836961, 
    farPlane=1.04866, width=1.32438, height=0.668655, cameraPosition=(0.021796, 
    0.0287169, 0.942809), cameraTarget=(0.021796, 0.0287169, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.843312, 
    farPlane=1.04231, cameraPosition=(0.020984, 0.027092, 0.942809), 
    cameraTarget=(0.020984, 0.027092, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.24492, height=0.628536, 
    cameraPosition=(0.0211846, 0.0383905, 0.942809), cameraTarget=(0.0211846, 
    0.0383905, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.849281, 
    farPlane=1.03634, cameraPosition=(0.0204212, 0.0414454, 0.942809), 
    cameraTarget=(0.0204212, 0.0414454, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.849281, 
    farPlane=1.03634, cameraPosition=(0.0181314, 0.039918, 0.942809), 
    cameraTarget=(0.0181314, 0.039918, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.849281, 
    farPlane=1.03634, cameraPosition=(0.019658, 0.0483188, 0.942809), 
    cameraTarget=(0.019658, 0.0483188, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.854893, 
    farPlane=1.03072, cameraPosition=(0.0212761, 0.0472322, 0.942809), 
    cameraTarget=(0.0212761, 0.0472322, 0))
s.Line(point1=(0.0505228518869595, 0.24), point2=(0.0505228518869595, 
    0.202743053436279))
s.VerticalConstraint(entity=g[21], addUndoState=False)
s.Line(point1=(0.0505228518869595, 0.202743053436279), point2=(0.03, 0.175))
s.Line(point1=(0.03, 0.175), point2=(0.03, 0.160713076591492))
s.VerticalConstraint(entity=g[23], addUndoState=False)
s.delete(objectList=(g[22], g[23], c[68]))
s.delete(objectList=(g[21], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.907914, 
    farPlane=0.977704, width=0.49412, height=0.249471, cameraPosition=(
    0.0467576, 0.167607, 0.942809), cameraTarget=(0.0467576, 0.167607, 0))
s.Spot(point=(0.04, 0.2))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.878023, 
    farPlane=1.00759, width=0.91739, height=0.463172, cameraPosition=(
    0.0491703, 0.13927, 0.942809), cameraTarget=(0.0491703, 0.13927, 0))
s.delete(objectList=(g[2], g[3], g[5], g[6], g[8], g[10], g[11], g[12], g[14], 
    g[15], g[16], g[17], g[18], g[19], g[20], v[24], c[12], c[15], c[16], 
    c[51], c[55], c[58]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.869489, 
    farPlane=1.01613, width=1.03824, height=0.524188, cameraPosition=(
    0.0456507, 0.136712, 0.942809), cameraTarget=(0.0456507, 0.136712, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0564723, 
    0.136712, 0.942809), cameraTarget=(0.0564723, 0.136712, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.85983, 
    farPlane=1.02579, width=1.17501, height=0.593241, cameraPosition=(
    0.0433486, 0.139942, 0.942809), cameraTarget=(0.0433486, 0.139942, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.854533, 
    farPlane=1.03108, cameraPosition=(0.0599184, 0.143546, 0.942809), 
    cameraTarget=(0.0599184, 0.143546, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.10451, height=0.557646, 
    cameraPosition=(0.0657322, 0.141232, 0.942809), cameraTarget=(0.0657322, 
    0.141232, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.85983, 
    farPlane=1.02579, cameraPosition=(0.0603147, 0.140555, 0.942809), 
    cameraTarget=(0.0603147, 0.140555, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.03824, height=0.524188, 
    cameraPosition=(0.0619906, 0.135661, 0.942809), cameraTarget=(0.0619906, 
    0.135661, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.864809, 
    farPlane=1.02081, cameraPosition=(0.0581711, 0.135661, 0.942809), 
    cameraTarget=(0.0581711, 0.135661, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.10451, height=0.557647, 
    cameraPosition=(0.0562004, 0.142023, 0.942809), cameraTarget=(0.0562004, 
    0.142023, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.85983, 
    farPlane=1.02579, cameraPosition=(0.058232, 0.139991, 0.942809), 
    cameraTarget=(0.058232, 0.139991, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.17501, height=0.593241, 
    cameraPosition=(0.0573026, 0.146716, 0.942809), cameraTarget=(0.0573026, 
    0.146716, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.854533, 
    farPlane=1.03108, cameraPosition=(0.0637864, 0.145275, 0.942809), 
    cameraTarget=(0.0637864, 0.145275, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.854533, 
    farPlane=1.03108, cameraPosition=(0.0587434, 0.144554, 0.942809), 
    cameraTarget=(0.0587434, 0.144554, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.25001, height=0.631107, 
    cameraPosition=(0.0578467, 0.151479, 0.942809), cameraTarget=(0.0578467, 
    0.151479, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.848899, 
    farPlane=1.03672, cameraPosition=(0.0616787, 0.151479, 0.942809), 
    cameraTarget=(0.0616787, 0.151479, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.842905, 
    farPlane=1.04271, width=1.41468, height=0.714246, cameraPosition=(
    0.0700081, 0.157022, 0.942809), cameraTarget=(0.0700081, 0.157022, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0830186, 
    0.150079, 0.942809), cameraTarget=(0.0830186, 0.150079, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.50498, height=0.759836, 
    cameraPosition=(0.0893578, 0.144678, 0.942809), cameraTarget=(0.0893578, 
    0.144678, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.111503, 
    0.135445, 0.942809), cameraTarget=(0.111503, 0.135445, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.836528, 
    farPlane=1.04909, cameraPosition=(0.11178, 0.137661, 0.942809), 
    cameraTarget=(0.11178, 0.137661, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.829744, 
    farPlane=1.05587, cameraPosition=(0.121007, 0.138584, 0.942809), 
    cameraTarget=(0.121007, 0.138584, 0))
session.viewports['Viewport: 1'].view.setValues(width=1.41468, height=0.714246, 
    cameraPosition=(0.116384, 0.141381, 0.942809), cameraTarget=(0.116384, 
    0.141381, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.836528, 
    farPlane=1.04909, cameraPosition=(0.0999041, 0.130099, 0.942809), 
    cameraTarget=(0.0999041, 0.130099, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    showImage=True, imageName='protese-grid-overlay', xScale=0.233, 
    yScale=0.233)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.233, yScale=0.233)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.233, yScale=0.233)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.233, yScale=0.233)
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=False)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.233, yScale=0.233)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.233, yScale=0.233)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.233, yScale=0.233)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.778915, 
    farPlane=1.1067, width=2.05065, height=1.03533, cameraPosition=(0.244046, 
    0.125901, 0.942809), cameraTarget=(0.244046, 0.125901, 0))
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=True)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.848899, 
    farPlane=1.03672, width=1.3298, height=0.671391, cameraPosition=(0.212515, 
    0.109001, 0.942809), cameraTarget=(0.212515, 0.109001, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0959229, 
    0.104106, 0.942809), cameraTarget=(0.0959229, 0.104106, 0))
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.743868, 
    farPlane=1.14175, width=2.48917, height=1.25673, cameraPosition=(0.198336, 
    0.0313056, 0.942809), cameraTarget=(0.198336, 0.0313056, 0))
s.imageOptions.setValues(origin=(0.264999985694885, 0.230000004172325))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    0.265, 0.23), xScale=0.233, yScale=0.233, translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    0.265, 0.23), xScale=0.233, yScale=0.233, translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    0.265, 0.23), xScale=0.233, yScale=0.233, translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    0.265, 0.23), xScale=0.233, yScale=0.233, translucency=0.99)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Model-1'].parts['implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    showImage=True, imageName='protese-grid-overlay')
session.Image(name='protese-grid-overlay2', 
    fileName='C:/temp/protese-grid-overlay2.png')
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    imageName='protese-grid-overlay2')
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.06557, 
    farPlane=3.40286, width=2.38807, height=1.20569, cameraPosition=(0.129596, 
    0.0658676, 3.23421), cameraTarget=(0.129596, 0.0658676, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.164736, 
    0.00726805, 3.23421), cameraTarget=(0.164736, 0.00726805, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.0548, 
    farPlane=3.41362, cameraPosition=(0.160343, -0.0132417, 3.23421), 
    cameraTarget=(0.160343, -0.0132417, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.0548, 
    farPlane=3.41362, cameraPosition=(0.145701, -0.0205666, 3.23421), 
    cameraTarget=(0.145701, -0.0205666, 0))
s1.resetView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.87421, 
    farPlane=4.05399, width=1.27291, height=0.642666, cameraPosition=(0.370006, 
    0.525484, 3.9641), cameraTarget=(0.370006, 0.525484, 0.5))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0984106, 
    0.148318, 3.9641), cameraTarget=(0.0984106, 0.148318, 0.5))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.86847, 
    farPlane=4.05973, cameraPosition=(0.213136, 0.0780386, 3.9641), 
    cameraTarget=(0.213136, 0.0780386, 0.5))
s1.imageOptions.setValues(origin=(0.284999996423721, 0.180000007152557))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    0.285, 0.18), translucency=0.98)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    0.285, 0.18), translucency=0.98)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.84161, 
    farPlane=4.08659, width=1.53255, height=0.773752, cameraPosition=(0.358116, 
    0.0793061, 3.9641), cameraTarget=(0.358116, 0.0793061, 0.5))
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=True, 
    positionMethod=MANUAL, origin=(0, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.82548, 
    farPlane=4.10272, width=1.96292, height=0.991039, cameraPosition=(0.460726, 
    0.109751, 3.9641), cameraTarget=(0.460726, 0.109751, 0.5))
session.viewports['Viewport: 1'].imageOptions.setValues(
    positionMethod=AUTO_ALIGN)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.8796, 
    farPlane=4.0486, width=1.05726, height=0.533788, cameraPosition=(0.410091, 
    -0.00877959, 3.9641), cameraTarget=(0.410091, -0.00877959, 0.5))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0120798, 
    0.128721, 3.9641), cameraTarget=(0.0120798, 0.128721, 0.5))
session.viewports['Viewport: 1'].view.setValues(width=1.12474, height=0.56786, 
    cameraPosition=(0.00139135, 0.13069, 3.9641), cameraTarget=(0.00139135, 
    0.13069, 0.5))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.0199863, 
    0.10102, 3.9641), cameraTarget=(-0.0199863, 0.10102, 0.5))
session.viewports['Viewport: 1'].imageOptions.setValues(xScale=0.5, yScale=0.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.86237, 
    farPlane=4.06583, width=1.27291, height=0.642666, cameraPosition=(
    -0.0270838, 0.110428, 3.9641), cameraTarget=(-0.0270838, 0.110428, 0.5))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0431564, 
    0.09481, 3.9641), cameraTarget=(0.0431564, 0.09481, 0.5))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0618871, 
    0.101838, 3.9641), cameraTarget=(0.0618871, 0.101838, 0.5))
session.viewports['Viewport: 1'].imageOptions.setValues(xScale=0.6, yScale=0.6)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0665698, 
    0.108085, 3.9641), cameraTarget=(0.0665698, 0.108085, 0.5))
session.viewports['Viewport: 1'].imageOptions.setValues(xScale=0.57, 
    yScale=0.57)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0712525, 
    0.102619, 3.9641), cameraTarget=(0.0712525, 0.102619, 0.5))
session.viewports['Viewport: 1'].view.setValues(width=1.19653, height=0.604106, 
    cameraPosition=(0.0584454, 0.110279, 3.9641), cameraTarget=(0.0584454, 
    0.110279, 0.5))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    gridSpacing=5.0, gridAuto=OFF)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    0.285, 0.18), translucency=0.98)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.9616, 
    farPlane=3.9666, width=0.0313339, height=0.0158199, cameraPosition=(
    -0.210214, 0.199081, 3.9641), cameraTarget=(-0.210214, 0.199081, 0.5))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.96175, 
    farPlane=3.96645, cameraPosition=(-0.214902, 0.199908, 3.9641), 
    cameraTarget=(-0.214902, 0.199908, 0.5))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.96175, 
    farPlane=3.96645, cameraPosition=(-0.212481, 0.199908, 3.9641), 
    cameraTarget=(-0.212481, 0.199908, 0.5))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.96409, 
    farPlane=3.96412, width=0.000198067, height=0.0001, cameraPosition=(
    -0.210945, 0.201035, 3.9641), cameraTarget=(-0.210945, 0.201035, 0.5))
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Model-1'].parts['implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=177.481, 
    farPlane=199.643, width=156.911, height=79.2214, cameraPosition=(8.82707, 
    -0.326756, 188.562), cameraTarget=(8.82707, -0.326756, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    showImage=True, imageName='osso-protese')
session.viewports['Viewport: 1'].view.setValues(nearPlane=125.9, 
    farPlane=251.223, width=887.307, height=447.984, cameraPosition=(35.5843, 
    -63.3246, 188.562), cameraTarget=(35.5843, -63.3246, 0))
session.viewports['Viewport: 1'].imageOptions.setValues(showImage=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=331.95, 
    farPlane=820.847, width=3058.56, height=1544.21, cameraPosition=(-110.574, 
    -395.987, 576.398), cameraTarget=(-110.574, -395.987, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    imageName='protese-grid-overlay2')
session.viewports['Viewport: 1'].view.setValues(nearPlane=452.635, 
    farPlane=700.162, width=1548.54, height=781.829, cameraPosition=(-68.977, 
    -160.106, 576.398), cameraTarget=(-68.977, -160.106, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.5, yScale=0.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=540.494, 
    farPlane=612.303, width=449.242, height=226.814, cameraPosition=(19.2269, 
    26.4021, 576.398), cameraTarget=(19.2269, 26.4021, 0))
s.imageOptions.setValues(origin=(53.75, 38.75))
s.imageOptions.setValues(origin=(195.0, 120.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=479.77, 
    farPlane=673.027, width=1368.29, height=690.825, cameraPosition=(-39.9356, 
    51.6153, 576.398), cameraTarget=(-39.9356, 51.6153, 0))
s.imageOptions.setValues(origin=(575.0, 283.75))
s.imageOptions.setValues(origin=(48.75, 17.5))
s.imageOptions.setValues(origin=(-286.25, -243.75))
s.imageOptions.setValues(origin=(-72.5, -63.75))
s.imageOptions.setValues(origin=(-92.5, -257.5))
s.imageOptions.setValues(origin=(-66.25, -100.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=533.17, 
    farPlane=619.627, width=540.875, height=273.077, cameraPosition=(-24.6665, 
    50.6838, 576.398), cameraTarget=(-24.6665, 50.6838, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-39.5894, 
    -1.07813, 576.398), cameraTarget=(-39.5894, -1.07813, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=540.493, 
    farPlane=612.303, width=508.423, height=256.693, cameraPosition=(-33.358, 
    -1.35884, 576.398), cameraTarget=(-33.358, -1.35884, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.35, yScale=0.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=554.512, 
    farPlane=598.284, width=273.844, height=138.259, cameraPosition=(-25.6921, 
    3.80486, 576.398), cameraTarget=(-25.6921, 3.80486, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.375, yScale=0.375)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.36, yScale=0.36)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.36, yScale=0.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=553.115, 
    farPlane=599.681, width=291.324, height=147.084, cameraPosition=(-27.9376, 
    2.04292, 576.398), cameraTarget=(-27.9376, 2.04292, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-38.2974, 
    1.8642, 576.398), cameraTarget=(-38.2974, 1.8642, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-21.5074, 
    -3.13987, 576.398), cameraTarget=(-21.5074, -3.13987, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-14.5414, 
    -3.13987, 576.398), cameraTarget=(-14.5414, -3.13987, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=551.628, 
    farPlane=601.168, width=350.746, height=177.085, cameraPosition=(-15.2883, 
    -8.48026, 576.398), cameraTarget=(-15.2883, -8.48026, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=550.047, 
    farPlane=602.749, cameraPosition=(-8.83678, -7.40441, 576.398), 
    cameraTarget=(-8.83678, -7.40441, 0))
s.ArcByCenterEnds(center=(-8.75, 25.0), point1=(-28.75, 12.5), point2=(3.75, 
    43.75), direction=CLOCKWISE)
s.Line(point1=(-28.75, 12.5), point2=(4.33257796284227, 44.6238669442634))
s.autoDimension(objectList=(g[2], g[3]))
#: 2 dimensions added
s.Line(point1=(-23.2548047681825, 17.8359481433983), point2=(-20.8853215328854, 
    15.3957495832728))
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s.CoincidentConstraint(entity1=v[3], entity2=g[3], addUndoState=False)
s.Line(point1=(-1.5179859084954, 38.942848507222), point2=(1.05573523044586, 
    36.2923167268746))
s.PerpendicularConstraint(entity1=g[3], entity2=g[5], addUndoState=False)
s.CoincidentConstraint(entity1=v[5], entity2=g[3], addUndoState=False)
s.Line(point1=(1.05573523044586, 36.2923167268746), point2=(-20.8853215328854, 
    15.3957495832728))
s.Line(point1=(-19.1458641843488, 17.052401205353), point2=(-27.0270201386884, 
    25.3274872023612))
s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s.CoincidentConstraint(entity1=v[7], entity2=g[6], addUndoState=False)
s.Line(point1=(-15.4219285795968, 20.5990612975507), point2=(1.24999999976717, 
    3.09380654423046))
s.PerpendicularConstraint(entity1=g[6], entity2=g[8], addUndoState=False)
s.CoincidentConstraint(entity1=v[9], entity2=g[6], addUndoState=False)
s.Line(point1=(1.24999999976717, 3.09380654423046), point2=(12.5, 
    13.8082576699458))
s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s.Line(point1=(12.5, 13.8082576699458), point2=(-4.17192857929744, 
    31.3135124247357))
s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s.CoincidentConstraint(entity1=v[12], entity2=g[6], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=573.183, 
    farPlane=579.613, width=40.2224, height=20.3075, cameraPosition=(-0.17563, 
    35.662, 576.398), cameraTarget=(-0.17563, 35.662, 0))
s.Line(point1=(-0.301176384064844, 35.0), point2=(-1.79435143039154, 
    36.5678095939656))
s.PerpendicularConstraint(entity1=g[6], entity2=g[11], addUndoState=False)
s.CoincidentConstraint(entity1=v[13], entity2=g[6], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=567.157, 
    farPlane=585.639, width=130.861, height=66.0693, cameraPosition=(13.9929, 
    44.5596, 576.398), cameraTarget=(13.9929, 44.5596, 0))
s.Line(point1=(-1.79435143039154, 36.5678095939656), point2=(-20.6390392305357, 
    18.6202107992506))
s.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s.CoincidentConstraint(entity1=v[15], entity2=g[7], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(13.1103, 
    29.8686, 576.398), cameraTarget=(13.1103, 29.8686, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(9.33931, 
    27.8616, 576.398), cameraTarget=(9.33931, 27.8616, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=571.42, 
    farPlane=581.376, width=62.2796, height=31.4437, cameraPosition=(-9.64149, 
    24.772, 576.398), cameraTarget=(-9.64149, 24.772, 0))
s.delete(objectList=(g[7], ))
s.Line(point1=(-20.6390392305357, 18.6202107992506), point2=(-19.1458641845256, 
    17.0524012051002))
s.CoincidentConstraint(entity1=v[16], entity2=g[6], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(width=66.2549, height=33.4508, 
    cameraPosition=(-8.09256, 25, 576.398), cameraTarget=(-8.09256, 25, 0))
s.delete(objectList=(g[6], ))
s.Line(point1=(-20.8853215328854, 15.3957495832728), point2=(-19.1458641845256, 
    17.0524012051002))
s.Line(point1=(-15.4219285795968, 20.5990612975507), point2=(-16.9151036258443, 
    22.166870891446))
s.ParallelConstraint(entity1=g[8], entity2=g[15], addUndoState=False)
s.CoincidentConstraint(entity1=v[17], entity2=g[12], addUndoState=False)
s.Line(point1=(-4.17192857929744, 31.3135124247357), point2=(-5.665103625485, 
    32.8813220192028))
s.ParallelConstraint(entity1=g[10], entity2=g[16], addUndoState=False)
s.CoincidentConstraint(entity1=v[18], entity2=g[12], addUndoState=False)
s.Line(point1=(-0.301176384064844, 35.0), point2=(1.05573523044586, 
    36.2923167268746))
s.PerpendicularConstraint(entity1=g[11], entity2=g[17], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=568.232, 
    farPlane=584.564, width=115.629, height=58.3789, cameraPosition=(2.75458, 
    30.4382, 576.398), cameraTarget=(2.75458, 30.4382, 0))
s.delete(objectList=(g[12], ))
s.Line(point1=(-20.6390392305357, 18.6202107992506), point2=(-16.9151036258443, 
    22.166870891446))
s.Line(point1=(-5.66510362572118, 32.8813220189779), point2=(-1.79435143039154, 
    36.5678095939656))
s.PerpendicularConstraint(entity1=g[16], entity2=g[19], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(width=108.691, height=54.8761, 
    cameraPosition=(1.58261, 29.1283, 576.398), cameraTarget=(1.58261, 29.1283, 
    0))
s.delete(objectList=(g[3], ))
s.Line(point1=(-28.75, 12.5), point2=(-23.2548047681825, 17.8359481433983))
s.Line(point1=(-1.5179859084954, 38.942848507222), point2=(4.33257796284227, 
    44.6238669442634))
s.PerpendicularConstraint(entity1=g[5], entity2=g[21], addUndoState=False)
p = mdb.models['Model-1'].Part(name='implante-2', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['implante-2']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=120.169, 
    farPlane=135.318, width=107.152, height=54.0987, viewOffsetX=4.52923, 
    viewOffsetY=1.90639)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['implante-2']
f1, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    -11.618536, 27.844653, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=132.21, gridSpacing=3.3, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['implante-2']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.Line(point1=(-17.131464, -15.344653), point2=(15.9511139628423, 
    16.7792139442634))
s1.ParallelConstraint(entity1=g[2], entity2=g[18], addUndoState=False)
p = mdb.models['Model-1'].parts['implante-2']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=119.279, 
    farPlane=136.208, width=106.358, height=53.6979, viewOffsetX=4.47849, 
    viewOffsetY=1.89227)
mdb.models['Model-1'].HomogeneousSolidSection(name='section-imp-CoCr', 
    material='Co-Cr', thickness=11.5)
p = mdb.models['Model-1'].parts['implante-2']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[1], sketchPlaneSide=SIDE1, origin=(
    -17.626212, 34.141115, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=127.73, gridSpacing=3.19, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['implante-2']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=94.7084, 
    farPlane=111.053, width=115.725, height=58.4273, cameraPosition=(-6.50484, 
    34.6237, 102.881), cameraTarget=(-6.50484, 34.6237, 0))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Material(name='titanium')
mdb.models['Model-1'].materials['titanium'].Elastic(table=((110000.0, 0.3), ))
del mdb.models['Model-1'].sections['section-imp-CoCr']
mdb.models['Model-1'].HomogeneousSolidSection(name='CoCr-imp-section', 
    material='Co-Cr', thickness=11.5)
p = mdb.models['Model-1'].parts['implante-2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['implante-2']
p.SectionAssignment(region=region, sectionName='CoCr-imp-section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].HomogeneousSolidSection(name='Tit-imp-sect', 
    material='titanium', thickness=11.5)
p = mdb.models['Model-1'].parts['implante-2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-2')
p = mdb.models['Model-1'].parts['implante-2']
p.SectionAssignment(region=region, sectionName='Tit-imp-sect', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['implante']
p = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['osso']
a1.Instance(name='osso-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['implante-2']
a1.Instance(name='implante-2-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-1', ), vector=(12.727422, -3.373867, 
    0.0))
#: The instance implante-2-1 was translated by 12.727422, -3.373867, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-1', ), vector=(-3.636395, 3.389398, 
    0.0))
#: The instance implante-2-1 was translated by -3.636395, 3.389398, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-1', ), vector=(1.286861, -1.325266, 
    0.0))
#: The instance implante-2-1 was translated by 1.286861, -1.325266, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-1', ), vector=(0.746588, -0.783905, 
    0.0))
#: The instance implante-2-1 was translated by 746.588E-03, -783.905E-03, 0. with respect to the assembly coordinate system
p = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].Part(name='implante-2-Copy', 
    objectToCopy=mdb.models['Model-1'].parts['implante-2'], 
    compressFeatureList=ON, scale=1.05)
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
del a.features['implante-2-1']
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['implante-2-Copy']
a1.Instance(name='implante-2-Copy-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(17.100793, -5.80506, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 17.100793, -5.80506, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(-3.818215, 3.558868, 
    0.0))
#: The instance implante-2-Copy-1 was translated by -3.818215, 3.558868, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(-3.071546, 
    -2.982535, 0.0))
#: The instance implante-2-Copy-1 was translated by -3.071546, -2.982535, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.907, 
    farPlane=238.174, width=107.878, height=54.3994, viewOffsetX=4.2598, 
    viewOffsetY=13.5059)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.712379, 0.678466, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 712.379E-03, 678.466E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.712379, 0.678466, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 712.379E-03, 678.466E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.783917, -0.8231, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 783.917E-03, -823.1E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.977, 
    farPlane=239.104, width=121.58, height=61.3087, viewOffsetX=6.49759, 
    viewOffsetY=12.3685)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.712379, 0.678466, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 712.379E-03, 678.466E-03, 0. with respect to the assembly coordinate system
p1 = mdb.models['Model-1'].parts['implante-2-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
import job
mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
#: Warning: The following parts have some elements without any section assigned: 
#:  
#:     implante-2-Copy
#: 
#: 
#: The following part instances are not meshed:
#: 
#:     osso-1
#:     implante-2-Copy-1
#: 
#: Unmeshed regions will be excluded from your analysis.
mdb.models['Model-1'].keywordBlock.setValues(edited = 0)
p=mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].Part(name='implante-2-Copy2', 
    objectToCopy=mdb.models['Model-1'].parts['implante-2'], 
    compressFeatureList=ON, scale=1.2)
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
del a.features['implante-2-Copy-1']
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['implante-2-Copy2']
a1.Instance(name='implante-2-Copy2-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy2-1', ), vector=(3.088465, 
    -3.180638, 0.0))
#: The instance implante-2-Copy2-1 was translated by 3.088465, -3.180638, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy2-1', ), vector=(4.363674, 
    -4.067278, 0.0))
#: The instance implante-2-Copy2-1 was translated by 4.363674, -4.067278, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy2-1', ), vector=(4.363674, 
    -4.067278, 0.0))
#: The instance implante-2-Copy2-1 was translated by 4.363674, -4.067278, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy2-1', ), vector=(0.814147, 0.77539, 
    0.0))
#: The instance implante-2-Copy2-1 was translated by 814.147E-03, 775.39E-03, 0. with respect to the assembly coordinate system
a = mdb.models['Model-1'].rootAssembly
del a.features['implante-2-Copy2-1']
p1 = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].Part(name='implante-2-Copy3', 
    objectToCopy=mdb.models['Model-1'].parts['implante-2'], 
    compressFeatureList=ON, scale=1.1)
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['Model-1'].parts['implante-2-Copy2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['implante-2-Copy2']
p = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['Model-1'].parts['implante-2-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['implante-2-Copy']
p = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['implante-2-Copy3']
a1.Instance(name='implante-2-Copy3-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy3-1', ), vector=(4.000035, 
    -3.728338, 0.0))
#: The instance implante-2-Copy3-1 was translated by 4.000035, -3.728338, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy3-1', ), vector=(4.000035, 
    -3.728338, 0.0))
#: The instance implante-2-Copy3-1 was translated by 4.000035, -3.728338, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy3-1', ), vector=(2.128914, 2.027568, 
    0.0))
#: The instance implante-2-Copy3-1 was translated by 2.128914, 2.027568, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy3-1', ), vector=(0.746301, 0.710774, 
    0.0))
#: The instance implante-2-Copy3-1 was translated by 746.301E-03, 710.774E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy3-1', ), vector=(1.415547, 
    -1.457792, 0.0))
#: The instance implante-2-Copy3-1 was translated by 1.415547, -1.457792, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy3-1', ), vector=(0.821246, 
    -0.862295, 0.0))
#: The instance implante-2-Copy3-1 was translated by 821.246E-03, -862.295E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy3-1', ), vector=(0.746301, 0.710774, 
    0.0))
#: The instance implante-2-Copy3-1 was translated by 746.301E-03, 710.774E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy3-1', ), vector=(0.821246, 
    -0.862295, 0.0))
#: The instance implante-2-Copy3-1 was translated by 821.246E-03, -862.295E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.514, 
    farPlane=253.231, width=237.629, height=119.828, viewOffsetX=7.2235, 
    viewOffsetY=-1.82181)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'implante-2-Copy3-1', ))
p1 = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].Part(name='implante-2-Copy', 
    objectToCopy=mdb.models['Model-1'].parts['implante-2'], 
    compressFeatureList=ON, scale=1.08)
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'implante-2-Copy3-1', ))
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['implante-2-Copy']
a1.Instance(name='implante-2-Copy-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(3.927307, -3.66055, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 3.927307, -3.66055, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(3.927307, -3.66055, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 3.927307, -3.66055, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.732732, 0.697851, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 732.732E-03, 697.851E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(1.465465, 1.395702, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 1.465465, 1.395702, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.732732, 0.697851, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 732.732E-03, 697.851E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.806315, -0.846617, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 806.315E-03, -846.617E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.732732, 0.697851, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 732.732E-03, 697.851E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.806315, -0.846617, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 806.315E-03, -846.617E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.806315, -0.846617, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 806.315E-03, -846.617E-03, 0. with respect to the assembly coordinate system
p1 = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].Part(name='implante-2-Copy2', 
    objectToCopy=mdb.models['Model-1'].parts['implante-2'], 
    compressFeatureList=ON, scale=1.07)
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'implante-2-Copy-1', ))
a = mdb.models['Model-1'].rootAssembly
del a.features['implante-2-Copy3-1']
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'implante-2-Copy-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'implante-2-Copy-1', ))
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['implante-2-Copy2']
a1.Instance(name='implante-2-Copy2-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy2-1', ), vector=(8.919482, 
    -9.365311, 0.0))
#: The instance implante-2-Copy2-1 was translated by 8.919482, -9.365311, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy2-1', ), vector=(3.130052, 3.039345, 
    0.0))
#: The instance implante-2-Copy2-1 was translated by 3.130052, 3.039345, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy2-1', ), vector=(0.725948, 0.691389, 
    0.0))
#: The instance implante-2-Copy2-1 was translated by 725.948E-03, 691.389E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy2-1', ), vector=(0.725948, 0.691389, 
    0.0))
#: The instance implante-2-Copy2-1 was translated by 725.948E-03, 691.389E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy2-1', ), vector=(0.798849, 
    -0.838778, 0.0))
#: The instance implante-2-Copy2-1 was translated by 798.849E-03, -838.778E-03, 0. with respect to the assembly coordinate system
a = mdb.models['Model-1'].rootAssembly
del a.features['implante-2-Copy2-1']
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'implante-2-Copy-1', ))
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(0.806315, -0.846617, 
    0.0))
#: The instance implante-2-Copy-1 was translated by 806.315E-03, -846.617E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy-1', ), vector=(-0.806315, 0.846617, 
    0.0))
#: The instance implante-2-Copy-1 was translated by -806.315E-03, 846.617E-03, 0. with respect to the assembly coordinate system
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
a1 = mdb.models['Model-1'].rootAssembly
a1.InstanceFromBooleanCut(name='Part-1', 
    instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['implante-2-Copy-1'], 
    cuttingInstances=(a1.instances['osso-1'], ), originalInstances=SUPPRESS)
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['Part-1']
p = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#* FeatureError: Regeneration failed
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
del a.features['Part-1-1']
a = mdb.models['Model-1'].rootAssembly
a.features['osso-1'].resume()
a = mdb.models['Model-1'].rootAssembly
a.features['implante-2-Copy-1'].resume()
a1 = mdb.models['Model-1'].rootAssembly
a1.InstanceFromBooleanCut(name='Part-1', 
    instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['osso-1'], 
    cuttingInstances=(a1.instances['implante-2-Copy-1'], ), 
    originalInstances=SUPPRESS)
a = mdb.models['Model-1'].rootAssembly
a.features['implante-2-Copy-1'].resume()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-1-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#fffe ]', ), )
s2 = a.instances['implante-2-Copy-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#8000 ]', ), )
region1=a.Surface(side1Edges=side1Edges1+side1Edges2, name='surf-imp-bone')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-1-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#70000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='surf-bone-imp')
mdb.models['Model-1'].Tie(name='Constraint-1', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220.469, 
    farPlane=245.278, width=175.086, height=88.2901, viewOffsetX=30.0381, 
    viewOffsetY=11.3696)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.764, 
    farPlane=245.982, width=174.526, height=88.0079, viewOffsetX=19.6696, 
    viewOffsetY=-1.30048)
session.viewports['Viewport: 1'].view.setValues(width=185.665, height=93.6244, 
    viewOffsetX=22.9376, viewOffsetY=-2.10687)
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.925, 
    farPlane=246.822, width=184.958, height=93.2679, viewOffsetX=20.1286, 
    viewOffsetY=-0.283407)
session.viewports['Viewport: 1'].view.setValues(width=196.811, height=99.2455, 
    viewOffsetX=23.4603, viewOffsetY=-0.957186)
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.087, 
    farPlane=247.659, width=196.011, height=98.8419, viewOffsetX=21.4421, 
    viewOffsetY=-1.43427)
del mdb.models['Model-1'].constraints['Constraint-1']
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-1-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#fffe ]', ), )
s2 = a.instances['implante-2-Copy-1'].edges
side1Edges2 = s2.getSequenceFromMask(mask=('[#8000 ]', ), )
region1=a.Surface(side1Edges=side1Edges1+side1Edges2, name='surf-impbone')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-1-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#7fffe ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='SURF-boneimp')
mdb.models['Model-1'].Tie(name='Constraint-1', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
mdb.save()
#: The model database has been saved to "C:\temp\g13-umero.cae".
