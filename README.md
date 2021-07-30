# Book Details Scraper

The goal of this project is to create a flask api endpoint which is returning book details from a [isbn](https://fr.wikipedia.org/wiki/International_Standard_Book_Number).
The following information needs to be extracted from the website book details page ( book cover, title, authors, number of pages, category, short description).
No need to store data into a database.

Endpoint: /api/v1/book-details/<isbn>/ [GET Method]

Request:

```
{
  'isbn': string
}
```

Response:
```
{
  'isbn': string,
  'title': string,
  'short_description': string (optional),
  'num_pages': string,
  'authors': string (if many separated by comma)
  'category': string,
  'book_cover_url': string
}
```


To find a book detail page based ona isbn:
You will need to use selenium zith python to automatically do this actions
- Copy isbn into search bar into the page https://www.paperbackswap.com/index.php
- Click on the button "Search"
- Then, the bot needs to check that it is redirected to abook details page

Once on thepage you can extract information.
Example of page from where you can extract information:https://www.paperbackswap.com/Infernal-Devices-K-W-Jeter/book/0857660977/

Hints about scraping data: https://pypi.org/project/beautifulsoup4/
