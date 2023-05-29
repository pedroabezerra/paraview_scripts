# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
granularrotatingdrum249700vtk = LegacyVTKReader(registrationName='granularrotatingdrum249700.vtk*', FileNames=['/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum249700.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum312125.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum374550.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum436975.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum499400.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum561825.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum624250.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum686675.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum749100.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum811525.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum873950.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum936375.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum998800.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1061225.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1123650.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1186075.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1248500.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1310925.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1373350.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1435775.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1498200.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1560625.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1623050.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1685475.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1747900.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1810325.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1872750.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1935175.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum1997600.vtk', '/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/postpostrotating/granularrotatingdrum2060025.vtk'])

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
granularrotatingdrum249700vtkDisplay = Show(granularrotatingdrum249700vtk, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
granularrotatingdrum249700vtkDisplay.Representation = 'Surface'
granularrotatingdrum249700vtkDisplay.ColorArrayName = [None, '']
granularrotatingdrum249700vtkDisplay.SelectTCoordArray = 'None'
granularrotatingdrum249700vtkDisplay.SelectNormalArray = 'None'
granularrotatingdrum249700vtkDisplay.SelectTangentArray = 'None'
granularrotatingdrum249700vtkDisplay.OSPRayScaleArray = 'f'
granularrotatingdrum249700vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
granularrotatingdrum249700vtkDisplay.SelectOrientationVectors = 'None'
granularrotatingdrum249700vtkDisplay.ScaleFactor = 0.029429924441501498
granularrotatingdrum249700vtkDisplay.SelectScaleArray = 'None'
granularrotatingdrum249700vtkDisplay.GlyphType = 'Arrow'
granularrotatingdrum249700vtkDisplay.GlyphTableIndexArray = 'None'
granularrotatingdrum249700vtkDisplay.GaussianRadius = 0.001471496222075075
granularrotatingdrum249700vtkDisplay.SetScaleArray = ['POINTS', 'f']
granularrotatingdrum249700vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
granularrotatingdrum249700vtkDisplay.OpacityArray = ['POINTS', 'f']
granularrotatingdrum249700vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
granularrotatingdrum249700vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
granularrotatingdrum249700vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
granularrotatingdrum249700vtkDisplay.SelectInputVectors = ['POINTS', 'f']
granularrotatingdrum249700vtkDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
granularrotatingdrum249700vtkDisplay.ScaleTransferFunction.Points = [-0.072925203767, 0.0, 0.5, 0.0, 0.074316078498, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
granularrotatingdrum249700vtkDisplay.OpacityTransferFunction.Points = [-0.072925203767, 0.0, 0.5, 0.0, 0.074316078498, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData('/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/dados/rot_.csv', proxy=granularrotatingdrum249700vtk, WriteTimeSteps=1,
    PointDataArrays=['f', 'id', 'radius', 'type', 'v'])

# create a new 'STL Reader'
a01stl = STLReader(registrationName='01.stl', FileNames=['/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/meshes/01.stl'])

# show data in view
a01stlDisplay = Show(a01stl, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'STLSolidLabeling'
sTLSolidLabelingLUT = GetColorTransferFunction('STLSolidLabeling')

# trace defaults for the display properties.
a01stlDisplay.Representation = 'Surface'
a01stlDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
a01stlDisplay.LookupTable = sTLSolidLabelingLUT
a01stlDisplay.SelectTCoordArray = 'None'
a01stlDisplay.SelectNormalArray = 'None'
a01stlDisplay.SelectTangentArray = 'None'
a01stlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
a01stlDisplay.SelectOrientationVectors = 'None'
a01stlDisplay.ScaleFactor = 30.0
a01stlDisplay.SelectScaleArray = 'STLSolidLabeling'
a01stlDisplay.GlyphType = 'Arrow'
a01stlDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
a01stlDisplay.GaussianRadius = 1.5
a01stlDisplay.SetScaleArray = [None, '']
a01stlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
a01stlDisplay.OpacityArray = [None, '']
a01stlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
a01stlDisplay.DataAxesGrid = 'GridAxesRepresentation'
a01stlDisplay.PolarAxes = 'PolarAxesRepresentation'
a01stlDisplay.SelectInputVectors = [None, '']
a01stlDisplay.WriteLog = ''

# show color bar/color legend
a01stlDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'STLSolidLabeling'
sTLSolidLabelingPWF = GetOpacityTransferFunction('STLSolidLabeling')

# get 2D transfer function for 'STLSolidLabeling'
sTLSolidLabelingTF2D = GetTransferFunction2D('STLSolidLabeling')

# Properties modified on a01stlDisplay
a01stlDisplay.Scale = [0.001, 1.0, 1.0]

# Properties modified on a01stlDisplay.DataAxesGrid
a01stlDisplay.DataAxesGrid.Scale = [0.001, 1.0, 1.0]

# Properties modified on a01stlDisplay.PolarAxes
a01stlDisplay.PolarAxes.Scale = [0.001, 1.0, 1.0]

# Properties modified on a01stlDisplay
a01stlDisplay.Scale = [0.001, 0.001, 1.0]

# Properties modified on a01stlDisplay.DataAxesGrid
a01stlDisplay.DataAxesGrid.Scale = [0.001, 0.001, 1.0]

# Properties modified on a01stlDisplay.PolarAxes
a01stlDisplay.PolarAxes.Scale = [0.001, 0.001, 1.0]

# Properties modified on a01stlDisplay
a01stlDisplay.Scale = [0.001, 0.001, 0.001]

# Properties modified on a01stlDisplay.DataAxesGrid
a01stlDisplay.DataAxesGrid.Scale = [0.001, 0.001, 0.001]

# Properties modified on a01stlDisplay.PolarAxes
a01stlDisplay.PolarAxes.Scale = [0.001, 0.001, 0.001]

# hide color bar/color legend
a01stlDisplay.SetScalarBarVisibility(renderView1, False)

# Properties modified on a01stlDisplay
a01stlDisplay.Opacity = 0.2

# set active source
SetActiveSource(granularrotatingdrum249700vtk)

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=granularrotatingdrum249700vtk,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 0.029429924441501498
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1
glyph1.GlyphType = 'Sphere'
glyph1.OrientationArray = ['POINTS', 'v']
glyph1.ScaleArray = ['POINTS', 'radius']
glyph1.ScaleFactor = 2.0
glyph1.GlyphMode = 'All Points'

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = [None, '']
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'Normals'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'Normals'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 0.03000828493386507
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.0015004142466932535
glyph1Display.SetScaleArray = ['POINTS', 'Normals']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'Normals']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'
glyph1Display.SelectInputVectors = ['POINTS', 'Normals']
glyph1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-0.999990701675415, 0.0, 0.5, 0.0, 0.999990701675415, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-0.999990701675415, 0.0, 0.5, 0.0, 0.999990701675415, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'type'))

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'type'
typeLUT = GetColorTransferFunction('type')

# get opacity transfer function/opacity map for 'type'
typePWF = GetOpacityTransferFunction('type')

# get 2D transfer function for 'type'
typeTF2D = GetTransferFunction2D('type')

# set active source
SetActiveSource(granularrotatingdrum249700vtk)

# reset view to fit data bounds
renderView1.ResetCamera(-0.054888900369405746, 0.09624270349740982, -0.09694570302963257, -0.009825710207223892, 0.003984749782830477, 0.29828399419784546, True)

# set active source
SetActiveSource(a01stl)

# set active source
SetActiveSource(glyph1)

# reset view to fit data bounds
renderView1.ResetCamera(-0.057885825634002686, 0.09901499003171921, -0.09994129836559296, -0.006971656810492277, 0.0010987650603055954, 0.3011816143989563, True)

# reset view to fit data
renderView1.ResetCamera(True)

# hide color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, False)

# set active source
SetActiveSource(a01stl)

# set active source
SetActiveSource(glyph1)

# set active source
SetActiveSource(granularrotatingdrum249700vtk)

# create a new 'Annotate Time'
annotateTime1 = AnnotateTime(registrationName='AnnotateTime1')

# show data in view
annotateTime1Display = Show(annotateTime1, renderView1, 'TextSourceRepresentation')

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on annotateTime1Display
annotateTime1Display.FontSize = 19

# Properties modified on annotateTime1Display
annotateTime1Display.FontSize = 20

# Properties modified on annotateTime1Display
annotateTime1Display.FontSize = 21

# Properties modified on annotateTime1Display
annotateTime1Display.FontSize = 22

# Properties modified on annotateTime1Display
annotateTime1Display.FontSize = 23

# Properties modified on annotateTime1Display
annotateTime1Display.FontSize = 24

# Properties modified on annotateTime1Display
annotateTime1Display.Bold = 1

# Properties modified on annotateTime1Display
annotateTime1Display.Opacity = 0.9

# Properties modified on annotateTime1Display
annotateTime1Display.Opacity = 1.0

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# reset view to fit data
renderView1.ResetCamera(True)

# save data
SaveData('/home/n001/Documents/Pedro_Antonio/naoesferica/ar09/imagens/t_.csv', proxy=annotateTime1, WriteTimeSteps=1,
    RowDataArrays=['Text'],
    FieldAssociation='Row Data')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(742, 423)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 0.9487760958424981]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.15059080719947815]
renderView1.CameraParallelScale = 0.1106999029713137

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).