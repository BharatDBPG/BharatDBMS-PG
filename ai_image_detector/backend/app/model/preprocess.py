import numpy as np
import cv2
import torch
from PIL import Image
import torchvision.transforms as T

# Standard image size required by the neural network models
IMG_SIZE = 224

# Defines the sequence of transformations to convert a raw image 
# into a format (Tensor) that PyTorch can process.
transform = T.Compose([
    T.ToPILImage(),
    T.Resize((IMG_SIZE, IMG_SIZE)),
    T.ToTensor()
])


# Converts a grayscale image into a frequency spectrum map using 
# Fast Fourier Transform (FFT) to reveal hidden digital patterns.
def log_fft_spectrum(img_gray):
    fft = np.fft.fft2(img_gray)
    fft_shift = np.fft.fftshift(fft)
    mag = np.abs(fft_shift) + 1e-8
    log_mag = np.log(mag)
    log_mag = (log_mag - log_mag.min()) / (log_mag.max() - log_mag.min() + 1e-8)
    return log_mag.astype(np.float32)


# Takes a raw uploaded image and prepares two versions for the AI: 
# a standard resized version and a frequency-domain version.
def preprocess_image(image: Image.Image):
    img = np.array(image)

    # Convert to grayscale and resize for mathematical consistency
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (IMG_SIZE, IMG_SIZE))
    gray = gray.astype(np.float32) / 255.0

    # Generate the frequency map (the "X-ray" of the image)
    freq = log_fft_spectrum(gray)

    # Convert back to standard pixel values (0-255) before final transformation
    gray = (gray * 255).astype(np.uint8)
    freq = (freq * 255).astype(np.uint8)

    # Apply the standard transforms and expand to 3 color channels
    gray = transform(gray).repeat(3, 1, 1)
    freq = transform(freq).repeat(3, 1, 1)

    # Add a 'batch' dimension so the AI sees it as a list of one image
    gray = gray.unsqueeze(0)
    freq = freq.unsqueeze(0)

    return gray, freq