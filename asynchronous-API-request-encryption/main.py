from rsa import generate_keypair, save_key_to_file, load_key_from_file, rsa_encrypt, rsa_decrypt
from aes import generate_key, aes_encrypt, aes_decrypt
from api import get_random_text, generation_text

def main():
    
    private_key, public_key = generate_keypair()

    save_key_to_file(private_key, 'private_key.pem')
    save_key_to_file(public_key, 'public_key.pem')

    loaded_private_key = load_key_from_file('private_key.pem')
    loaded_public_key = load_key_from_file('public_key.pem')


    message_to_encrypt = generation_text()
    print("message_to_encrypt:", message_to_encrypt)
    
    ciphertext = rsa_encrypt(message_to_encrypt, loaded_public_key)
    print("ciphertext:", ciphertext)

    decrypted_message = rsa_decrypt(ciphertext, loaded_private_key)
    print("decrypted_message:", decrypted_message)
    

    key = generate_key()

    message_to_encrypt = generation_text()
    print("message_to_encrypt:", message_to_encrypt)

    encrypted_message = aes_encrypt(message_to_encrypt.encode('utf-8'), key)
    print(f"encrypted_message: {encrypted_message.decode('utf-8')}")

    decrypted_message = aes_decrypt(encrypted_message, key)
    print(f"decrypted_message: {decrypted_message.decode('utf-8')}")


if __name__ == "__main__":
    main()

