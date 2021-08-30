from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# url = "http://olympus.realpython.org/profiles/aphrodite"
url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
# print(page)
# print()

# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
html = page.read().decode("utf-8")
# print(html)
# print()

start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
# print(title)
# print()

# using regexp
pattern = "<title.*?>.*?</title.*?>"
match_result = re.search(pattern, html, re.IGNORECASE)
title = match_result.group()
title = re.sub("<.*?>", "", title)
# print(title)

# using beautifulsoap
soap = BeautifulSoup(html, "html.parser")
# print(soap.get_text())
# print(soap.find_all("img"))

image1, image2 = soap.find_all("img")
# print(image1["src"])
# print(image2["src"])
# print(soap.title)
# print(soap.title.string)

image3 = soap.find_all("img", src="/static/grapes.png")
print(image3)
