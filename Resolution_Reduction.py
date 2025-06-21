import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Load grayscale image
img = cv2.imread('Images/input.jpeg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

# Create output folder
os.makedirs("results", exist_ok=True)

def blockwise_average(img, block_size):
    h, w = img.shape
    result = img.copy()

    for y in range(0, h - block_size + 1, block_size):
        for x in range(0, w - block_size + 1, block_size):
            block = img[y:y + block_size, x:x + block_size]
            avg = int(np.mean(block))
            result[y:y + block_size, x:x + block_size] = avg
    return result


# Apply for block sizes 3, 5, and 7
block_sizes = [3, 5, 7]

for b in block_sizes:
    reduced_img = blockwise_average(img, b)
    filename = f"results/blockwise_{b}x{b}.png"
    cv2.imwrite(filename, reduced_img)
    print(f"Saved: {filename}")

    # Show with matplotlib
    plt.figure()
    plt.imshow(reduced_img, cmap='gray')
    plt.title(f'Blockwise Average {b}x{b}')
    plt.axis('off')

plt.show()
