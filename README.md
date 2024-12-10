# chat-using-gemini
## CSCA 5028 Applications of Software Architecture for Big Data Final Project
### By Alice Liang
## Link to [app](https://chat-using-gemini-9141a48a06cb.herokuapp.com/)

### Project Description

The product I developed for this course is a web application that will try to solve the problem of interacting with private & business specific data using a large language model (LLM). Existing LLMs like ChatGPT are not trained with any private company data. This limits the knowledge necessary to address questions regarding customer support, operations, company operations, employee benefits, etc. This project is geared towards businesses, specifically customer service, HR departments, and employees who need accurate and fast access to private company information. What is unique about this product is its ability to integrate a LLM with private data. Users will be able to upload documents in formats such as .doc, .docx, .txt, .pdf, and .html, and ask questions based on the contents of those documents. This system is built using a combination of a vector database FAISS, LangChain framework, and a front-end interface to process the data and give answers based on user input.

### Project Architecture

The following diagram shows the architecture and workflow of the application:
!(https://github.com/aliceliang22/chat-using-gemini/blob/main/src/static/images/diagram.jpg)