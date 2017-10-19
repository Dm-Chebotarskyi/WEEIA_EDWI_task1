import sys
from urllib import urlopen
from BeautifulSoup import BeautifulSoup as bs
import re
import string

fNameHTML = "res.html"
fNameTXT = "res.txt"

url = sys.argv[1]

soap = bs(urlopen(url))
content = soap.prettify()
with open(fNameHTML, "w") as f:
    f.write(content)

content = re.sub('<.*?>', '', content).lower()

content = content.translate(None, string.punctuation)

with open(fNameTXT, "w") as f:
    f.write(content)


