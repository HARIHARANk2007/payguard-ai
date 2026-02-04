# PayGuard AI 🛡️

An AI-powered fraud detection system for payment transactions. PayGuard AI uses explainable rule-based risk scoring to help users identify potentially fraudulent payments before approving them.

## Features

- **Real-time Risk Assessment** – Instantly evaluate transaction safety
- **Explainable AI** – Clear reasons for each risk decision
- **Simple UI** – Easy-to-use web interface
- **REST API** – Integrate with any payment system

## Risk Scoring Rules

| Rule | Condition | Points |
|------|-----------|--------|
| High Amount | ≥ ₹10,000 | +40 |
| New Payee | First-time recipient | +30 |
| Urgency | Pressure detected | +20 |
| Unusual Time | Night transaction | +10 |

**Risk Levels:**
- 🔴 **HIGH** (≥70 points) – Block or review
- 🟠 **MEDIUM** (40-69 points) – Proceed with caution
- 🟢 **LOW** (<40 points) – Safe to proceed

## Project Structure

```
payguard-ai/
├── backend/
│   ├── main.py           # FastAPI server
│   ├── risk_engine.py    # Risk calculation logic
│   ├── test_engine.py    # Test script
│   └── requirements.txt  # Python dependencies
├── frontend/
│   └── index.html        # Web UI
└── README.md
```

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/payguard-ai.git
cd payguard-ai
```

### 2. Set up the backend

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt
```

### 3. Run the server

```bash
cd backend
uvicorn main:app --reload
```

Server runs at `http://127.0.0.1:8000`

### 4. Open the frontend

Open `frontend/index.html` in your browser.

## API Usage

### POST `/check-transaction`

**Request:**
```json
{
  "amount": 25000,
  "new_payee": 1,
  "time_of_day": "night",
  "urgent": 1
}
```

**Response:**
```json
{
  "risk_level": "HIGH",
  "reasons": [
    "High transaction amount",
    "Payment to a new payee",
    "Urgency or pressure detected",
    "Unusual transaction time"
  ]
}
```

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **Frontend:** HTML, CSS, JavaScript
- **API Docs:** Swagger UI at `/docs`

## License

MIT License

---

Built with ❤️ for safer digital payments
