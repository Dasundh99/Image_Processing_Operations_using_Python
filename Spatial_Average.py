import cv2
import matplotlib.pyplot as plt
import os

img = cv2.imread('Images/input.jpeg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found. Please check the path.")
    exit()

# Define the kernel sizes
kernel_sizes = [3, 10, 20]

os.makedirs('results', exist_ok=True)

# Apply average filter
for k in kernel_sizes:
    blurred = cv2.blur(img, (k, k))
    filename = f'results/blur_{k}x{k}.png'
    cv2.imwrite(filename, blurred)
    print(f"Saved: {filename}")

    plt.figure()
    plt.imshow(blurred, cmap='gray')
    plt.title(f'{k}x{k} Averaging Filter')
    plt.axis('off')

plt.show()
