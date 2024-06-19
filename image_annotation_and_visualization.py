import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

image_path = 'path/to/image'
annotation_path = 'path/to/annotation'
output_image_path = 'path/to/output'

image = Image.open(image_path)
image = image.resize((1920, 1080), Image.LANCZOS)
image_width, image_height = image.size

annotations = []
with open(annotation_path, 'r') as file:
    for line in file:
        parts = line.strip().split()
        class_id = int(parts[0])
        x_center = float(parts[1]) * image_width
        y_center = float(parts[2]) * image_height
        width = float(parts[3]) * image_width
        height = float(parts[4]) * image_height
        annotations.append((class_id, x_center, y_center, width, height))

fig, ax = plt.subplots(1, figsize=(19.2, 10.8), dpi=100)
ax.imshow(image)

for annotation in annotations:
    class_id, x_center, y_center, width, height = annotation
    x_min = x_center - (width / 2)
    y_min = y_center - (height / 2)
    rect = patches.Rectangle((x_min, y_min), width, height, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

plt.axis('off') 
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.margins(0, 0)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0)
plt.close()