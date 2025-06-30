from PIL import Image
import os

input_folder = 'screenshots/'
output_folder = 'cropped/'

os.makedirs(output_folder, exist_ok=True)

def screenshot_cropper(filename):
    img = Image.open(os.path.join(input_folder, filename))
    width, height = img.size
    print(f"Width: {width}, Height: {height}")

    # Example crop: remove 100px border
    cropped_image = img.crop((100, 100, width - 100, height - 100))

    cropped_image.save(os.path.join(output_folder, filename))
    print(f"Cropped {filename} saved successfully!")

for file in os.listdir(input_folder):
    if file.endswith('.png'):
        screenshot_cropper(file)
