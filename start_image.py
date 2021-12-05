import time
from PIL import Image, ImageFilter

img_names = [f"cat_00{x+1}.jpeg" for x in range(4)]

t1 = time.perf_counter()

size = (200, 200)


for img_name in img_names:
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f"processed/{img_name}")
    img.close()
    print(f"{img_name} was processed")

t2 = time.perf_counter()
print(f"finished processing {len(img_names)} pictures in {t2 - t1} seconds")
