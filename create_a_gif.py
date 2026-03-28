import imageio.v3 as iio 

filenames=["dancingchick1.png","dancingchick2.png"]
images=[]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite("ckick.gif",images, duration=500,loop=0)
