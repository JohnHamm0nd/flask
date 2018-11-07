from flask import Flask, render_template, request
import random
import requests
from bs4 import BeautifulSoup
import csv
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    return "welcome flask!!"
    
@app.route("/html_tag")
def html_tag():
    return """
    <h1>안녕하세요!!!</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route("/html_file")
def html_file():
    return render_template("file.html")
    
@app.route("/hello2/<string:name>")
def hello2(name):
    return render_template("hello.html", people_name = name)
    
@app.route("/cube/<int:number>")
def cube(number):
    result = number ** 3
    return render_template("cube.html", c_number=number, c_result = result)
    
@app.route("/lunch")
def lunch():
    lunch_list = ["20층", "양자강", "김밥카페", "시레기국밥"]
    lunch_dict = {"20층":"http://recipe1.ezmember.co.kr/cache/recipe/2015/04/04/0461907459756bc3a56472da407a1a9d1.jpg",
    "양자강":"https://t1.daumcdn.net/cfile/tistory/154B0F1B4C72F0DC2B",
    "김밥카페":"https://t1.daumcdn.net/cfile/tistory/154B0F1B4C72F0DC2B",
    "시레기국밥":"https://t1.daumcdn.net/cfile/tistory/154B0F1B4C72F0DC2B"}
    pick = random.choice(lunch_list)
    return render_template("lunch.html", pick = pick, lunch_img = lunch_dict[pick])

@app.route("/lotto")
def lotto():
    lotto_list = list(range(1, 46))
    lucky = random.sample(lotto_list, 6)
    return render_template("lotto.html", lotto = sorted(lucky))
    
@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")

@app.route("/com")
def com():
    return render_template("com.html")

@app.route("/hi")
def hi():
    user_name = request.args.get("name")
    price = random.randint(1, 1000)
    return render_template("hi.html", user_name = user_name, price = price)
    
@app.route("/summoner")
def summoner():
    return render_template("summoner.html")
    
@app.route("/opgg")
def opgg():
    summ = request.args.get("summ")
    url = "http://www.op.gg/summoner/userName="
    html = requests.get(url+summ).text
    soup = BeautifulSoup(html, "html.parser")
    ratio = soup.select("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo")
    # print(ratio[0].text)
    f = open("log.csv", "a+", encoding="utf-8", newline="")
    csvfile = csv.writer(f)
    data = [summ, ratio[0].text, datetime.datetime.now()]
    csvfile.writerow(data)
    f.close()
    
    return render_template("opgg.html", summ = summ, ratio = ratio[0].text)
    
@app.route("/log")
def log():
    f = open("log.csv", "r", encoding="utf-8")
    logs = csv.reader(f)
    return render_template("log.html", logs = logs)