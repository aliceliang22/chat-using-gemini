#!/usr/bin/env python3

import os
from flask import Flask, request, render_template
from datacollector import load_files

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)