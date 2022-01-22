import urllib.request
import random
import re


def getlink():
    fp = urllib.request.urlopen(
        "https://api.hackertarget.com/pagelinks/?q=https://www.reddit.com/r/Drumkits/top/?sort=top&t=week")
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    links = mystr.splitlines()
    random_number = random.randint(1, 100)
    proper_links = []
    for i in links:
        if re.search(r"https:\/\/drive\.google\.com.+", i) or re.search(r"https:\/\/mega\.nz\/?.+", i):
            proper_links.append(i)
    return proper_links[random_number % len(proper_links)]


print(getlink())
