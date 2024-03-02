import asyncio
import tkinter as tk
from rsa import generate_keypair, save_key_to_file, load_key_from_file, rsa_encrypt, rsa_decrypt
from aes import generate_key, aes_encrypt, aes_decrypt
from api import get_random_text, generation_text

async def encrypt_and_display_text():
    private_key, public_key = generate_keypair()

    save_key_to_file(private_key, 'private_key.pem')
    save_key_to_file(public_key, 'public_key.pem')

    loaded_private_key = load_key_from_file('private_key.pem')
    loaded_public_key = load_key_from_file('public_key.pem')

    message_to_encrypt = generation_text()
    print("message_to_encrypt:", message_to_encrypt)

    ciphertext = await asyncio.to_thread(rsa_encrypt, message_to_encrypt, loaded_public_key)
    print("ciphertext:", ciphertext)

    decrypted_message = await asyncio.to_thread(rsa_decrypt, ciphertext, loaded_private_key)
    print("decrypted_message:", decrypted_message)

    # Отображение результата в окне
    result_text = f"Original Text: {message_to_encrypt}\nCiphertext: {ciphertext}\nDecrypted Text: {decrypted_message}"

    # Создание и настройка окна
    window = tk.Tk()
    window.title("Encryption Results")

    # Создание текстового виджета
    text_widget = tk.Text(window, height=10, width=50)
    text_widget.insert(tk.END, result_text)
    text_widget.pack()

    # Запуск главного цикла
    window.mainloop()

if __name__ == "__main__":
    asyncio.run(encrypt_and_display_text())
