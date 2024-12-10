#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    response = '<h4 style = "text-align: center;"> Welcome ' + input_text + '! <br> Status: 200 OK </h4>'
    return response, 200

if __name__ == '__main__':
	    app.run(debug=True)