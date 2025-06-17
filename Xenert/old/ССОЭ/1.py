import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from pyproj import Proj, transform
from PIL import Image

def mercator_to_ginzburg(lon, lat):
    # Define the Mercator and Ginzburg projections
    mercator = Proj(init='epsg:3857')  # Mercator projection
    ginzburg = Proj(init='epsg:3395')  # Ginzburg IV projection
    
    # Convert coordinates from Mercator to Ginzburg
    x, y = transform(mercator, ginzburg, lon, lat)
    return x, y

def convert_map_projection(input_image_path, output_image_path):
    # Open the image using PIL
    img = Image.open(input_image_path)

    # Get image size
    width, height = img.size

    # Extract the image coordinates from the pixels
    lon_vals = [i * (360 / width) - 180 for i in range(width)]
    lat_vals = [90 - j * (180 / height) for j in range(height)]

    # Create a new image for the transformed map
    new_img = Image.new("RGB", (width, height), "white")

    # Iterate through each pixel in the original image and convert coordinates
    for i in range(width):
        print(i)
        for j in range(height):
            lon, lat = lon_vals[i], lat_vals[j]
            x, y = mercator_to_ginzburg(lon, lat)
            new_x = int((x + 20037508.342789244) / (40075016.685578488 / width))
            new_y = int((20037508.342789244 - y) / (40075016.685578488 / height))

            # Copy pixel color from original image to new image
            pixel_color = img.getpixel((i, j))
            new_img.putpixel((new_x, new_y), pixel_color)

    # Save the transformed image
    new_img.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "лицо.png"
    output_image_path = "ginzburg_projection.png"
    
    convert_map_projection(input_image_path, output_image_path)
    print(f"Conversion completed. Transformed image saved to {output_image_path}.")
