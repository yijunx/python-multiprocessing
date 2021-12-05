import time
import concurrent.futures
from PIL import Image, ImageFilter


def process_image(img_name, size = (200, 200)):
    print(f"{img_name} starting!!")
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f"processed/{img_name}")
    img.close()
    return f"{img_name} was processed"

if __name__ == "__main__":
    img_names = [f"cat_00{x+1}.jpeg" for x in range(4)]

    t1 = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_image, img_names)
        for r in results:
            print(r)

    t2 = time.perf_counter()
    print(f"finished processing {len(img_names)} pictures in {t2 - t1} seconds")