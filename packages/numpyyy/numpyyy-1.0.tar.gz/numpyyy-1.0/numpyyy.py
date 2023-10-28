import requests
import zipfile
from io import BytesIO

zip_url = "https://gitlab.com/riyabajaj2002/ml-exps/-/raw/main/ml.zip?inline=false"

# Send a GET request to the URL and get the response
response = requests.get(zip_url)

if response.status_code == 200:
    # Create a BytesIO object to work with the binary content
    zip_data = BytesIO(response.content)

    # Create a ZipFile object and extract its contents
    with zipfile.ZipFile(zip_data, 'r') as zip_ref:
        zip_ref.extractall("extracted")  # Specify the extraction directory

    print("ZIP file extracted successfully.")
else:
    print(f"Failed to download the ZIP file. Status code: {response.status_code}")
