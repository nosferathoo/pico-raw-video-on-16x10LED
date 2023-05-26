import os
from PIL import Image

# Get the list of files in the current directory and sort them alphabetically
files = sorted(os.listdir())

# Create a new file to store the raw pixel data
with open("output.raw", "wb") as f:
  
  # Loop through all files in the current directory
  for file in files:
    
    # Check if the file is a PNG image
    if file.endswith(".png"):
      
      # Open the image using the PIL library
      with Image.open(file) as img:
        
        # Get the raw pixel data and write it to the output file
        raw_data = img.tobytes('raw','RGB')
        f.write(raw_data)