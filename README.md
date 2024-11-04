# README for Image Customization Project

## Project Overview
This project automates the creation of customized images using a template. It overlays logos, names, and numbers on the template image and can make logos translucent to create a watermark effect. The generated images are saved to an output directory.

## Features
- Customizes template images with logos, names, and numbers.
- Resizes and pastes logos onto the template.
- Applies transparency to logos for a watermark effect.
- Saves multiple customized outputs based on input data.

## Requirements
Ensure the following Python package is installed:

```bash
pip install pillow
```

## File Structure
```
project_root/
│
├── test2.py                    # Main Python script
├── template_image.png          # Template image for customization
├── logo1.png                   # Example logo for 'Alice'
├── logo2.png                   # Example logo for 'Bob'
├── arial.ttf                   # Font file for text rendering
│
└── output_images/              # Directory for saving customized images
    ├── Alice_creative.png      # Generated image for Alice
    └── Bob_creative.png        # Generated image for Bob
```

## How to Run
1. Ensure that all required images (template and logos) and the font file are in the project directory.
2. Run the script:

```bash
python test2.py
```

3. The customized images will be saved in the `output_images` directory.

## Code Explanation
### Main Steps in `test2.py`
1. **Import Libraries**: `Pillow` library (`PIL`) for image processing and `os` for file handling.
2. **Directory Setup**: Creates an `output_images` directory if it doesn't exist.
3. **Load and Process Data**:
   - Reads `template_image.png` as the base image.
   - Loads and resizes the logo image.
   - Adjusts the transparency of the logo to create a watermark effect.
4. **Customize with Text**:
   - Uses `ImageDraw` to add the name and number to the image.
5. **Save Output**: Saves the final image with a unique filename based on the input data.

## Customization
- **Logo Transparency**: Adjust the `0.5` factor in the `transparent_logo.putpixel()` function for different transparency levels.
- **Font and Coordinates**: Change `font_path`, `font_size`, and coordinates in the `draw.text()` function to match your design needs.

## Sample Input Data
Modify the `custom_data` list in the script to customize images for different entries:

```python
custom_data = [
    {'name': 'Alice', 'number': '01', 'logo_path': 'logo1.png'},
    {'name': 'Bob', 'number': '02', 'logo_path': 'logo2.png'},
    # Add more entries as needed
]
```

## License
This project is open-source and available under the [MIT License](LICENSE).

