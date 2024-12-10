#!/usr/bin/env python3

from flask import Flask, request, render_template
from .datacollector import load_files
from .database import save_to_database
from .dataanalyzer import chat
import os

app = Flask(__name__)

if "GOOGLE_API_KEY" not in os.environ:
    os.environ['GOOGLE_API_KEY'] = 'AIzaSyBLO1FX2OkTeShNK7Q6c2_nwu6FadObZn8'

chat_history = []

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    global chat_history

    files = request.files.getlist("documents")
    documents = load_files(files)

    # Message for successfully uploading documents
    filenames = []
    for file in files:
        if file != None and file.filename != '':
            filenames.append(file.filename)

    count = len(files)
    is_are = "s are" if (count > 1) else " is"
    message = '<h3 style = "font-family:Courier New; text-align: center;"> The following file' + is_are + ' successfully uploaded: ' + ', '.join(filenames) + '.'

    # Save documents to vector database
    if documents and len(documents) > 0:
        # Create a vector store (database) using FAISS
        save_to_database(documents, "faiss")

        message += "<br>File" + is_are + " also saved to the database."

    return message

if __name__ == '__main__':
	    app.run(debug=True)