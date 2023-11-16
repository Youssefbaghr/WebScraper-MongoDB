
# WebScraper-MongoDB

Description

This Python-based project is a web scraping and content analysis tool that extracts information from websites, performs various analyses on the gathered data, and stores the insights in a MongoDB database. The project utilizes the BeautifulSoup library for web scraping, MongoDB for database storage, and provides functionalities for extracting paragraphs, headings, links, and performing content analysis such as word count, sentence count, average content length, average sentence length, and keyword occurrences.

## Installation

This project is licensed under the MIT License.

Clone the repository:

```bash
  git clone https://github.com/Youssefbaghr/WebScraper-MongoDB.git

```
Install the required dependencies using pip:

```bash
pip install -r requirements.txt

```
## Usage/Examples

Configure MongoDB Connection: Replace the MongoDB connection string in main.py with your own connection string from MongoDB Atlas or your local MongoDB instance.

Run the Project:

Modify the extract_and_save_info() function in main.py by providing the desired website URL and keyword to search for.

Run the main.py file:

```bash
python main.py

```

```python 
# Connect to MongoDB
client = MongoClient(
    'YOUR_MONGODB_URL',
)
```


## License

This project is licensed under the MIT License.





