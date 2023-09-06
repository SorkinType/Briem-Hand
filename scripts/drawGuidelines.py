overlap = 10 # left and right overlap of the guidelines
defaultThickness = 16 # default guideline thickness
thickerThickness = defaultThickness * 2 # thicker guideline thickness

		
# from https://github.com/mekkablue/Glyphs-Scripts/blob/a4421210dd17305e3205b7ca998cab579b778bf6/Paths/Fill%20Up%20with%20Rectangles.py
def drawRect(myBottomLeft, myTopRight):
	try:
		myRect = GSPath()
		myCoordinates = [[myBottomLeft[0], myBottomLeft[1]], [myTopRight[0], myBottomLeft[1]], [myTopRight[0], myTopRight[1]], [myBottomLeft[0], myTopRight[1]]]

		for thisPoint in myCoordinates:
			newNode = GSNode()
			newNode.type = GSLINE
			newNode.position = (thisPoint[0], thisPoint[1])
			myRect.nodes.append(newNode)

		myRect.closed = True
		return myRect

	except Exception as e:
		return False

		

font = Glyphs.font
for glyph in font.glyphs:
	if not glyph.selected:
		continue
	for layer in glyph.layers:
		
		master = layer.master
		
		# this is where you define the heights
		heightsAndThicknesses = [
			(-244, defaultThickness), # descender
			(0, thickerThickness), #  baseline 
			(524, defaultThickness), # x height
			(639, defaultThickness) # ascender
		]
		
		for height, thickness in heightsAndThicknesses:
			bottomLeft = (-overlap, height)
			topRight = (layer.width+overlap, height+thickness)
			print(bottomLeft, topRight)
			layerRect = drawRect(bottomLeft, topRight)
			layer.shapes.append(layerRect)
		
print('done')