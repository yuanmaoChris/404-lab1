import requests
print(requests.__version__)
git = requests.get("https://raw.githubusercontent.com/yuanmaoChris/404-lab1/master/lab1.py")
print(git.content)
