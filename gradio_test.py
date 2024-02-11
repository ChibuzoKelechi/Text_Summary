import gradio
from gradio_client import Client
from transformers import pipeline

summarizer = pipeline(task="summarization")


def summarize_text(text):
    # summary = summary(text)
    return 'summary'


app = gradio.Interface(
    title='Text Summarizer',
    fn=summarize_text,
    inputs='text',
    outputs='text'
)

app.launch()