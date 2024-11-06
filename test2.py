from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageDraw, ImageFont
import io
import os
import requests

app = Flask(__name__)

# Define the route for the API
@app.route('/edit-image', methods=['POST'])
def edit_image():
    # Parse JSON request
    data = request.get_json()

    try:
        # Load the template image
        template_img_path = data['templateImg']
        template_img = Image.open(template_img_path).convert('RGBA')

        # Load the logo image
        logo_img_path = data['logoImg']
        if logo_img_path.startswith('http'):  # Check if the logo path is a URL
            response = requests.get(logo_img_path)
            logo_img = Image.open(io.BytesIO(response.content)).convert('RGBA')
        else:  # Assume it's a local file path
            logo_img = Image.open(logo_img_path).convert('RGBA')
        
        # Resize the logo
        logo_size = data['logoSize']
        logo_img = logo_img.resize((logo_size, logo_size))

        # Remove the background and make the logo translucent
        logo_data = logo_img.getdata()
        new_logo_data = []
        for item in logo_data:
            r, g, b, a = item
            if r > 240 and g > 240 and b > 240:
                new_logo_data.append((255, 255, 255, 0))  # Make background fully transparent
            else:
                new_logo_data.append((r, g, b, int(a * 0.5)))  # Apply translucency to the logo
        logo_img.putdata(new_logo_data)

        # Paste the logo onto the template at specified position
        logo_position = data['logoPosition']
        template_img.paste(logo_img, (logo_position['x'], logo_position['y']), logo_img)

        # Draw texts on the template
        draw = ImageDraw.Draw(template_img)
        for text_item in data['texts']:
            text = text_item['text']
            font_size = text_item['fontSize']
            color = text_item['color']
            position = text_item['position']
            
            # Load the font
            font = ImageFont.truetype("arial.ttf", font_size)
            
            # Draw the text on the image
            draw.text((position['x'], position['y']), text, font=font, fill=color)

        # Save the edited image to disk
        output_path = "output_images/customized_image.png"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        template_img.save(output_path)

        # Optionally: Save the edited image to an in-memory file to return in response
        output = io.BytesIO()
        template_img.save(output, format='PNG')
        output.seek(0)

        # Return the image as response
        return send_file(output, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
