from bs4 import BeautifulSoup
import urllib.request
from sys import argv

print(""" .|'''.|                                                   
 ||..  '    ....  ... ..   ....   ... ...    ....  ... ..  
  ''|||.  .|   ''  ||' '' '' .||   ||'  || .|...||  ||' '' 
.     '|| ||       ||     .|' ||   ||    | ||       ||     
|'....|'   '|...' .||.    '|..'|'  ||...'   '|...' .||.    
                                   ||                      
                                  ''''                     """)

class Scraper:
    def __init__(self,file):
        self.file = file
        
    def scrapelinks(self):
        #Fast parser to parse HTML websites
        parser = "lxml"
        soup = BeautifulSoup(self.file,parser)
        #It locates all the anchor elements it sotres them in variable
        contain_links = soup.find_all("a")
        #it looks for a tag called href which is the link in every element then prints the links
        for tag in contain_links:
            link = tag.get("href")
            print(link+"\n")
            
            
    def scrapetitles(self):
        #Fast parser to parse HTML websites     
        parser = "lxml"
        soup = BeautifulSoup(self.file,parser)
        #finds the H1 html elements then prints them
        titles = soup.find_all("h1")
        print(titles)
        
    def scrapep(self):
        #Fast parser to parse HTML websites
        parser = "lxml"
        soup = BeautifulSoup(self.file,parser)
        #finds paragraphs in html 
        paragraphs = soup.find_all("p")
        #counter to count the paragraphs
        count = 0
        #print every paragraph sepreatly
        for paragraph in paragraphs:
            count += 1
            print("Paragraph"+ str(count)+ "\n" + str(paragraph)+ "\n")
            
    def downloadhtml(self):
        parser = "lxml"
        soup = BeautifulSoup(self.file,parser)
        #downloads a html file of the site given
        with open("Downlodedhtml.html", "a") as download_file:
            download_file.write(soup.prettify())
            




    
args = argv[1:]
if len(argv)==3:
    url = str(args[0])
    if url == None:
        url = str(input("Enter the site you want to scrape : \n"))
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    r = urllib.request.Request(url,headers={'User-Agent': user_agent})
    with urllib.request.urlopen(r) as response:
        the_page = response.read()
        
    if str(args[1]) == "links":
        Scraper(the_page).scrapelinks()
    elif str(args[1]) == "titles":
        Scraper(the_page).scrapetitles()
    elif str(args[1]) == "paragraphs":
        Scraper(the_page).scrapep()
    elif str(args[1]) == "downloadhtml":
        Scraper(the_page).downloadhtml()
else:
    url = str(input("Enter the site you want to scrape : \n"))
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    r = urllib.request.Request(url,headers={'User-Agent': user_agent})
    with urllib.request.urlopen(r) as response:
        the_page = response.read()
    scrapetype = str(input("What you want to scrap ? "))
    if scrapetype == "links":
        Scraper(the_page).scrapelinks()
    elif scrapetype == "titles":
        Scraper(the_page).scrapetitles()
    elif scrapetype == "paragraphs":
        Scraper(the_page).scrapep()
    elif scrapetype == "downloadhtml":
        Scraper(the_page).downloadhtml()

        
