from PIL import Image
import os

# Path to your frames folder
image_folder = 'frames'
output_gif = 'output.gif'  # You can change the output GIF name here

# List all the image files in the frames folder, sorted to maintain correct order
image_files = sorted([
    os.path.join(image_folder, file)
    for file in os.listdir(image_folder)
    if file.endswith(('png', 'jpg', 'jpeg'))
])

# Open and resize all images to the same size (200x200)
frame_size = (200, 200)
frames = [Image.open(img).resize(frame_size) for img in image_files]

# Create the GIF
frames[0].save(
    output_gif,           # Save to output.gif (or any name you want)
    format='GIF',         # Format for the output file
    append_images=frames[1:],  # Add remaining frames to the GIF
    save_all=True,        # Save all frames, not just the first
    duration=500,         # Duration per frame (100ms per frame)
    loop=0                # Loop indefinitely (set to 1 if you want it to loop only once)
)

print(f"GIF saved as: {output_gif}")
