import cv2
import numpy as nl

# Load the freezer image
image_path = "freezer_image (1).jpg"
image = cv2.imread(image_path)

# Preprocess the image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

# Perform contour detection
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the detected contours and count the number of items
item_count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:  # Adjust this threshold based on your images
        item_count += 1

# Print the count
print("Number of items in the freezer:", item_count)
