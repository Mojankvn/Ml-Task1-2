# Import libraries
import os
import requests
from bs4 import BeautifulSoup

def scrape_medium_article(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <p> tags containing the text of the article
        paragraphs = soup.find_all('p')
        
        # Extract text from each paragraph and concatenate
        article_text = '\n'.join([p.get_text() for p in paragraphs])
        
        return article_text
    else:
        print("Failed to fetch the article. Status code:", response.status_code)
        return None

def save_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Article text saved to '{filename}'.")

if __name__ == "__main__":
    #  Run the python script with the given URL of the Medium article
    url = input("Enter the URL of the Medium article: ")
    article_text = scrape_medium_article(url)
    
    if article_text:
        #  Create a new folder called "scraped_articles" in the local machine
        folder_name = "scraped_articles"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        #  Save the scraped text to a .txt file in the "scraped_articles" folder
        filename = os.path.join(folder_name, "scraped_article.txt")
        save_to_file(article_text, filename)
