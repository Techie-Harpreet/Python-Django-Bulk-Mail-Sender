# Python Django Bulk Mail Sender

## 📌 Overview
Python Django Bulk Mail Sender is a web-based application that allows users to send multiple emails at once. It is built using the Django framework and supports email sending via an SMTP server. Additionally, it utilizes **Celery** and **Redis** for background task processing.

## 🚀 Features
- 📧 **User Authentication & SMTP Configuration** - Each user can register and set up their **personal SMTP settings**.
- ✉️ **Single Email Sending** - Option to send a single email at a time.
- 📑 **Bulk Email Sending via CSV** - Users can upload a **formatted CSV file** containing email addresses.
- 🔑 **Secure SMTP Authentication** - Ensures safe SMTP server usage.
- 📄 **Custom Email Templates** - Supports both HTML and text-based email templates.
- 📊 **Email Status Tracking** - Check the status of sent emails.
- 📂 **CSV Upload** - Upload recipient lists as a CSV file.
- 🔍 **Error Handling & Logging** - Keeps logs of failed emails.
- ⚡ **Celery & Redis Integration** - Handles email sending in the background for better performance.

## 🛠 Installation

### Prerequisites
To run this project, you need:
- Python 3.8+
- Django
- Celery
- Redis
- SMTP Server (Gmail, Outlook, etc.)

### Steps
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Techie-Harpreet/Python-Django-Bulk-Mail-Sender.git
   cd Python-Django-Bulk-Mail-Sender
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv env
   source env/bin/activate  # Linux/macOS
   env\Scripts\activate  # Windows
   ```
3. **Install required packages:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Install and run Redis server:**
   ```sh
   # Linux/macOS
   redis-server

   # Windows (Manually install Redis and then run it)
   ```
5. **Run Celery worker:**
   ```sh
   celery -A bulkmail worker --loglevel=info
   ```
6. **Apply database migrations:**
   ```sh
   python manage.py makemigrations
   ```
8. **Apply database migrations:**
   ```sh
    python manage.py migrate
   ```
8. **Run the server:**
   ```sh
   python manage.py runserver
   ```

## 🎯 Usage
### 1️⃣ User Registration
![Login & Register](https://raw.githubusercontent.com/Techie-Harpreet/Python-Django-Bulk-Mail-Sender/refs/heads/main/images/register%20page.png )

### 2️⃣ User Login
![Login & Register](https://raw.githubusercontent.com/Techie-Harpreet/Python-Django-Bulk-Mail-Sender/refs/heads/main/images/login%20page.png)

1. **Register and log in as a user.**
2. **Set up your SMTP configuration** to send emails via your personal server.

### 3️⃣ Single Email Sending
![Single Email Dashboard](https://raw.githubusercontent.com/Techie-Harpreet/Python-Django-Bulk-Mail-Sender/refs/heads/main/images/single%20mail%20send%20page.png)

1. Navigate to the **Single Email** section.
2. Enter the recipient email address and message.
3. Click **Send** to instantly send the email.

### 4️⃣ Bulk Email Sending
![Bulk Email Dashboard](https://raw.githubusercontent.com/Techie-Harpreet/Python-Django-Bulk-Mail-Sender/refs/heads/main/images/bulk%20mail%20send%20page.png)

1. Go to the **Bulk Email** section.
2. Upload a [**formatted CSV file**](https://github.com/Techie-Harpreet/Python-Django-Bulk-Mail-Sender/blob/main/data.csv) containing email addresses.
3. Click **Send** and Celery & Redis will process emails in the background.



## 🤝 Contributing
If you want to contribute to this project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add some feature'`).
4. Push the changes (`git push origin feature-branch`).
5. Create a Pull Request.

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
📢 Connect with Me

🔗[LinkedIn](https://www.linkedin.com/in/harpreetsinghbansal/)

📧 Email: contact@harpreetsinghbansal.com

---
🙌 **If you like this project, don't forget to ⭐ it!**
---


