#5
import imageio
import os

images = []
for n in os.listdir("images"):
    image = imageio.imread(f"images/{n}")
    images.append(image)
imageio.mimsave("fun.gif",images)