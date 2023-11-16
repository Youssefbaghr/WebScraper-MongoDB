from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
from datetime import datetime
import logging
from collections import Counter
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Connect to MongoDB
client = MongoClient(
    'YOUR_MONGODB_URL',
)
db = client['website_data']
collection = db['web_info']


# Function to extract different types of content
def extract_content(soup, content_type):
  if content_type == 'paragraphs':
    return [para.get_text(strip=True) for para in soup.find_all('p')]
  elif content_type == 'headings':
    return [
        heading.get_text(strip=True)
        for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    ]
  elif content_type == 'links':
    return [link.get('href') for link in soup.find_all('a', href=True)]


# Function to count sentences
def count_sentences(text_list):
  sentences = re.split(r'[.!?]', ' '.join(text_list))
  sentences = [sent.strip() for sent in sentences if sent.strip()]
  return len(sentences)


# Function to analyze content length
def analyze_content_length(text_list):
  total_length = sum(len(text) for text in text_list)
  return total_length / len(text_list) if len(text_list) > 0 else 0


# Function to perform word count analysis
def word_count_analysis(text_list):
  words = ' '.join(text_list).split()
  word_count = Counter(words)
  return len(words), word_count.most_common(10)


# Function to calculate average sentence length
def calculate_avg_sentence_length(text_list):
  sentences = re.split(r'[.!?]', ' '.join(text_list))
  sentences = [sent.strip() for sent in sentences if sent.strip()]
  words_in_sentences = [len(sent.split()) for sent in sentences]
  return sum(words_in_sentences) / len(
      words_in_sentences) if words_in_sentences else 0


# Function to perform keyword analysis
def keyword_analysis(text_list, keyword):
  return sum(text.lower().count(keyword.lower()) for text in text_list)


# Function to extract and save data
def extract_and_save_info(url):
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses
    soup = BeautifulSoup(response.text, 'html.parser')

    extracted_info = extract_content(soup, 'paragraphs')
    headings = extract_content(soup, 'headings')
    links = extract_content(soup, 'links')

    total_words, most_common_words = word_count_analysis(extracted_info)

    data_to_save = {
        'url': url,
        'date': datetime.now(),
        'data': {
            'extracted_info': extracted_info,
            'headings': headings,
            'links': links,
        },
        'analysis': {
            'total_words':
            total_words,
            'most_common_words':
            most_common_words,
            'average_content_length':
            analyze_content_length(extracted_info),
            'total_sentences':
            count_sentences(extracted_info),
            'average_sentence_length':
            calculate_avg_sentence_length(extracted_info),
            'keyword_occurrences':
            keyword_analysis(extracted_info, 'example_keyword')
        }
    }

    collection.insert_one(data_to_save)
    logger.info("Data saved successfully to MongoDB.")

  except requests.RequestException as e:
    logger.error(f"Failed to fetch the website. Error: {e}")
  except Exception as ex:
    logger.error(f"An error occurred: {ex}")


# URL of the website you want to extract information from
website_url = 'URL'

# Call the function to extract and save information
extract_and_save_info(website_url)
