from playwright.async_api import async_playwright
import os
import requests
from  openai import OpenAI 
from dotenv import load_dotenv
import gradio as gr
from bs4 import BeautifulSoup

def create_brochure(url_to_scrape):
    result= scrape_content(url_to_scrape)
    soup = BeautifulSoup(result, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    text= ''
    links=[]
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    links = [link.get('href') for link in soup.find_all('a')]
    links = [link for link in links if link]
    return f"the scrape result is as follows:\n \
         {title} \n\n \
            {text} \n \n \
                {links} \n \n"

def scrape_content(url_to_scrape):
    response = requests.get(url_to_scrape).content
    return response

app = gr.Interface(
    fn=create_brochure,
    inputs=["text"],
    outputs=gr.Textbox(),
    theme="gradio/monochrome"
)

app.launch()

