import pyshorteners, config
url = input("Enter Your URL\n")
shortener = pyshorteners.Shortener(api_key=config.API_KEY)
shortenedURL = shortener.bitly.short(url)
print(f"Shortened URL - {shortenedURL}")