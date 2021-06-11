# importing modules
import requests
from lxml import etree

# manually storing desired URL
url = 'https://en.wikipedia.org/wiki/Delhi_Public_School_Society'

# fetching its url through requests module
req = requests.get(url)

store = etree.fromstring(req.text)

# this will give Motto portion of above
# URL's info box of Wikipedia's page
output = store.xpath("//th[normalize-space()='Motto']/following-sibling::td/i")
print(output)
# printing the text portion
if len(output) > 0:
    print(output[0].text)
else:
    print('Motto not found')

# Run this program on your installed Python or
# on your local system using cmd or any IDE.
