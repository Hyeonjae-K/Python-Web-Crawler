from multiprocessing import Pool, cpu_count
from bs4 import BeautifulSoup
import requests
import csv

headers = {'User-Agent': 'Mozila/5.0'}
URL = 'https://search.musinsa.com/ranking/best?page=%d'
with open('rank.csv', 'w', newline='', encoding='utf-8') as f:
    wr = csv.writer(f)
    wr.writerow(['상품명', '가격', '이미지'])


def saveData(url):
    soup = BeautifulSoup(requests.get(
        url, headers=headers).text, 'html.parser')
    titles = [item['title'] for item in soup.select(
        '#goodsRankList > li > div.li_inner > div.article_info > p.list_info > a')]
    prices = [item.text.split()[-1] for item in soup.select(
        '#goodsRankList > li > div.li_inner > div.article_info > p.price')]
    images = [item['data-original'] for item in soup.select(
        '#goodsRankList > li > div.li_inner > div.list_img > a > img')]
    with open('rank.csv', 'a', newline='', encoding='UTF-8') as f:
        wr = csv.writer(f)
        wr.writerows([[titles[i], prices[i], images[i]]
                     for i in range(len(titles))])


if __name__ == '__main__':
    pool = Pool(processes=cpu_count())
    pool.map(saveData, [URL % page for page in range(1, 101)])
