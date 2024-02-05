from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests


pg = "https://www.easylaw.go.kr"
r = requests.get(pg + "/CSP/OnhunqueansLstRetrieve.laf")

if r.status_code == 200 : 

    #print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    #class = onehundred_category_title_list
    bb = soup.find("div", "onehundred_category_title_list") #main category list
    maxpg = 1 #list page 형식에 이용
    qna = ""   #list page 형식에 이용
    seq = -1 #list page 형식에 이용
    for lss in bb.find_all('a') : 
        if lss['class'][0] == 'ast_all' : continue 
        # print(pg + lss['href'])
        cc = requests.get(pg + lss['href'])
        
        if cc.status_code == 200 : 

            soup2 = BeautifulSoup(cc.text, 'html.parser')
            
            cat = soup2.find('ul','qa_tab')
 
            for lbb in cat.find_all('a') :
                #subcategory
                maxpg = 1   
                
                subb = requests.get(pg +'/CSP/' +lbb['href'])

                soup3 = BeautifulSoup(subb.text, 'html.parser')

                try :
                    pga = soup3.find('a','nex0')
                    # print(pga['onclick'])
                    maxpg = int(pga['onclick'].split(',')[2].replace("'",''))
                    qna = str(pga['onclick'].split(',')[3].replace("'",''))
                    seq = int(pga['onclick'].split(',')[4].replace("'",''))
                except Exception as ex :    
                    pass
                

                #sub에 main page 
                for r in range(maxpg) : 
                    # print(str(r) + ' : ' + qna + ' : ' + str(seq))
                    req = requests.get(pg + '/CSP/OnhunqueansLstRetrieve.laf?curPage=' + str(r) + '&search_put=&astSeq=' + str(qna) + '&onhunqnaAstSeq='+str(seq)+'&pageType=20')
                    # print(r)
                    if req.status_code == 200 :
                        soup3 = BeautifulSoup(req.text, 'html.parser')
                        
                        qaa = soup3.find_all('li','qa')
                        
                        #print(lss['title']+ ',' +  lbb['title'])
                        for ccc in qaa :
                            ppppp = ccc.find('a')['href']
                            
                            reqq = requests.get(pg + '/CSP/' + ppppp)
                            
                            if reqq.status_code == 200 : 

                                soup4 = BeautifulSoup(reqq.text, 'html.parser')

                                qaa = soup3.find_all('li','qa')
                                print(lss['title'] + ' : ' + lbb['title'])
                                print(ccc.find('a').text)
                                print(ccc.find('p').text)

                            
# Main > Subcategory 정보들 가져와서 >  Page로 돌면서 > 하나하나 들어가서 데이터 가져옴