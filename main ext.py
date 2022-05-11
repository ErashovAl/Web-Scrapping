import bs4
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com'
# url_add = '/ru/all/'
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}

def resp(url_add = ''):

    response = requests.get(url+url_add, headers=headers)
    response.raise_for_status()
    text = response.text
    return text

def seach_in_soup():
    soup = bs4.BeautifulSoup(resp('/ru/all/'), features='html.parser')
    articles = soup.find_all('article')

    for article in articles:
        
        time_stamp = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
        headline = article.find(class_='tm-article-snippet__title_h2').find('a').text
        headline_link = article.find(class_='tm-article-snippet__title_h2').find('a').attrs['href']
        
        soup_page = bs4.BeautifulSoup(resp(headline_link), features='html.parser')
        ext_body = soup_page.find(class_='article-formatted-body').text
        text_for_search = headline + ext_body

        for word in KEYWORDS:

            if word in text_for_search:
                res = f"<{time_stamp}> - <{headline}> - <{url+headline_link}>"
                print(res,'\n')


if __name__ == '__main__':
    
    seach_in_soup()