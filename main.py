import requests
from bs4 import BeautifulSoup  as scrapy
from urllib.parse import urlparse
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from flask import Flask, request, send_from_directory
import os
import json

#app flask mak api function
app = Flask(__name__)

# Create the ThreadPoolExecutor outside the fast_download function.
executor = ThreadPoolExecutor()

@app.route('/', methods=['GET'])
def home():
    return """<!DOCTYPE html>
<html>
<head>
    <style>
        /* CSS styles */
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 20px;
        }

        h1 {
            color: #333;
            font-size: 24px;
        }

        p {
            color: #666;
            font-size: 16px;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            border-radius: 4px;
            padding: 30px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .api-link {
            color: #007bff;
            text-decoration: none;
        }

        .api-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>How to Use this API?</h1>
        <p>
            To use the API, make a GET request to the following URL:
            <br>
            <a href="https://webpage.com/apii?url=(pdf_url)" class="api-link">https://webpage.com/apii?url=(pdf_url)</a>
        </p>
        <p>
            Replace "(pdf_url)" in the URL with the actual URL of the PDF file you want to retrieve data from.
        </p>
    </div>
</body>
</html>
"""

payload = {}
headers = {
  'authority': 'homework.study.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'max-age=0',
  'dnt': '1',
  'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
def study(url):
    try:
        response = requests.request("GET", f'http://api.scraperapi.com?api_key=<your_api>&url={url}', headers=headers, data=payload)
        soup = scrapy(response.content, 'html.parser')
        x0 = soup.find('div','</div>',class_="headerTitle maxWidth")
        wikiContent = soup.find('div','</div>',class_="wikiContent")
        answerhtml=str('''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>NX pro</title>
            <meta name="description" content="">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="shortcut icon" type="image/x-icon" href="assets/img/favicon.ico">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css">
            <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-mml-chtml.min.js"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous">
        <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js" integrity="sha384-XjKyOOlGwcjNTAIQHIpgOno0Hl1YQqzUOEleOLALmuqehneUG+vnGctmUb0ZY0l8" crossorigin="anonymous"></script>
        <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                renderMathInElement(document.body, {
                // customised options
                // • auto-render specific keys, e.g.:
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false},
                    {left: '{eq}', right: '{/eq}', display: false},
                    {left: '\begin{align*}', right: '\end{align*}', display: true},
                    {left: '\\(', right: '\\)', display: false},
                    {left: '\\[', right: '\\]', display: true}
                ],
                // • rendering keys, e.g.:
                throwOnError : false
                });
            });
        </script>
        </head>
        <body>
            <div class="container">
                <div id="app">
                    <div class="container">
                        <div class="section">
                            <div class="box" style="word-break: break-all;">
                                <h1>Question Link</h1>
                                <div class="url">'''+str(url)+'''</div>

                            </div>
                            <div class="box">
                                <div class="content">
                                    <h1>Question</h1>
                                    <div class="questionnx">'''+str(x0)+'''</div><br>
                                    <div class="rate">
                                        <h3>Expert-verified <img src="https://png.pngtree.com/png-clipart/20230422/original/pngtree-instagram-bule-tick-insta-blue-star-vector-png-image_9074860.png" style="width:27px;"></h3>
                                    </div>
                                    <br>

                                </div>
                            </div>
                            <div class="box">
                                <div class="content">
                                    <h1>Answer</h1>
                                    <div class="answernx"></div>'''+str(wikiContent)+'''
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                renderMathInElement(document.body, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false},
                    {left: '\\(', right: '\\)', display: false},
                    {left: '\\[', right: '\\]', display: true},
                    {left: '\\begin{align*}', right: '\\end{align*}', display: true}
                ],
                throwOnError: false
                });
            });
        </script>
        </html>''')
        return answerhtml
    except Exception as e:
       print(f"An error occurred: {e}")    


@app.route('/apii', methods=['GET'])
def process_slideshare_api():
  try:  
    with app.app_context():
        url = request.args.get('url')
        if url:
            result = study(url)
            return result
        else:
            return "Error: Missing 'url' parameter.", 400
  except Exception as e :
    print(f"An error occurred: {e}")    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
