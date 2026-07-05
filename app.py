from flask import Flask, send_from_directory

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

if __name__ == "__main__":
    app.run(debug=True)