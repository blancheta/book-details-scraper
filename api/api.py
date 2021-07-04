from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests

# flask start
app = Flask(__name__)
app.config["DEBUG"]=True

@app.route('/', methods = ['GET'])
def home():
    return "<h1> copy this link and add ibsn code to get book details </h1> <p>http://127.0.0.1:5000/api/v1/book-details/?ibsn=</p>"


@app.route('/api/v1/book-details/', methods=["GET"])
def get_book_detils():
    ibsn = request.args.get('ibsn')
    # connect to website
    url = "https://www.paperbackswap.com/book/browser.php?k=" + ibsn
    html = requests.get(url)
    # -------------------- SCRAPING --------------------------#
    soup = BeautifulSoup(html.text, 'html.parser')

    isbn = soup.find("span", itemprop="isbn").text
    title = soup.find(class_="book_title").text
    try:
        description = soup.find("span", itemprop="description").text
    except :
        description = ""
    num_pages = soup.find("span", itemprop="numPages").text
    
    book_author = soup.find(class_="book_author").text
    categorie = soup.find("ul", itemprop="genre")
    cover = soup.find(id="book_image_l")['src']
    categorie_list = []
    for i in categorie:
        categorie_list.append(i.text)

    return jsonify(
        isbn = ibsn,
        title = title,
        description = description,
        num_pages = num_pages,
        book_author =book_author,
        categorie = categorie_list,
        book_cover_url = cover

    ), 200

app.run()