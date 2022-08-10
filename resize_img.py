
import sys
import os

import cv2

img_path = sys.argv[1]
fig = eval(sys.argv[2])

img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

if fig > 1.0:
    img = cv2.resize(img, dsize=(0, 0), fx=fig, fy=fig, interpolation=cv2.INTER_LANCZOS4)
elif fig < 1.0:
    img = cv2.resize(img, dsize=(0, 0), fx=fig, fy=fig, interpolation=cv2.INTER_AREA)


img_dir = os.path.dirname(img_path)
img_file = os.path.basename(img_path)
name, ext = os.path.splitext(img_file)

cv2.imwrite(os.path.join(img_dir, name + ".webp"), img, [cv2.IMWRITE_WEBP_QUALITY, 101])
