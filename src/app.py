#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist("documents")
    return "Documents Uploaded Successfully. <br> Status: 200 OK"

if __name__ == '__main__':
	    app.run(debug=True)