import pyshorteners
url = input("Enter Your URL\n")
shortener = pyshorteners.Shortener(api_key="API KEY HERE")
shortenedURL = shortener.bitly.short(url)
print(f"Shortened URL - {shortenedURL}")
