# RB Rate Limit Lab 🔒

**RB Education Hub Labs** ka ek practical demo jisme hum  
**Rate Limiting & Brute Force Protection** ko samajhte aur test karte hain.

Is lab ka purpose hai dikhana:

- Kaise **login page** brute-force ke liye vulnerable ho sakta hai
- Kaise basic **rate limit protection** lagai ja sakti hai
- Kaise attacker **rate limit ko bypass** karne ki koshish karta hai (Burp Suite use karke)

---

## 🧪 Features

- `login-vulnerable` → **No Rate Limit** (Brute Force friendly 😈)
- `login` → **Rate Limiting Enabled**
  - Max 3 wrong attempts
  - Phir temporary block (20 seconds)
- Simple & colourful UI (TailwindCSS)
- Perfect for:
  - Students
  - Bug Bounty beginners
  - Cyber Security training

---

## 🛠 Requirements

- Python 3.8+  
- `pip` installed

---

## 📦 Installation

```bash
git clone https://github.com/rbrizwan89-ctrl/RB-RateLimit-Lab.git
cd RB-RateLimit-Lab
pip install flask
