#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <main style = " text-align: center; ">
        <h2> Chat With Private Data Using Gemini from Google </h2>
        <h4> Developed by Alice Liang </h4>
        <p> Please enter your text in the following text box, then hit the submit button </p>
        <form action="/echo_user_input" method="POST">
            <input name="user_input">
            <input type="submit" value="Sobmit">
        </form>
    </main>
    '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    response = "You entered: " + input_text + "<br> Status: 200 OK"
    return response, 200

if __name__ == '__main__':
	    app.run(debug=True)