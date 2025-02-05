from playwright.async_api import async_playwright
import os
import requests
from  openai import OpenAI 
from dotenv import load_dotenv
import gradio as gr

async def scrape_content(url_to_scrape):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url_to_scrape)
        content = await page.content()  # Scrape the entire HTML content of the page
        await browser.close()
        print(content)
        return content

app = gr.Interface(
    fn=scrape_content,
    inputs=["text"],
    outputs=gr.Textbox(),
)

app.launch()

