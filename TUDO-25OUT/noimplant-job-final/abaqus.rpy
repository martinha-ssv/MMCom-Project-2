# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-18.57.30 176069
# Run by ltiaulas2019 on Fri Oct 25 19:30:09 2024
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
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=193.188, 
    farPlane=224.56, width=215.078, height=111.599, viewOffsetX=6.18407, 
    viewOffsetY=-3.81622)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.13, 
    farPlane=223.618, width=203.671, height=105.415, viewOffsetX=4.37008, 
    viewOffsetY=-2.15913)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['osso-4'], )
a.deleteMesh(regions=partInstances)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['osso-4'], )
a.seedPartInstance(regions=partInstances, size=1.5, deviationFactor=0.1, 
    minSizeFactor=0.1)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['osso-4'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='CORT-NO-IMP', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['CORT-NO-IMP'].submit(consistencyChecking=OFF)
#: The job input file "CORT-NO-IMP.inp" has been submitted for analysis.
#: Job CORT-NO-IMP: Analysis Input File Processor completed successfully.
#: Job CORT-NO-IMP: Abaqus/Standard completed successfully.
#: Job CORT-NO-IMP completed successfully. 
o3 = session.openOdb(name='C:/temp/CORT-NO-IMP.odb')
#: Model: C:/temp/CORT-NO-IMP.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          14
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.111, 
    farPlane=355.037, width=212.574, height=110.023, viewOffsetX=-2.76861, 
    viewOffsetY=-3.67157)
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.257, 
    farPlane=355.891, width=211.757, height=109.6, viewOffsetX=67.9164, 
    viewOffsetY=-12.1804)
session.viewports['Viewport: 1'].view.setValues(width=199.047, height=103.022, 
    viewOffsetX=63.9979, viewOffsetY=-11.0495)
session.viewports['Viewport: 1'].view.setValues(nearPlane=222.231, 
    farPlane=354.917, width=199.928, height=103.477, viewOffsetX=58.7519, 
    viewOffsetY=-9.96683)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourStyle=CONTINUOUS, maxValue=2.7487, minValue=0.00566885)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourStyle=DISCRETE)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourStyle=CONTINUOUS)
session.viewports['Viewport: 1'].view.setValues(width=188.079, height=97.3446, 
    viewOffsetX=54.9004, viewOffsetY=-8.9516)
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.317, 
    farPlane=353.831, width=188.85, height=97.744, viewOffsetX=53.9387, 
    viewOffsetY=-8.7508)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.167, 
    farPlane=223.581, width=203.709, height=105.7, viewOffsetX=4.47102, 
    viewOffsetY=-2.6296)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['osso-4'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0:94 #10 #0:76 #800 ]', ), )
a.Set(nodes=nodes1, name='POINTS-NOO')
#: The set 'POINTS-NOO' has been created (2 nodes).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['CORT-NO-IMP'].submit(consistencyChecking=OFF)
#: The job input file "CORT-NO-IMP.inp" has been submitted for analysis.
#: Job CORT-NO-IMP: Analysis Input File Processor completed successfully.
#: Job CORT-NO-IMP: Abaqus/Standard completed successfully.
#: Job CORT-NO-IMP completed successfully. 
o3 = session.openOdb(name='C:/temp/CORT-NO-IMP.odb')
#: Model: C:/temp/CORT-NO-IMP.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          15
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.265, 
    farPlane=352.883, width=167.577, height=86.7332, viewOffsetX=48.3455, 
    viewOffsetY=-4.7424)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.033, 
    farPlane=353.115, width=189.457, height=98.0577, viewOffsetX=54.7201, 
    viewOffsetY=-7.58751)
session.printToFile(fileName='CORT-NOIMP-SM', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='CORT-NOIMP-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
leaf = dgo.LeafFromNodeSets(nodeSets=("POINTS-NOO", ))
dg = session.DisplayGroup(leaf=leaf, name='DisplayGroup-2')
#: The selected probe values were written to file "C:/temp/CORT-NOIMP-SM.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#: The selected probe values were written to file "C:/temp/CORT-NOIMP-u(actually-sm).rpt".
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].Material(name='trabecular')
mdb.models['Model-1'].materials['trabecular'].Elastic(table=((1380.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='tab-sect', 
    material='trabecular', thickness=22.5)
mdb.models['Model-1'].parts['osso'].sectionAssignments[0].setValues(
    sectionName='tab-sect')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='TRAB-NOIMP', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['TRAB-NOIMP'].submit(consistencyChecking=OFF)
#: The job input file "TRAB-NOIMP.inp" has been submitted for analysis.
#: Job TRAB-NOIMP: Analysis Input File Processor completed successfully.
#: Job TRAB-NOIMP: Abaqus/Standard completed successfully.
#: Job TRAB-NOIMP completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/CORT-NO-IMP.odb'])
o3 = session.openOdb(name='C:/temp/TRAB-NOIMP.odb')
#: Model: C:/temp/TRAB-NOIMP.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          15
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.265, 
    farPlane=352.883, width=167.577, height=86.7332, viewOffsetX=49.6094, 
    viewOffsetY=-2.74005)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.038, 
    farPlane=353.11, width=189.46, height=98.0598, viewOffsetX=54.8189, 
    viewOffsetY=-2.94386)
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.21, 
    farPlane=353.938, width=188.761, height=97.6975, viewOffsetX=55.3283, 
    viewOffsetY=-8.74973)
session.printToFile(fileName='TRAB-NOIMP-sm', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='TRAB-NOIMP-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
#: The selected probe values were written to file "C:/temp/TRAB-NOIMP-u.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#: The selected probe values were written to file "C:/temp/TRAB-NOIMP-sm.rpt".
p = mdb.models['Model-1'].parts['osso']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['osso']
f, e, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
    7.982133, 4.983682, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=204.04, gridSpacing=5.1, transform=t)
g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['osso']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=190.371, 
    farPlane=217.711, width=188.826, height=97.7313, cameraPosition=(5.26295, 
    0.601595, 204.041), cameraTarget=(5.26295, 0.601595, 0))
s.Spline(points=((-12.75, -2.55), (-6.375, -2.55), (0.0, -2.55), (6.375, 
    -2.55), (11.475, -2.55), (17.85, 6.375), (19.125, 20.4), (14.025, 29.325), 
    (2.55, 33.15), (-11.475, 31.875), (-17.85, 24.225), (-20.4, 12.75), (
    -17.85, 1.275), (-12.75, -2.55)))
s.Spline(points=((-8.925, -10.2), (-2.55, -10.2), (2.55, -10.2), (8.925, 
    -10.2), (12.75, -11.475), (14.025, -16.575), (10.2, -21.675), (5.1, 
    -17.85), (1.275, -15.3), (-2.55, -19.125), (-5.1, -20.4), (-8.925, 
    -16.575), (-8.925, -10.2)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=191.191, 
    farPlane=216.891, width=177.496, height=91.8675, cameraPosition=(9.32965, 
    0.128906, 204.041), cameraTarget=(9.32965, 0.128906, 0))
p = mdb.models['Model-1'].parts['osso']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=195.684, 
    farPlane=222.064, width=181.404, height=93.89, viewOffsetX=17.5567, 
    viewOffsetY=-0.157187)
del mdb.models['Model-1'].parts['osso'].sectionAssignments[0]
p = mdb.models['Model-1'].parts['osso']
f1, e, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    7.980404, -2.164877, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=204.04, gridSpacing=5.1, transform=t)
g, v, d1, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['osso']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['osso']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-2')
p = mdb.models['Model-1'].parts['osso']
p.SectionAssignment(region=region, sectionName='osso-section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['osso']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#6 ]', ), )
region = p.Set(faces=faces, name='Set-3')
p = mdb.models['Model-1'].parts['osso']
p.SectionAssignment(region=region, sectionName='tab-sect', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
#: Warning: Failed to attach mesh to geometry for instance 'osso-4'.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='DIV-NOIMP', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['osso-4'].faces
pickedRegions = f1.getSequenceFromMask(mask=('[#7 ]', ), )
a.setMeshControls(regions=pickedRegions, elemShape=QUAD)
elemType1 = mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS6M, elemLibrary=STANDARD)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['osso-4'].faces
faces1 = f1.getSequenceFromMask(mask=('[#7 ]', ), )
pickedRegions =(faces1, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['osso-4'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['DIV-NOIMP'].submit(consistencyChecking=OFF)
#: The job input file "DIV-NOIMP.inp" has been submitted for analysis.
#: Job DIV-NOIMP: Analysis Input File Processor completed successfully.
#: Job DIV-NOIMP: Abaqus/Standard completed successfully.
#: Job DIV-NOIMP completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/TRAB-NOIMP.odb'])
o3 = session.openOdb(name='C:/temp/DIV-NOIMP.odb')
#: Model: C:/temp/DIV-NOIMP.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       6
#: Number of Node Sets:          16
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.29, 
    farPlane=352.858, width=167.595, height=86.743, viewOffsetX=44.1373, 
    viewOffsetY=-8.43188)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.842, 
    farPlane=352.306, width=178.732, height=92.5069, viewOffsetX=46.6961, 
    viewOffsetY=-9.59576)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.063, 
    farPlane=353.085, width=178.113, height=92.1865, viewOffsetX=47.6538, 
    viewOffsetY=-9.22649)
session.printToFile(fileName='DIV-NOIMP-u', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(fileName='DIV-NOIMP-SM(Actually-u)', format=PNG, 
    canvasObjects=(session.viewports['Viewport: 1'], ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.975, 
    farPlane=222.773, width=192.284, height=99.7721, viewOffsetX=4.8723, 
    viewOffsetY=-4.16789)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['osso-4'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0:123 #8000000 #0:52 #10000 ]', ), )
a.Set(nodes=nodes1, name='DIV-NOIMP')
#: The set 'DIV-NOIMP' has been created (2 nodes).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['DIV-NOIMP'].submit(consistencyChecking=OFF)
#: The job input file "DIV-NOIMP.inp" has been submitted for analysis.
#: Job DIV-NOIMP: Analysis Input File Processor completed successfully.
#: Job DIV-NOIMP: Abaqus/Standard completed successfully.
#: Job DIV-NOIMP completed successfully. 
o3 = session.openOdb(name='C:/temp/DIV-NOIMP.odb')
#: Model: C:/temp/DIV-NOIMP.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       6
#: Number of Node Sets:          17
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
leaf = dgo.LeafFromNodeSets(nodeSets=("DIV-NOIMP", ))
dg = session.DisplayGroup(leaf=leaf, name='DisplayGroup-3')
#: The selected probe values were written to file "C:/temp/DIVNOIMP-sm.rpt".
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#: The selected probe values were written to file "C:/temp/DIVNOIMP-u.rpt".
session.viewports['Viewport: 1'].view.setValues(nearPlane=221.438, 
    farPlane=355.709, width=225.458, height=116.691, viewOffsetX=-1.84673, 
    viewOffsetY=-2.61775)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=223.339, 
    farPlane=353.809, width=200.924, height=103.993, viewOffsetX=-0.982897, 
    viewOffsetY=0.509361)
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, 
    tensorQuantity=ALL_PRINCIPAL_COMPONENTS, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=226.288, 
    farPlane=350.86, width=158.943, height=82.2647, viewOffsetX=22.4333, 
    viewOffsetY=11.9639)
session.viewports['Viewport: 1'].view.setValues(nearPlane=225.625, 
    farPlane=351.523, width=158.477, height=82.0237, viewOffsetX=7.52588, 
    viewOffsetY=0.367768)
session.viewports['Viewport: 1'].view.setValues(width=168.592, height=87.2586, 
    viewOffsetX=9.62077, viewOffsetY=-0.271565)
session.viewports['Viewport: 1'].view.setValues(nearPlane=224.844, 
    farPlane=352.304, width=168.01, height=86.9573, viewOffsetX=13.2836, 
    viewOffsetY=-5.87055)
session.viewports['Viewport: 1'].view.setValues(width=178.77, height=92.5266, 
    viewOffsetX=15.5818, viewOffsetY=-6.50244)
mdb.save()
#: The model database has been saved to "C:\temp\g13-umero.cae".
