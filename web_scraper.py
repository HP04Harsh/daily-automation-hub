import time
import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
URL = "https://example-shop.com" # Replace with your product link
TARGET_PRICE = 150.00
CHECK_INTERVAL = 3600 # Check every hour (in seconds)

# Email Settings (Using a Gmail App Password is recommended)
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password" 
RECEIVER_EMAIL = "your_email@gmail.com"

# Web browser identity to prevent the website from blocking the script
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def check_price():
    try:
        response = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # FIND THE PRICE: Update the tag and class/id based on the target website
        # Example: <span id="priceblock_ourprice">$199.99</span>
        price_text = soup.find(id="priceblock_ourprice").get_text()
        
        # Clean the string to extract numerical value (e.g., "$199.99" -> 199.99)
        current_price = float("".join(c for c in price_text if c.isdigit() or c == '.'))
        
        if current_price <= TARGET_PRICE:
            send_alert(current_price)
            return True # Stop tracking once alert is sent
            
    except Exception as e:
        print(f"Error checking price: {e}")
    return False

def send_alert(price):
    msg = MIMEText(f"Good news! The price dropped to ${price}.\n\nBuy it here: {URL}")
    msg["Subject"] = "🚨 Price Drop Alert!"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP_SSL("://gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    print("Alert email sent successfully!")

if __name__ == "__main__":
    print("Starting price tracker...")
    while True:
        alert_triggered = check_price()
        if alert_triggered:
            break
        time.sleep(CHECK_INTERVAL)