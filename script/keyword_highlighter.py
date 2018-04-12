# -*- coding: utf8 -*-
import os
import re
import urllib

keywords_path = "keywords.txt"

def get_extension(filename):
    return filename.split(".")[-1]

def get_file_content(path):
    return file.read(open(path, "r"))

def load_keywords(path, keywords = []):
    for line in open(path, "r"):
        keywords.append(line.strip())
    return keywords

def search_and_replace(content, keywords):
    for keyword in keywords:
        occurances = re.findall(keyword, content, flags=re.IGNORECASE)
        if occurances != []:
            occurance = occurances[0]
            content = re.sub(occurance, construct_tag(occurance), content, 1, flags=re.IGNORECASE)
    return content

def construct_tag(keyword):
    return "<a href=\"natureforpeople.org/knowledge-base/?" + urllib.urlencode({"query": keyword.lower()}) +"\" class=\"content-tag\">" + keyword + "</a>"

def update_file(path, content):
    file = open(path, "w")
    file.write(content)
    print file
    file.close()

def swap_content_keywords(keywords):
    for root, directories, filenames in os.walk('../content/'):
        for filename in filenames:
            if get_extension(filename) in ["lr"]:
                path    = os.path.join(root,filename)
                content = search_and_replace(get_file_content(path), keywords)
                update_file(path, content)

if __name__ == '__main__':
    keywords = load_keywords(keywords_path)
    swap_content_keywords(keywords)
    print "Done"