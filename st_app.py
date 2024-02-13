import streamlit as st 
import pdfkit
from PyPDF2 import PdfReader

from transformers import pipeline

summarizer = pipeline(task="summarization")

# Basic text summary
st.set_page_config(
    page_title='Text Summarizer'
)

st.title('Text Summarization')

# Text summary function

def summarize_text(text):
    summary = summarizer(text)
    summary = summary[0]['summary_text']
    return summary

input = st.text_area('Enter long text')

output = summarize_text(input)


if st.button('Summarize text'):
    st.markdown(f'''
            <div style="background-color: black; color: white; font-weight: bold; padding: 1rem; border-radius: 10px;">
            <h4>Results</h4>
                <p>
                    {output}
                </p>
            </div>
                ''', unsafe_allow_html=True)
    st.success('Done')
    
    
#####

# PDF summary section

st.subheader('PDF summary')

try:
    # Upload file
    uploaded_pdf = st.file_uploader('Choose a pdf file', type=['pdf'])

    if uploaded_pdf is not None:
        st.success('Succesfully uploaded')
        
    # Extract PDF content    
    def extract_text(pdf_file):
        pdf_content = PdfReader(pdf_file)
        pages =pdf_content.pages
        # page_count = len(pages)
        
        page_text_stack = []

        for page in pages:
            page_text = page.extract_text()
            page_text_stack.append(page_text)
        
        pages_stack = []
        
        for text_stack in page_text_stack:
            pages_stack.append(text_stack)

        return page_text
    
    pdf_input = extract_text(uploaded_pdf)
    pdf_output = summarize_text(pdf_input)
    
    summary_pdf = pdfkit.from_sting(pdf_input, 'Summary.pdf')


except: # Handle blank file error
    st.error('Please select a valid file')

#  Prepare output 




if st.button('Summarize pdf page'):
    st.markdown(f'''
            <div style="background-color: black; color: white; font-weight: bold; padding: 1rem; border-radius: 10px;">
            <h4>Download the summary here </h4>
                <p>
                    {pdf_output}
                </p>
            </div>
                ''', unsafe_allow_html=True)
    st.write('Download summary pdf here')
    download_button = st.download_button(summary_pdf, label='Download summary')
    st.success('PDF page summarized :)', icon="✅")