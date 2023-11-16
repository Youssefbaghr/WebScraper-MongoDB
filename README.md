#WebScraper-MongoDB

Description
This Python-based project is a web scraping and content analysis tool that extracts information from websites, performs various analyses on the gathered data, and stores the insights in a MongoDB database. The project utilizes the BeautifulSoup library for web sProject Titlecraping, MongoDB for database storage, and provides functionalities for extracting paragraphs, headings, links, and performing content analysis such as word count, sentence count, average content length, average sentence length, and keyword occurrences.

Documentation
Installation
To use this project, follow these steps:

Clone the repository:


git clone https://github.com/username/repository.git
Install the required dependencies using pip:


pip install -r requirements.txt
Usage
Modify the extract_and_save_info() function in main.py by providing the desired website URL and keyword to search for.

Run the main.py file:
Configuration
MongoDB Configuration: Make sure to replace the MongoDB connection string in main.py with your own connection string from MongoDB Atlas or your local MongoDB instance.
Contributing
Contributions are welcome! Fork the repository and create a pull request for any suggested improvements or additional features.

License
This project is licensed under the MIT License.
