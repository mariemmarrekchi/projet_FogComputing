import socket
from PIL import Image
import io

# Function to receive an image part from the server
def receive_image_part(client_socket):
    image_data = b""
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        image_data += chunk
    return image_data

#adress server
adress1='192.168.88.230'
adress2='192.168.88.223'
adress3='192.168.88.216'
# List of host and port pairs to connect to
hosts_and_ports = [
    (adress1, 8082),
    (adress2, 8081),
    (adress3, 8083),
    # Add more host and port combinations as needed
]

# Create a list to store image data from each host
image_parts = []

# Iterate over the list and connect to each host
for host, port in hosts_and_ports:
    try:
        # Create a new TCP socket for each host
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the current host
        client_socket.connect((host, port))
        
        # Receive the image part and add it to the list
        image_data = receive_image_part(client_socket)
        image_parts.append(image_data)
        
        # Close the client socket
        client_socket.close()
        
    except ConnectionError:
        print(f"Failed to connect to {host}:{port}")

# Create a list of image objects from the received image data
image_objects = [Image.open(io.BytesIO(image_data)) for image_data in image_parts]

# Get the dimensions of the images
width, height = image_objects[0].size

# Calculate the total width and height for the merged image
total_width = width
total_height = height * len(image_objects)

# Create a new image with the total width and height
merged_image = Image.new("RGB", (total_width, total_height))

# Paste the image objects into the new image vertically
for i, image_obj in enumerate(image_objects):
    merged_image.paste(image_obj, (0, i * height))

# Save the merged image
merged_image.save('merged_image.jpg')
