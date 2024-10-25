# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-18.57.30 176069
# Run by ltiaulas2019 on Fri Oct 25 16:33:31 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=363.485931396484, 
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
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=127.939, 
    farPlane=148.754, width=143.115, height=74.0723, viewOffsetX=7.48757, 
    viewOffsetY=-1.87001)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=169.223, 
    farPlane=207.901, width=267.128, height=138.258, cameraPosition=(7.27366, 
    -3.94324, 188.562), cameraTarget=(7.27366, -3.94324, 0))
session.Image(name='imp2', fileName='C:/temp/imp2.jpeg')
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    showImage=True, imageName='imp2')
session.viewports['Viewport: 1'].view.setValues(nearPlane=117.356, 
    farPlane=259.768, width=983.575, height=509.073, cameraPosition=(138.977, 
    -29.932, 188.562), cameraTarget=(138.977, -29.932, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(245.927, 
    66.5629, 188.562), cameraTarget=(245.927, 66.5629, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=125.644, 
    farPlane=251.48, width=767.925, height=397.458, cameraPosition=(198.148, 
    85.3462, 188.562), cameraTarget=(198.148, 85.3462, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=129.419, 
    farPlane=247.705, cameraPosition=(188.012, 66.9945, 188.562), 
    cameraTarget=(188.012, 66.9945, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=145.157, 
    farPlane=231.967, width=529.769, height=274.194, cameraPosition=(144.33, 
    75.6925, 188.562), cameraTarget=(144.33, 75.6925, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=147.761, 
    farPlane=229.363, cameraPosition=(162.644, 78.0246, 188.562), 
    cameraTarget=(162.644, 78.0246, 0))
session.viewports['Viewport: 1'].view.setValues(width=563.584, height=291.696, 
    cameraPosition=(169.095, 76.8869, 188.562), cameraTarget=(169.095, 76.8869, 
    0))
session.Image(name='imp', fileName='C:/temp/imp.jpeg')
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    imageName='imp', translucency=0.99)
session.Image(name='protese-grid-overlay2', 
    fileName='C:/temp/protese-grid-overlay2.png')
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    imageName='protese-grid-overlay2', translucency=0.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63.7836, 
    farPlane=313.34, width=1723.57, height=892.076, cameraPosition=(539.216, 
    8.75336, 188.562), cameraTarget=(539.216, 8.75336, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(454.716, 
    161.588, 188.562), cameraTarget=(454.716, 161.588, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=63.7836, 
    farPlane=313.34, width=1522.95, height=788.239, cameraPosition=(405.348, 
    175.151, 188.562), cameraTarget=(405.348, 175.151, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=71.2703, 
    farPlane=305.854, cameraPosition=(381.417, 145.461, 188.562), 
    cameraTarget=(381.417, 145.461, 0))
session.viewports['Viewport: 1'].view.setValues(width=1620.16, height=838.552, 
    cameraPosition=(405.765, 137.422, 188.562), cameraTarget=(405.765, 137.422, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=63.7836, 
    farPlane=313.34, cameraPosition=(381.325, 137.422, 188.562), cameraTarget=(
    381.325, 137.422, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.5, yScale=0.5, translucency=0.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=129.177, 
    farPlane=247.947, width=724.803, height=375.139, cameraPosition=(175.428, 
    137.97, 188.562), cameraTarget=(175.428, 137.97, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    0.5, 0.0), translucency=0.99)
s.imageOptions.setValues(origin=(5.5, -5.0))
s.imageOptions.setValues(origin=(-145.75, -125.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=129.177, 
    farPlane=247.947, width=820.284, height=424.557, cameraPosition=(201.626, 
    145.962, 188.562), cameraTarget=(201.626, 145.962, 0))
s.imageOptions.setValues(origin=(-322.0, -250.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.1413, 
    farPlane=285.983, width=1345.68, height=696.488, cameraPosition=(229.023, 
    160.959, 188.562), cameraTarget=(229.023, 160.959, 0))
s.imageOptions.setValues(origin=(-472.0, -352.5))
s.imageOptions.setValues(origin=(-835.75, -605.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.743, 
    farPlane=348.381, width=2207.59, height=1142.59, cameraPosition=(474.229, 
    178.505, 188.562), cameraTarget=(474.229, 178.505, 0))
s.imageOptions.setValues(origin=(-682.0, -567.5))
s.imageOptions.setValues(origin=(-308.25, -383.75))
s.imageOptions.setValues(origin=(-108.25, -23.75))
s.imageOptions.setValues(origin=(-87.0, -158.75))
session.viewports['Viewport: 1'].view.setValues(nearPlane=171.334, 
    farPlane=205.79, width=210.27, height=108.83, cameraPosition=(33.2327, 
    32.4961, 188.562), cameraTarget=(33.2327, 32.4961, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(34.0257, 
    10.016, 188.562), cameraTarget=(34.0257, 10.016, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=174.253, 
    farPlane=202.871, width=174.647, height=90.3927, cameraPosition=(25.557, 
    11.0689, 188.562), cameraTarget=(25.557, 11.0689, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=175.111, 
    farPlane=202.013, cameraPosition=(24.6788, 8.87223, 188.562), 
    cameraTarget=(24.6788, 8.87223, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=175.918, 
    farPlane=201.206, width=154.318, height=79.871, cameraPosition=(20.4086, 
    9.33966, 188.562), cameraTarget=(20.4086, 9.33966, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=176.677, 
    farPlane=200.447, cameraPosition=(21.5725, 12.4452, 188.562), 
    cameraTarget=(21.5725, 12.4452, 0))
session.viewports['Viewport: 1'].view.setValues(width=164.168, height=84.9691, 
    cameraPosition=(23.4453, 12.5226, 188.562), cameraTarget=(23.4453, 12.5226, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=175.918, 
    farPlane=201.206, cameraPosition=(28.6046, 12.6259, 188.562), 
    cameraTarget=(28.6046, 12.6259, 0))
session.viewports['Viewport: 1'].view.setValues(width=174.647, height=90.3927, 
    cameraPosition=(30.8538, 12.6819, 188.562), cameraTarget=(30.8538, 12.6819, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=175.111, 
    farPlane=202.013, cameraPosition=(28.4388, 9.27709, 188.562), 
    cameraTarget=(28.4388, 9.27709, 0))
session.viewports['Viewport: 1'].view.setValues(width=185.795, height=96.1624, 
    cameraPosition=(30.6915, 9.32266, 188.562), cameraTarget=(30.6915, 9.32266, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=174.253, 
    farPlane=202.871, cameraPosition=(32.7935, 3.71416, 188.562), 
    cameraTarget=(32.7935, 3.71416, 0))
session.viewports['Viewport: 1'].view.setValues(width=197.654, height=102.3, 
    cameraPosition=(35.3987, 3.60602, 188.562), cameraTarget=(35.3987, 3.60602, 
    0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=173.339, 
    farPlane=203.785, cameraPosition=(37.8833, 3.73032, 188.562), 
    cameraTarget=(37.8833, 3.73032, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=169.065, 
    farPlane=208.059, width=269.318, height=139.392, cameraPosition=(64.9867, 
    14.495, 188.562), cameraTarget=(64.9867, 14.495, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(47.5513, 
    -20.7341, 188.562), cameraTarget=(47.5513, -20.7341, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(50.0904, 
    -18.5323, 188.562), cameraTarget=(50.0904, -18.5323, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.6, yScale=0.6, translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.55, yScale=0.55, translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.575, yScale=0.575, translucency=0.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=166.496, 
    farPlane=210.628, width=304.797, height=157.755, cameraPosition=(54.9851, 
    -12.8316, 188.562), cameraTarget=(54.9851, -12.8316, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.475, yScale=0.475, translucency=0.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=167.82, 
    farPlane=209.304, width=286.509, height=148.29, cameraPosition=(44.4076, 
    -8.27151, 188.562), cameraTarget=(44.4076, -8.27151, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    -88.0, -158.75), xScale=0.475, yScale=0.475, translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    -86.0, -158.75), xScale=0.475, yScale=0.475, translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    -85.0, -158.75), xScale=0.475, yScale=0.475, translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    -84.0, -158.75), xScale=0.475, yScale=0.475, translucency=0.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=171.334, 
    farPlane=205.79, width=237.97, height=123.167, cameraPosition=(31.5785, 
    -13.6247, 188.562), cameraTarget=(31.5785, -13.6247, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.45, yScale=0.45, translucency=0.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=173.339, 
    farPlane=203.785, width=185.795, height=96.1625, cameraPosition=(10.0656, 
    -18.9482, 188.562), cameraTarget=(10.0656, -18.9482, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    -81.0, -158.75), xScale=0.45, yScale=0.45, translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    -80.0, -158.75), xScale=0.425, yScale=0.425, translucency=0.99)
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.42, yScale=0.42, translucency=0.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=182.906, 
    farPlane=194.218, width=78.131, height=40.4386, cameraPosition=(-20.3682, 
    -25.0681, 188.562), cameraTarget=(-20.3682, -25.0681, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    -79.0, -158.75), xScale=0.42, yScale=0.42, translucency=0.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=176.628, 
    farPlane=200.496, width=145.653, height=75.3859, cameraPosition=(4.72194, 
    -11.6068, 188.562), cameraTarget=(4.72194, -11.6068, 0))
s.ArcByCenterEnds(center=(-12.5, -12.5), point1=(-35.0, -26.25), point2=(2.5, 
    10.0), direction=CLOCKWISE)
s.Line(point1=(-35.0, -26.25), point2=(2.12676682292801, 9.44015023439202))
session.viewports['Viewport: 1'].view.setValues(nearPlane=177.344, 
    farPlane=199.78, width=154.95, height=80.1978, cameraPosition=(16.9538, 
    -18.8657, 188.562), cameraTarget=(16.9538, -18.8657, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6.33813, 
    -17.8913, 188.562), cameraTarget=(6.33813, -17.8913, 0))
session.viewports['Viewport: 1'].view.setValues(width=164.84, height=85.3168, 
    cameraPosition=(9.74165, -19.3126, 188.562), cameraTarget=(9.74165, 
    -19.3126, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=175.867, 
    farPlane=201.257, cameraPosition=(12.9535, -21.5932, 188.562), 
    cameraTarget=(12.9535, -21.5932, 0))
p = mdb.models['Model-1'].Part(name='Part-9', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-9']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-9']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=108.148, 
    farPlane=121.292, width=86.8337, height=44.9428, viewOffsetX=1.21278, 
    viewOffsetY=1.40795)
p1 = mdb.models['Model-1'].parts['implante-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Model-1'].parts['Part-9']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].parts.changeKey(fromName='Part-9', 
    toName='cabeça-implante')
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=166.675, 
    farPlane=210.448, width=302.318, height=156.472, cameraPosition=(40.1382, 
    -11.0402, 188.562), cameraTarget=(40.1382, -11.0402, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    showImage=True, imageName='protese-grid-overlay2')
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    xScale=0.42, yScale=0.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=147.927, 
    farPlane=229.196, width=561.287, height=290.508, cameraPosition=(19.5994, 
    -63.0559, 188.562), cameraTarget=(19.5994, -63.0559, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(38.65, 13.8951, 
    188.562), cameraTarget=(38.65, 13.8951, 0))
s1.imageOptions.setValues(origin=(-100.0, -122.5))
session.viewports['Viewport: 1'].view.setValues(nearPlane=174.369, 
    farPlane=202.755, width=173.227, height=89.6575, cameraPosition=(-19.5343, 
    12.858, 188.562), cameraTarget=(-19.5343, 12.858, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(origin=(
    -81.0, -122.5), xScale=0.42, yScale=0.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=179.875, 
    farPlane=197.249, width=119.993, height=62.1051, cameraPosition=(-0.786351, 
    20.3347, 188.562), cameraTarget=(-0.786351, 20.3347, 0))
s1.ArcByCenterEnds(center=(-15.0, 23.75), point1=(-37.5, 10.0), point2=(0.0, 
    46.25), direction=CLOCKWISE)
s1.Line(point1=(-37.5, 10.0), point2=(-0.373233177071986, 45.690150234392))
session.viewports['Viewport: 1'].view.setValues(nearPlane=184.164, 
    farPlane=192.96, width=53.6806, height=27.7836, cameraPosition=(-17.3123, 
    17.6449, 188.562), cameraTarget=(-17.3123, 17.6449, 0))
s1.Line(point1=(-31.3884151314266, 15.8750976935303), point2=(
    -27.9004371978081, 12.2467200438114))
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.CoincidentConstraint(entity1=v[3], entity2=g[3], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=184.676, 
    farPlane=192.448, width=47.4321, height=24.5496, cameraPosition=(-6.81209, 
    30.0047, 188.562), cameraTarget=(-6.81209, 30.0047, 0))
s1.Line(point1=(-6.00250231557477, 40.2787051112224), point2=(-2.5, 
    36.6352184386818))
s1.CoincidentConstraint(entity1=v[5], entity2=g[3], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=182.569, 
    farPlane=194.555, width=82.7794, height=42.8444, cameraPosition=(-0.818081, 
    33.5418, 188.562), cameraTarget=(-0.818081, 33.5418, 0))
s1.Line(point1=(-2.5, 36.6352184386818), point2=(-27.9004371978081, 
    12.2467200438114))
session.viewports['Viewport: 1'].view.setValues(width=88.0632, height=45.5792, 
    cameraPosition=(0.943735, 34.7165, 188.562), cameraTarget=(0.943735, 
    34.7165, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-1.21495, 
    27.0738, 188.562), cameraTarget=(-1.21495, 27.0738, 0))
s1.Line(point1=(-4.20306767493223, 35.0), point2=(-5.85458646915504, 
    36.7200443723123))
s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s1.CoincidentConstraint(entity1=v[7], entity2=g[6], addUndoState=False)
s1.Line(point1=(-5.85458646915504, 36.7200443723123), point2=(
    -27.7364525660523, 15.7099392300297))
s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s1.Line(point1=(-27.7364525660523, 15.7099392300297), point2=(
    -26.0849337719229, 13.9898948576441))
s1.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s1.CoincidentConstraint(entity1=v[10], entity2=g[6], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=179.875, 
    farPlane=197.249, width=119.993, height=62.1051, cameraPosition=(7.64341, 
    32.9948, 188.562), cameraTarget=(7.64341, 32.9948, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(10.2831, 
    20.6945, 188.562), cameraTarget=(10.2831, 20.6945, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=180.886, 
    farPlane=196.238, width=93.6842, height=48.4885, cameraPosition=(5.50806, 
    19.7019, 188.562), cameraTarget=(5.50806, 19.7019, 0))
s1.Line(point1=(-21.25, 18.6322076502186), point2=(-1.25000000046566, 
    -2.19764155663154))
s1.PerpendicularConstraint(entity1=g[6], entity2=g[10], addUndoState=False)
s1.CoincidentConstraint(entity1=v[11], entity2=g[6], addUndoState=False)
s1.Line(point1=(-1.25000000046566, -2.19764155663154), point2=(
    11.4537517152554, 10.0))
s1.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s1.Line(point1=(11.4537517152554, 10.0), point2=(-8.54624828400387, 
    30.8298492072019))
s1.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s1.CoincidentConstraint(entity1=v[14], entity2=g[6], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=175.97, 
    farPlane=201.154, width=173.935, height=90.0244, cameraPosition=(27.5272, 
    12.9493, 188.562), cameraTarget=(27.5272, 12.9493, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(22.3889, 
    20.7157, 188.562), cameraTarget=(22.3889, 20.7157, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=177.436, 
    farPlane=199.688, width=153.689, height=79.5455, cameraPosition=(11.7099, 
    21.0673, 188.562), cameraTarget=(11.7099, 21.0673, 0))
mdb.models['Model-1'].sketches['__profile__'].imageOptions.setValues(
    showImage=False, xScale=0.42, yScale=0.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=180.396, 
    farPlane=196.728, width=99.6641, height=51.5835, cameraPosition=(-2.9327, 
    22.0376, 188.562), cameraTarget=(-2.9327, 22.0376, 0))
s1.delete(objectList=(g[6], ))
s1.Line(point1=(-27.9004371978081, 12.2467200438114), point2=(
    -26.0849337719229, 13.9898948576441))
s1.Line(point1=(-4.20306767493223, 35.0), point2=(-2.5, 36.6352184386818))
s1.PerpendicularConstraint(entity1=g[7], entity2=g[14], addUndoState=False)
s1.Line(point1=(-21.25, 18.6322076502186), point2=(-22.9015187941377, 
    20.3522520224645))
s1.ParallelConstraint(entity1=g[10], entity2=g[15], addUndoState=False)
s1.CoincidentConstraint(entity1=v[15], entity2=g[8], addUndoState=False)
s1.Line(point1=(-8.54624828400387, 30.8298492072019), point2=(
    -10.1977670785777, 32.5498935799973))
s1.ParallelConstraint(entity1=g[12], entity2=g[16], addUndoState=False)
s1.CoincidentConstraint(entity1=v[16], entity2=g[8], addUndoState=False)
s1.delete(objectList=(g[8], ))
s1.Line(point1=(-27.7364525660523, 15.7099392300297), point2=(
    -22.9015187941377, 20.3522520224645))
s1.PerpendicularConstraint(entity1=g[9], entity2=g[17], addUndoState=False)
s1.Line(point1=(-10.1977670785777, 32.5498935799973), point2=(
    -5.85458646915504, 36.7200443723123))
s1.PerpendicularConstraint(entity1=g[16], entity2=g[18], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=180.396, 
    farPlane=196.728, width=112.793, height=58.3788, cameraPosition=(-1.43494, 
    21.9427, 188.562), cameraTarget=(-1.43494, 21.9427, 0))
s1.delete(objectList=(g[3], ))
s1.Line(point1=(-31.3884151314266, 15.8750976935303), point2=(
    -6.00250231557477, 40.2787051112224))
s1.PerpendicularConstraint(entity1=g[4], entity2=g[19], addUndoState=False)
s1.delete(objectList=(g[2], ))
p = mdb.models['Model-1'].Part(name='haste-implante', 
    dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['haste-implante']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['haste-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(width=90.3559, height=46.7658, 
    viewOffsetX=1.24204, viewOffsetY=0.407425)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(width=91.8988, height=47.5644, 
    viewOffsetX=3.81272, viewOffsetY=-0.943787)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['haste-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Model-1'].parts['haste-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].Part(name='haste-implante-Copy', 
    objectToCopy=mdb.models['Model-1'].parts['haste-implante'], 
    compressFeatureList=ON, scale=0.85)
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=96.1674, 
    farPlane=108.954, width=87.9667, height=45.5293, viewOffsetX=3.88524, 
    viewOffsetY=-0.733817)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=195.291, 
    farPlane=224.803, width=191.52, height=99.1257, viewOffsetX=5.83596, 
    viewOffsetY=-2.36232)
o3 = session.openOdb(name='C:/temp/boneimp-alumina.odb')
#: Model: C:/temp/boneimp-alumina.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       20
#: Number of Node Sets:          31
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.621, 
    farPlane=362.714, width=192.583, height=99.6759, viewOffsetX=-0.429736, 
    viewOffsetY=-1.12075)
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.474, 
    farPlane=362.862, width=192.459, height=99.6116, viewOffsetX=33.9252, 
    viewOffsetY=-6.44556)
session.viewports['Viewport: 1'].view.setValues(width=204.743, height=105.969, 
    viewOffsetX=35.9673, viewOffsetY=-7.94043)
session.viewports['Viewport: 1'].view.setValues(nearPlane=227.527, 
    farPlane=363.809, width=203.895, height=105.531, viewOffsetX=42.3543, 
    viewOffsetY=-9.18982)
session.viewports['Viewport: 1'].view.setValues(width=191.717, height=99.2276, 
    viewOffsetX=40.1013, viewOffsetY=-7.78796)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['haste-implante-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['haste-implante-Copy']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['haste-implante-Copy']
p.SectionAssignment(region=region, sectionName='Tit-imp-sect', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p1 = mdb.models['Model-1'].parts['cabeça-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['cabeça-implante']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['cabeça-implante']
p.SectionAssignment(region=region, sectionName='CoCr-imp-section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=108.148, 
    farPlane=121.292, width=86.8337, height=44.9428, viewOffsetX=3.61797, 
    viewOffsetY=-0.0962313)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.177, 
    farPlane=223.917, width=169.995, height=87.985, viewOffsetX=10.2325, 
    viewOffsetY=0.563704)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/boneimp-alumina.odb'])
o3 = session.openOdb(name='C:/temp/boneimp-alumina.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.415, 
    farPlane=362.92, width=204.692, height=105.943, viewOffsetX=44.8583, 
    viewOffsetY=-9.65823)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/boneimp-alumina.odb'])
o3 = session.openOdb(name='C:/temp/boneimp-CoCr.odb')
#: Model: C:/temp/boneimp-CoCr.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       17
#: Number of Node Sets:          28
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
p = mdb.models['Model-1'].parts['cabeça-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].sections['CoCr-imp-section'].setValues(material='Co-Cr', 
    thickness=22.5)
mdb.models['Model-1'].sections['Tit-imp-sect'].setValues(material='titanium', 
    thickness=22.5)
mdb.models['Model-1'].sections['sect-alumina'].setValues(material='alumina', 
    thickness=22.5)
mdb.models['Model-1'].sections['steel-sect'].setValues(
    material='stainless-steel-316', thickness=22.5)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='BLAH-bonebase', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['BLAH-bonebase'].submit(consistencyChecking=OFF)
#: The job input file "BLAH-bonebase.inp" has been submitted for analysis.
#: Job BLAH-bonebase: Analysis Input File Processor completed successfully.
#: Job BLAH-bonebase: Abaqus/Standard completed successfully.
#: Job BLAH-bonebase completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/boneimp-CoCr.odb'])
o3 = session.openOdb(name='C:/temp/BLAH-bonebase.odb')
#: Model: C:/temp/BLAH-bonebase.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       21
#: Number of Node Sets:          32
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.326, 
    farPlane=362.001, width=170.693, height=88.346, viewOffsetX=42.8072, 
    viewOffsetY=-6.54813)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.085, 
    farPlane=362.242, width=192.976, height=99.8795, viewOffsetX=47.3296, 
    viewOffsetY=-9.23233)
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.247, 
    farPlane=363.08, width=192.27, height=99.514, viewOffsetX=53.1989, 
    viewOffsetY=-6.41748)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourStyle=CONTINUOUS, maxValue=6.75763, minValue=0.000862774)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.printToFile(fileName='BLAH-BoneBase-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
leaf = dgo.LeafFromNodeSets(nodeSets=("PONTOS-BASE-SEM-CORTICAL", ))
dg = session.DisplayGroup(leaf=leaf, name='DisplayGroup-2')
#: The selected probe values were written to file "C:/temp/blah-bonebase.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#: The selected probe values were written to file "C:/temp/blah-bonebase-u.rpt".
session.printToFile(fileName='BLAH-BoneBase-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.031, 
    farPlane=224.063, width=192.246, height=99.7521, viewOffsetX=18.2692, 
    viewOffsetY=-2.65276)
session.printToFile(fileName='BLAH-Mesh-Used', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
p = mdb.models['Model-1'].parts['cabeça-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=106.739, 
    farPlane=122.7, width=109.77, height=56.8142, viewOffsetX=12.6513, 
    viewOffsetY=-4.91818)
session.viewports['Viewport: 1'].view.setValues(nearPlane=106.303, 
    farPlane=123.136, width=109.322, height=56.582, viewOffsetX=6.2093, 
    viewOffsetY=-1.32303)
session.viewports['Viewport: 1'].view.setValues(nearPlane=105.763, 
    farPlane=123.676, width=123.095, height=63.7106, viewOffsetX=11.7478, 
    viewOffsetY=-3.72671)
session.viewports['Viewport: 1'].view.setValues(nearPlane=105.239, 
    farPlane=124.2, width=122.486, height=63.3953, viewOffsetX=8.61023, 
    viewOffsetY=1.6838)
session.viewports['Viewport: 1'].view.setValues(width=130.363, height=67.4724, 
    viewOffsetX=11.0796, viewOffsetY=0.919652)
session.viewports['Viewport: 1'].view.setValues(nearPlane=104.68, 
    farPlane=124.76, width=129.612, height=67.0836, viewOffsetX=8.5718, 
    viewOffsetY=-0.0637812)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['Model-1'].parts['cabeça-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['cabeça-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('implante-2-Copy4-1', 'RP-9', 'RP-7', 'Partition edge-10', 
    'Partition edge-9', 'RP-6', 'RP-4', 'Partition edge-6', 'Partition edge-5', 
    'RP-2', 'RP-1', 'Partition edge-2', 'Partition edge-1', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('bone-base-1', 'RP-8', ))
a = mdb.models['Model-1'].rootAssembly
a.features['imp-osso-1'].resume()
a = mdb.models['Model-1'].rootAssembly
a.features['osso-divided-1'].resume()
a = mdb.models['Model-1'].rootAssembly
del a.features['osso-divided-1']
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('imp-osso-1', 'RP-3', 'Partition edge-4', 'Partition edge-3', 
    ))
a = mdb.models['Model-1'].rootAssembly
a.features['osso-1'].resume()
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('osso-1', 'RP-5', 'Partition edge-8', 'Partition edge-7', ))
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['osso-divided']
a1.Instance(name='osso-divided-1', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['cabeça-implante']
a1.Instance(name='cabeça-implante-1', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['haste-implante']
a1.Instance(name='haste-implante-1', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('haste-implante-1', ), vector=(0.851534, 0.817609, 
    0.0))
#: The instance haste-implante-1 was translated by 851.534E-03, 817.609E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(18.563383, 
    17.845075, 0.0))
#: The instance cabeça-implante-1 was translated by 18.563383, 17.845075, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.209, 
    farPlane=239.728, width=113.29, height=58.636, viewOffsetX=18.8854, 
    viewOffsetY=13.0429)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(3.774926, 3.821993, 
    0.0))
#: The instance cabeça-implante-1 was translated by 3.774926, 3.821993, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(5.946516, 5.907068, 
    0.0))
#: The instance cabeça-implante-1 was translated by 5.946516, 5.907068, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-0.851534, 
    -0.817609, 0.0))
#: The instance cabeça-implante-1 was translated by -851.534E-03, -817.609E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-1.651519, 1.720044, 
    0.0))
#: The instance cabeça-implante-1 was translated by -1.651519, 1.720044, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(width=120.812, height=62.5291, 
    viewOffsetX=19.8991, viewOffsetY=12.215)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-3.502502, 3.643487, 
    0.0))
#: The instance cabeça-implante-1 was translated by -3.502502, 3.643487, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('haste-implante-1', ), vector=(10.0, -10.414925, 
    0.0))
#: The instance haste-implante-1 was translated by 10., -10.414925, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.991, 
    farPlane=240.945, width=127.509, height=65.9952, viewOffsetX=19.76, 
    viewOffsetY=11.2809)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220.618, 
    farPlane=240.319, width=127.872, height=66.1831, viewOffsetX=25.1208, 
    viewOffsetY=16.2184)
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.742, 
    farPlane=239.194, width=120.812, height=62.5291, viewOffsetX=23.2343, 
    viewOffsetY=17.4468)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-1.651519, 1.720044, 
    0.0))
#: The instance cabeça-implante-1 was translated by -1.651519, 1.720044, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-0.851534, 
    -0.817609, 0.0))
#: The instance cabeça-implante-1 was translated by -851.534E-03, -817.609E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-0.851534, 
    -0.817609, 0.0))
#: The instance cabeça-implante-1 was translated by -851.534E-03, -817.609E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('haste-implante-1', ), vector=(1.703068, 1.635218, 
    0.0))
#: The instance haste-implante-1 was translated by 1.703068, 1.635218, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('haste-implante-1', ), vector=(4.343181, 4.170151, 
    0.0))
#: The instance haste-implante-1 was translated by 4.343181, 4.170151, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.964, 
    farPlane=242.972, width=172.139, height=89.0948, viewOffsetX=36.9465, 
    viewOffsetY=23.9142)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.255, 
    farPlane=243.681, width=171.58, height=88.8052, viewOffsetX=31.8656, 
    viewOffsetY=18.8729)
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.209, 
    farPlane=239.728, width=113.291, height=58.6362, viewOffsetX=23.9083, 
    viewOffsetY=20.7739)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-0.851534, 
    -0.817609, 0.0))
#: The instance cabeça-implante-1 was translated by -851.534E-03, -817.609E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(1.0, 1.0, 0.0))
#: The instance cabeça-implante-1 was translated by 1., 1., 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-0.3, 0.0, 0.0))
#: The instance cabeça-implante-1 was translated by -300.E-03, 0., 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-0.1, -0.1, 0.0))
#: The instance cabeça-implante-1 was translated by -100.E-03, -100.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.57, 
    farPlane=237.367, width=95.1018, height=49.2222, viewOffsetX=-4.48151, 
    viewOffsetY=2.02191)
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.157, 
    farPlane=237.78, width=94.9261, height=49.1312, viewOffsetX=9.13025, 
    viewOffsetY=12.2862)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.21, 
    farPlane=238.726, width=113.804, height=58.9018, viewOffsetX=11.7654, 
    viewOffsetY=11.207)
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.702, 
    farPlane=239.234, width=113.543, height=58.7671, viewOffsetX=18.5897, 
    viewOffsetY=15.8228)
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.722, 
    farPlane=239.214, width=113.553, height=58.7725, viewOffsetX=22.4455, 
    viewOffsetY=17.6096)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-0.2, -0.2, 0.0))
#: The instance cabeça-implante-1 was translated by -200.E-03, -200.E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('haste-implante-1', ), vector=(0.825759, -0.860022, 
    0.0))
#: The instance haste-implante-1 was translated by 825.759E-03, -860.022E-03, 0. with respect to the assembly coordinate system
a = mdb.models['Model-1'].rootAssembly
del a.features['haste-implante-1']
session.viewports['Viewport: 1'].view.setValues(width=120.802, height=62.5238, 
    viewOffsetX=25.3133, viewOffsetY=17.7896)
p1 = mdb.models['Model-1'].parts['haste-implante-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['haste-implante-Copy']
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['Model-1'].parts['haste-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].Part(name='haste-implante-Copy', 
    objectToCopy=mdb.models['Model-1'].parts['haste-implante'], 
    compressFeatureList=ON, scale=0.5)
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Model-1'].parts['haste-implante-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['haste-implante-Copy']
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['Model-1'].parts['haste-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].Part(name='haste-implante-Copy', 
    objectToCopy=mdb.models['Model-1'].parts['haste-implante'], 
    compressFeatureList=ON, scale=0.75)
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['haste-implante-Copy']
a1.Instance(name='haste-implante-Copy-1', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('haste-implante-Copy-1', ), vector=(9.527814, 
    9.148231, 0.0))
#: The instance haste-implante-Copy-1 was translated by 9.527814, 9.148231, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=203.878, 
    farPlane=221.272, width=106.411, height=55.0757, viewOffsetX=8.09912, 
    viewOffsetY=9.17309)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('haste-implante-Copy-1', ), vector=(7.5, -7.811193, 
    0.0))
#: The instance haste-implante-Copy-1 was translated by 7.5, -7.811193, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('haste-implante-Copy-1', ), vector=(-0.969688, 
    1.287636, 0.0))
#: The instance haste-implante-Copy-1 was translated by -969.688E-03, 1.287636, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=198.587, 
    farPlane=226.563, width=192.437, height=99.6005, viewOffsetX=31.8396, 
    viewOffsetY=17.1406)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197.815, 
    farPlane=227.335, width=191.69, height=99.2135, viewOffsetX=22.1976, 
    viewOffsetY=0.558499)
session.viewports['Viewport: 1'].view.setValues(width=203.921, height=105.544, 
    viewOffsetX=25.4694, viewOffsetY=0.0621853)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.869, 
    farPlane=228.281, width=202.95, height=105.042, viewOffsetX=33.7671, 
    viewOffsetY=0.57242)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.944, 
    farPlane=228.207, width=203.027, height=105.082, viewOffsetX=31.2277, 
    viewOffsetY=0.955682)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197.876, 
    farPlane=227.274, width=180.245, height=93.29, viewOffsetX=24.3089, 
    viewOffsetY=1.6695)
session.viewports['Viewport: 1'].view.setValues(nearPlane=198.692, 
    farPlane=226.458, width=180.988, height=93.6747, viewOffsetX=25.433, 
    viewOffsetY=0.31053)
session.viewports['Viewport: 1'].view.setValues(width=192.485, height=99.6254, 
    viewOffsetX=28.9282, viewOffsetY=-0.0999231)
a1 = mdb.models['Model-1'].rootAssembly
a1.InstanceFromBooleanCut(name='BLAH-osso-cut-imp-dim', 
    instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['osso-divided-1'], 
    cuttingInstances=(a1.instances['haste-implante-Copy-1'], 
    a1.instances['cabeça-implante-1'], ), originalInstances=SUPPRESS)
a = mdb.models['Model-1'].rootAssembly
a.features['cabeça-implante-1'].resume()
a = mdb.models['Model-1'].rootAssembly
a.features['haste-implante-Copy-1'].resume()
a1 = mdb.models['Model-1'].rootAssembly
a1.makeIndependent(instances=(a1.instances['cabeça-implante-1'], ))
a1 = mdb.models['Model-1'].rootAssembly
a1.makeIndependent(instances=(a1.instances['haste-implante-Copy-1'], ))
a1 = mdb.models['Model-1'].rootAssembly
a1.makeIndependent(instances=(a1.instances['BLAH-osso-cut-imp-dim-1'], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=199.221, 
    farPlane=225.14, width=159.955, height=82.7884, viewOffsetX=24.8327, 
    viewOffsetY=12.2724)
session.viewports['Viewport: 1'].view.setValues(nearPlane=200.562, 
    farPlane=223.799, width=142.288, height=73.6443, viewOffsetX=20.576, 
    viewOffsetY=13.8462)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201.221, 
    farPlane=223.14, width=142.755, height=73.8862, viewOffsetX=26.6552, 
    viewOffsetY=10.3006)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201.185, 
    farPlane=223.176, width=142.729, height=73.8729, viewOffsetX=28.7137, 
    viewOffsetY=11.4656)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'BLAH-osso-cut-imp-dim-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=202.946, 
    farPlane=221.414, width=127.22, height=65.8455, viewOffsetX=28.4379, 
    viewOffsetY=12.2411)
session.viewports['Viewport: 1'].view.setValues(nearPlane=202.41, 
    farPlane=221.951, width=126.883, height=65.6714, viewOffsetX=24.6144, 
    viewOffsetY=18.6721)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
t = a.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    -3.949464, 29.909297, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=114.67, gridSpacing=2.86, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
a = mdb.models['Model-1'].rootAssembly
a.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(width=76.4511, height=39.5691, 
    cameraPosition=(-0.797738, 25.1597, 114.679), cameraTarget=(-0.797738, 
    25.1597, 0))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.485, 
    farPlane=227.876, width=215.836, height=111.711, viewOffsetX=76.2465, 
    viewOffsetY=-4.6837)
session.viewports['Viewport: 1'].view.setValues(nearPlane=195.636, 
    farPlane=228.725, width=214.903, height=111.228, viewOffsetX=57.817, 
    viewOffsetY=5.74309)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201.805, 
    farPlane=222.555, width=127.022, height=65.743, viewOffsetX=31.6473, 
    viewOffsetY=15.0049)
session.viewports['Viewport: 1'].view.setValues(nearPlane=202.398, 
    farPlane=221.963, width=127.394, height=65.9359, viewOffsetX=30.2188, 
    viewOffsetY=17.4524)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['haste-implante-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['haste-implante-Copy']
f1, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    -5.723137, 12.792699, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=90.49, gridSpacing=2.26, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['haste-implante-Copy']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['cabeça-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=108.032, 
    farPlane=121.407, width=92.2775, height=47.7604, viewOffsetX=2.46143, 
    viewOffsetY=0.398178)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=206.101, 
    farPlane=218.259, width=74.3318, height=38.4722, viewOffsetX=8.22436, 
    viewOffsetY=15.1179)
a = mdb.models['Model-1'].rootAssembly
f21 = a.instances['cabeça-implante-1'].faces
t = a.MakeSketchTransform(sketchPlane=f21[0], sketchPlaneSide=SIDE1, origin=(
    -3.949464, 29.909297, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=114.67, gridSpacing=2.86, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
a = mdb.models['Model-1'].rootAssembly
a.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=110.082, 
    farPlane=119.276, width=56.1078, height=29.0399, cameraPosition=(-2.2348, 
    19.4412, 114.679), cameraTarget=(-2.2348, 19.4412, 0))
s.Line(point1=(-12.577387, -24.072022), point2=(-3.53372134856995, 
    -15.3782997298523))
session.viewports['Viewport: 1'].view.setValues(nearPlane=110.082, 
    farPlane=119.276, width=63.499, height=32.8654, cameraPosition=(-1.81175, 
    17.4043, 114.679), cameraTarget=(-1.81175, 17.4043, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(12.3967, 
    25.8702, 114.679), cameraTarget=(12.3967, 25.8702, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=109.789, 
    farPlane=119.569, cameraPosition=(19.1816, 31.4609, 114.679), 
    cameraTarget=(19.1816, 31.4609, 0))
s.Line(point1=(15.5057132633189, 2.9244058334168), point2=(24.549379822928, 
    11.618128234392))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
pickedFaces = f1.getSequenceFromMask(mask=('[#1 ]', ), )
a.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=203.949, 
    farPlane=220.411, width=113.428, height=58.7076, viewOffsetX=19.8797, 
    viewOffsetY=17.756)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
mdb.models['Model-1'].constraints.delete(('Constraint-1', 'Constraint-2', 
    'Constraint-3', 'Constraint-4', 'Constraint-5', 'Constraint-6', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
mdb.models['Model-1'].loads.delete(('Load-1', 'Load-2', ))
del mdb.models['Model-1'].boundaryConditions['BC-1']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'BLAH-osso-cut-imp-dim-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'cabeça-implante-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#5 ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-35')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['BLAH-osso-cut-imp-dim-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#2220004 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-35')
mdb.models['Model-1'].Tie(name='Constraint-1', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'BLAH-osso-cut-imp-dim-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'BLAH-osso-cut-imp-dim-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'haste-implante-Copy-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['haste-implante-Copy-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#3ffe ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-37')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['BLAH-osso-cut-imp-dim-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1011f9f9 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-37')
mdb.models['Model-1'].Tie(name='Constraint-2', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'haste-implante-Copy-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'BLAH-osso-cut-imp-dim-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'haste-implante-Copy-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['haste-implante-Copy-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-39')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-39')
mdb.models['Model-1'].Tie(name='Constraint-3', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'haste-implante-Copy-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'BLAH-osso-cut-imp-dim-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=198.197, 
    farPlane=226.164, width=192.374, height=99.5675, viewOffsetX=54.0923, 
    viewOffsetY=15.4729)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197.426, 
    farPlane=226.935, width=191.625, height=99.1801, viewOffsetX=45.5713, 
    viewOffsetY=10.3513)
session.viewports['Viewport: 1'].view.setValues(nearPlane=199.734, 
    farPlane=224.626, width=171.3, height=88.6602, viewOffsetX=39.7716, 
    viewOffsetY=11.8461)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197.363, 
    farPlane=226.997, width=203.792, height=105.477, viewOffsetX=47.166, 
    viewOffsetY=8.63313)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.554, 
    farPlane=227.807, width=202.956, height=105.045, viewOffsetX=34.7263, 
    viewOffsetY=6.30027)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197.487, 
    farPlane=226.874, width=180.183, height=93.2581, viewOffsetX=29.9305, 
    viewOffsetY=9.24847)
session.viewports['Viewport: 1'].view.setValues(nearPlane=198.302, 
    farPlane=226.058, width=180.927, height=93.6433, viewOffsetX=37.1047, 
    viewOffsetY=9.51423)
session.viewports['Viewport: 1'].view.setValues(nearPlane=207.681, 
    farPlane=216.679, width=54.9708, height=28.4514, viewOffsetX=33.9949, 
    viewOffsetY=27.5087)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['BLAH-osso-cut-imp-dim-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#1000000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.892094324145155)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['BLAH-osso-cut-imp-dim-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#1000000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.950256886674919)
session.viewports['Viewport: 1'].view.setValues(nearPlane=206.079, 
    farPlane=218.281, width=84.1151, height=43.5357, viewOffsetX=44.7812, 
    viewOffsetY=29.6023)
session.viewports['Viewport: 1'].view.setValues(nearPlane=205.713, 
    farPlane=218.648, width=83.9656, height=43.4584, viewOffsetX=23.222, 
    viewOffsetY=32.7707)
session.viewports['Viewport: 1'].view.setValues(nearPlane=206.101, 
    farPlane=218.26, width=74.3318, height=38.4722, viewOffsetX=20.6928, 
    viewOffsetY=34.2375)
session.viewports['Viewport: 1'].view.setValues(nearPlane=206.454, 
    farPlane=217.906, width=74.4594, height=38.5382, viewOffsetX=19.6519, 
    viewOffsetY=33.4534)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['cabeça-implante-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#8 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.643430213779026)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['cabeça-implante-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#8 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.25134009099111)
session.viewports['Viewport: 1'].view.setValues(nearPlane=202.872, 
    farPlane=221.488, width=128.216, height=66.3611, viewOffsetX=37.1052, 
    viewOffsetY=33.9697)
session.viewports['Viewport: 1'].view.setValues(nearPlane=202.332, 
    farPlane=222.028, width=127.874, height=66.1844, viewOffsetX=34.5952, 
    viewOffsetY=22.7815)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201.702, 
    farPlane=222.658, width=144.269, height=74.67, viewOffsetX=39.6491, 
    viewOffsetY=22.3888)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201.068, 
    farPlane=223.292, width=143.816, height=74.4352, viewOffsetX=40.0668, 
    viewOffsetY=17.7962)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
del mdb.models['Model-1'].steps['Step-1']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].view.setValues(nearPlane=201.101, 
    farPlane=223.259, width=143.84, height=74.4476, viewOffsetX=37.8132, 
    viewOffsetY=10.0197)
session.viewports['Viewport: 1'].view.setValues(nearPlane=199.686, 
    farPlane=224.675, width=171.961, height=89.0023, viewOffsetX=47.3843, 
    viewOffsetY=6.39209)
session.viewports['Viewport: 1'].view.setValues(nearPlane=198.935, 
    farPlane=225.425, width=171.314, height=88.6679, viewOffsetX=42.5761, 
    viewOffsetY=2.48952)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197.307, 
    farPlane=227.054, width=204.57, height=105.88, viewOffsetX=53.3217, 
    viewOffsetY=-0.357045)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.424, 
    farPlane=227.937, width=203.655, height=105.406, viewOffsetX=53.0831, 
    viewOffsetY=10.0187)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.494, 
    farPlane=227.866, width=203.728, height=105.444, viewOffsetX=51.1814, 
    viewOffsetY=5.28181)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197.431, 
    farPlane=226.93, width=180.872, height=93.6147, viewOffsetX=45.1458, 
    viewOffsetY=8.95818)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
p = mdb.models['Model-1'].parts['cabeça-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['cabeça-implante-1'].edges
a.ReferencePoint(point=a.instances['cabeça-implante-1'].InterestingPoint(
    edge=e11[3], rule=CENTER))
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['cabeça-implante-1'].edges
a.ReferencePoint(point=a.instances['cabeça-implante-1'].InterestingPoint(
    edge=e21[4], rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['BLAH-osso-cut-imp-dim-1'].edges
a.ReferencePoint(point=a.instances['BLAH-osso-cut-imp-dim-1'].InterestingPoint(
    edge=e11[25], rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=209.227, 
    farPlane=215.133, width=36.0602, height=18.6638, viewOffsetX=8.4846, 
    viewOffsetY=41.5702)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[286], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-91')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-41')
mdb.models['Model-1'].Coupling(name='Constraint-4', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=210.477, 
    farPlane=213.884, width=20.7857, height=10.7581, viewOffsetX=29.4752, 
    viewOffsetY=37.5264)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[287], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-92')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['BLAH-osso-cut-imp-dim-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#2000000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-42')
mdb.models['Model-1'].Coupling(name='Constraint-5', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=208.153, 
    farPlane=216.207, width=55.5483, height=28.7503, viewOffsetX=45.0214, 
    viewOffsetY=40.3072)
session.viewports['Viewport: 1'].view.setValues(nearPlane=207.906, 
    farPlane=216.454, width=55.4824, height=28.7162, viewOffsetX=38.2027, 
    viewOffsetY=33.0367)
session.viewports['Viewport: 1'].view.setValues(nearPlane=206.729, 
    farPlane=217.632, width=75.1709, height=38.9065, viewOffsetX=46.2362, 
    viewOffsetY=34.2439)
session.viewports['Viewport: 1'].view.setValues(nearPlane=206.39, 
    farPlane=217.971, width=75.0477, height=38.8427, viewOffsetX=35.5943, 
    viewOffsetY=28.8546)
session.viewports['Viewport: 1'].view.setValues(nearPlane=204.364, 
    farPlane=219.997, width=107.717, height=55.7516, viewOffsetX=48.979, 
    viewOffsetY=30.2711)
session.viewports['Viewport: 1'].view.setValues(nearPlane=203.883, 
    farPlane=220.477, width=107.464, height=55.6205, viewOffsetX=40.0831, 
    viewOffsetY=27.2939)
session.viewports['Viewport: 1'].view.setValues(nearPlane=203.903, 
    farPlane=220.458, width=107.474, height=55.6259, viewOffsetX=36.9121, 
    viewOffsetY=28.6483)
session.viewports['Viewport: 1'].view.setValues(nearPlane=204.848, 
    farPlane=219.513, width=89.68, height=46.416, viewOffsetX=31.4322, 
    viewOffsetY=27.832)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[285], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-93')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-43')
mdb.models['Model-1'].Coupling(name='Constraint-6', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[285], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-94')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['BLAH-osso-cut-imp-dim-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#2000000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-44')
mdb.models['Model-1'].Coupling(name='Constraint-7', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=203.374, 
    farPlane=220.986, width=121.317, height=62.7905, viewOffsetX=45.4341, 
    viewOffsetY=28.8573)
session.viewports['Viewport: 1'].view.setValues(nearPlane=202.861, 
    farPlane=221.5, width=121.011, height=62.6319, viewOffsetX=29.7271, 
    viewOffsetY=18.3585)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201.025, 
    farPlane=223.336, width=153.59, height=79.4944, viewOffsetX=39.8294, 
    viewOffsetY=18.8915)
session.viewports['Viewport: 1'].view.setValues(nearPlane=200.35, 
    farPlane=224.01, width=153.075, height=79.2277, viewOffsetX=45.9496, 
    viewOffsetY=14.7849)
session.viewports['Viewport: 1'].view.setValues(width=143.919, height=74.4889, 
    viewOffsetX=43.6809, viewOffsetY=14.2766)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201.095, 
    farPlane=223.266, width=144.426, height=74.751, viewOffsetX=39.8405, 
    viewOffsetY=15.3259)
session.viewports['Viewport: 1'].view.setValues(nearPlane=200.35, 
    farPlane=224.01, width=162.846, height=84.285, viewOffsetX=45.6119, 
    viewOffsetY=18.7118)
session.viewports['Viewport: 1'].view.setValues(nearPlane=199.637, 
    farPlane=224.723, width=162.267, height=83.9851, viewOffsetX=43.0019, 
    viewOffsetY=6.19543)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197.25, 
    farPlane=227.111, width=205.35, height=106.284, viewOffsetX=53.991, 
    viewOffsetY=7.60141)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.364, 
    farPlane=227.997, width=204.428, height=105.806, viewOffsetX=55.2905, 
    viewOffsetY=14.3811)
session.viewports['Viewport: 1'].view.setValues(width=192.232, height=99.4941, 
    viewOffsetX=53.9801, viewOffsetY=14.3053)
session.viewports['Viewport: 1'].view.setValues(nearPlane=197.374, 
    farPlane=226.986, width=193.151, height=99.9698, viewOffsetX=51.9316, 
    viewOffsetY=8.05723)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[286], )
region = a.Set(referencePoints=refPoints1, name='Set-95')
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
    region=region, cf1=150.0, cf2=-259.0, distributionType=UNIFORM, field='', 
    localCsys=None)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[287], )
region = a.Set(referencePoints=refPoints1, name='Set-96')
mdb.models['Model-1'].ConcentratedForce(name='Load-2', createStepName='Step-1', 
    region=region, cf1=-50.0, cf2=89.0, distributionType=UNIFORM, field='', 
    localCsys=None)
session.viewports['Viewport: 1'].view.setValues(width=205.406, height=106.313, 
    viewOffsetX=56.5105, viewOffsetY=7.94197)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['BLAH-osso-cut-imp-dim-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#800000 ]', ), )
region = a.Set(edges=edges1, name='Set-97')
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(width=217.472, height=112.558, 
    viewOffsetX=61.5997, viewOffsetY=8.26914)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['cabeça-implante-1'], 
    a.instances['haste-implante-Copy-1'], 
    a.instances['BLAH-osso-cut-imp-dim-1'], )
a.seedPartInstance(regions=partInstances, size=1.5, deviationFactor=0.1, 
    minSizeFactor=0.1)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
f2 = a.instances['haste-implante-Copy-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#1 ]', ), )
f3 = a.instances['BLAH-osso-cut-imp-dim-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#1f ]', ), )
pickedRegions = faces1+faces2+faces3
a.setMeshControls(regions=pickedRegions, elemShape=QUAD)
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
f2 = a.instances['haste-implante-Copy-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#1 ]', ), )
f3 = a.instances['BLAH-osso-cut-imp-dim-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#1f ]', ), )
pickedRegions =((faces1+faces2+faces3), )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['cabeça-implante-1'], 
    a.instances['haste-implante-Copy-1'], 
    a.instances['BLAH-osso-cut-imp-dim-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=193.365, 
    farPlane=230.995, width=257.838, height=133.786, viewOffsetX=109.401, 
    viewOffsetY=12.6892)
session.viewports['Viewport: 1'].view.setValues(nearPlane=192.384, 
    farPlane=231.977, width=256.529, height=133.107, viewOffsetX=80.0733, 
    viewOffsetY=1.78864)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='BLAH-reduced-imp', model='Model-1', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.474, 
    farPlane=227.886, width=217.599, height=112.907, viewOffsetX=64.3993, 
    viewOffsetY=0.500908)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['BLAH-osso-cut-imp-dim-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0:109 #40000000 #0:10 #100 ]', ), )
n2 = a.instances['haste-implante-Copy-1'].nodes
nodes2 = n2.getSequenceFromMask(mask=('[#0:19 #1 ]', ), )
n3 = a.instances['cabeça-implante-1'].nodes
nodes3 = n3.getSequenceFromMask(mask=('[#0:43 #8000000 ]', ), )
a.Set(nodes=nodes1+nodes2+nodes3, name='BLAH-pontos')
#: The set 'BLAH-pontos' has been created (4 nodes).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['Model-1'].parts['cabeça-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['haste-implante-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['haste-implante-Copy']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['haste-implante-Copy']
p.SectionAssignment(region=region, sectionName='Tit-imp-sect', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=85.1865, 
    farPlane=95.8031, width=73.2469, height=37.9107, viewOffsetX=3.33801, 
    viewOffsetY=0.0091908)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['BLAH-reduced-imp'].submit(consistencyChecking=OFF)
#: The job input file "BLAH-reduced-imp.inp" has been submitted for analysis.
#: Job BLAH-reduced-imp: Analysis Input File Processor completed successfully.
#: Job BLAH-reduced-imp: Abaqus/Standard completed successfully.
#: Job BLAH-reduced-imp completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/BLAH-bonebase.odb'])
o3 = session.openOdb(name='C:/temp/BLAH-reduced-imp.odb')
#: Model: C:/temp/BLAH-reduced-imp.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             4
#: Number of Element Sets:       7
#: Number of Node Sets:          18
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=226.706, 
    farPlane=358.323, width=191.199, height=98.9596, viewOffsetX=4.83343, 
    viewOffsetY=-1.08379)
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.925, 
    farPlane=359.104, width=190.54, height=98.6187, viewOffsetX=36.6733, 
    viewOffsetY=-12.1043)
session.viewports['Viewport: 1'].view.setValues(width=202.7, height=104.912, 
    viewOffsetX=39.4438, viewOffsetY=-12.7275)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.985, 
    farPlane=360.044, width=201.859, height=104.477, viewOffsetX=56.5354, 
    viewOffsetY=-7.21601)
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.05, 
    farPlane=359.98, width=201.917, height=104.507, viewOffsetX=59.2169, 
    viewOffsetY=-7.85301)
session.printToFile(fileName='BLAH-reduced-imp-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
leaf = dgo.LeafFromNodeSets(nodeSets=("BLAH-PONTOS", ))
dg = session.DisplayGroup(leaf=leaf, name='DisplayGroup-3')
#: The selected probe values were written to file "C:/temp/blah-reducedimp-sm.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#: The selected probe values were written to file "C:/temp/blah-reducedimp-u.rpt".
session.printToFile(fileName='BLAH-reduced-imp-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('osso-divided-1', 'cabeça-implante-1', 
    'haste-implante-Copy-1', 'BLAH-osso-cut-imp-dim-1', 'RP-2', 'RP-1', 
    'Partition edge-4', 'Partition edge-3', 'Partition face-1', 'RP-3', 
    'Partition edge-2', 'Partition edge-1', 'Partition face-1', 
    'Partition face-1', ))
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['imp-osso']
a1.Instance(name='imp-osso-1', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['implante-2-Copy4']
a1.Instance(name='implante-2-Copy4-1', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy4-1', ), vector=(13.871379, 
    -5.815267, 0.0))
#: The instance implante-2-Copy4-1 was translated by 13.871379, -5.815267, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(width=179.244, height=92.7722, 
    viewOffsetX=2.35511, viewOffsetY=-0.377747)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
mdb.models['Model-1'].constraints.delete(('Constraint-1', 'Constraint-2', 
    'Constraint-3', 'Constraint-4', 'Constraint-5', 'Constraint-6', 
    'Constraint-7', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
mdb.models['Model-1'].loads.delete(('Load-1', 'Load-2', ))
del mdb.models['Model-1'].boundaryConditions['BC-1']
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.594, 
    farPlane=252.186, width=218.22, height=112.945, viewOffsetX=14.4675, 
    viewOffsetY=1.54761)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.801, 
    farPlane=246.979, width=154.163, height=79.7906, viewOffsetX=30.5444, 
    viewOffsetY=9.35531)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'imp-osso-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'implante-2-Copy4-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'imp-osso-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.437, 
    farPlane=244.343, width=121.793, height=63.0368, viewOffsetX=32.208, 
    viewOffsetY=11.8863)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['implante-2-Copy4-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#14000 ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-45')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['imp-osso-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#122040 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-45')
mdb.models['Model-1'].Tie(name='Constraint-1', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.445, 
    farPlane=246.335, width=164.479, height=85.1301, viewOffsetX=45.3684, 
    viewOffsetY=15.947)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'implante-2-Copy4-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'imp-osso-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.01, 
    farPlane=243.77, width=114.778, height=59.4059, viewOffsetX=30.2098, 
    viewOffsetY=13.7163)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'implante-2-Copy4-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'imp-osso-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['implante-2-Copy4-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#3ffe ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-47')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['imp-osso-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#3e81c3f ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-47')
mdb.models['Model-1'].Tie(name='Constraint-2', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'implante-2-Copy4-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.009, 
    farPlane=243.771, width=114.777, height=59.4056, viewOffsetX=30.2118, 
    viewOffsetY=20.2001)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.makeIndependent(instances=(a1.instances['imp-osso-1'], ))
a1 = mdb.models['Model-1'].rootAssembly
a1.makeIndependent(instances=(a1.instances['implante-2-Copy4-1'], ))
session.viewports['Viewport: 1'].view.setValues(width=122.397, height=63.3492, 
    viewOffsetX=33.5178, viewOffsetY=19.9369)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['implante-2-Copy4-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#8000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.721443606823772)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['implante-2-Copy4-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#10000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.843522483592236)
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.915, 
    farPlane=239.865, width=66.9084, height=34.63, viewOffsetX=33.3129, 
    viewOffsetY=24.4478)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['imp-osso-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#10000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.836716351180651)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['imp-osso-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#20000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.332143676865156)
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.509, 
    farPlane=243.27, width=122.375, height=63.338, viewOffsetX=54.8052, 
    viewOffsetY=33.0237)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.987, 
    farPlane=243.793, width=122.091, height=63.1913, viewOffsetX=32.8076, 
    viewOffsetY=14.9035)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.385, 
    farPlane=244.394, width=137.806, height=71.3245, viewOffsetX=36.521, 
    viewOffsetY=14.7376)
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.775, 
    farPlane=245.004, width=137.431, height=71.1306, viewOffsetX=36.5944, 
    viewOffsetY=20.056)
session.viewports['Viewport: 1'].view.setValues(width=129.202, height=66.8716, 
    viewOffsetX=34.4558, viewOffsetY=19.9316)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['implante-2-Copy4-1'].edges
a.ReferencePoint(point=a.instances['implante-2-Copy4-1'].InterestingPoint(
    edge=e21[16], rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['implante-2-Copy4-1'].edges
a.ReferencePoint(point=a.instances['implante-2-Copy4-1'].InterestingPoint(
    edge=e11[15], rule=CENTER))
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['imp-osso-1'].edges
a.ReferencePoint(point=a.instances['imp-osso-1'].InterestingPoint(edge=e21[17], 
    rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=232.053, 
    farPlane=236.726, width=28.5224, height=14.7624, viewOffsetX=3.22111, 
    viewOffsetY=39.7293)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[317], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-101')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['implante-2-Copy4-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#10000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-49')
mdb.models['Model-1'].Coupling(name='Constraint-3', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.404, 
    farPlane=243.376, width=123.825, height=64.0887, viewOffsetX=11.416, 
    viewOffsetY=53.8511)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.875, 
    farPlane=243.904, width=123.535, height=63.9385, viewOffsetX=34.8384, 
    viewOffsetY=30.8842)
session.viewports['Viewport: 1'].view.setValues(nearPlane=231.717, 
    farPlane=237.062, width=32.6302, height=16.8885, viewOffsetX=34.279, 
    viewOffsetY=31.4873)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[319], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-102')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['imp-osso-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#20000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-50')
mdb.models['Model-1'].Coupling(name='Constraint-4', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=230.972, 
    farPlane=237.807, width=47.1471, height=24.4021, viewOffsetX=40.0139, 
    viewOffsetY=33.7625)
session.viewports['Viewport: 1'].view.setValues(nearPlane=230.761, 
    farPlane=238.019, width=47.1039, height=24.3798, viewOffsetX=27.2169, 
    viewOffsetY=25.052)
session.viewports['Viewport: 1'].view.setValues(nearPlane=230.761, 
    farPlane=238.019, width=47.1039, height=24.3798, viewOffsetX=20.7627, 
    viewOffsetY=24.7261)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.467, 
    farPlane=239.312, width=67.8967, height=35.1416, viewOffsetX=24.7034, 
    viewOffsetY=26.1523)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.16, 
    farPlane=239.62, width=67.8057, height=35.0945, viewOffsetX=22.241, 
    viewOffsetY=25.8614)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.167, 
    farPlane=239.613, width=67.8076, height=35.0955, viewOffsetX=20.1533, 
    viewOffsetY=25.7768)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[318], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-103')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['implante-2-Copy4-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#10000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-51')
mdb.models['Model-1'].Coupling(name='Constraint-5', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[318], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-104')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['imp-osso-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#20000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-52')
mdb.models['Model-1'].Coupling(name='Constraint-6', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220.747, 
    farPlane=248.032, width=187.768, height=97.1838, viewOffsetX=65.9695, 
    viewOffsetY=38.0029)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.981, 
    farPlane=248.798, width=187.117, height=96.8466, viewOffsetX=37.6319, 
    viewOffsetY=12.5709)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.058, 
    farPlane=249.721, width=210.878, height=109.145, viewOffsetX=42.0639, 
    viewOffsetY=14.193)
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.148, 
    farPlane=250.632, width=210.002, height=108.691, viewOffsetX=41.6251, 
    viewOffsetY=3.17248)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.061, 
    farPlane=249.718, width=210.881, height=109.147, viewOffsetX=41.9621, 
    viewOffsetY=3.08423)
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.215, 
    farPlane=250.564, width=210.067, height=108.725, viewOffsetX=29.5208, 
    viewOffsetY=3.73285)
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.21, 
    farPlane=250.569, width=210.062, height=108.723, viewOffsetX=34.9334, 
    viewOffsetY=-1.41933)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220.03, 
    farPlane=248.75, width=175.93, height=91.0567, viewOffsetX=26.5298, 
    viewOffsetY=1.7847)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220.839, 
    farPlane=247.94, width=176.577, height=91.3916, viewOffsetX=27.2933, 
    viewOffsetY=-0.651769)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[317], )
region = a.Set(referencePoints=refPoints1, name='Set-105')
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
    region=region, cf1=150.0, cf2=-259.0, distributionType=UNIFORM, field='', 
    localCsys=None)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[319], )
region = a.Set(referencePoints=refPoints1, name='Set-106')
mdb.models['Model-1'].ConcentratedForce(name='Load-2', createStepName='Step-1', 
    region=region, cf1=-50.0, cf2=89.0, distributionType=UNIFORM, field='', 
    localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220.742, 
    farPlane=248.037, width=187.765, height=97.1824, viewOffsetX=28.2043, 
    viewOffsetY=3.20657)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['imp-osso-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#8000 ]', ), )
region = a.Set(edges=edges1, name='Set-107')
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.147, 
    farPlane=250.632, width=223.407, height=115.63, viewOffsetX=36.7144, 
    viewOffsetY=7.02492)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.259, 
    farPlane=251.521, width=222.497, height=115.159, viewOffsetX=28.1741, 
    viewOffsetY=-7.83578)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.253, 
    farPlane=251.527, width=222.491, height=115.156, viewOffsetX=34.0467, 
    viewOffsetY=-6.29641)
p = mdb.models['Model-1'].parts['haste-implante-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[1].setValues(
    sectionName='Tit-imp-sect')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='BLAH-implant-base', model='Model-1', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['imp-osso-1'], a.instances['implante-2-Copy4-1'], )
a.seedPartInstance(regions=partInstances, size=1.5, deviationFactor=0.1, 
    minSizeFactor=0.1)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['imp-osso-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#f ]', ), )
f2 = a.instances['implante-2-Copy4-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions = faces1+faces2
a.setMeshControls(regions=pickedRegions, elemShape=QUAD)
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['imp-osso-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#f ]', ), )
f2 = a.instances['implante-2-Copy4-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =((faces1+faces2), )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['imp-osso-1'], a.instances['implante-2-Copy4-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['BLAH-implant-base'].submit(consistencyChecking=OFF)
#: The job input file "BLAH-implant-base.inp" has been submitted for analysis.
#: Job BLAH-implant-base: Analysis Input File Processor completed successfully.
#: Job BLAH-implant-base: Abaqus/Standard completed successfully.
#: Job BLAH-implant-base completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/BLAH-reduced-imp.odb'])
o3 = session.openOdb(name='C:/temp/BLAH-implant-base.odb')
#: Model: C:/temp/BLAH-implant-base.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       22
#: Number of Node Sets:          32
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=230.131, 
    farPlane=361.206, width=182.222, height=94.3135, viewOffsetX=3.53688, 
    viewOffsetY=-1.1715)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.38, 
    farPlane=361.956, width=181.628, height=94.006, viewOffsetX=50.2167, 
    viewOffsetY=-7.22154)
session.printToFile(fileName='BLAH-base-imp-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='BLAH-base-imp-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.018, 
    farPlane=249.761, width=186.299, height=96.6664, viewOffsetX=29.0399, 
    viewOffsetY=-6.09657)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['imp-osso-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0:92 #2000 #0:7 #2000 ]', ), )
n2 = a.instances['implante-2-Copy4-1'].nodes
nodes2 = n2.getSequenceFromMask(mask=('[#0:10 #40000 #0:55 #10000 ]', ), )
a.Set(nodes=nodes1+nodes2, name='BLAH-pontos-mat')
#: The set 'BLAH-pontos-mat' has been created (4 nodes).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['BLAH-implant-base'].submit(consistencyChecking=OFF)
#: The job input file "BLAH-implant-base.inp" has been submitted for analysis.
#: Job BLAH-implant-base: Analysis Input File Processor completed successfully.
#: Job BLAH-implant-base: Abaqus/Standard completed successfully.
#: Job BLAH-implant-base completed successfully. 
o3 = session.openOdb(name='C:/temp/BLAH-reduced-imp.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(width=199.617, height=103.317, 
    viewOffsetX=33.0412, viewOffsetY=-5.56388)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/BLAH-reduced-imp.odb'])
o3 = session.openOdb(name='C:/temp/bone-imp-base.odb')
#: Model: C:/temp/bone-imp-base.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       16
#: Number of Node Sets:          27
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/bone-imp-base.odb'])
o3 = session.openOdb(name='C:/temp/BLAH-implant-base.odb')
#: Model: C:/temp/BLAH-implant-base.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       22
#: Number of Node Sets:          33
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.332, 
    farPlane=362.005, width=193.181, height=99.9852, viewOffsetX=1.71582, 
    viewOffsetY=-1.81904)
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[1].setValues(
    sectionName='CoCr-imp-section')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='BLAH-CoCr', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['BLAH-CoCr'].submit(consistencyChecking=OFF)
#: The job input file "BLAH-CoCr.inp" has been submitted for analysis.
#: Job BLAH-CoCr: Analysis Input File Processor completed successfully.
#: Job BLAH-CoCr: Abaqus/Standard completed successfully.
#: Job BLAH-CoCr completed successfully. 
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
odb = session.odbs['C:/temp/BLAH-implant-base.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/BLAH-implant-base.odb'])
o3 = session.openOdb(name='C:/temp/BLAH-CoCr.odb')
#: Model: C:/temp/BLAH-CoCr.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       22
#: Number of Node Sets:          33
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=230.152, 
    farPlane=361.184, width=182.239, height=94.3223, viewOffsetX=3.59095, 
    viewOffsetY=-1.96172)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.374, 
    farPlane=361.962, width=181.623, height=94.0035, viewOffsetX=48.2141, 
    viewOffsetY=-7.66612)
session.printToFile(fileName='BLAH-CoCr-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='BLAH-CoCr-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
leaf = dgo.LeafFromNodeSets(nodeSets=("BLAH-PONTOS-MAT", ))
dg = session.DisplayGroup(leaf=leaf, name='DisplayGroup-4')
#: The selected probe values were written to file "C:/temp/blah-CoCr-u.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#: The selected probe values were written to file "C:/temp/blah-CoCr-sm.rpt".
odb = session.odbs['C:/temp/BLAH-implant-base.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.542, 
    farPlane=362.794, width=192.516, height=99.6411, viewOffsetX=55.5562, 
    viewOffsetY=-8.71379)
#: The selected probe values were written to file "C:/temp/blah-baseimp-sm.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#: The selected probe values were written to file "C:/temp/blah-baseimp-u.rpt".
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[0].setValues(
    sectionName='Tit-imp-sect')
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[1].setValues(
    sectionName='Tit-imp-sect')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='BLAH-tit', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['BLAH-tit'].submit(consistencyChecking=OFF)
#: The job input file "BLAH-tit.inp" has been submitted for analysis.
#: Job BLAH-tit: Analysis Input File Processor completed successfully.
#: Job BLAH-tit: Abaqus/Standard completed successfully.
#: Job BLAH-tit completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/BLAH-implant-base.odb'])
o3 = session.openOdb(name='C:/temp/BLAH-tit.odb')
#: Model: C:/temp/BLAH-tit.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       22
#: Number of Node Sets:          33
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.567, 
    farPlane=361.769, width=170.87, height=88.4377, viewOffsetX=45.7514, 
    viewOffsetY=-8.16678)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.331, 
    farPlane=362.005, width=193.181, height=99.9852, viewOffsetX=53.0326, 
    viewOffsetY=-11.121)
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.487, 
    farPlane=362.849, width=192.469, height=99.6171, viewOffsetX=57.5553, 
    viewOffsetY=-7.69088)
session.printToFile(fileName='BLAH-tit-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
#: The selected probe values were written to file "C:/temp/blah-tit-sm.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#: The selected probe values were written to file "C:/temp/blah-tit-u.rpt".
session.printToFile(fileName='BLAH-tit-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[0].setValues(
    sectionName='sect-alumina')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='BLAH-Alumina', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['BLAH-Alumina'].submit(consistencyChecking=OFF)
#: The job input file "BLAH-Alumina.inp" has been submitted for analysis.
#: Job BLAH-Alumina: Analysis Input File Processor completed successfully.
#: Job BLAH-Alumina: Abaqus/Standard completed successfully.
#: Job BLAH-Alumina completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/BLAH-tit.odb'])
o3 = session.openOdb(name='C:/temp/BLAH-Alumina.odb')
#: Model: C:/temp/BLAH-Alumina.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       22
#: Number of Node Sets:          33
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=227.6, 
    farPlane=363.737, width=216.978, height=112.302, viewOffsetX=-4.58887, 
    viewOffsetY=-0.567485)
session.viewports['Viewport: 1'].view.setValues(nearPlane=226.659, 
    farPlane=364.678, width=216.081, height=111.838, viewOffsetX=62.3866, 
    viewOffsetY=-9.12623)
session.printToFile(fileName='BLAH-alumina-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='BLAH-alumina-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
#: The selected probe values were written to file "C:/temp/blah-alumina-u.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#: The selected probe values were written to file "C:/temp/blah-alumina-sm.rpt".
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[1].setValues(
    sectionName='steel-sect')
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[0].setValues(
    sectionName='CoCr-imp-section')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='BLAH-steel', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['BLAH-steel'].submit(consistencyChecking=OFF)
#: The job input file "BLAH-steel.inp" has been submitted for analysis.
#: Job BLAH-steel: Analysis Input File Processor completed successfully.
#: Job BLAH-steel: Abaqus/Standard completed successfully.
#: Job BLAH-steel completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/BLAH-Alumina.odb'])
o3 = session.openOdb(name='C:/temp/BLAH-steel.odb')
#: Model: C:/temp/BLAH-steel.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       22
#: Number of Node Sets:          33
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.563, 
    farPlane=361.774, width=170.866, height=88.4359, viewOffsetX=54.4495, 
    viewOffsetY=-7.52189)
session.viewports['Viewport: 1'].view.setValues(width=182.277, height=94.342, 
    viewOffsetX=57.8281, viewOffsetY=-8.6742)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.322, 
    farPlane=362.015, width=181.582, height=93.9818, viewOffsetX=48.7051, 
    viewOffsetY=-8.1843)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.375, 
    farPlane=361.961, width=181.624, height=94.0036, viewOffsetX=49.9721, 
    viewOffsetY=-7.95776)
session.printToFile(fileName='BLAH-steel-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='BLAH-steel-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
#: The selected probe values were written to file "C:/temp/blah-steel-u.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#: The selected probe values were written to file "C:/temp/blah-steel-sm.rpt".
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['osso-cut']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['osso-divided']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['haste-implante-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['BLAH-osso-cut-imp-dim']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['BLAH-osso-cut-imp-dim'].sectionAssignments[0].setValues(
    sectionName='osso-section', offsetType=MIDDLE_SURFACE, offsetField='', 
    offset=0.0)
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='CORT-steel', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['CORT-steel'].submit(consistencyChecking=OFF)
#: The job input file "CORT-steel.inp" has been submitted for analysis.
#: Job CORT-steel: Analysis Input File Processor completed successfully.
#: Job CORT-steel: Abaqus/Standard completed successfully.
#: Job CORT-steel completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/BLAH-steel.odb'])
o3 = session.openOdb(name='C:/temp/CORT-steel.odb')
#: Model: C:/temp/CORT-steel.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       22
#: Number of Node Sets:          33
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('implante-2-Copy4-1', 'RP-2', 'RP-1', 'Partition edge-2', 
    'Partition edge-1', ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('imp-osso-1', 'RP-3', 'Partition edge-4', 'Partition edge-3', 
    ))
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['osso-cut']
a1.Instance(name='osso-cut-1', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['implante-2-Copy4']
a1.Instance(name='implante-2-Copy4-1', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('implante-2-Copy4-1', ), vector=(13.496435, 
    -5.70859, 0.0))
#: The instance implante-2-Copy4-1 was translated by 13.496435, -5.70859, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
mdb.models['Model-1'].constraints.delete(('Constraint-1', 'Constraint-2', 
    'Constraint-3', 'Constraint-4', 'Constraint-5', 'Constraint-6', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
mdb.models['Model-1'].loads.delete(('Load-1', 'Load-2', ))
del mdb.models['Model-1'].boundaryConditions['BC-1']
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.366, 
    farPlane=245.414, width=134.957, height=69.85, viewOffsetX=16.7165, 
    viewOffsetY=6.6623)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'osso-cut-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'implante-2-Copy4-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'osso-cut-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['implante-2-Copy4-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#14000 ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-53')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['osso-cut-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#4001 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-53')
mdb.models['Model-1'].Tie(name='Constraint-1', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'implante-2-Copy4-1', ))
a = mdb.models['Model-1'].rootAssembly
a.features['osso-cut-1'].suppress()
a = mdb.models['Model-1'].rootAssembly
a.features['osso-cut-1'].resume()
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'implante-2-Copy4-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['implante-2-Copy4-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#3ffe ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-55')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['osso-cut-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#3ffe ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-55')
mdb.models['Model-1'].Tie(name='Constraint-2', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'implante-2-Copy4-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.63, 
    farPlane=246.15, width=161.949, height=83.8205, viewOffsetX=13.352, 
    viewOffsetY=1.6088)
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.957, 
    farPlane=246.822, width=161.459, height=83.5672, viewOffsetX=33.2024, 
    viewOffsetY=2.0101)
session.viewports['Viewport: 1'].view.setValues(width=151.77, height=78.5524, 
    viewOffsetX=31.3663, viewOffsetY=3.41436)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.701, 
    farPlane=246.079, width=152.281, height=78.8165, viewOffsetX=34.726, 
    viewOffsetY=11.183)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.662, 
    farPlane=246.118, width=152.254, height=78.8026, viewOffsetX=33.7629, 
    viewOffsetY=11.181)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.makeIndependent(instances=(a1.instances['implante-2-Copy4-1'], ))
a1 = mdb.models['Model-1'].rootAssembly
a1.makeIndependent(instances=(a1.instances['osso-cut-1'], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.667, 
    farPlane=240.112, width=69.9502, height=36.2044, viewOffsetX=15.4541, 
    viewOffsetY=28.4414)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['implante-2-Copy4-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#8000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.72370449598439)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['implante-2-Copy4-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#10000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.863684242117237)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.897, 
    farPlane=238.883, width=54.9071, height=28.4185, viewOffsetX=19.4615, 
    viewOffsetY=28.5213)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['osso-cut-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#20000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.822212027643138)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['osso-cut-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#40000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.299465079203775)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.508, 
    farPlane=252.271, width=245.863, height=127.252, viewOffsetX=51.713, 
    viewOffsetY=30.7932)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215.546, 
    farPlane=253.233, width=244.771, height=126.687, viewOffsetX=40.4062, 
    viewOffsetY=0.177663)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215.538, 
    farPlane=253.241, width=244.762, height=126.683, viewOffsetX=36.251, 
    viewOffsetY=-0.130194)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.646, 
    farPlane=251.134, width=205.284, height=106.25, viewOffsetX=27.1441, 
    viewOffsetY=0.69802)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['implante-2-Copy4-1'].edges
a.ReferencePoint(point=a.instances['implante-2-Copy4-1'].InterestingPoint(
    edge=e11[16], rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['implante-2-Copy4-1'].edges
a.ReferencePoint(point=a.instances['implante-2-Copy4-1'].InterestingPoint(
    edge=e21[15], rule=CENTER))
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['osso-cut-1'].edges
a.ReferencePoint(point=a.instances['osso-cut-1'].InterestingPoint(edge=e11[18], 
    rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.477, 
    farPlane=244.303, width=121.319, height=62.7913, viewOffsetX=41.3646, 
    viewOffsetY=14.5047)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[348], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-111')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['implante-2-Copy4-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#10000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-57')
mdb.models['Model-1'].Coupling(name='Constraint-3', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[350], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-112')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['osso-cut-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#40000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-58')
mdb.models['Model-1'].Coupling(name='Constraint-4', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[349], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-113')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['implante-2-Copy4-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#10000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-59')
mdb.models['Model-1'].Coupling(name='Constraint-5', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[349], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-114')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['osso-cut-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#40000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-60')
mdb.models['Model-1'].Coupling(name='Constraint-6', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220.908, 
    farPlane=247.872, width=185.618, height=96.0707, viewOffsetX=70.5082, 
    viewOffsetY=16.9188)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220.147, 
    farPlane=248.633, width=184.978, height=95.7398, viewOffsetX=58.1737, 
    viewOffsetY=11.393)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.471, 
    farPlane=246.309, width=145.946, height=75.5377, viewOffsetX=44.4462, 
    viewOffsetY=11.9546)
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.15, 
    farPlane=245.63, width=146.391, height=75.7682, viewOffsetX=44.9499, 
    viewOffsetY=8.6768)
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.117, 
    farPlane=245.662, width=146.37, height=75.757, viewOffsetX=43.1953, 
    viewOffsetY=3.88893)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.397, 
    farPlane=246.382, width=165.118, height=85.4605, viewOffsetX=50.6967, 
    viewOffsetY=1.80346)
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.673, 
    farPlane=247.106, width=164.58, height=85.1822, viewOffsetX=50.0144, 
    viewOffsetY=-2.03198)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[348], )
region = a.Set(referencePoints=refPoints1, name='Set-115')
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
    region=region, cf1=150.0, cf2=-259.0, distributionType=UNIFORM, field='', 
    localCsys=None)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[350], )
region = a.Set(referencePoints=refPoints1, name='Set-116')
mdb.models['Model-1'].ConcentratedForce(name='Load-2', createStepName='Step-1', 
    region=region, cf1=-50.0, cf2=89.0, distributionType=UNIFORM, field='', 
    localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.242, 
    farPlane=252.538, width=249.606, height=129.189, viewOffsetX=79.8518, 
    viewOffsetY=9.91949)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['osso-cut-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#10000 ]', ), )
region = a.Set(edges=edges1, name='Set-117')
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=211.607, 
    farPlane=257.172, width=312.849, height=161.923, viewOffsetX=106.401, 
    viewOffsetY=15.1206)
session.viewports['Viewport: 1'].view.setValues(nearPlane=210.445, 
    farPlane=258.335, width=311.13, height=161.033, viewOffsetX=97.0163, 
    viewOffsetY=-1.78974)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['osso-cut-1'], a.instances['implante-2-Copy4-1'], )
a.seedPartInstance(regions=partInstances, size=1.5, deviationFactor=0.1, 
    minSizeFactor=0.1)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['osso-cut-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
f2 = a.instances['implante-2-Copy4-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions = faces1+faces2
a.setMeshControls(regions=pickedRegions, elemShape=QUAD)
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['osso-cut-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
f2 = a.instances['implante-2-Copy4-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =((faces1+faces2), )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['osso-cut-1'], a.instances['implante-2-Copy4-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=213.027, 
    farPlane=255.753, width=261.59, height=135.733, viewOffsetX=75.8486, 
    viewOffsetY=-2.10914)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['CORT-steel'].submit(consistencyChecking=OFF)
#: The job input file "CORT-steel.inp" has been submitted for analysis.
#: Job CORT-steel: Analysis Input File Processor completed successfully.
#: Job CORT-steel: Abaqus/Standard completed successfully.
#: Job CORT-steel completed successfully. 
o3 = session.openOdb(name='C:/temp/CORT-steel.odb')
#: Model: C:/temp/CORT-steel.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       21
#: Number of Node Sets:          31
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.699, 
    farPlane=363.244, width=193.194, height=99.9923, viewOffsetX=5.59539, 
    viewOffsetY=-2.37306)
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.915, 
    farPlane=364.029, width=192.535, height=99.6508, viewOffsetX=48.2945, 
    viewOffsetY=-7.81366)
session.viewports['Viewport: 1'].view.setValues(width=204.821, height=106.01, 
    viewOffsetX=50.9316, viewOffsetY=-9.62589)
session.viewports['Viewport: 1'].view.setValues(nearPlane=227.965, 
    farPlane=364.978, width=203.975, height=105.572, viewOffsetX=54.6954, 
    viewOffsetY=-8.17505)
session.printToFile(fileName='CORT-steel-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='CORT-steel-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.366, 
    farPlane=251.414, width=235.849, height=122.377, viewOffsetX=64.7416, 
    viewOffsetY=-3.61637)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['osso-cut-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0:75 #20000 ]', ), )
n2 = a.instances['implante-2-Copy4-1'].nodes
nodes2 = n2.getSequenceFromMask(mask=('[#0:42 #1 #0:27 #40 ]', ), )
a.Set(nodes=nodes1+nodes2, name='CORT-point-ev')
#: The set 'CORT-point-ev' has been created (3 nodes).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['CORT-steel'].submit(consistencyChecking=OFF)
#: The job input file "CORT-steel.inp" has been submitted for analysis.
#: Job CORT-steel: Analysis Input File Processor completed successfully.
#: Job CORT-steel: Abaqus/Standard completed successfully.
#: Job CORT-steel completed successfully. 
o3 = session.openOdb(name='C:/temp/CORT-steel.odb')
#: Model: C:/temp/CORT-steel.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       21
#: Number of Node Sets:          32
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.943, 
    farPlane=363.001, width=170.887, height=88.4468, viewOffsetX=37.4857, 
    viewOffsetY=-7.84522)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.705, 
    farPlane=363.239, width=193.199, height=99.9945, viewOffsetX=42.0489, 
    viewOffsetY=-9.67472)
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.86, 
    farPlane=364.083, width=192.488, height=99.6269, viewOffsetX=55.8077, 
    viewOffsetY=-9.276)
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.915, 
    farPlane=364.029, width=192.534, height=99.6509, viewOffsetX=52.5537, 
    viewOffsetY=-7.70417)
leaf = dgo.LeafFromNodeSets(nodeSets=("CORT-POINT-EV", ))
dg = session.DisplayGroup(leaf=leaf, name='DisplayGroup-5')
#: The selected probe values were written to file "C:/temp/cort-steel-sm.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#: The selected probe values were written to file "C:/temp/cort-steel-u.rpt".
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[1].setValues(
    sectionName='CoCr-imp-section')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='CORT-CoCr', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['CORT-CoCr'].submit(consistencyChecking=OFF)
#: The job input file "CORT-CoCr.inp" has been submitted for analysis.
#: Job CORT-CoCr: Analysis Input File Processor completed successfully.
#: Job CORT-CoCr: Abaqus/Standard completed successfully.
#: Job CORT-CoCr completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/CORT-steel.odb'])
o3 = session.openOdb(name='C:/temp/CORT-CoCr.odb')
#: Model: C:/temp/CORT-CoCr.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       21
#: Number of Node Sets:          32
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=227.968, 
    farPlane=364.976, width=216.996, height=112.312, viewOffsetX=15.7187, 
    viewOffsetY=-3.72815)
session.viewports['Viewport: 1'].view.setValues(nearPlane=227.095, 
    farPlane=365.848, width=216.166, height=111.882, viewOffsetX=63.7558, 
    viewOffsetY=-6.70465)
session.viewports['Viewport: 1'].view.setValues(nearPlane=227.09, 
    farPlane=365.853, width=216.162, height=111.88, viewOffsetX=62.3959, 
    viewOffsetY=-6.9764)
session.viewports['Viewport: 1'].view.setValues(width=203.193, height=105.168, 
    viewOffsetX=58.903, viewOffsetY=-6.55636)
session.printToFile(fileName='CORT-CoCr-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=227.96, 
    farPlane=364.983, width=191.733, height=99.2361, viewOffsetX=54.4786, 
    viewOffsetY=-6.58532)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='CORT-CoCr-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
#: The selected probe values were written to file "C:/temp/cort-CoCr-u.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#: The selected probe values were written to file "C:/temp/cort-CoCr-sm.rpt".
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[1].setValues(
    sectionName='Tit-imp-sect')
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[0].setValues(
    sectionName='Tit-imp-sect')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='CORT-tit', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['CORT-tit'].submit(consistencyChecking=OFF)
#: The job input file "CORT-tit.inp" has been submitted for analysis.
#: Job CORT-tit: Analysis Input File Processor completed successfully.
#: Job CORT-tit: Abaqus/Standard completed successfully.
#: Job CORT-tit completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/CORT-CoCr.odb'])
o3 = session.openOdb(name='C:/temp/CORT-tit.odb')
#: Model: C:/temp/CORT-tit.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       21
#: Number of Node Sets:          32
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.956, 
    farPlane=362.987, width=170.897, height=88.4519, viewOffsetX=39.0991, 
    viewOffsetY=-6.34103)
session.viewports['Viewport: 1'].view.setValues(nearPlane=229.718, 
    farPlane=363.226, width=193.21, height=100, viewOffsetX=45.6105, 
    viewOffsetY=-7.67102)
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.874, 
    farPlane=364.07, width=192.5, height=99.6328, viewOffsetX=55.2432, 
    viewOffsetY=-7.88495)
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.928, 
    farPlane=364.015, width=192.546, height=99.6564, viewOffsetX=56.4665, 
    viewOffsetY=-7.76573)
session.printToFile(fileName='CORT-tit-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='CORT-tit-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
#: The selected probe values were written to file "C:/temp/cort-tit-u.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#: The selected probe values were written to file "C:/temp/cort-tit-sm.rpt".
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].parts['implante-2-Copy4'].sectionAssignments[0].setValues(
    sectionName='sect-alumina')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='CORT-alumina', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['CORT-alumina'].submit(consistencyChecking=OFF)
#: The job input file "CORT-alumina.inp" has been submitted for analysis.
#: Job CORT-alumina: Analysis Input File Processor completed successfully.
#: Job CORT-alumina: Abaqus/Standard completed successfully.
#: Job CORT-alumina completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/CORT-tit.odb'])
o3 = session.openOdb(name='C:/temp/CORT-alumina.odb')
#: Model: C:/temp/CORT-alumina.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       21
#: Number of Node Sets:          32
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=228.807, 
    farPlane=364.137, width=205.565, height=106.395, viewOffsetX=7.37049, 
    viewOffsetY=-3.25878)
session.viewports['Viewport: 1'].view.setValues(nearPlane=227.974, 
    farPlane=364.969, width=204.817, height=106.008, viewOffsetX=60.5111, 
    viewOffsetY=-6.98231)
session.printToFile(fileName='CORT-alumina-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='CORT-alumina-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#: The selected probe values were written to file "C:/temp/cort-alumina-sm.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#: The selected probe values were written to file "C:/temp/cort-alumina-u.rpt".
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('osso-cut-1', 'RP-3', 'Partition edge-4', 'Partition edge-3', 
    ))
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('implante-2-Copy4-1', 'RP-2', 'RP-1', 'Partition edge-2', 
    'Partition edge-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
mdb.models['Model-1'].constraints.delete(('Constraint-1', 'Constraint-2', 
    'Constraint-3', 'Constraint-4', 'Constraint-5', 'Constraint-6', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
del mdb.models['Model-1'].loads['Load-1']
del mdb.models['Model-1'].loads['Load-2']
del mdb.models['Model-1'].boundaryConditions['BC-1']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['osso']
a1.Instance(name='osso-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=195.846, 
    farPlane=221.901, width=181.555, height=93.968, viewOffsetX=0.558015, 
    viewOffsetY=-1.8531)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.959, 
    farPlane=222.788, width=180.733, height=93.5424, viewOffsetX=34.1802, 
    viewOffsetY=-2.64033)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.955, 
    farPlane=222.793, width=180.729, height=93.5403, viewOffsetX=30.658, 
    viewOffsetY=-2.29929)
a1 = mdb.models['Model-1'].rootAssembly
a1.makeIndependent(instances=(a1.instances['osso-1'], ))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['osso-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#2 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.521863051284112)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['osso-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#4 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.0956787337250094)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['osso-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#2 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.692706925754561)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['osso-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#4 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.211895011759906)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['osso-1'].edges
a.ReferencePoint(point=a.instances['osso-1'].InterestingPoint(edge=e21[4], 
    rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['osso-1'].edges
a.ReferencePoint(point=a.instances['osso-1'].InterestingPoint(edge=e11[2], 
    rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=197.22, 
    farPlane=220.528, width=142.743, height=73.8802, viewOffsetX=25.8366, 
    viewOffsetY=7.014)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['osso']
f, e2, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
    7.982133, 4.983682, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=204.04, gridSpacing=5.1, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['osso']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(width=188.826, height=97.7313, 
    cameraPosition=(7.29287, -0.30328, 204.041), cameraTarget=(7.29287, 
    -0.30328, 0))
s1.Line(point1=(-26.0684961894204, 5.1), point2=(24.2293252267945, 29.325))
s1.CoincidentConstraint(entity1=v[2], entity2=g[3], addUndoState=False)
s1.CoincidentConstraint(entity1=v[3], entity2=g[3], addUndoState=False)
p = mdb.models['Model-1'].parts['osso']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e, d1 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=195.786, 
    farPlane=221.961, width=160.373, height=83.0047, viewOffsetX=0.640188, 
    viewOffsetY=0.428103)
p = mdb.models['Model-1'].parts['osso']
f1, e2, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    10.809982, -5.105844, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=204.04, gridSpacing=5.1, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['osso']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
#: Warning: Coincident point selected
#: Warning: Coincident point selected
session.viewports['Viewport: 1'].view.setValues(nearPlane=177.82, 
    farPlane=191.572, width=83.9279, height=43.4388, cameraPosition=(7.66109, 
    12.7576, 184.696), cameraTarget=(7.66109, 12.7576, 0))
s.Spot(point=(-3.74743448131295, 27.302026))
s.CoincidentConstraint(entity1=v[4], entity2=g[2], addUndoState=False)
s.EqualDistanceConstraint(entity1=v[0], entity2=v[1], midpoint=v[4], 
    addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=166.869, 
    farPlane=202.523, width=246.247, height=127.451, cameraPosition=(63.3745, 
    19.0458, 184.696), cameraTarget=(63.3745, 19.0458, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(40.7773, 
    -0.621643, 184.696), cameraTarget=(40.7773, -0.621643, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=165.731, 
    farPlane=203.661, cameraPosition=(48.6708, 0.926971, 184.696), 
    cameraTarget=(48.6708, 0.926971, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=166.869, 
    farPlane=202.523, width=217.584, height=112.616, cameraPosition=(40.933, 
    4.46906, 184.696), cameraTarget=(40.933, 4.46906, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=167.939, 
    farPlane=201.453, cameraPosition=(40.2492, 2.82703, 184.696), 
    cameraTarget=(40.2492, 2.82703, 0))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
#* FeatureError: Regeneration failed
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.902, 
    farPlane=222.845, width=192.213, height=99.4844, viewOffsetX=44.9345, 
    viewOffsetY=0.765841)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('osso-1', 'RP-2', 'RP-1', 'Partition edge-4', 
    'Partition edge-3', 'Partition edge-2', 'Partition edge-1', ))
p1 = mdb.models['Model-1'].parts['haste-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].Part(name='haste-implante-Copy05', 
    objectToCopy=mdb.models['Model-1'].parts['haste-implante'], 
    compressFeatureList=ON, scale=0.5)
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['osso-divided']
a1.Instance(name='osso-divided-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['cabeça-implante']
a1.Instance(name='cabeça-implante-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['haste-implante-Copy05']
a1.Instance(name='haste-implante-Copy05-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(37.126767, 35.69015, 
    0.0))
#: The instance cabeça-implante-1 was translated by 37.126767, 35.69015, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.414, 
    farPlane=241.522, width=135.292, height=70.0235, viewOffsetX=7.91437, 
    viewOffsetY=7.92768)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-2.17159, -2.085075, 
    0.0))
#: The instance cabeça-implante-1 was translated by -2.17159, -2.085075, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-6.346478, 
    -6.100902, 0.0))
#: The instance cabeça-implante-1 was translated by -6.346478, -6.100902, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-5.0, 5.207462, 
    0.0))
#: The instance cabeça-implante-1 was translated by -5., 5.207462, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-0.851534, 
    -0.817609, 0.0))
#: The instance cabeça-implante-1 was translated by -851.534E-03, -817.609E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(width=144.343, height=74.7081, 
    viewOffsetX=8.77822, viewOffsetY=8.12211)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-1.887463, 
    -1.910996, 0.0))
#: The instance cabeça-implante-1 was translated by -1.887463, -1.910996, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.594, 
    farPlane=237.342, width=84.041, height=43.4974, viewOffsetX=3.7398, 
    viewOffsetY=9.23583)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-1.751251, 1.821743, 
    0.0))
#: The instance cabeça-implante-1 was translated by -1.751251, 1.821743, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.91, 
    farPlane=241.026, width=145.436, height=75.2738, viewOffsetX=14.3102, 
    viewOffsetY=4.44848)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-0.41288, 0.430011, 
    0.0))
#: The instance cabeça-implante-1 was translated by -412.88E-03, 430.011E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('haste-implante-Copy05-1', ), vector=(11.616684, 
    9.791408, 0.0))
#: The instance haste-implante-Copy05-1 was translated by 11.616684, 9.791408, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.947, 
    farPlane=242.989, width=173.537, height=89.8184, viewOffsetX=29.9958, 
    viewOffsetY=7.39271)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220.567, 
    farPlane=240.369, width=137.118, height=70.9688, viewOffsetX=35.8241, 
    viewOffsetY=14.9662)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'osso-divided-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
t = a.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    -3.717042, 30.056806, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=114.67, gridSpacing=2.86, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
a = mdb.models['Model-1'].rootAssembly
a.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=108.015, 
    farPlane=121.342, width=92.045, height=47.64, cameraPosition=(0.787438, 
    28.165, 114.679), cameraTarget=(0.787438, 28.165, 0))
s1.Line(point1=(-12.577387, -24.072022), point2=(-0.360481565713301, 
    -12.3278491532349))
s1.Line(point1=(12.3324748422126, -0.126045444388801), point2=(24.549379822928, 
    11.618128234392))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
pickedFaces = f1.getSequenceFromMask(mask=('[#1 ]', ), )
a.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'osso-divided-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.107, 
    farPlane=243.83, width=183.903, height=95.1831, viewOffsetX=56.0895, 
    viewOffsetY=20.4714)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
a1 = mdb.models['Model-1'].rootAssembly
a1.InstanceFromBooleanCut(name='Part-2', 
    instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['osso-divided-1'], 
    cuttingInstances=(a1.instances['haste-implante-Copy05-1'], 
    a1.instances['cabeça-implante-1'], ), originalInstances=SUPPRESS)
a = mdb.models['Model-1'].rootAssembly
a.features['cabeça-implante-1'].resume()
a = mdb.models['Model-1'].rootAssembly
a.features['haste-implante-Copy05-1'].resume()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.411, 
    farPlane=244.525, width=172.315, height=89.1855, viewOffsetX=51.4218, 
    viewOffsetY=20.162)
a1 = mdb.models['Model-1'].rootAssembly
a1.makeIndependent(instances=(a1.instances['Part-2-1'], ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Part-2-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.967, 
    farPlane=240.969, width=128.54, height=66.5291, viewOffsetX=30.3861, 
    viewOffsetY=21.8308)
a = mdb.models['Model-1'].rootAssembly
f21 = a.instances['cabeça-implante-1'].faces
t = a.MakeSketchTransform(sketchPlane=f21[0], sketchPlaneSide=SIDE1, origin=(
    -3.717042, 30.056806, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=114.67, gridSpacing=2.86, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
a = mdb.models['Model-1'].rootAssembly
a.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.Line(point1=(-12.4412637836467, -23.9411660581075), point2=(
    -0.360481565713301, -12.3278491532349))
s.Line(point1=(12.3324748422126, -0.126045444388801), point2=(24.549379822928, 
    11.618128234392))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
pickedFaces = f1.getSequenceFromMask(mask=('[#1 ]', ), )
a.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'Part-2-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'cabeça-implante-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#a ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-61')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-2-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#622 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-61')
mdb.models['Model-1'].Tie(name='Constraint-1', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].view.setValues(width=137.118, height=70.9688, 
    viewOffsetX=34.2516, viewOffsetY=22.8553)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Part-2-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'haste-implante-Copy05-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'Part-2-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['haste-implante-Copy05-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#3ffe ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-63')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-2-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#fff800 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-63')
mdb.models['Model-1'].Tie(name='Constraint-2', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.673, 
    farPlane=239.263, width=107.592, height=55.6866, viewOffsetX=26.9882, 
    viewOffsetY=20.3937)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'haste-implante-Copy05-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-65')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['haste-implante-Copy05-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-65')
mdb.models['Model-1'].Tie(name='Constraint-3', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.586, 
    farPlane=242.35, width=163.604, height=84.6769, viewOffsetX=52.433, 
    viewOffsetY=31.6743)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.908, 
    farPlane=243.028, width=163.096, height=84.4144, viewOffsetX=43.6595, 
    viewOffsetY=13.9342)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.104, 
    farPlane=243.832, width=183.901, height=95.1823, viewOffsetX=51.1714, 
    viewOffsetY=15.1876)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.356, 
    farPlane=244.58, width=183.267, height=94.8542, viewOffsetX=45.9266, 
    viewOffsetY=4.87761)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.353, 
    farPlane=244.584, width=183.264, height=94.8527, viewOffsetX=46.2714, 
    viewOffsetY=10.1791)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.947, 
    farPlane=242.989, width=153.338, height=79.3635, viewOffsetX=35.0826, 
    viewOffsetY=10.618)
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.658, 
    farPlane=242.279, width=153.838, height=79.6223, viewOffsetX=40.6118, 
    viewOffsetY=13.168)
session.viewports['Viewport: 1'].view.setValues(width=144.582, height=74.8318, 
    viewOffsetX=37.7594, viewOffsetY=13.3601)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.332, 
    farPlane=241.604, width=145.053, height=75.0758, viewOffsetX=35.3297, 
    viewOffsetY=14.4983)
session.viewports['Viewport: 1'].view.setValues(width=136.328, height=70.5596, 
    viewOffsetX=32.7614, viewOffsetY=14.619)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.968, 
    farPlane=240.969, width=136.745, height=70.7758, viewOffsetX=39.7378, 
    viewOffsetY=12.6859)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.936, 
    farPlane=241.001, width=136.725, height=70.7653, viewOffsetX=37.3257, 
    viewOffsetY=13.1999)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.937, 
    farPlane=240.999, width=136.726, height=70.7656, viewOffsetX=38.8727, 
    viewOffsetY=16.2094)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['cabeça-implante-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#10 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.743316281902921)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['cabeça-implante-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#20 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.853240172844233)
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.943, 
    farPlane=236.993, width=79.7703, height=41.287, viewOffsetX=37.4866, 
    viewOffsetY=22.7666)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-2-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#10 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.851684135970547)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-2-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#20 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.390877390296611)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.304, 
    farPlane=244.633, width=194.917, height=100.884, viewOffsetX=84.6837, 
    viewOffsetY=25.5444)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215.514, 
    farPlane=245.422, width=194.206, height=100.516, viewOffsetX=58.741, 
    viewOffsetY=25.2069)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.33, 
    farPlane=241.606, width=136.349, height=70.5708, viewOffsetX=41.1718, 
    viewOffsetY=29.479)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.966, 
    farPlane=240.97, width=136.745, height=70.7754, viewOffsetX=39.3144, 
    viewOffsetY=19.2449)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['cabeça-implante-1'].edges
a.ReferencePoint(point=a.instances['cabeça-implante-1'].InterestingPoint(
    edge=e1[4], rule=CENTER))
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['cabeça-implante-1'].edges
a.ReferencePoint(point=a.instances['cabeça-implante-1'].InterestingPoint(
    edge=e11[5], rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-2-1'].edges
a.ReferencePoint(point=a.instances['Part-2-1'].InterestingPoint(edge=e1[5], 
    rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.943, 
    farPlane=236.993, width=79.7709, height=41.2873, viewOffsetX=22.8037, 
    viewOffsetY=29.5873)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[396], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-121')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-67')
mdb.models['Model-1'].Coupling(name='Constraint-4', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.628, 
    farPlane=238.308, width=108.056, height=55.9268, viewOffsetX=38.7182, 
    viewOffsetY=30.9301)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.163, 
    farPlane=238.773, width=107.83, height=55.8099, viewOffsetX=34.3675, 
    viewOffsetY=24.2877)
session.viewports['Viewport: 1'].view.setValues(width=101.36, height=52.4612, 
    viewOffsetX=34.3369, viewOffsetY=24.8308)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[397], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-122')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-2-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-68')
mdb.models['Model-1'].Coupling(name='Constraint-5', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[395], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-123')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-69')
mdb.models['Model-1'].Coupling(name='Constraint-6', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[395], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-124')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-2-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-70')
mdb.models['Model-1'].Coupling(name='Constraint-7', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.249, 
    farPlane=244.688, width=195.666, height=101.272, viewOffsetX=70.5427, 
    viewOffsetY=36.7012)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215.457, 
    farPlane=245.479, width=194.95, height=100.901, viewOffsetX=54.3551, 
    viewOffsetY=7.01993)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215.453, 
    farPlane=245.484, width=194.946, height=100.899, viewOffsetX=54.109, 
    viewOffsetY=2.36103)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[396], )
region = a.Set(referencePoints=refPoints1, name='Set-125')
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
    region=region, cf1=150.0, cf2=-259.0, distributionType=UNIFORM, field='', 
    localCsys=None)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[397], )
region = a.Set(referencePoints=refPoints1, name='Set-126')
mdb.models['Model-1'].ConcentratedForce(name='Load-2', createStepName='Step-1', 
    region=region, cf1=-50.0, cf2=89.0, distributionType=UNIFORM, field='', 
    localCsys=None)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-2-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#8 ]', ), )
region = a.Set(edges=edges1, name='Set-127')
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=213.551, 
    farPlane=247.386, width=232.638, height=120.407, viewOffsetX=71.7026, 
    viewOffsetY=8.44993)
session.viewports['Viewport: 1'].view.setValues(nearPlane=212.634, 
    farPlane=248.302, width=231.639, height=119.89, viewOffsetX=55.8163, 
    viewOffsetY=-6.00813)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['haste-implante-Copy05']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['implante-2-Copy4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['haste-implante-Copy05']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['haste-implante-Copy05']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['haste-implante-Copy05']
p.SectionAssignment(region=region, sectionName='Tit-imp-sect', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['cabeça-implante']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['BLAH-osso-cut-imp-dim']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['osso-divided']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['cabeça-implante-1'], 
    a.instances['haste-implante-Copy05-1'], a.instances['Part-2-1'], )
a.seedPartInstance(regions=partInstances, size=1.5, deviationFactor=0.1, 
    minSizeFactor=0.1)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
f2 = a.instances['haste-implante-Copy05-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#1 ]', ), )
f3 = a.instances['Part-2-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#7 ]', ), )
pickedRegions = faces1+faces2+faces3
a.setMeshControls(regions=pickedRegions, elemShape=QUAD)
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
f2 = a.instances['haste-implante-Copy05-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#1 ]', ), )
f3 = a.instances['Part-2-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#7 ]', ), )
pickedRegions =((faces1+faces2+faces3), )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['cabeça-implante-1'], 
    a.instances['haste-implante-Copy05-1'], a.instances['Part-2-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='DIV-05imp', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['DIV-05imp'].submit(consistencyChecking=OFF)
#: The job input file "DIV-05imp.inp" has been submitted for analysis.
#: Job DIV-05imp: Analysis Input File Processor completed successfully.
#: Job DIV-05imp: Abaqus/Standard completed successfully.
#: Job DIV-05imp completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/CORT-alumina.odb'])
o3 = session.openOdb(name='C:/temp/DIV-05imp.odb')
#: Model: C:/temp/DIV-05imp.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             4
#: Number of Element Sets:       6
#: Number of Node Sets:          17
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.055, 
    farPlane=361.011, width=227.87, height=117.939, viewOffsetX=15.3599, 
    viewOffsetY=-0.94298)
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.148, 
    farPlane=361.918, width=226.947, height=117.462, viewOffsetX=55.666, 
    viewOffsetY=-8.21808)
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.142, 
    farPlane=361.924, width=226.941, height=117.459, viewOffsetX=60.7995, 
    viewOffsetY=-7.78969)
session.printToFile(fileName='DIV-05imp-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='DIV-05imp-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=212.683, 
    farPlane=248.253, width=246.481, height=127.894, viewOffsetX=62.972, 
    viewOffsetY=-7.50601)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-2-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0:72 #800000 #0:30 #100000 ]', ), )
n2 = a.instances['haste-implante-Copy05-1'].nodes
nodes2 = n2.getSequenceFromMask(mask=('[#0:8 #10 ]', ), )
n3 = a.instances['cabeça-implante-1'].nodes
nodes3 = n3.getSequenceFromMask(mask=('[#0:43 #8000000 ]', ), )
a.Set(nodes=nodes1+nodes2+nodes3, name='DIV-05imp')
#: The set 'DIV-05imp' has been created (4 nodes).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['DIV-05imp'].submit(consistencyChecking=OFF)
#: The job input file "DIV-05imp.inp" has been submitted for analysis.
#: Job DIV-05imp: Analysis Input File Processor completed successfully.
#: Job DIV-05imp: Abaqus/Standard completed successfully.
#: Job DIV-05imp completed successfully. 
o3 = session.openOdb(name='C:/temp/DIV-05imp.odb')
#: Model: C:/temp/DIV-05imp.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             4
#: Number of Element Sets:       6
#: Number of Node Sets:          18
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
leaf = dgo.LeafFromNodeSets(nodeSets=("DIV-05IMP", ))
dg = session.DisplayGroup(leaf=leaf, name='DisplayGroup-6')
#: The selected probe values were written to file "C:/temp/div-05imp-sm.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#: The selected probe values were written to file "C:/temp/div-05imp-u.rpt".
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('osso-divided-1', 'cabeça-implante-1', 
    'haste-implante-Copy05-1', 'Part-2-1', 'RP-3', 'Partition edge-4', 
    'Partition edge-3', 'Partition face-2', 'RP-2', 'RP-1', 'Partition edge-2', 
    'Partition edge-1', 'Partition face-2', 'Partition face-1', 
    'Partition face-2', 'Partition face-1', ))
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['osso-divided']
a1.Instance(name='osso-divided-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['cabeça-implante']
a1.Instance(name='cabeça-implante-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['haste-implante-Copy']
a1.Instance(name='haste-implante-Copy-1', part=p, dependent=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(18.563383, 
    17.845075, 0.0))
#: The instance cabeça-implante-1 was translated by 18.563383, 17.845075, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.742, 
    farPlane=239.194, width=106.75, height=55.2507, viewOffsetX=14.4459, 
    viewOffsetY=8.4246)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(4.459887, 4.430301, 
    0.0))
#: The instance cabeça-implante-1 was translated by 4.459887, 4.430301, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.678, 
    farPlane=242.258, width=143.445, height=74.2431, viewOffsetX=20.9063, 
    viewOffsetY=3.74581)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.382, 
    farPlane=241.554, width=143.906, height=74.4821, viewOffsetX=22.059, 
    viewOffsetY=19.324)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(9.527814, 9.148231, 
    0.0))
#: The instance cabeça-implante-1 was translated by 9.527814, 9.148231, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-2.831194, 
    -2.866495, 0.0))
#: The instance cabeça-implante-1 was translated by -2.831194, -2.866495, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-2.831194, 
    -2.866495, 0.0))
#: The instance cabeça-implante-1 was translated by -2.831194, -2.866495, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-7.5, 7.811193, 
    0.0))
#: The instance cabeça-implante-1 was translated by -7.5, 7.811193, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(-1.277301, 
    -1.226414, 0.0))
#: The instance cabeça-implante-1 was translated by -1.277301, -1.226414, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.171, 
    farPlane=237.766, width=89.2357, height=46.186, viewOffsetX=19.5818, 
    viewOffsetY=23.4756)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(0.61932, -0.645017, 
    0.0))
#: The instance cabeça-implante-1 was translated by 619.32E-03, -645.017E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(0.1, 0.1, 0.0))
#: The instance cabeça-implante-1 was translated by 100.E-03, 100.E-03, 0. with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('cabeça-implante-1', ), vector=(0.1, 0.1, 0.0))
#: The instance cabeça-implante-1 was translated by 100.E-03, 100.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.051, 
    farPlane=237.885, width=102.24, height=52.9167, viewOffsetX=48.0915, 
    viewOffsetY=36.0177)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.609, 
    farPlane=238.327, width=102.037, height=52.8118, viewOffsetX=33.8226, 
    viewOffsetY=26.5134)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.609, 
    farPlane=238.328, width=102.037, height=52.8117, viewOffsetX=29.1408, 
    viewOffsetY=22.3423)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.762, 
    farPlane=243.174, width=174.912, height=90.5299, viewOffsetX=47.8951, 
    viewOffsetY=26.0235)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('haste-implante-Copy-1', ), vector=(16.515692, 
    2.367778, 0.0))
#: The instance haste-implante-Copy-1 was translated by 16.515692, 2.367778, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=213.477, 
    farPlane=247.459, width=233.641, height=120.927, viewOffsetX=70.3742, 
    viewOffsetY=34.8882)
session.viewports['Viewport: 1'].view.setValues(nearPlane=212.558, 
    farPlane=248.379, width=232.635, height=120.406, viewOffsetX=55.5953, 
    viewOffsetY=11.0371)
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
session.viewports['Viewport: 1'].view.setValues(nearPlane=214.556, 
    farPlane=246.38, width=195.04, height=100.948, viewOffsetX=44.4194, 
    viewOffsetY=12.7977)
a1 = mdb.models['Model-1'].rootAssembly
a1.InstanceFromBooleanCut(name='Part-3', 
    instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['osso-divided-1'], 
    cuttingInstances=(a1.instances['haste-implante-Copy-1'], 
    a1.instances['cabeça-implante-1'], ), originalInstances=SUPPRESS)
a = mdb.models['Model-1'].rootAssembly
a.features['haste-implante-Copy-1'].resume()
a = mdb.models['Model-1'].rootAssembly
a.features['cabeça-implante-1'].resume()
a1 = mdb.models['Model-1'].rootAssembly
a1.makeIndependent(instances=(a1.instances['Part-3-1'], ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
mdb.models['Model-1'].constraints.delete(('Constraint-1', 'Constraint-2', 
    'Constraint-3', 'Constraint-4', 'Constraint-5', 'Constraint-6', 
    'Constraint-7', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
mdb.models['Model-1'].loads.delete(('Load-1', 'Load-2', ))
del mdb.models['Model-1'].boundaryConditions['BC-1']
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.818, 
    farPlane=241.118, width=146.651, height=75.9026, viewOffsetX=31.7557, 
    viewOffsetY=15.892)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
t = a.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    -3.491898, 29.652401, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=114.67, gridSpacing=2.86, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
a = mdb.models['Model-1'].rootAssembly
a.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=111.428, 
    farPlane=117.93, width=44.8924, height=23.2351, cameraPosition=(-11.4248, 
    11.9943, 114.679), cameraTarget=(-11.4248, 11.9943, 0))
s1.Line(point1=(-12.577387, -24.072022), point2=(-3.53372134856995, 
    -15.3782997298523))
session.viewports['Viewport: 1'].view.setValues(nearPlane=103.974, 
    farPlane=125.384, width=147.855, height=76.5258, cameraPosition=(-29.6079, 
    4.95208, 114.679), cameraTarget=(-29.6079, 4.95208, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(17.8803, 
    43.1685, 114.679), cameraTarget=(17.8803, 43.1685, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=103.291, 
    farPlane=126.067, cameraPosition=(23.735, 35.4508, 114.679), cameraTarget=(
    23.735, 35.4508, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=111.164, 
    farPlane=118.194, width=42.8936, height=22.2006, cameraPosition=(20.3722, 
    37.6892, 114.679), cameraTarget=(20.3722, 37.6892, 0))
s1.Line(point1=(15.5057132633189, 2.9244058334168), point2=(24.549379822928, 
    11.618128234392))
session.viewports['Viewport: 1'].view.setValues(nearPlane=110.177, 
    farPlane=119.181, width=62.1764, height=32.1809, cameraPosition=(23.3739, 
    39.8437, 114.679), cameraTarget=(23.3739, 39.8437, 0))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
pickedFaces = f1.getSequenceFromMask(mask=('[#1 ]', ), )
a.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(width=155.554, height=80.5104, 
    viewOffsetX=35.2379, viewOffsetY=17.3743)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Part-3-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'Part-3-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'cabeça-implante-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#5 ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-71')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-3-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#2220004 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-71')
mdb.models['Model-1'].Tie(name='Constraint-1', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.878, 
    farPlane=241.058, width=129.616, height=67.0859, viewOffsetX=31.8929, 
    viewOffsetY=18.1535)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Part-3-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'Part-3-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'haste-implante-Copy-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.633, 
    farPlane=236.303, width=80.7185, height=41.7778, viewOffsetX=27.6135, 
    viewOffsetY=12.4792)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['haste-implante-Copy-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#3ffe ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-73')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-3-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1c11f9f9 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-73')
mdb.models['Model-1'].Tie(name='Constraint-2', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(width=85.7246, height=44.3688, 
    viewOffsetX=29.802, viewOffsetY=12.4272)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'haste-implante-Copy-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-75')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['haste-implante-Copy-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-75')
mdb.models['Model-1'].Tie(name='Constraint-3', main=region1, secondary=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, 
    constraintEnforcement=SURFACE_TO_SURFACE, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.821, 
    farPlane=241.116, width=146.653, height=75.9035, viewOffsetX=50.915, 
    viewOffsetY=14.5341)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.206, 
    farPlane=241.731, width=146.243, height=75.6913, viewOffsetX=47.8312, 
    viewOffsetY=2.44542)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'cabeça-implante-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.762, 
    farPlane=243.174, width=174.913, height=90.5303, viewOffsetX=55.9123, 
    viewOffsetY=-0.189016)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.043, 
    farPlane=243.893, width=174.335, height=90.2314, viewOffsetX=50.6872, 
    viewOffsetY=4.85491)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.04, 
    farPlane=243.896, width=174.333, height=90.2303, viewOffsetX=50.3579, 
    viewOffsetY=2.44286)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.184, 
    farPlane=244.753, width=196.52, height=101.714, viewOffsetX=59.3969, 
    viewOffsetY=-1.73101)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215.332, 
    farPlane=245.605, width=195.746, height=101.313, viewOffsetX=56.3331, 
    viewOffsetY=4.06161)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.292, 
    farPlane=244.644, width=196.619, height=101.765, viewOffsetX=56.3247, 
    viewOffsetY=4.63615)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215.392, 
    farPlane=245.544, width=195.801, height=101.341, viewOffsetX=51.2907, 
    viewOffsetY=2.89295)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215.455, 
    farPlane=245.481, width=184.107, height=95.2888, viewOffsetX=47.0992, 
    viewOffsetY=4.60372)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.288, 
    farPlane=244.648, width=184.818, height=95.6572, viewOffsetX=51.1148, 
    viewOffsetY=1.25085)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.288, 
    farPlane=244.648, width=173.729, height=89.9178, viewOffsetX=47.2848, 
    viewOffsetY=2.62817)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.087, 
    farPlane=243.849, width=174.371, height=90.25, viewOffsetX=49.2131, 
    viewOffsetY=6.58564)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.058, 
    farPlane=239.879, width=115.144, height=59.5955, viewOffsetX=34.872, 
    viewOffsetY=19.6007)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['cabeça-implante-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#8 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.742675111845416)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['cabeça-implante-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#10 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.854669773138499)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-3-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#1000000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.866068696877637)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-3-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#2000000 ]', ), )
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.307897069448421)
session.viewports['Viewport: 1'].view.setValues(nearPlane=211.342, 
    farPlane=249.594, width=262.849, height=136.044, viewOffsetX=80.8972, 
    viewOffsetY=6.70406)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['cabeça-implante-1'].edges
a.ReferencePoint(point=a.instances['cabeça-implante-1'].InterestingPoint(
    edge=e11[3], rule=CENTER))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-3-1'].edges
a.ReferencePoint(point=a.instances['Part-3-1'].InterestingPoint(edge=e1[25], 
    rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['cabeça-implante-1'].edges
a.ReferencePoint(point=a.instances['cabeça-implante-1'].InterestingPoint(
    edge=e11[4], rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.563, 
    farPlane=238.373, width=96.6821, height=50.0401, viewOffsetX=42.0101, 
    viewOffsetY=26.1544)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[436], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-131')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-77')
mdb.models['Model-1'].Coupling(name='Constraint-4', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[435], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-132')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-3-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#2000000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-78')
mdb.models['Model-1'].Coupling(name='Constraint-5', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[434], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-133')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['cabeça-implante-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-79')
mdb.models['Model-1'].Coupling(name='Constraint-6', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[434], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-134')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-3-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#2000000 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, name='s_Surf-80')
mdb.models['Model-1'].Coupling(name='Constraint-7', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=220.394, 
    farPlane=240.543, width=138.779, height=71.8285, viewOffsetX=53.0571, 
    viewOffsetY=29.7024)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.809, 
    farPlane=241.128, width=138.411, height=71.6379, viewOffsetX=40.9978, 
    viewOffsetY=17.8725)
session.viewports['Viewport: 1'].view.setValues(width=147.245, height=76.2099, 
    viewOffsetX=42.6606, viewOffsetY=18.3029)
session.viewports['Viewport: 1'].view.setValues(nearPlane=219.127, 
    farPlane=241.809, width=146.789, height=75.974, viewOffsetX=45.2964, 
    viewOffsetY=6.89173)
session.viewports['Viewport: 1'].view.setValues(width=156.183, height=80.8364, 
    viewOffsetX=47.4564, viewOffsetY=7.30831)
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.438, 
    farPlane=242.498, width=155.668, height=80.5695, viewOffsetX=46.8105, 
    viewOffsetY=5.42413)
session.viewports['Viewport: 1'].view.setValues(nearPlane=217.711, 
    farPlane=243.226, width=175.588, height=90.8797, viewOffsetX=52.5061, 
    viewOffsetY=7.05773)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.944, 
    farPlane=243.992, width=174.97, height=90.5597, viewOffsetX=52.3212, 
    viewOffsetY=0.10061)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.992, 
    farPlane=243.945, width=175.008, height=90.5796, viewOffsetX=50.7927, 
    viewOffsetY=0.650935)
session.viewports['Viewport: 1'].view.setValues(nearPlane=216.989, 
    farPlane=243.948, width=175.005, height=90.5782, viewOffsetX=52.0019, 
    viewOffsetY=0.760981)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[436], )
region = a.Set(referencePoints=refPoints1, name='Set-135')
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
    region=region, cf1=150.0, cf2=-259.0, distributionType=UNIFORM, field='', 
    localCsys=None)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[435], )
region = a.Set(referencePoints=refPoints1, name='Set-136')
mdb.models['Model-1'].ConcentratedForce(name='Load-2', createStepName='Step-1', 
    region=region, cf1=-50.0, cf2=89.0, distributionType=UNIFORM, field='', 
    localCsys=None)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-3-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#800000 ]', ), )
region = a.Set(edges=edges1, name='Set-137')
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=215.274, 
    farPlane=245.663, width=209.036, height=108.192, viewOffsetX=60.7727, 
    viewOffsetY=5.7549)
session.viewports['Viewport: 1'].view.setValues(nearPlane=214.436, 
    farPlane=246.501, width=208.222, height=107.77, viewOffsetX=56.8716, 
    viewOffsetY=-0.814913)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['cabeça-implante-1'], 
    a.instances['haste-implante-Copy-1'], a.instances['Part-3-1'], )
a.seedPartInstance(regions=partInstances, size=1.5, deviationFactor=0.1, 
    minSizeFactor=0.1)
session.viewports['Viewport: 1'].view.setValues(width=221.465, height=114.914, 
    viewOffsetX=61.9544, viewOffsetY=0.915247)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
f2 = a.instances['haste-implante-Copy-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#1 ]', ), )
f3 = a.instances['Part-3-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#1f ]', ), )
pickedRegions = faces1+faces2+faces3
a.setMeshControls(regions=pickedRegions, elemShape=QUAD)
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['cabeça-implante-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
f2 = a.instances['haste-implante-Copy-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#1 ]', ), )
f3 = a.instances['Part-3-1'].faces
faces3 = f3.getSequenceFromMask(mask=('[#1f ]', ), )
pickedRegions =((faces1+faces2+faces3), )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['cabeça-implante-1'], 
    a.instances['haste-implante-Copy-1'], a.instances['Part-3-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='DIV-075imp', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['DIV-075imp'].submit(consistencyChecking=OFF)
#: The job input file "DIV-075imp.inp" has been submitted for analysis.
#: Job DIV-075imp: Analysis Input File Processor completed successfully.
#: Job DIV-075imp: Abaqus/Standard completed successfully.
#: Job DIV-075imp completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/DIV-05imp.odb'])
o3 = session.openOdb(name='C:/temp/DIV-075imp.odb')
#: Model: C:/temp/DIV-075imp.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             4
#: Number of Element Sets:       7
#: Number of Node Sets:          17
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.904, 
    farPlane=356.537, width=168.602, height=87.2638, viewOffsetX=44.8262, 
    viewOffsetY=-8.05838)
session.viewports['Viewport: 1'].view.setValues(width=179.866, height=93.0938, 
    viewOffsetX=48.5433, viewOffsetY=-9.75391)
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.669, 
    farPlane=356.772, width=179.177, height=92.7374, viewOffsetX=50.3846, 
    viewOffsetY=-9.60388)
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.962, 
    farPlane=358.479, width=189.172, height=97.9104, viewOffsetX=44.5351, 
    viewOffsetY=-11.3712)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.888, 
    farPlane=357.553, width=189.954, height=98.3152, viewOffsetX=55.3453, 
    viewOffsetY=-9.26799)
session.printToFile(fileName='DIV-075imp-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='DIV-075imp-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=214.471, 
    farPlane=246.466, width=221.549, height=114.957, viewOffsetX=62.0447, 
    viewOffsetY=0.65579)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-3-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0:37 #200000 #0:26 #2000000 ]', ), )
n2 = a.instances['haste-implante-Copy-1'].nodes
nodes2 = n2.getSequenceFromMask(mask=('[#0:18 #10000 ]', ), )
n3 = a.instances['cabeça-implante-1'].nodes
nodes3 = n3.getSequenceFromMask(mask=('[#0:44 #40000000 ]', ), )
a.Set(nodes=nodes1+nodes2+nodes3, name='DIV075-point')
#: The set 'DIV075-point' has been created (4 nodes).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['DIV-075imp'].submit(consistencyChecking=OFF)
#: The job input file "DIV-075imp.inp" has been submitted for analysis.
#: Job DIV-075imp: Analysis Input File Processor completed successfully.
#: Job DIV-075imp: Abaqus/Standard completed successfully.
#: Job DIV-075imp completed successfully. 
o3 = session.openOdb(name='C:/temp/DIV-075imp.odb')
#: Model: C:/temp/DIV-075imp.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             4
#: Number of Element Sets:       7
#: Number of Node Sets:          18
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.904, 
    farPlane=356.537, width=168.602, height=87.2638, viewOffsetX=38.9978, 
    viewOffsetY=-6.67998)
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.669, 
    farPlane=356.772, width=190.614, height=98.6568, viewOffsetX=45.83, 
    viewOffsetY=-9.97171)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.841, 
    farPlane=357.599, width=189.915, height=98.2949, viewOffsetX=54.8533, 
    viewOffsetY=-9.93513)
leaf = dgo.LeafFromNodeSets(nodeSets=("DIV075-POINT", ))
dg = session.DisplayGroup(leaf=leaf, name='DisplayGroup-7')
#: The selected probe values were written to file "C:/temp/div-075imp-sm.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#: The selected probe values were written to file "C:/temp/div-075imp-u.rpt".
mdb.save()
#: The model database has been saved to "C:\temp\g13-umero.cae".
