import imageio
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import re, sys

if len(sys.argv)!=2 or '.' not in sys.argv[1]:
	print('Usage\n\t'+sys.argv[0]+' <image-file>')
	exit(0)

LINE = 64

def get_ascii(p):
	p = 255 - p
	if p<=12:
		return ' '
	if p<=50:
		return '.'
	if p<=75:
		return '*'
	if p<=100:
		return '='
	if p<=125:
		return '|'
	if p<=150:
		return 'J'
	if p<=200:
		return 'P'
	return 'B'

def to_grayscale(img):
	if len(img.shape) == 2:
		return img
	g = np.sum(img, axis=2)
	g = g / 3
	return g

img = imageio.imread(sys.argv[1])
h = len(img)
w = len(img[0])
ar = float(h)/w
new_size = (int(LINE * 1.75), int(ar*LINE))
print(new_size)
img = np.array(Image.fromarray(img).resize(new_size))

img = to_grayscale(img)

print(img)
print(img.shape)

filename = sys.argv[1]
filename = re.sub(r'[.*\.](.*)', '.txt', filename)
file = open(filename, 'w')

for i in range(len(img)):
	ascii_str = ''
	for j in range(len(img[0])):
		ascii_str = ascii_str + get_ascii(img[i][j])
	print(ascii_str)
	ascii_str = ascii_str + '\n'
	file.write(ascii_str)

print("Ascii image saved to "+filename)