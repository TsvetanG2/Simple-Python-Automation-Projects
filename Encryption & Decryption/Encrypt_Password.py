import base64


def ecnrypt_password(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)


user_password = input('Insert your password here: ') #Whatever is input will pass through our function


ecnrypt_password(user_password)