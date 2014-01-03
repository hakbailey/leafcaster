import Image

pic = Image.open('/Users/melonbreath/Dropbox/Programming/NEDCC Project/files/test02.jpg')
pixels = pic.load()

#User input
xDim = 27.1
yDim = 18.0
docWeight = 5.1
maskX = 35.0
maskY = 25.0

#Inital calculations
pxPerCM = ((pic.size[0] / xDim) + (pic.size[1] / yDim)) / 2
xcm = pic.size[0] / pxPerCM
ycm = pic.size[1] / pxPerCM
area = xcm * ycm
maskArea = maskX * maskY

print(str(pxPerCM) + " pixels per cm")
#print pic.size
print(str(xcm) + " cm wide")
print(str(ycm) + " cm high")

totalCount = 0
docCount = 0

for x in range(0, pic.size[0]):
    for y in range(0, pic.size[1]):
        totalCount += 1
        if pixels[x,y][0] > 60 or pixels[x,y][1] > 60 or pixels[x,y][2] > 60:
            pixels[x,y] = (0, 255, 0)
            docCount += 1
           
totalArea = pic.size[0] * pic.size[1]
totalAreaCM = totalCount / (pxPerCM * pxPerCM)
docArea = docCount / (pxPerCM * pxPerCM)

#Weight calculations
pulpArea = maskArea - docArea
pulpWeight = pulpArea * docWeight / docArea

#print("Total number of pixels is " + str(totalCount))
#print("Total area in pixels is " + str(totalArea))
#print("Total area in cm squared is " + str(totalAreaCM))
#print("Document area in pixels is " + str(docCount))
print("Document area in cm squared is " + str(docArea))
print("Amount of pulp needed is " + str(pulpWeight) + " grams")

#pic.show()