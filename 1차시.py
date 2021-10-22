from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozila/5.0'}
URL = 'https://search.musinsa.com/ranking/best?page=%d'

for page in range(1, 101):
    soup = BeautifulSoup(requests.get(
        URL % page, headers=headers).text, 'html.parser')
    titles = [item['title'] for item in soup.select(
        '#goodsRankList > li > div.li_inner > div.article_info > p.list_info > a')]
    prices = [item.text.split()[-1] for item in soup.select(
        '#goodsRankList > li > div.li_inner > div.article_info > p.price')]
    images = [item['data-original'] for item in soup.select(
        '#goodsRankList > li > div.li_inner > div.list_img > a > img')]
    print(len(titles), len(prices), len(images))

    for i in range(len(titles)):
        print(titles[i], prices[i], images[i])
