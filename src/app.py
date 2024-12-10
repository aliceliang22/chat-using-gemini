#!/usr/bin/env python3

from flask import Flask, request, render_template
from .datacollector import load_files
from .database import save_to_database
from .dataanalyzer import chat
import getpass
import os

app = Flask(__name__)

if "GOOGLE_API_KEY" not in os.environ:
   os.environ["GOOGLE_API_KEY"] = getpass.getpass("AIzaSyBLO1FX2OkTeShNK7Q6c2_nwu6FadObZn8")

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

    message = "The following file(s) is/are successfully uploaded: " + ", ".join(filenames) + ". <br> Status: 200 OK"

    # Save documents to vector database
    if documents and len(documents) > 0:
        # Create a vector store (database) using FAISS
        save_to_database(documents, "faiss")

        message += "<br>File(s) is/are also saved to database."


    return message

if __name__ == '__main__':
	    app.run(debug=True)