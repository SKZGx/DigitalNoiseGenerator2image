# Digital Noise Image Processor

This Flask application allows users to upload images and add digital noise to them. It's a simple example demonstrating image processing capabilities using the Flask web framework and the Pillow library.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip: ```pip install -r requirements.txt```


## Usage
1. Run the Flask application: ```python app.py```
3. Open your web browser
4. You'll see an option to upload images and adjust the noise level.
5. Select an image file and choose the noise level.
6. Click the "Recycle Files" button to process the image.
7. The processed image with digital noise will be saved in the output_folder.

## Configuration
You can configure the following parameters in the app.py file:

* input_folder: Path to the folder containing input images.
* output_folder: Path to the folder where processed images will be saved.
