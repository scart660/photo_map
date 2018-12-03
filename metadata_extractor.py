from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

img= Image.open('img1.jpg')
exif_data = img._getexif()
print(exif_data[34853])
print(exif_data)

for k,v in exif_data[34853].items():
    print('{}:{}'.format(GPSTAGS[k],v))
    pass


def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)