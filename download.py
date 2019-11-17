import urllib

def download(url, filepath):
    urllib.urlretrieve(url, filepath)
    print(filepath + " saved")

url = "http://67.media.tumblr.com/11d3eca270be8ee61777c7de4a3ffe40/tumblr_o6qjneQG2P1r2xjmjo1_1280.jpg"
savedir = "E:/bain/wanimal/"
filepath = savedir + "o.jpg"

download(url, filepath)



