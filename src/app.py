#!/usr/bin/env python3

from flask import Flask, request, render_template
from .datacollector import load_files

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist("documents")
    documents = load_files(files)

    # Message for successfully uploading documents
    filenames = []
    for file in files:
        if file != None and file.filename != '':
            filenames.append(file.filename)

    message = "The following documents are successfully uploaded: " + ", ".join(filenames) + ". <br> Status: 200 OK"

    return message

if __name__ == '__main__':
	    app.run(debug=True)