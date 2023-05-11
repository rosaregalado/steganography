from PIL import Image


def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    print(red_channel)  # Start coding here!

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    encoded_image = Image.open(path_to_png)
    get_encoded_image_px = encoded_image.getpixel((0, 0)) 
    for px in get_encoded_image_px:
        print(bin(px))


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass

decode_image('encoded_sample.png')