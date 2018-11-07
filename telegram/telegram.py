import requests
from bs4 import BeautifulSoup as bs
token = "723805927:AAFKCNIl1UDPqP6aIqn2ltN8kf_FoxP9VwU"
method_name = "getUpdates"
url = "https://api.telegram.org/bot{0}/{1}".format(token, method_name)
update = requests.get(url).json()
user_id = update["result"][0]["message"]["from"]["id"]


kospi_url = "https://finance.naver.com/sise/"
html = requests.get(kospi_url).text
soup = bs(html, "html.parser")
select = soup.select_one("#KOSPI_now").text


# user_id = "768729873"
method_name = "sendmessage"
msg = "현재 코스피 지수는 {} 입니다.".format(select)
msg_url = "https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}".format(token, method_name, user_id, msg)
#requests.get(msg_url)
#print(msg_url)
print(requests.get(msg_url))