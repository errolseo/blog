
import os
import cv2

def is_image_by_extension(filepath):
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".ico"}
    _, extension = os.path.splitext(filepath)
    return extension.lower() in image_extensions

img_dir = "C:/Users/errol/workspace/blog/static/images/OCR"
for item in os.listdir(img_dir):
    
    if not is_image_by_extension(item):
        continue
    
    img = cv2.imread(os.path.join(img_dir, item), cv2.IMREAD_UNCHANGED)
    
    # if fig > 1.0:
    #     img = cv2.resize(img, dsize=(0, 0), fx=fig, fy=fig, interpolation=cv2.INTER_LANCZOS4)
    # elif fig < 1.0:
    #     img = cv2.resize(img, dsize=(0, 0), fx=fig, fy=fig, interpolation=cv2.INTER_AREA)

    name, ext = os.path.splitext(item)
    pre, post = name.split("-", 1)

    cv2.imwrite(os.path.join(img_dir, pre, post + ".webp"), img, [cv2.IMWRITE_WEBP_QUALITY, 101])
