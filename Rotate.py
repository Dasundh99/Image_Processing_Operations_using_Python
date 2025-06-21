import cv2
import os
import matplotlib.pyplot as plt

img = cv2.imread('Images/input.jpeg')

if img is None:
    print("Error: Image not found!")
    exit()

(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# --- Rotate by 45 degrees ---
rotation_matrix_45 = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_45 = cv2.warpAffine(img, rotation_matrix_45, (w, h))

# --- Rotate by 90 degrees ---
rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


os.makedirs("results", exist_ok=True)

cv2.imwrite('results/rotate_45.png', rotated_45)
cv2.imwrite('results/rotate_90.png', rotated_90)
print("Saved rotated images.")

titles = ['Original', 'Rotated 45°', 'Rotated 90°']
images = [img, rotated_45, rotated_90]

for i in range(3):
    plt.figure()
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.show()
