import asyncio
import tkinter as tk
from rsa import generate_keypair, save_key_to_file, load_key_from_file, rsa_encrypt, rsa_decrypt
from aes import generate_key, aes_encrypt, aes_decrypt
from api import get_random_text, generation_text

def run_asyncio_coroutine(coroutine):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coroutine)

async def encrypt_and_display_text_rsa(window):
    # RSA key generation
    private_key_rsa, public_key_rsa = generate_keypair()
    save_key_to_file(private_key_rsa, 'private_key_rsa.pem')
    save_key_to_file(public_key_rsa, 'public_key_rsa.pem')
    loaded_private_key_rsa = load_key_from_file('private_key_rsa.pem')
    loaded_public_key_rsa = load_key_from_file('public_key_rsa.pem')

    # Creating text widget without horizontal scrollbar
    text_widget_rsa = tk.Text(window, height=10, width=40, wrap="none")
    text_widget_rsa.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    # Encrypt and display text for RSA
    message_to_encrypt_rsa = generation_text()
    text_widget_rsa.insert(tk.END, "Original Text (RSA):\n" + message_to_encrypt_rsa + "\n\n")

    ciphertext_rsa = await asyncio.to_thread(rsa_encrypt, message_to_encrypt_rsa, loaded_public_key_rsa)
    text_widget_rsa.insert(tk.END, "Encrypted Text (RSA):\n" + ciphertext_rsa.decode('latin-1') + "\n\n")

    decrypted_message_rsa = await asyncio.to_thread(rsa_decrypt, ciphertext_rsa, loaded_private_key_rsa)
    text_widget_rsa.insert(tk.END, "Decrypted Text (RSA):\n" + decrypted_message_rsa + "\n\n")

async def encrypt_and_display_text_aes(window):
    # AES key generation
    key_aes = generate_key()

    # Creating text widget without horizontal scrollbar
    text_widget_aes = tk.Text(window, height=10, width=40, wrap="none")
    text_widget_aes.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    # Encrypt and display text for AES
    message_to_encrypt_aes = generation_text()
    text_widget_aes.insert(tk.END, "Original Text (AES):\n" + message_to_encrypt_aes + "\n\n")

    ciphertext_aes = await asyncio.to_thread(aes_encrypt, message_to_encrypt_aes.encode('utf-8'), key_aes)
    text_widget_aes.insert(tk.END, "Encrypted Text (AES):\n" + ciphertext_aes.decode('latin-1') + "\n\n")

    decrypted_message_aes = await asyncio.to_thread(aes_decrypt, ciphertext_aes, key_aes)

    # Display decrypted text in the same window
    text_widget_aes.insert(tk.END, "Decrypted Text (AES):\n" + decrypted_message_aes.decode('utf-8') + "\n\n")

async def main():
    window = tk.Tk()
    window.title("Encryption Results")

    # Run both tasks with the same window
    await asyncio.gather(
        encrypt_and_display_text_rsa(window),
        encrypt_and_display_text_aes(window),
    )

    # Function to close the Tkinter window
    def close_window():
        window.destroy()

    # Add a close button centered at the bottom of the window
    close_button = tk.Button(window, text="Close", command=close_window)
    close_button.pack(side=tk.BOTTOM, pady=10)

    window.mainloop()

# Run the Tkinter GUI in the main thread
if __name__ == "__main__":
    run_asyncio_coroutine(main())
