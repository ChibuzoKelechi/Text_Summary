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

if st.button('Summarize text'):
    with st.spinner('Summarizing'):
         output = summarize_text(input)
         st.success('Summary complete ')
        
    st.markdown(f'''
            <div style="background-color: black; color: white; font-weight: bold; padding: 1rem; border-radius: 10px;">
            <h4>Results</h4>
                <div>
                    {output}
                </div>
            </div>
                ''', unsafe_allow_html=True)
    
    
    
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

        return page_text_stack
    


except: # Handle blank file error
    st.error('Please select a valid file')


def check_page_count(pdf):
    pdf_content = PdfReader(pdf)
    pages =pdf_content.pages
    page_count = len(pages)
    
    return page_count
    

# Processs to trigger summary
if st.button('Summarize pdf content'):
    with st.spinner('Extracting text from PDF...'):
        pdf_input = extract_text(uploaded_pdf)
        st.success('Text extracted')

    num_of_pages = check_page_count(uploaded_pdf)
    st.success(f'NUmber of pages is {num_of_pages}.')
    
    pdf_output = []
    
    for stack in pdf_input:
        summarize_text(stack)
        pdf_output.append(stack)
    
    with st.spinner('Summarizing extracted text...'):
        pdf_summary = '\n\n'.join(pdf_output)
        st.success('Summary complete')

        
    st.markdown(f'''
            <div style="background-color: black; color: white; font-weight: bold; padding: 1rem; border-radius: 10px;">
             <h4>Summary </h4>
                <p>{pdf_summary}</p>
            </div>
                ''', unsafe_allow_html=True)
    
    st.success('PDF page summarized :)', icon="✅")
    
    
    # if st.button('Generate pdf download link'):
    #     download_button = st.download_button(label='Download summary PDF', data=pdf_summary, file_name='summary.pdf', mime='application/pdf')   
        

  

st.write('')
st.write('')


st.markdown("<hr style='border: 1px dashed #ddd; margin: 2rem;'>", unsafe_allow_html=True) #Horizontal line

st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        Project by <a href="https://github.com/ChibuzoKelechi" target="_blank" style="color: white; font-weight: bold; text-decoration: none;">
         kelechi_tensor</a>
    </div>
    
    <div style="text-align: center; padding: 1rem;">
        Resources <a href="https://huggingface.co" target="_blank" style="color: white; font-weight: bold; text-decoration: none;">
         Hugging face</a>
    </div>
""",
unsafe_allow_html=True)
