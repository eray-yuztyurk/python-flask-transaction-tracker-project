# imports & instantiation
from flask import Flask, request, url_for, redirect, render_template
app = Flask("Financial Transaction App")

# Record samples
transaction_records = [
    {'id': 101, 'date': '2024-01-10', 'amount': 150},
    {'id': 102, 'date': '2024-01-11', 'amount': 220},
    {'id': 103, 'date': '2024-01-12', 'amount': -80},
    {'id': 104, 'date': '2024-01-13', 'amount': 340},
    {'id': 105, 'date': '2024-01-14', 'amount': -120},
    {'id': 106, 'date': '2024-01-15', 'amount': 500},
    {'id': 107, 'date': '2024-01-16', 'amount': -60},
    {'id': 108, 'date': '2024-01-17', 'amount': 275},
    {'id': 109, 'date': '2024-01-18', 'amount': 430},
    {'id': 110, 'date': '2024-01-19', 'amount': -95},
    {'id': 111, 'date': '2024-01-20', 'amount': 380},
    {'id': 112, 'date': '2024-01-21', 'amount': 210}
]

# CRUD Operations
# READ operation
@app.route("/", methods=["GET"])
def get_transactions():
    _total = 0
    for ta in transaction_records:
        _total += float(ta["amount"])

    return render_template("transactions.html", 
                            transaction_records=transaction_records, 
                            show_add_button=True,
                            total_balance=_total)

# CREATE operation
@app.route("/append", methods=["GET", "POST"])
def append_transaction():
    if request.method == "GET":
        return render_template("form.html")

    if request.method == "POST":

        new_transaction = {
            'id': len(transaction_records) + 1,
            'date': request.form["date"],
            'amount': float(request.form["amount"])
        }

        transaction_records.append(new_transaction)

        return redirect(url_for("get_transactions"))

# UPDATE operation
@app.route("/update/<int:transaction_id>", methods=["GET", "POST"])
def update_transaction(transaction_id):
    if request.method == "GET":
        for ta in transaction_records:
            if int(ta["id"]) == transaction_id:
                return render_template("update.html", transaction = ta)

        else:
            return {"message": f"Transaction {transaction_id} could not be found"}, 404

    if request.method == "POST":
        for ta in transaction_records:
            if int(ta["id"]) == transaction_id:
                ta["date"] = request.form["date"]
                ta["amount"] = float(request.form["amount"])
                break

        return redirect(url_for("get_transactions"))  

# DELETE operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for ta in transaction_records:
        if ta["id"] == transaction_id:
            transaction_records.remove(ta)
            break
            
    return redirect(url_for("get_transactions"))

# SEARCH Transaction
@app.route("/search", methods=["GET", "POST"])
def search_transaction():
    if request.method == "POST":
        _min = float(request.form["min_amount"])
        _max = float(request.form["max_amount"])
        
        found_transactions = []

        for ta in transaction_records:
            if ta["amount"] >= _min and ta["amount"] <= _max:
                found_transactions.append(ta)

        return render_template("transactions.html", transaction_records=found_transactions, heading="Found Transactions")

    return render_template("search.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(port=8080, debug=True)