NLP Text Analyzer App

This is a simple Natural Language Processing (NLP) web application built with Python and Streamlit. It allows users to input a block of text and perform basic NLP tasks, including sentiment analysis, keyword extraction, and simple text summarization.

Features
Sentiment Analysis: Determines the overall sentiment (positive, negative, or neutral) of the input text using the TextBlob library with a Naive Bayes analyzer. It also provides polarity and subjectivity scores.

Keyword Extraction: Identifies important noun phrases within the text.

Text Summarization: Provides a very basic summary by extracting the first few sentences of the input.

Requirements
To run this application, you need to have Python installed on your system. The required libraries are listed below and can be installed via pip:

streamlit

textblob

How to Run
Save the file: Save the provided Python code as app.py.

Install dependencies: Open your terminal or command prompt and run the following command to install the required libraries:

pip install streamlit textblob

If you encounter an error, you may need to install the TextBlob corpora. You can do this by running:

python -m textblob.download_corpora

Run the app: From the same directory where you saved app.py, execute the following command:

streamlit run app.py

A new browser tab will automatically open, and the NLP Text Analyzer app will be ready for you to use.

About the Code
The application is contained in a single Python script (app.py). It uses Streamlit's widgets like st.title, st.text_area, and st.button to create the user interface. The core NLP logic is handled by the TextBlob library, which provides a simple and intuitive API for common text processing tasks.
