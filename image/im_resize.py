from PIL import Image
import os
files = [f for f in os.listdir('.') if ('.jpg' in str(f))]
baseheight = 600

print(files)
for f in files:
    img = Image.open(f)
    hpercent = (baseheight/float(img.size[1]))
    wsize = int((float(img.size[0])*float(hpercent)))
    img = img.resize((wsize,baseheight), Image.ANTIALIAS)
    f_new="size/s_{}".format(str(f))
    print(f_new)
    img.save(f_new)

