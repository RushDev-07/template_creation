from PIL import Image, ImageDraw, ImageFont
import os

# Directory to save the generated images
output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

# Path to the template image
template_path = 'template_image.png'

# List of data for customization
custom_data = [
    {'name': 'Alice', 'number': '01', 'logo_path': 'logo1.png'},
    {'name': 'Bob', 'number': '02', 'logo_path': 'logo2.png'},
    # Add more entries as needed
]

# Font settings
font_path = 'arial.ttf'  # Path to your font file
font_size = 40
font = ImageFont.truetype(font_path, font_size)

for data in custom_data:
    # Open the template image
    image = Image.open(template_path).convert('RGBA')
    
    # Open the logo and add an alpha channel to adjust its transparency
    logo = Image.open(data['logo_path']).convert('RGBA')
    logo = logo.resize((1000, 1000))  # Resize as needed
    
    # Create a new image with the same size as the logo and an alpha channel
    transparent_logo = Image.new('RGBA', logo.size, (255, 255, 255, 0))
    
    for x in range(logo.width):
        for y in range(logo.height):
            r, g, b, a = logo.getpixel((x, y))
            transparent_logo.putpixel((x, y), (r, g, b, int(a * 0.5)))  # opacity
    
    # Paste the transparent logo onto the template
    image.paste(transparent_logo, (500, 500), transparent_logo)  #can be adjusted

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Add name and number
    draw.text((200, 50), data['name'], font=font, fill='black')  # Adjust coordinates
    draw.text((200, 100), data['number'], font=font, fill='black')

    # Save the customized image
    output_path = os.path.join(output_dir, f"{data['name']}_creative.png")
    image.save(output_path)


print(f"Generated {len(custom_data)} customized images in '{output_dir}'.")
