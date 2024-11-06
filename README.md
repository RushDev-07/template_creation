
---

# README for Image Customization API

## Project Overview

This project provides an API using Flask that allows users to customize images by overlaying logos, adding texts, and positioning elements based on user-defined parameters. Users can specify the logo size, position, translucency, and texts with configurable font size, color, and position. The API saves the customized image to disk and also returns it directly in the response.

## Features

- Customizes template images with logos and texts based on user configuration.
- Allows setting translucency for logos and removes their background.
- Saves customized images to disk and returns them directly in the response.
- Configurable via a JSON payload for flexible and dynamic image editing.

## Requirements

Make sure you have the following Python packages installed:

```bash
pip install flask pillow
```

## File Structure

```
project_root/
│
├── app.py                      # Main Flask API script
├── template_image.png          # Template image for customization
├── logo1.png                   # Example logo for 'Alice'
├── logo2.png                   # Example logo for 'Bob'
├── arial.ttf                   # Font file for text rendering
│
└── output_images/              # Directory for saving customized images
    ├── customized_image.png    # Example output file
```

## How to Run the API

1. Ensure that all required images (template and logos) and the font file are in the project directory.
2. Start the Flask API:

```bash
python test2.py
```

This will start the Flask server at `http://localhost:5000`.

### API Endpoint

- **URL**: `http://localhost:5000/edit-image`
- **Method**: POST

### JSON Payload Structure

The API accepts a JSON payload that matches the following structure:

```json
{
  "templateImg": "path/to/template_image.png",
  "logoImg": "path/to/logo_image.png",
  "logoSize": 100,
  "logoPosition": {
    "x": 50,
    "y": 50
  },
  "texts": [
    {
      "text": "Hello, World!",
      "fontSize": 40,
      "color": "black",
      "position": {
        "x": 200,
        "y": 50
      }
    },
    {
      "text": "Sample Text",
      "fontSize": 30,
      "color": "blue",
      "position": {
        "x": 200,
        "y": 100
      }
    }
  ]
}
```

### Sending a Request

You can test the API using a tool like **Postman** or **cURL**.

#### Example `curl` Request

Save your JSON payload in a file named `request.json` and then send a POST request as follows:

```bash
curl -X POST http://localhost:5000/edit-image \
-H "Content-Type: application/json" \
-d @request.json --output customized_image.png
```

This command will save the returned image as `customized_image.png`.

### API Response

The API returns the customized image as a PNG file directly in the response. The image is also saved to the `output_images` directory on the server.

## Code Explanation

### Main Steps in `test2.py`

1. **Route Definition**: The `/edit-image` endpoint accepts POST requests with a JSON payload.
2. **Image Processing**:
   - Loads the template and logo images based on paths provided in the JSON payload.
   - Resizes the logo as specified by `logoSize`, removes the background color, and makes it translucent.
   - Pastes the logo onto the template at the specified coordinates (`logoPosition`).
3. **Text Overlay**:
   - Draws each text entry on the template at specified positions with font size and color as defined in the JSON payload.
4. **Saving and Returning Image**: Saves the customized image to the `output_images` directory and returns it in the response.

## Customization Options

- **Logo Transparency**: Adjusts the translucency of the logo based on an alpha channel modification.
- **Dynamic Texts**: Supports multiple text entries, allowing flexible placement and styling.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

This README now includes clear instructions for setting up and using the Flask API, along with example requests and JSON payload details. Let me know if there are any additional adjustments you'd like!
