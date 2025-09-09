import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

import nltk 

# Download necsessary NLTK resources on first run
@st.cache_resource(show_spinner=False)
def download_nltk_resources():
    nltk.download('punkt')  
    nltk.download('punkt_tab')
    return True
download_nltk_resources()   

st.set_page_config(page_title="Text Summarization",  layout="centered")

st.title("Text Summarization")

text = st.text_area("Enter text to summarize", height=300)
num_sentences = st.slider("Select Number of sentences in summary", 1, 10, 3)

if st.button("Summarize"):
    if not text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        try:
            #Parse the input text
            parser = PlaintextParser.from_string(text, Tokenizer("english"))         
            #initialize the textrank summarizer
            summarizer = TextRankSummarizer()
            #Generate the summary
            summary = summarizer(parser.document, num_sentences)    
            #join the sentences in the summary
            summary_text = ' '.join(str(sentence) for sentence in summary)  
            st.subheader("Summary")
            st.write(summary_text)
        except Exception as e:
            st.error(f"An error occurred while summarizing the text: {e}")
            st.write("Please ensure that the input text is valid and try again.")