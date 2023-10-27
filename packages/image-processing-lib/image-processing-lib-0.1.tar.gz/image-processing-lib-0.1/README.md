# Overview
This Python module provides utility functions for various image processing tasks, such as image conversion, display, normalization, and enhancement. It leverages the power of libraries like cv2 and numpy to handle and manipulate image data.

# Functions
**open_img**

Purpose: Convert the image to a specified color space.
Inputs: Image data (or path), desired color space, and data type specifications.
Output: Image converted to the specified color space.

**display**

Purpose: Display images with their labels.
Inputs: Multiple images and labels, display size and layout specifications.
Output: None, this displays the image.

**normalize_img**

Purpose: Normalize an image.
Inputs: Image data.
Output: Normalized image.

**flatten_unflatten**

Purpose: Flatten or reshape an image.
Inputs: Image data, operation type (flatten or reshape), and desired shape if reshaping.
Output: Flattened or reshaped image.

**binary**

Purpose: Convert an image to a binary format based on a threshold.
Inputs: Image data and threshold value.
Output: Binarized image.

**img2blocs**

Purpose: Split an image into blocks/blocs of a certain size.
Inputs: Image data, block size, and padding type.
Output: List of blocks/blocs.

**resize_img**

Purpose: Resize an image to the specified dimensions.
Inputs: Image data and desired dimensions (width & height).
Output: Resized image.

**rotate_img**

Purpose: Rotate an image by a specified angle.
Inputs: Image data and rotation angle.
Output: Rotated image.

**enhance_img**

Purpose: Enhance an image by adding noise, applying blur, and adjusting contrast.
Inputs: Image data, and specifications for noise, blur, and contrast adjustments.
Output: Enhanced image.

# Requirements
cv2
numpy
matplotlib

Usage
First, make sure you have the required libraries installed:

bash
Copy code
pip install opencv-python numpy matplotlib
To use the functions in your code:

```python
Copy code
import cv2
import numpy as np
from YOUR_MODULE_NAME import FUNCTION_NAME

# Load an image
image = cv2.imread("path_to_image.jpg")

# Use any of the provided functions
processed_image = FUNCTION_NAME(image, ...other_args)
Replace YOUR_MODULE_NAME with the name of this module and FUNCTION_NAME with the name of the function you wish to use.
```

# Contribution
Feel free to fork this module and contribute by submitting a pull request. Ensure any new features or changes are well-documented and include relevant tests.

