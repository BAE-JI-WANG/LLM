from bs4 import BeautifulSoup
import pandas as pd
import requests

class ParsingLawData:
    def __init__(self):
        self.maxpg = 1
        self.qna = ""
        self.seq = -1
    
    def get_html(self, url):
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
    def get_titles(self, url):
        title_list = []
        soup = self.get_html(url)
        print(soup)
        # for i in range(0, 100, 2):
        #     titles = soup.select(f'#Ak_contents > div.vote_list > ul > li:nth-child({i}) > div > div.ttl > a')
        #     for title in titles:
        #         title_list.append(title.get_text().replace('\r\n', '').strip(' '))
                
        # return title_list
    
    def get_answers(self, url):
        answer_list = []
        soup = self.get_html(url)
        for i in range(0, 100, 2):
            answers = soup.select(f'#Ak_contents > div.vote_list > ul > li:nth-child({i}) > div > div.ans > p')
            for ans in answers:
                answer_list.append(ans.get_text())
                
        return answer_list