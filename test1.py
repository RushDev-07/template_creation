from PIL import Image, ImageDraw, ImageFont

def create_custom_creative(template_path, logo_path, name, number, output_path):
    # Open template image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Load logo and paste it on template
    logo = Image.open(logo_path)
    logo = logo.resize((100, 100))  # Resize if needed
    img.paste(logo, (50, 50))  # Position the logo on the template

    # Customize name
    font = ImageFont.truetype('arial.ttf', 40)
    draw.text((200, 150), name, font=font, fill="black")

    # Customize number
    draw.text((200, 250), str(number), font=font, fill="black")

    # Save the customized creative
    img.save(output_path)

# Example usage
create_custom_creative('output_johndoe.png', 'download (1).png', 'John Doe', 123456, 'output_johndoe(1).png')
#customers = [
#    {'name': 'John Doe', 'number': 123456, 'logo': 'logo1.png'},
#    {'name': 'Jane Smith', 'number': 789101, 'logo': 'logo2.png'},
#    # Add more customers
#]

#for customer in customers:
#    output_file = f"creative_{customer['name'].replace(' ', '_')}.png"
#    create_custom_creative('template.png', customer['logo'], customer['name'], customer['number'], output_file)

