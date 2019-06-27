from PIL import Image, ImageEnhance
import os


def reduce_opacity(im, opacity):
    """Returns an image with reduced opacity."""
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

def watermark(im, mark, position, opacity=1):
    """Adds a watermark to an image."""
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    # create a transparent layer the size of the image and draw the
    # watermark in that layer.
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    if position == 'tile':
        for y in range(0, im.size[1], mark.size[1]):
            for x in range(0, im.size[0], mark.size[0]):
                layer.paste(mark, (x, y))
    elif position == 'scale':
        # scale, but preserve the aspect ratio
        ratio = min(
            float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        x=(im.size[0] - w) / 2;
        y=(im.size[1] - h) / 2;
        layer.paste(mark, (int(x),int(y)))
    else:
        layer.paste(mark, position)
    # composite the watermark with the layer
    return Image.composite(layer, im, layer)

def test():
    files = [f for f in os.listdir('.') if ('.jpg' in str(f))]
    for f in files:
        im = Image.open('bkg4.jpg')
        mark = Image.open('Logo.jpg')
        #watermark(im, mark, 'tile', 0.06).show() 
        imw=watermark(im, mark, 'scale', 0.06)
        imw=imw.convert('RGB')
        #watermark(im, mark, (100, 100), 0.5).show()
        f_new="water/w_{}".format(str(f))
        imw.save(f_new)

if __name__ == '__main__':
    test()
