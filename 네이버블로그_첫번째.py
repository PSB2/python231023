import requests
from bs4 import BeautifulSoup

# URL of the Naver blog page
url = "https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0"

# Send an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all blog post elements
blog_post_elements = soup.find_all("div", class_="desc_inner")

# Iterate through the blog post elements and extract required information
for post_element in blog_post_elements:
    # Extracting blog name and address
    blog_name = post_element.find("span", class_="user_name").text.strip()
    blog_address = "https://blog.naver.com/" + post_element.find("a", class_="desc_inner")["href"].split("/")[-1]

    # Extracting post title
    post_title = post_element.find("a", class_="desc_inner").text.strip()

    # Extracting date
    post_date = post_element.find("span", class_="se_publishDate").text.strip()

    # Print the extracted information
    print("Blog Name:", blog_name)
    print("Blog Address:", blog_address)
    print("Post Title:", post_title)
    print("Date:", post_date)
    print("-------------------")
