from PIL import Image
path = "E:/FYP/Fire Dataset/FireImageSample/Image1/1.png"
im = Image.open(path,'r')

pix_val = list(im.getdata())

print (pix_val)