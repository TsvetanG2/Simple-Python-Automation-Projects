import base64


def decrypt_password(password):
    decrypted_bytes = base64.b64decode(password.encode())
    decrypted_data = decrypted_bytes.decode()
    print(f'Decoded password: {decrypted_data}')


base64_string = input('Insert The Base64 String: ') #Whatever is input will pass through our function
decrypt_password(base64_string)