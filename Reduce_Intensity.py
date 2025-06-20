import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load image
img = cv2.imread('Images/img.png', cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Image not found!")
    exit()

# Input levels
levels = int(input("Enter intensity levels (e.g., 2, 4, 8, 16...): "))
if levels <= 0 or levels > 256 or (levels & (levels - 1)) != 0:
    print("Invalid input. Must be power of 2 and ≤ 256.")
    exit()

# Reduce intensity
factor = 256 // levels
reduced = (img // factor) * factor

# Save and show using matplotlib
os.makedirs("results", exist_ok=True)
cv2.imwrite(f"results/reduced_{levels}.png", reduced)
print(f"Saved: results/reduced_{levels}.png")

plt.imshow(reduced, cmap='gray')
plt.title(f'Reduced to {levels} levels')
plt.axis('off')
plt.show()
