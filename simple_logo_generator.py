from PIL import Image, ImageDraw, ImageFont
import random

def generate_logo(word, output_path='logo.png', width=400, height=200):
    # Create a new image with white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 72)  # You can use any other .ttf file
    except IOError:
        font = ImageFont.load_default()

    # Calculate text size and position
    text_width, text_height = draw.textsize(word, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Choose a random color
    text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw the text on the image
    draw.text((text_x, text_y), word, font=font, fill=text_color)

    # Save the image
    image.save(output_path)
    print(f"Logo saved as {output_path}")

if __name__ == "__main__":
    word = input("Enter the word for the logo: ")
    generate_logo(word)
from PIL import Image, ImageDraw, ImageFont
import random

def generate_logo(word, output_path='logo.png', width=400, height=200):
    # Create a new image with white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 72)  # You can use any other .ttf file
    except IOError:
        font = ImageFont.load_default()

    # Calculate text size and position
    text_width, text_height = draw.textsize(word, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Choose a random color
    text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw the text on the image
    draw.text((text_x, text_y), word, font=font, fill=text_color)

    # Save the image
    image.save(output_path)
    print(f"Logo saved as {output_path}")

if __name__ == "__main__":
    word = input("Enter the word for the logo: ")
    generate_logo(word)
