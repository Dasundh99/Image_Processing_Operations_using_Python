import cv2
import matplotlib.pyplot as plt
import os

# Step 1: Load the grayscale image
img = cv2.imread('Images/img.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found. Please check the path.")
    exit()

# Step 2: Define the kernel sizes
kernel_sizes = [3, 10, 20]

# Step 3: Create a folder for results
os.makedirs('results', exist_ok=True)

# Step 4: Apply average (mean) filter for each kernel size
for k in kernel_sizes:
    blurred = cv2.blur(img, (k, k))  # Apply averaging filter
    filename = f'results/blur_{k}x{k}.png'
    cv2.imwrite(filename, blurred)  # Save the image
    print(f"Saved: {filename}")

    # Show using matplotlib
    plt.figure()
    plt.imshow(blurred, cmap='gray')
    plt.title(f'{k}x{k} Averaging Filter')
    plt.axis('off')

plt.show()
