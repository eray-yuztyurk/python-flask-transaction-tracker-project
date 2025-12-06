# Transaction Tracker (Flask Project)

This is a small Flask app I put together to practice how basic CRUD operations,
forms, and templates work in a simple web application.  
The idea is pretty straightforward: you can add transactions, edit them,
remove them, search by amount and see the total balance.

It’s not connected to a real database — everything stays in memory — which keeps
the project easy to understand while experimenting with Flask.

---
## Table of Contents
- [What the App Includes](#what-the-app-includes)
- [Project Structure](#project-structure)
- [How the Data Works](#how-the-data-works)
- [Routes](#routes)
- [How to Run the App](#how-to-run-the-app)
- [About This Project](#about-this-project)
- [License](#license)
  
## What the App Includes

- A table showing all transactions
- Buttons to edit or delete any record
- A form to add new transactions
- A form to update existing ones
- A simple search page (min/max amount)
- Automatic total balance calculation
- A clean UI thanks to Bootstrap

Nothing fancy, just the essentials to see the full flow of a small Flask app.

---

## Project Structure

```
python-flask-transaction-tracker-project/
│
├─ app.py
├─ templates/
│   ├─ transactions.html
│   ├─ form.html
│   ├─ update.html
│   └─ search.html
└─ requirements.txt
```

The structure is kept minimal so the focus stays on the Flask logic.

---

## How the Data Works

All transaction records are stored in a simple Python list.  
Each new entry gets an auto-incremented ID so it’s easy to update or remove it.

Since it's in memory, the data resets every time the server restarts — which is
fine for a small practice project like this.

---

## Routes

| Route | Method | Purpose |
|-------|--------|----------|
| `/` | GET | Show all transactions |
| `/append` | GET/POST | Add a new transaction |
| `/update/<id>` | GET/POST | Update an existing one |
| `/delete/<id>` | GET | Delete a transaction |
| `/search` | GET/POST | Filter transactions by amount |

Each page is rendered with a Jinja2 template.

---

## How to Run the App

1. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:

   ```bash
   python app.py
   ```

4. Open the app in your browser:

   ```
   http://127.0.0.1:8080
   ```

---

## About This Project

This was mainly built to get a better feel for Flask:
routing, handling forms, passing values into templates, and managing simple data.
It’s also something I made as a practice exercise based on what I learned in my course,
so it reflects the concepts I was working through at the time.

---

## License

MIT License.
