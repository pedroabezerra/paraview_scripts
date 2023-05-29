# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
for i in range(4,10,1):
    print(i)
    # create a new 'Legacy VTK Reader'
    granularrotatingdrum249700vtk = LegacyVTKReader(registrationName='granularrotatingdrum249700.vtk*', FileNames=[f'/home/n001/Documents/Pedro_Antonio/naoesferica/ar0{i}/postpostrotating/granularrotatingdrum249700.vtk'])

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

    # a texture
    prancheta1copiar3 = CreateTexture('/home/n001/Documents/Pedro_Antonio/logo_flowlab/Prancheta 1 copiar 3.png')

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # update the view to ensure updated data information
    renderView1.Update()

    # save data
    SaveData(f'/home/n001/Documents/Pedro_Antonio/naoesferica/ar0{i}/dados/rot_.csv', proxy=granularrotatingdrum249700vtk, WriteTimeSteps=1,
        WriteTimeStepsSeparately=1,
        PointDataArrays=['f', 'id', 'radius', 'type', 'v'])

    # create a new 'STL Reader'
    geostl = STLReader(registrationName='geo.stl', FileNames=['/home/n001/Documents/Pedro_Antonio/geometry/geo.stl'])

    # show data in view
    geostlDisplay = Show(geostl, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    geostlDisplay.Representation = 'Surface'
    geostlDisplay.ColorArrayName = [None, '']
    geostlDisplay.SelectTCoordArray = 'None'
    geostlDisplay.SelectNormalArray = 'None'
    geostlDisplay.SelectTangentArray = 'None'
    geostlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    geostlDisplay.SelectOrientationVectors = 'None'
    geostlDisplay.ScaleFactor = 0.030000001192092896
    geostlDisplay.SelectScaleArray = 'None'
    geostlDisplay.GlyphType = 'Arrow'
    geostlDisplay.GlyphTableIndexArray = 'None'
    geostlDisplay.GaussianRadius = 0.0015000000596046448
    geostlDisplay.SetScaleArray = [None, '']
    geostlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    geostlDisplay.OpacityArray = [None, '']
    geostlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    geostlDisplay.DataAxesGrid = 'GridAxesRepresentation'
    geostlDisplay.PolarAxes = 'PolarAxesRepresentation'
    geostlDisplay.SelectInputVectors = [None, '']
    geostlDisplay.WriteLog = ''

    # update the view to ensure updated data information
    renderView1.Update()

    # reset view to fit data
    renderView1.ResetCamera(True)

    # Properties modified on geostlDisplay
    geostlDisplay.Opacity = 0.2

    # create a new 'Annotate Time'
    annotateTime1 = AnnotateTime(registrationName='AnnotateTime1')

    # show data in view
    annotateTime1Display = Show(annotateTime1, renderView1, 'TextSourceRepresentation')

    # update the view to ensure updated data information
    renderView1.Update()

    # Properties modified on annotateTime1Display
    annotateTime1Display.Bold = 1

    # Properties modified on annotateTime1Display
    annotateTime1Display.FontSize = 2

    # Properties modified on annotateTime1Display
    annotateTime1Display.FontSize = 24

    # create a new 'Logo'
    logo1 = Logo(registrationName='Logo1')

    # change texture
    logo1.Texture = prancheta1copiar3

    # show data in view
    logo1Display = Show(logo1, renderView1, 'LogoSourceRepresentation')

    # update the view to ensure updated data information
    renderView1.Update()

    # Properties modified on logo1Display
    logo1Display.WindowLocation = 'Upper Right Corner'

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

    # hide color bar/color legend
    glyph1Display.SetScalarBarVisibility(renderView1, False)

    # set active source
    SetActiveSource(geostl)

    # reset view to fit data
    renderView1.ResetCamera(True)

    #change interaction mode for render view
    renderView1.InteractionMode = '2D'

    # reset view to fit data
    renderView1.ResetCamera(True)

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
    renderView1.CameraPosition = [0.0, 0.0, 0.9487761014163308]
    renderView1.CameraFocalPoint = [0.0, 0.0, 0.15059080719947815]
    renderView1.CameraParallelScale = 0.11069990374434566

    #--------------------------------------------
    # uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).bash: /opt/paraview-5.11.1/bin/pvbatch: No such file or directory
