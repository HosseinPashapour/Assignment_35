from PIL import Image
import numpy as np
import os


def encrypt_image(image_path):
    img = Image.open(image_path)
    img_arr = np.array(img)
    secret_key = np.random.randint(0, 256, size=img_arr.shape, dtype=np.uint8)
    encrypted_img_arr = np.bitwise_xor(img_arr, secret_key)
    encrypted_img = Image.fromarray(encrypted_img_arr)
    encrypted_img.save('Encrypted_image.bmp')
    np.save('secret_key.npy', secret_key)


if __name__ == "__main__":
    image_path = 'path_to_image.jpg'
    encrypt_image(image_path)
