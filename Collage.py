def collage():
  #Written by Brad Snurka
  #10/4/16 - 10/17/16
  #Ver 0.1
  
  canvas = makeEmptyPicture(700, 515, makeColor(25, 13, 71))

  signature = makePicture(getMediaPath("signature.jpg"))
  sun = makePicture(getMediaPath("volleyball.png"))
  
  placeSun(sun)
  
  
  signature(signature, canvas) #Writes my signature to canvas in upper right - Should be last
  show(canvas)
  
	#Indivdual Planets
	
	#Sun
def placeSun(src, target):
	darken(sun, 4)
	
	
	
	
  #Functions Used
  
  #Copys a chunk from one picture to another
def copy(picture, startX, endX, target):
  #Copies from input picture from Start-end px and puts it to the target in corresponding location
  for x in range(startX, endX):
    for y in range(0, getHeight(picture)):
      setColor(getPixel(target, x, y), getColor(getPixel(picture, x/2, y))) #Need /2 to stretch the picture out properly to fit new canvas size
	  
  #Gradually blurs a picture
  #Can be run multiple times in a loop to blue a lot    
def blur(src):
  target = duplicatePicture(src)
  for x in range(1, getWidth(src)-1):
    for y in range(1, getHeight(src)-1):
      top = getPixel(src, x, y-1)
      left = getPixel(src, x-1, y)
      bottom = getPixel(src, x, y+1)
      right = getPixel(src, x+1, y)
      center = getPixel(target, x, y)
      
      newRed = (getRed(top) + getRed(left) + getRed(bottom) + getRed(right) + getRed(center))/5
      newGreen = (getGreen(top) + getGreen(left) + getGreen(bottom) + getGreen(right) + getGreen(center))/5
      newBlue = (getBlue(top) + getBlue(left) +getBlue(bottom) + getBlue(right) + getBlue(center))/5
      
      setColor(center, makeColor(newRed, newGreen, newBlue))
  return target
  
  #Scales a picture down from its original size to a new size as determined by scale factor  
def scaleDown(src, scaleFactor):
  print getWidth(src)/int(scaleFactor)
  newSize = makeEmptyPicture(getWidth(src)/int(scaleFactor), getHeight(src)/int(scaleFactor))
  sourceX = 0
  for x in range(0,getWidth(src)/scaleFactor):
    sourceY = 0
    for y in range(0, getHeight(src)/scaleFactor):
      setColor(getPixel(newSize, x, y), getColor(getPixel(src, sourceX, sourceY)))
      sourceY = sourceY + scaleFactor
    sourceX = sourceX + scaleFactor
  return newSize
  
  #Scales a picture up from its input size to a new size as determined by scale factor  
def scaleUp(src, target, scaleFactor):
  sourceX = 0
  for targetX in range(0, getWidth(src) * scaleFactor):
    sourceY = 0
    for targetY in range(0, getHeight(src) * scaleFactor):
      srcpx = getPixel(src, int(sourceX), int(sourceY))
      color = getColor(srcpx)
      setColor(getPixel(target, targetX, targetY),color)
      sourceY = sourceY + float(1/float(scaleFactor))
    sourceX = sourceX + float(1/float(scaleFactor))
  return target

  #Lightens a pictures a number of times based on input number
def lighten(src, num):
  for num in range(num):
    for px in getPixels(src):
      setColor(px, makeLigher(getColor(px)))
  return src

  #Darkens a picture a number of times based on an input number
def darken(src, num):
  for num in range(num):
    for px in getPixels(src):
      setColor(px, makeDarker(getColor(px)))
  return src
  
  #Mirrors the first quarter of a picture to the opposite quarter
def mirrorVert(src): 
  mirrorPoint = getWidth(src)/4
  width = getWidth(src)
  for y in range(0, getHeight(src)):
    for x in range(0,mirrorPoint):
      leftpx = getPixel(src, x, y)
      rightpx = getPixel(src, width - x -1, y)
      color = getColor(leftpx)
      setColor(rightpx, color)
  return src 

  #Mirrors the top half to the bottom half
def mirrorHoriz(src):
  mirrorPoint = getHeight(src)/4
  height = getHeight(src)
  for x in range(0, getWidth(src)):
    for y in range(0 , mirrorPoint):
      toppx = getPixel(src, x, y)
      bottompx = getPixel(src, x, height - y -1)
      color = getColor(toppx)
      setColor(bottompx, color)
  return src
  
  #Returns luminance of a pixel
def luminance(pixel):
  r = getRed(pixel)
  g = getGreen(pixel)
  b = getBlue(pixel)
  return (r+g+b)/3
  
  #Converts a given picture to blue cyanotype
def cyanotype(src):
  grayscale(src)
  for px in getPixels(src):
    blue = getBlue(px)
    if (blue < 63):
      setBlue(px, (blue*2))
    elif (63 < blue <= 191):
      setBlue(px, (blue * 1.3))
    elif (blue > 191):
      setBlue(px,(blue * 1.2))
    setGreen(px,(getGreen(px) * .75))
    setRed(px,(getRed(px) * .75))
  return src  
  
  #Converts picture to grayscale
def grayscale(src):
  for p in getPixels(src):
    intensity = luminance(p)
    setColor(p, makeColor(intensity, intensity, intensity))
  return src
  
  #Performs a color swap on a picture
  #Red become Blue
  #Green becomes Red
  #Blue becomes Green
def swap(src):
  for p in getPixels(src):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    setColor(p, makeColor(blue, red, green))
  return src
  
  #Posterizes a picture
def posterize(src):
  for px in getPixels(src):
    luminance = luminance(px)
    if (luminance < 50):
      setColor(px, black)
    elif (50 <= luminance <= 165):
      setColor(px, gray)
    elif (luminance > 165):
      setColor(px, white)
  return src  
	
def chromakeySun(src, target):
  for px in getPixels(src):
    x = getX(px)
    y = getY(px)
    if ((getRed(px) > 230) and (getGreen(px) > 230) and (getBlue(px) < 100)):
      bgpx = getPixel(target, x, y)
      bgcol = getColor(bgpx)
      setColor(px, bgcol)
			
  #Writes my signature at a scale of 1/10th to the canvas
def signature(src, target):
  src = scaleDown(src, 10)
  for px in getPixels(src):
    if (getRed(px) < 50) and (getGreen(px) < 50) and (getBlue(px) < 50):
      srcColor = makeColor(107, 106, 109)
      trgLoc = getPixel(target, getX(px), getY(px))
      setColor(trgLoc, srcColor)
  return target