# Import required libraries
import requests
from bs4 import BeautifulSoup

# Website URL (Indeed Jobs)
url = "https://www.indeed.com/jobs?q=python+backend+developer"

# Add headers so the request looks like it comes from a real browser
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}

# Send GET request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all h2 tags
    headings = soup.find_all("h2")

    # Print each heading
    for heading in headings:
        print(heading.get_text(strip=True))

else:
    print(f"Request Failed! Status Code: {response.status_code}")