from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Encrypt the image by applying a basic mathematical operation to each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

    # Save the encrypted image
    img.save("encrypted_image.png")
    print("Image encrypted and saved as encrypted_image.png")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Decrypt the image by reversing the mathematical operation applied during encryption
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    # Save the decrypted image
    img.save("decrypted_image.png")
    print("Image decrypted and saved as decrypted_image.png")

# Example usage
image_path = "C:/Users/Dhilipan/Downloads/Wallaper.jpg"  # Replace with the path to your image
encryption_key = 42

# Encrypt the image
encrypt_image(image_path, encryption_key)

# Decrypt the encrypted image
decrypt_image("encrypted_image.png", encryption_key)
