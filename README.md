# chat-using-gemini
## CSCA 5028 Applications of Software Architecture for Big Data Final Project
### By Alice Liang
## Link to [app](https://chat-using-gemini-9141a48a06cb.herokuapp.com/)

### Project Description

The product I developed for this course is a web application that will try to solve the problem of interacting with private & business specific data using a large language model (LLM). Existing LLMs like ChatGPT are not trained with any private company data. This limits the knowledge necessary to address questions regarding customer support, operations, company operations, employee benefits, etc. This project is geared towards businesses, specifically customer service, HR departments, and employees who need accurate and fast access to private company information. What is unique about this product is its ability to integrate a LLM with private data. Users will be able to upload documents in formats such as .doc, .docx, .txt, .pdf, and .html, and ask questions based on the contents of those documents. This system is built using a combination of a vector database FAISS, LangChain framework, and a front-end interface to process the data and give answers based on user input.

### Project Architecture

The following diagram shows the architecture and workflow of the application:
![picture of diagram](https://github.com/aliceliang22/chat-using-gemini/blob/main/src/static/images/diagram.jpg)

#### This application includes the following components (see diagram):
1. Front End (Web Page):
    - A form with two HTML inputs (types of File and Submit) for selecting users' private data (documents in .doc, .docx, .txt, .pdf, and .html formats) from local folders and for uploading users' private data to the database in the back end.
    - A form with two HTML inputs (types of Text and Submit) for entering questions related to the provided private data and for submitting questions to the back end.
    - A text box for displaying the answers for questions related to the provided private data.
2. Back End:
    - A data collector with 4 loaders (Word  loader, text loader, PDF loader and HTML loader) for loading user’s private data in different formats of files.
    - A vector database FAISS (Facebook AI Similarity Search) for storing user’s data in smaller segmented chunks as vector in Python Numpy array for quick scalable similarity search of the multimedia data.
    - A data analyzer for analyzing a user's question with chat history and finding the answer from the FAISS database using the large language model Gemini from Google.

### Communications between Components
#### Communications between different components are as follows:

1. Communication between Front End and Data Collector

    After the user selects file(s) from his/her local folder and hits the Upload button, the form for uploading files uses the Action call-back to call the REST endpoint ‘/upload’ defined by Python Flask (see upload() function in app.py), which then calls the data collector to load different formats of data using the corresponding data loaders (see load_file() function in datacollector.py) and returns all uploaded documents to the upload() function.

2. Communication between Data Collector and Vector Database FAISS

    After upload() functions gets all uploaded documents, it then call the save_to_database() function in database.py to split all documents into small chunks (or tokens) using LangChain’s splitter and save the tokens in the form of matrix (based on token similarities) to the vector database FAISS.

3. Communication among Front End, Data Analyzer and Vector Database FAISS

    A REST endpoint ‘/’ with POST method and main() function in app.py is used for accepting Http requests for user’s questions from the front end web page using JavaScript AJAX (Asynchronous JavaScript and XML) API. Then, the main() function passes the question with chat history to the chat() function in dataanalyzer.py, which then use LangChain’s conservation retrieve chain with Google’s Gemini model to find answer from FAISS database (based on similarity) and returns the answer to the end point ‘/’ function main(). Consequently, the function main() sends the answer as HTTPresponse back to the AJAX function. AJAX function then generates HTML tags for displaying the answer to the front end web page.
