from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/products")
def products():
    return send_from_directory(".", "products.html")

@app.route("/about")
def about():
    return send_from_directory(".", "about.html")

@app.route("/contact")
def contact():
    return send_from_directory(".", "contact.html")

@app.route("/login")
def login():
    return send_from_directory(".", "login.html")

@app.route("/cart")
def cart():
    return send_from_directory(".", "cart.html")

@app.route("/checkout")
def checkout():
    return send_from_directory(".", "checkout.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))