from PIL import Image
import os

# input image path
# Access the document directory using the os module
downloads_directory = os.path.join(os.path.expanduser("~"), "Downloads")
# Define the path to the "infrastructure-images" folder within the Downloads directory
input_images_path = os.path.join(downloads_directory, "infrastructure-images")

# Create a new folder to save transparent images if it doesn't exist
output_images_path = "transparent_images"
try:
    os.mkdir(output_images_path)
except OSError as e:
    pass


def make_background_transparent(image_path, output_path_param, img_name):
    input_image = Image.open(image_path)

    # Convert the image to RGBA mode (if not already)
    if input_image.mode != 'RGBA':
        input_image = input_image.convert('RGBA')

    data = input_image.getdata()

    new_data = []
    for item in data:
        # Set the alpha value (transparency) of white pixels to 0 (fully transparent)
        if item[:3] == (255, 255, 255):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    input_image.putdata(new_data)

    output_path_param = os.path.join(output_path_param, img_name)
    input_image.save(output_path_param, format="PNG")

    # input_image.show()
    # Remember to close the image after processing
    input_image.close()


if __name__ == '__main__':
    for filename in os.listdir(input_images_path):

        input_image_path = os.path.join(input_images_path, filename)
        make_background_transparent(input_image_path, output_images_path, filename)



