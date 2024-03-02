# coding: latin-1
import asyncio
import tkinter as tk
from rsa import generate_keypair, save_key_to_file, load_key_from_file, rsa_encrypt, rsa_decrypt
from aes import generate_key, aes_encrypt, aes_decrypt
from api import get_random_text, generation_text

async def encrypt_and_display_text_rsa_aes():
    # RSA key generation
    private_key_rsa, public_key_rsa = generate_keypair()
    save_key_to_file(private_key_rsa, 'private_key_rsa.pem')
    save_key_to_file(public_key_rsa, 'public_key_rsa.pem')
    loaded_private_key_rsa = load_key_from_file('private_key_rsa.pem')
    loaded_public_key_rsa = load_key_from_file('public_key_rsa.pem')

    # AES key generation
    key_aes = generate_key()

    # Display the result in a window
    window = tk.Tk()
    window.title("Encryption Results")

    # Creating horizontal scrollbars and linking them to text widgets
    text_widget_rsa = tk.Text(window, height=10, width=40, wrap="none")
    text_widget_aes = tk.Text(window, height=10, width=40, wrap="none")

    text_widget_rsa.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    text_widget_aes.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

    
    scrollbar_x_rsa = tk.Scrollbar(window, orient=tk.HORIZONTAL, command=text_widget_rsa.xview)
    scrollbar_x_aes = tk.Scrollbar(window, orient=tk.HORIZONTAL, command=text_widget_aes.xview)

    scrollbar_x_rsa.pack(side=tk.BOTTOM, fill=tk.X)
    scrollbar_x_aes.pack(side=tk.BOTTOM, fill=tk.X)

    text_widget_rsa.config(xscrollcommand=scrollbar_x_rsa.set)
    text_widget_aes.config(xscrollcommand=scrollbar_x_aes.set)

    # Encrypt and display text for RSA
    message_to_encrypt_rsa = generation_text()
    text_widget_rsa.insert(tk.END, "Original Text (RSA):\n" + message_to_encrypt_rsa + "\n\n")

    ciphertext_rsa = await asyncio.to_thread(rsa_encrypt, message_to_encrypt_rsa, loaded_public_key_rsa)
    text_widget_rsa.insert(tk.END, "Encrypted Text (RSA):\n" + ciphertext_rsa.decode('latin-1') + "\n\n")

    decrypted_message_rsa = await asyncio.to_thread(rsa_decrypt, ciphertext_rsa, loaded_private_key_rsa)
    text_widget_rsa.insert(tk.END, "Decrypted Text (RSA):\n" + decrypted_message_rsa + "\n\n")

    # Encrypt and display text for AES
    message_to_encrypt_aes = generation_text()
    text_widget_aes.insert(tk.END, "Original Text (AES):\n" + message_to_encrypt_aes + "\n\n")

    ciphertext_aes = aes_encrypt(message_to_encrypt_aes.encode('utf-8'), key_aes)
    text_widget_aes.insert(tk.END, "Encrypted Text (AES):\n" + ciphertext_aes.decode('latin-1') + "\n\n")

    decrypted_message_aes = aes_decrypt(ciphertext_aes, key_aes)
    text_widget_aes.insert(tk.END, "Decrypted Text (AES):\n" + decrypted_message_aes.decode('utf-8') + "\n\n")

    # Start the main loop
    window.mainloop()

if __name__ == "__main__":
    asyncio.run(encrypt_and_display_text_rsa_aes())
