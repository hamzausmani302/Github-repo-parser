import requests;
from bs4 import BeautifulSoup;
from utils.ArgsParser import ArgsParser;
GITHUB_URL = ArgsParser.parseURL("https://www.github.com/");

class PageParser:
    @staticmethod
    def parse_user_page(uri):
        response = requests.get(uri);
        html_content = response.text;
        soup = BeautifulSoup(response.content,  "html5lib");
        els= soup.find("span" , attrs={"class" : "p-name vcard-fullname d-block overflow-hidden"})
        if(els.text.strip() == ""):
            els= soup.find("span" , attrs={"class" : "p-nickname"})
        

        follow_html = soup.find("span" , attrs={"class": "text-bold color-fg-default"})
        
        if(follow_html == None):
            return els.text.strip(),"-1";

        else:
            
            return els.text.strip(),follow_html.text.strip();



if __name__ == "main":
    pass
