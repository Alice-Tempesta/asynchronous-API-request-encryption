# asynchronous-API-request-encryption
<br> **Project description:** <br/>
This project is a Python script that interacts with the <a href=https://randommer.io/> Randomer<a/> API to extract random text and perform asynchronous 
RSA and AES (using the `cryptography` library) encryption on it and display the results in a special window.
The script involves using the API to generate random text, count words starting with a vowel and a consonant, and display the text in a frame.

<br> **Using the `asyncio` library:** <br/>
<br>The provided code uses asynchrony to perform encryption and decryption operations in the background without blocking the main program thread.
The main thread on which Tkinter runs remains responsive, allowing the user to interact with the interface while encryption operations are performed.<br/>
<br>The key role of async in this code is to use `await asyncio.to_thread(...)` to call the encryption and decryption functions on a separate thread.<br/>
<br>This allows other tasks to continue on the main thread, including updating the GUI.<br/>



## Instructions:

1. **Clone a project:**
   - Open a terminal (or command line) in the folder where you want to save the project.
   - Run the following command to clone the repository via git:
     <br> ```git clone git@github.com:Alice-Tempesta/asynchronous-API-request-encryption.git```<br/>

2. **Installing dependencies:**
   - Go to the project folder:
     ```cd your_repository```
   - Make sure you have all the necessary libraries installed:
     ```pip install -r requirements.txt```

3. **Obtaining an API key:**
   - Visit <a href=https://randommer.io/>Randomer<a/> and obtain an API key as described in the previous instructions.
     - Getting an API key:
     - Go to the Randomer website and follow these steps to obtain an API key:
     - Registration and login:
       - If you don't have an account, register on the Randomer website.
       - Log in to your account if you already have an account.
     - Navigation to the API Keys section:
       - After logging into your account, click on your email address in the panel and select "My account"
     - Creating a new API key:
       - On the page that opens, select `API Key` and generate a key
     - Copying a key.
4. **.env file configuration:**
   -  After creating the key, copy it and create a `.env` file in the root directory with your <a href=https://randommer.io/>Randomer<a/> API key:
  <br>```RANDOM_TEXT_API_KEY=your-api-key```<br/>
5. **Project launch:**
   - Execute the script,
by entering in the terminal:
     ```python main.py```
   - This script will automatically send a request to <a href=https://randommer.io/> Randomer<a/> API and encrypt the received text, after receiving the necessary information, 
click on the `Close` button at the bottom of the pop-up window
