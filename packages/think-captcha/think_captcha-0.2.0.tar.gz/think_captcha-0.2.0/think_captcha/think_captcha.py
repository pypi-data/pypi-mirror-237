import pytesseract

from PIL import Image
from scipy.ndimage import gaussian_filter
import numpy
from PIL import ImageFilter

def solve_captcha(file):
    sig = 1.5  # the blurring sigma
    original = Image.open(file)
    original.save("original.png")  # reading the image from the request
    black_and_white = original.convert("L")  # converting to black and white
    black_and_white.save("black_and_white.png")
    first_threshold = black_and_white.point(lambda p: p != 134 and 255)
    first_threshold.save("first_threshold.png")
    blur = numpy.array(first_threshold) # create an image array
    blurred = gaussian_filter(blur, sigma=sig)
    blurred = Image.fromarray(blurred)
    blurred.save("blurred.png")
    final = blurred.point(lambda p: p > 140 and 255)
    final = final.filter(ImageFilter.EDGE_ENHANCE_MORE)
    final = final.filter(ImageFilter.SHARPEN)
    final.save("final.png")
    number = pytesseract.image_to_string(Image.open('final.png'), lang='eng',
                                         config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ').strip()

    return number
