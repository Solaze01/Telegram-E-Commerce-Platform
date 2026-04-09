# 🛒 Telegram Marketplace Bot

> A full-featured, location-based marketplace built entirely inside Telegram.  
> Buyers discover nearby sellers, browse products, pay with crypto, and track deliveries — all without leaving the chat.

---

## 📹 Live Demo

[![Watch Demo](https://img.shields.io/badge/▶%20Watch%20Full%20Demo-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/b6v8RweIGVQ?si=xVlr6EX1AVsMH5h1)

> See the full buyer & seller experience in action — product browsing, cart, crypto payment, delivery tracking, and more.

---

## ✨ Features

### 👤 User System
- Role-based registration — choose **Buyer** or **Seller**
- Channel membership gating before access
- Referral system with affiliate discounts
- Location-based onboarding (address or live location)

### 🏪 Seller Side
- Create and manage a personal store
- Add products with name, price, description, stock, min quantity & image
- Edit or delete listings anytime
- View sales history & earnings
- Receive and confirm orders with delivery proof (photos)
- Wallet setup for crypto payouts

### 🛍️ Buyer Side
- Discover **nearby sellers** based on location
- Browse seller catalogues with product details
- Add to cart, adjust quantities, checkout
- Pay securely via **CryptoPay** (BTC, TON, USDT, etc.)
- Track order status & delivery updates
- Leave reviews and ratings per product

### 🤝 P2P Marketplace
- Create buy/sell crypto offers
- Browse and accept peer offers
- Secure transaction flow between users

### 💰 Payments & Payouts
- Integrated with **CryptoPay API** for live payments
- Automatic commission deduction (10%)
- Weekly payout reports for sellers
- Crypto wallet address management

### ⭐ Reviews & Trust
- Buyers review products after delivery
- Star ratings + written comments
- Sellers can view all their reviews

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-20.7-2CA5E0?style=flat&logo=telegram&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-316192?style=flat&logo=postgresql&logoColor=white)
![CryptoPay](https://img.shields.io/badge/CryptoPay-Payments-F7A600?style=flat)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=flat)

| Layer | Technology |
|---|---|
| Bot Framework | python-telegram-bot 20.7 |
| Database | PostgreSQL (psycopg2) |
| Payments | CryptoPay API |
| Hosting | Render |
| Location | Geocoding + distance calculation |
| Receipts | ReportLab PDF generation |

---

## ⚙️ Environment Variables

```env
BOT_TOKEN=your_telegram_bot_token
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432
DB_SSLMODE=require
CRYPTO_PAY_TOKEN=your_cryptopay_token
REQUIRED_CHANNEL=@yourchannel
CHANNEL_LINK=https://t.me/yourchannel
```

---

## 🚀 Setup

```bash
# 1. Clone the repo
git clone https://github.com/Solaze01/Telegram-E-Commerce-Platform.git
cd Telegram-E-Commerce-Platform

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your environment variables (create a .env file)

# 4. Run the bot
python bot.py
```

---

## 📁 Project Structure

```
├── bot.py              # Main bot logic & conversation handlers
├── database.py         # All database operations
├── config.py           # Environment config
├── utils.py            # Helper functions (geo, crypto, referrals)
├── payout_reporter.py  # Weekly seller payout reports
├── receipt_generator.py # PDF receipt generation
├── requirements.txt
├── Procfile            # For Render deployment
└── runtime.txt
```

---

## 💼 Built for a Client

This bot was commissioned and delivered as a complete product for a real business.  
Full source code is available **upon request** for serious inquiries.

> 🔒 *Client data and credentials are not included in this repository.*

---

## 📬 Want a Custom Bot?

I build Telegram bots for businesses, communities, and automation workflows.

[![Telegram](https://img.shields.io/badge/Telegram-@solaze__tech-2CA5E0?style=flat&logo=telegram)](https://t.me/solaze_tech)
[![Twitter](https://img.shields.io/badge/Twitter-@solazetech-1DA1F2?style=flat&logo=twitter&logoColor=white)](https://x.com/solazetech)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-brightgreen?style=flat)](https://aderinsola-1.github.io/Ezekiel/)
