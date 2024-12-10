#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify
from .datacollector import load_files
from .database import save_to_database
from .dataanalyzer import chat
import os

app = Flask(__name__)

if "GOOGLE_API_KEY" not in os.environ:
    os.environ['GOOGLE_API_KEY'] = 'AIzaSyBLO1FX2OkTeShNK7Q6c2_nwu6FadObZn8'

chat_history = []

@app.route("/", methods=['GET', 'POST'])
def main():
    global chat_history

    if request.method == 'POST':
        # chat with database using Google's Gemini
        prompt = request.form["prompt"]
        answer, chat_history = chat(prompt, chat_history, "faiss")

        # Create response in Json format for request from web page
        response = {}
        response["answer"] = answer
        return jsonify(response), 200
    else:
        chat_history = []
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

    count = len(files)
    is_are = "s are" if (count > 1) else " is"
    message = '<h3 style = "font-family:Courier New; text-align: center;"> The following file' + is_are + ' successfully uploaded: ' + ', '.join(filenames) + '.'

    # Save documents to vector database
    if documents and len(documents) > 0:
        # Create a vector store (database) using FAISS
        save_to_database(documents, "faiss")

        message += "<br>File" + is_are + " also saved to the database."

    message += "<br>Please click the left arrow at the top-left corner of your browser to go back and continue to chat. <br> Status: 200 OK"

    return message

if __name__ == '__main__':
	    app.run(debug=True)