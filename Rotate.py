import cv2
import os
import matplotlib.pyplot as plt

# Load image (color or grayscale)
img = cv2.imread('Images/img.png')  # You can use grayscale too if you prefer

if img is None:
    print("Error: Image not found!")
    exit()

# Get height and width of the image
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# --- Rotate by 45 degrees ---
rotation_matrix_45 = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_45 = cv2.warpAffine(img, rotation_matrix_45, (w, h))

# --- Rotate by 90 degrees ---
rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Create results folder
os.makedirs("results", exist_ok=True)

# Save images
cv2.imwrite('results/rotate_45.png', rotated_45)
cv2.imwrite('results/rotate_90.png', rotated_90)
print("Saved rotated images.")

# Show images using matplotlib
titles = ['Original', 'Rotated 45°', 'Rotated 90°']
images = [img, rotated_45, rotated_90]

for i in range(3):
    plt.figure()
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.show()
