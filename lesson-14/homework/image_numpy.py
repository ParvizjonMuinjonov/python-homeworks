from PIL import Image
import numpy as np

# Function to save image
def save_image(array, filename):
    img = Image.fromarray(array.astype(np.uint8))
    img.save(filename)

# Manipulation functions
def flip_horizontal(image):
    return np.fliplr(image)

def flip_vertical(image):
    return np.flipud(image)

def add_noise(image, noise_level=70):
    noise = np.random.randint(-noise_level, noise_level + 1, image.shape)
    return np.clip(image + noise, 0, 255)

def brighten_channels(image, increase=20):
    return np.clip(image + increase, 0, 255)

def apply_mask(image, size=100):
    masked_img = image.copy()
    height, width = image.shape[:2]
    center_y, center_x = height // 2, width // 2
    y_start = max(0, center_y - size // 2)
    y_end = min(height, center_y + size // 2)
    x_start = max(0, center_x - size // 2)
    x_end = min(width, center_x + size // 2)
    masked_img[y_start:y_end, x_start:x_end, :] = 0
    return masked_img

# Load image
img = Image.open("images/birds.jpg")
img_array = np.array(img)

# Perform manipulations
flipped_h = flip_horizontal(img_array)
flipped_v = flip_vertical(img_array)
noisy_img = add_noise(img_array)
bright_img = brighten_channels(img_array)
masked_img = apply_mask(img_array)

# Save all results (fixed filenames)
save_image(flipped_h, "images/birds_flipped_h.jpg")
save_image(flipped_v, "images/birds_flipped_v.jpg")
save_image(noisy_img, "images/birds_noisy.jpg")
save_image(bright_img, "images/birds_bright.jpg")
save_image(masked_img, "images/birds_masked.jpg")

print("All manipulations completed and saved!")