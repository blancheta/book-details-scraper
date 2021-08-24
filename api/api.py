"""
Book scraping API.
This api scrape paperbackswap website to get book request details
"""
import logging

from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests

# flask start
app = Flask(__name__)
app.config["DEBUG"] = True


class BadRequestException(Exception):
    """bad request inherit exception class"""

    pass


@app.route("/", methods=["GET"])
def home():
    """home page"""
    return (
        "<h1> copy this link and add ibsn code to get book details </h1> "
        "<p>http://127.0.0.1:5000/api/v1/book-details/?ibsn=</p> "
    )


@app.route("/api/v1/book-details/", methods=["GET"])
def get_book_details():
    """get book details"""
    # test and log
    url_test = "https://www.paperbackswap.com/book/browser.php?k=9782746040885"
    find_test = BeautifulSoup(requests.get(url_test).text, "html.parser").find(
        "span", itemprop="isbn"
    )
    # if the website code has been modified, then we intercept our code and send an error
    if find_test is None:
        logging.error("ALERT: the website code has modified")
        return (
            jsonify(
                error={
                    "code": "target_website_modified_error",
                    "message": "Target website has been modified",
                }
            ),
            422,
        )
    # we get the ibsn, we check and we return a message according to the result
    ibsn = request.args.get("ibsn")
    if not ibsn:
        raise BadRequestException("Bad request exception, isbn is missing")

    # connect to website
    url = "https://www.paperbackswap.com/book/browser.php?k=" + ibsn
    html = requests.get(url)
    # -------------------- SCRAPING --------------------------#
    soup = BeautifulSoup(html.text, "html.parser")
    try:
        isbn = soup.find("span", itemprop="isbn").text
        title = soup.find(class_="book_title").text

        if soup.find("span", itemprop="description"):
            description = soup.find("span", itemprop="description").text
        else:
            description = ""

        num_pages = soup.find("span", itemprop="numPages").text

        book_author = soup.find(class_="book_author").text
        categorie = soup.find("ul", itemprop="genre")
        cover = soup.find(id="book_image_l")["src"]
        categorie_list = [item.text for item in categorie]

        return (
            jsonify(
                isbn=isbn,
                title=title,
                description=description,
                num_pages=num_pages,
                book_author=book_author,
                categorie=categorie_list,
                book_cover_url=cover,
            ),
            200,
        )
    except Exception as e:
        logging.error(e)
        return (
            jsonify(
                error="<isbn> is incorrect",
            ),
            400,
        )


app.run()
