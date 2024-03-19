from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os
import random

app = Flask(__name__)

def is_image_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def add_digital_noise(input_path, output_path, noise_level):
    # Check if the file is a valid image file
    if not is_image_file(input_path):
        return

    # Open the image
    image = Image.open(input_path)

    # Get the image size
    width, height = image.size

    # Create a new image with the same size
    noisy_image = Image.new('RGB', (width, height))

    # Loop through each pixel and add digital noise
    for x in range(width):
        for y in range(height):
            # Get the pixel color
            pixel = image.getpixel((x, y))

            # Add random noise to each color channel based on the noise level
            noisy_pixel = tuple(c + random.randint(-noise_level, noise_level) for c in pixel)

            # Set the noisy pixel in the new image
            noisy_image.putpixel((x, y), noisy_pixel)

    # Save the noisy image to the output folder
    noisy_image.save(output_path)

# ... (other routes and functions)

@app.route('/')
def index():
    return render_template('index.html')

# ... (previous code)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        input_folder = os.getcwd()  # Assuming files are at the root of the server
        output_folder = os.path.join(os.getcwd(), 'output_folder')

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        noise_level = int(request.form.get('noise-level', 50))

        print(f"Processing files from {input_folder}")

        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)

            # Process only image files
            if os.path.isfile(input_path) and is_image_file(input_path):
                output_path = os.path.join(output_folder, filename)
                print(f"Processing file: {input_path}")
                add_digital_noise(input_path, output_path, noise_level)

        print("Processing complete")
        return redirect(url_for('index'))

    return render_template('upload.html')



if __name__ == '__main__':
    app.run(debug=True)
