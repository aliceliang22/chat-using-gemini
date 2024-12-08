#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <main style = " text-align: center; ">
        <h2> Chat With Private Data Using Gemini from Google </h2>
        <h4> Developed by Alice Liang </h4>

        <form action="/echo_user_input" method="POST">
            <input name="user_input">
            <input type="submit" value="Enter">
        </form>
    </main>
    '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text

if __name__ == '__main__':
	    app.run(debug=True)