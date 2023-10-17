from PIL import Image

# Load the three image parts
image_part1 = Image.open("part0.jpg")
image_part2 = Image.open("part1.jpg")
image_part3 = Image.open("part2.jpg")

# Ensure that all parts have the same width
width = image_part1.width

# Calculate the total height for the merged image
total_height = image_part1.height + image_part2.height + image_part3.height

# Create a new image with the width of one of the parts and the total height
merged_image = Image.new("RGB", (width, total_height))

# Paste the image parts into the new image vertically
merged_image.paste(image_part1, (0, 0))
merged_image.paste(image_part2, (0, image_part1.height))
merged_image.paste(image_part3, (0, image_part1.height + image_part2.height))

# Save the merged image
merged_image.save("merged_image.png")
