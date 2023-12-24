import base64

def pem_to_hex(private_key_pem):
    private_key_pem = private_key_pem.strip()

    # Remove '-----BEGIN EC PRIVATE KEY-----' and '-----END EC PRIVATE KEY-----' markers
    private_key_pem = private_key_pem.replace('-----BEGIN EC PRIVATE KEY-----', '')
    private_key_pem = private_key_pem.replace('-----END EC PRIVATE KEY-----', '')

    binary_key = base64.b64decode(private_key_pem)

    hex_key = binary_key.hex()

    return hex_key

user_input = input("Enter your PEM-formatted private key:\n")

try:
    hex_private_key = pem_to_hex(user_input)

    # Print the result
    print("\nHexadecimal Private Key:")
    print(hex_private_key)

except ValueError as e:
    print("Error:", str(e))
