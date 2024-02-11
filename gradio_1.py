import gradio
from gradio_client import Client
from transformers import pipeline

summarizer = pipeline(task="summarization")


def summarize_text(text):
    summary = summarizer(text, max_length=84)
    summary = summary[0]['summary_text']
    return summary


app = gradio.Interface(
    title='Text Summarizer',
    fn=summarize_text,
    inputs='text',
    outputs='text'
)

app.launch()