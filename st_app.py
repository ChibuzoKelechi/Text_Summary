import streamlit as str 
from PyPDF2 import PdfReader

from transformers import pipeline

summarizer = pipeline(task="summarization")

str.set_page_config(
    page_title='Text Summarizer'
)

str.title('Text Summarization')

def summarize_text(text):
    summary = summarizer(text)
    summary = summary[0]['summary_text']
    return summary

input = str.text_area('Enter long text')

output = summarize_text(input)


if str.button('Summarize text'):
    str.markdown(f'''
            <div style="background-color: black; color: white; font-weight: bold; padding: 1rem; border-radius: 10px;">
            <h4>Results</h4>
                <p>
                    {output}
                </p>
            </div>
                ''', unsafe_allow_html=True)
    str.success('Done')
    
    
#####

# PDF summary section
str.subheader('PDF summary')

try:
    uploaded_pdf = str.file_uploader('Choose a pdf file', type=['pdf'])

    if uploaded_pdf is not None:
        str.success('Succesfully uploaded')
        
    def extract_text(pdf_file):
        pdf_content = PdfReader(pdf_file)
        pages =  pdf_content.pages
        # page_count = len(pages)
        page_text = pages[17].extract_text()

        return page_text


    pdf_input = extract_text(uploaded_pdf)

    pdf_output = summarize_text(pdf_input)

except:
    str.error('Please select a valid file')  




if str.button('Summarize pdf page'):
    str.markdown(f'''
            <div style="background-color: black; color: white; font-weight: bold; padding: 1rem; border-radius: 10px;">
            <h4>Results</h4>
                <p>
                    {pdf_output}
                </p>
            </div>
                ''', unsafe_allow_html=True)
    str.success('PDF page summarized :)', icon="✅")