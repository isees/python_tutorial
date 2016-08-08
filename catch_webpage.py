from lxml import html
import requests

source = "http://cn163.net/archives/3479/"
page = requests.get(source)
tree = html.fromstring(page.content)
# print page.content
urlList = tree.xpath("//div[@id='content']//ol/li/a/@href")
# print urlList
for url in urlList:
    print url

