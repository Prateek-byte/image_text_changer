from PIL import Image, ImageDraw, ImageFont

# Use a raw string for the file path
image_path = r"C:\Users\prate\Desktop\cp_pract\timg.jpg"

# Open your image file
img = Image.open(image_path)

# Create a drawing context
draw = ImageDraw.Draw(img)

# Define the coordinates of the text area to cover.
x, y = 36, 1220   # Top-left corner of the text area (adjust these coordinates as needed)
w, h = 350, 50    # Width and height of the text area (adjust these as needed)

# Define the background color for covering the old text (adjust as necessary)
background_color = (255, 255, 255)  # White background

# Cover the old text area with a filled rectangle
draw.rectangle([x, y, x + w, y + h], fill=background_color)

# Define the new text and its properties
new_text = "HIMANSHU MISHRA"
text_color = (0, 0, 0)  # Black text
font_size = 36          # Adjust font size if needed

# Load a bold TrueType font (Arial Bold). Make sure the font file is accessible.
try:
    font = ImageFont.truetype("arialbd.ttf", font_size)
except IOError:
    # Fallback to the default font if Arial Bold isn't available.
    font = ImageFont.load_default()

# Calculate the width and height of the new text using textbbox
bbox = draw.textbbox((0, 0), new_text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Center the text within the rectangle
text_x = x + (w - text_width) / 2
text_y = y + (h - text_height) / 2

# Draw the new text onto the image
draw.text((text_x, text_y), new_text, fill=text_color, font=font)

# Save the modified image
output_path = r"C:\Users\prate\Desktop\cp_pract\modified_image.jpg"
img.save(output_path)

print(f"Modified image saved as {output_path}")
