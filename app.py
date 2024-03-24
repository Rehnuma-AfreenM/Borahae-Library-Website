from flask import Flask, render_template, jsonify

app = Flask(__name__)
BOOKS = [
    {
        "id": 1,
        "Book_name": "Before the coffee gets cold",
        "Author": "Toshikazu Kawaguchi",
        "Price": "Rs300",
    },
    {
        "id": 2,
        "Book_name": "Tales from the Cafe",
        "Author": "Toshikazu Kawaguchi",
        "Price": "Rs400",
    },
    {
        "id": 3,
        "Book_name": "Before Your Memory Fades",
        "Author": "Toshikazu Kawaguchi",
        "Price": "Rs400",
    },
    {
        "id": 4,
        "Book_name": "Before We Say Goodbye",
        "Author": "Toshikazu Kawaguchi",
        "Price": "Rs500",
    },
    {
        "id": 5,
        "Book_name": "Before We Forget Kindness",
        "Author": "Toshikazu Kawaguchi",
        "Price": "Rs600",
    },
]


@app.route("/")
def hello_world():
    return render_template("home.html", books=BOOKS)


@app.route("/api/books")
def list_books():
    return jsonify(BOOKS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
