# day1

파이썬 기초 + 웹 입문



### py.hphk.io

``` python
# 안녕
print("안녕하세요")
```

``` python
# hello
msg = "hello world!!"
print()
print(msg)

```



``` python
# 점심메뉴
import random
lunch_list = ["양자강", "20층", "김밥카페", "시레기국밥", "김치찌개", "된장찌개", "파스타" ]
pick = random.choice(lunch_list)

print("오늘의 추천 메뉴는 {menu}입니다.".format(menu=pick))
```



``` python

```

``` python
# 로또
import random

lotto_list = list(range(1, 46))

lotto = random.sample(lotto_list, 6)

print("로또 추쳔 번호는 {} 입니다.".format(sorted(lotto)))
```

```python
# 메뉴
import random
lunch_list = ["짜장면", "김밥", "제육덮밥", "파스타", "김치찌개"]
lunch_dict = {
  "짜장면":"https://blog.naver.com/self-innovator/221161640314",
  "김밥":"http://cafe.naver.com/bookchildlove/1232810",
  "제육덮밥":"http://cafe.naver.com/shopjirmsin/238846",
  "파스타":"http://post.naver.com/viewer/postView.nhn?volumeNo=14108790&memberNo=39744498",
  "김치찌개":"http://post.naver.com/viewer/postView.nhn?volumeNo=7374652&memberNo=33557461"
}

pick = random.choice(lunch_list)
print("오늘의 메뉴는 {} 입니다.".format(pick), lunch_dict[pick])
```

``` python
# 미세먼지
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=QaGapZXPV5DTM72fy6lrf3hJnrJxhila1UVkPlUCo0N0g0F0RZ9WEngT8RkNjNo4IF%2BikV%2BthQLze39nK4IQjA%3D%3D&numOfRows=10&pageSize=10&pageNo=3&startPage=3&sidoName=%EC%84%9C%EC%9A%B8&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
gangnam = soup('item')[7]
location = gangnam.stationName.text
time = gangnam.dataTime.text
dust = int(gangnam.pm10Value.text)

print("{0} 기준 {1}의 미세먼지 농도는 {2}입니다.".format(time,location,dust))

if (dust > 150):
  print("매우나쁨")
elif (80 < dust <=150):
  print("나쁨")
elif (31 < dust <+ 80):
  print("보통")
else:
  print("좋음")
```

``` python
# 코스피
import requests
from bs4 import BeautifulSoup as bs

url = "https://finance.naver.com/sise/"

html = requests.get(url).text

soup = bs(html, "html.parser")

select = soup.select_one("#KOSPI_now").text

print("현재 코스피 지수는 {} 입니다.".format(select))
```

