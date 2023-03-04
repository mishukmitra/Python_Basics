import os

files = os.listdir("images_file")

i = 1
for image in files:
    if image.endswith(".png"):
        os.rename(f"images_file/{image}", f"images_file/{i}.png")
        i = i + 1
        print(image)
