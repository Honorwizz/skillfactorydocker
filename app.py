import os
import requests
from urllib.parse import urlparse

def download_favicon(url):
    # Извлекаем домен сайта
    parsed_url = urlparse(url)
    favicon_url = f"{parsed_url.scheme}://{parsed_url.netloc}/favicon.ico"
    
    # Отправляем запрос на получение favicon
    response = requests.get(favicon_url, stream=True)
    
    if response.status_code == 200:
        # Сохраняем файл
        with open("favicon.ico", "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Favicon saved as favicon.ico")
    else:
        print(f"Favicon not found for {url}")

if __name__ == "__main__":
    site_url = input("Enter the website URL: ")
    download_favicon(site_url)
