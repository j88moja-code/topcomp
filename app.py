from flask import Flask, render_template, jsonify
from database import load_laptops_from_db

app = Flask(__name__)


@app.route("/")
def hello_topcomp():
  laptops = load_laptops_from_db()
  return render_template("home.html", laptops=laptops)


@app.route("/api/laptops")
def list_laptops():
  laptops = load_laptops_from_db()
  return jsonify(laptops)


# @app.route("/laptop/<id>")
# def show_laptop(id):

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
