# The NLP Text Analyzer app uses Streamlit and TextBlob to analyze text.
# To run this file, save it as 'app.py' and run `streamlit run app.py` in your terminal.
# You will need to install the libraries first: `pip install streamlit textblob`

import streamlit as st
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# --- Application setup ---
st.set_page_config(page_title="NLP Text Analyzer", page_icon="✍️", layout="wide")

st.title("✍️ NLP Text Analyzer")
st.markdown("Enter a block of text below to perform various NLP tasks.")

# --- Sample Text and User Input ---
sample_text = """
Streamlit is an amazing open-source Python library that makes it incredibly easy to create
beautiful, custom web apps for machine learning and data science. It is a fantastic tool
for data scientists and developers who want to share their work without needing to
be a web development expert. I'm absolutely loving the simplicity and power of this library.
"""

# Text area for user input
text_input = st.text_area(
    "Enter your text:",
    value=sample_text,
    height=250,
    placeholder="Type or paste your text here..."
)

# --- Analysis Button ---
if st.button("Analyze Text"):
    if text_input:
        # Default TextBlob for polarity/subjectivity
        blob_default = TextBlob(text_input)
        # Naive Bayes TextBlob for classification
        blob_nb = TextBlob(text_input, analyzer=NaiveBayesAnalyzer())

        # --- 1. Sentiment Analysis ---
        st.subheader("Sentiment Analysis")
        # Get sentiment polarity (from -1.0 to 1.0) and subjectivity (from 0.0 to 1.0)
        st.info(f"**Polarity:** {blob_default.sentiment.polarity:.2f} (Positive is > 0, Negative is < 0)")
        st.info(f"**Subjectivity:** {blob_default.sentiment.subjectivity:.2f} (Subjective is > 0.5, Objective is < 0.5)")

        # Use the Naive Bayes analyzer for classification
        sentiment_result = blob_nb.sentiment.classification

        if sentiment_result == 'pos':
            st.success(f"Overall sentiment is: **Positive**")
        elif sentiment_result == 'neg':
            st.error(f"Overall sentiment is: **Negative**")
        else:
            st.warning(f"Overall sentiment is: **Neutral**")

        st.markdown("---")

        # --- 2. Keyword Extraction (Noun Phrases) ---
        st.subheader("Keyword Extraction (Noun Phrases)")
        noun_phrases = blob_default.noun_phrases
        if noun_phrases:
            st.markdown(f"**Found {len(noun_phrases)} key phrases:**")
            for phrase in noun_phrases:
                st.write(f"- {phrase}")
        else:
            st.warning("No significant noun phrases found.")

        st.markdown("---")

        # --- 3. Text Summarization (Simple Sentence Extraction) ---
        st.subheader("Text Summarization (Simple Method)")
        sentences = [str(s) for s in blob_default.sentences]
        if len(sentences) > 2:
            summary = " ".join(sentences[:2])
            st.write(summary + "...")
        else:
            st.write("The text is too short to summarize.")

    else:
        st.warning("Please enter some text to analyze.")
