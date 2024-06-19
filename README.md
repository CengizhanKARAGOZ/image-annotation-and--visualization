# image-annotation-and-visualization

This repository contains a Python script for visualizing image annotations. The script reads annotations from a text file, resizes the corresponding image, and draws bounding boxes around annotated objects. The output is saved as a new image file with the annotations visualized.

## Features

- Load and resize images
- Read and parse annotation files
- Draw bounding boxes around annotated objects
- Save the annotated image

## How to Use

1. Place your images in the `path/to/image` directory.
2. Place your annotation files in the `path/to/annotation` directory.
3. Update the `image_path`, `annotation_path`, and `output_image_path` variables in the script with your file paths.
4. Run the script to generate the annotated image.

## Requirements

- Python 3.x
- matplotlib
- Pillow

## Example

```python
# Example of how to use the script
image_path = '../image1.jpg'
annotation_path = '../annotation1.txt'
output_image_path = '../output1.jpg'

# Run the script to generate the annotated image
