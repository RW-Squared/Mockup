from PIL import Image

# Replace 'image.webp' with your actual filename
img_path = 'FinalBanner.webp'

try:
    # Open the image file
    with Image.open(img_path) as img:
        width, height = img.size
        
        print(f"Width: {width} pixels")
        print(f"Height: {height} pixels")
        print(f"Aspect Ratio: {round(width/height * 100)}x (horizontal)")
except FileNotFoundError:
    print("Error: The file could not be found.")
