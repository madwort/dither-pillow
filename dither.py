from PIL import Image, ImageDraw
import random

image_height = 32
image_width = 64
band_size = 2
new_img = Image.new('RGB', (image_width, image_height), '#b10019')
pencil = ImageDraw.Draw(new_img)
for row in range(image_height):
    band = row//band_size
    ratio = (1+(band))/16
    for col in range(image_width):
        if random.random() > ratio:
            print('.', end="")
            # pencil.rectangle((row, col, 1, 1), fill ='#310074')
        else:
            print(' ', end="")
    print("  ", "row:", row, "band:", band, "ratio:", ratio)

# new_img.show()
