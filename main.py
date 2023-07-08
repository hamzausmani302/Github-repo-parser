import sys;

from utils.PageParser import PageParser;
from utils.ArgsParser import ArgsParser;
from utils.FileWriter import CSVWriter;
from models.User import User;
import requests;
import argparse;
from bs4 import BeautifulSoup;

parser = argparse.ArgumentParser()
parser.add_argument('--peopleType' , type=str , default="watchers"  );
parser.add_argument('--url' , type=str , required=True  );
parser.add_argument('--outfile' , type=str ,default="content/results.csv")
args = parser.parse_args();


if(args.peopleType.lower() == "watchers"):

    stargazers_URL =  "/watchers"
elif(args.peopleType.lower() == "stargazers"):
    stargazers_URL =  "/stargazers"
else:
    print("Invalid Argument : watchers OR stargazers");
    exit(1);

GITHUB_REPO_URL = ArgsParser.parseURL(args.url) + stargazers_URL;
GITHUB_URL = ArgsParser.parseURL("https://www.github.com/");



try:
    
    users = [];
    html_content = requests.get(GITHUB_REPO_URL);   
    
    soup = BeautifulSoup(html_content.content, 'html5lib');
    order_list = soup.find("ol" );

    for component in soup.findAll('li' , attrs={'class' : "col-md-4 mb-3"}):
        
        name_html = component.findAll("h3")[0].a;
        print(name_html.text , GITHUB_URL   + name_html['href'] );
        
        fullName , nF = PageParser.parse_user_page(GITHUB_URL   + name_html['href'])

        users.append( User(GITHUB_URL   + name_html['href'] , name_html.text , fullName , nF ))


    writer = CSVWriter(args.outfile);
    _users = writer.sort(users);
    writer.write(_users);
    
    pass
except:
    print("Error occured")


