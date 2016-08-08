import glob, os

os.chdir("D:/workspace/nginx-1.9.7/html/images")

index = 0
for file in glob.glob("*.jpg"):
    if index == 30:
        break
    print "<img src='./images/" + file+"' />"
