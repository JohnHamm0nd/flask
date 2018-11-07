# C9 파이썬 환경 설정

### pyenv

[pyenv github](https://github.com/pyenv/pyenv#installation)



- install

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

>pyenv github 에서 현재 컴퓨터로 파일 복사

- 환경변수 설정

```bash
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

$ source ~/.bash_profile
# 환경변수 추가후 bash_profile 실행 => 터미널 새로고침
```

- python install

```bash
$ pyenv install 3.6.1
$ pyenv global 3.6.1
$ python -V

# pyenv global 3.6.1 한 후에도 파이썬 버전이 3.6.1 로 바뀌지 않을 경우
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

### pyenv-virtualenv

- virtualenv install

```bash
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_ROOT/plugins/pyenv-virtualenv
```

- setting

```bash
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
$ source ~/.bash_profile
```

- 가상환경 만들기

```bash
$ pyenv virtualenv <파이썬 버전> <설정한 가상환경 이름>
```

- 가상환경 사용하기

```bash
$ pyenv shell tele
```

- 모듈 설치

``` bash
$ pip install bs4
$ pip install requests
```

### 텔레그램 pc에 설치

- install

- bot init

@BotFather 검색

start 버튼클릭

/newbot 입력

이름을 생성 => 중복가능

username => `bot`으로 끝나야하고 유니크한 값

token`, `url

url 클릭하여 봇 활성화

### telegram.py

```
import requests
token = "봇의 토큰값"
method_name = "getUpdates"
url = 'https://api.telegram.org/bot{0}/{1}'.format(token,method_name)

print(url)
print(requests.get(url))
import requests
token = "763337042:AAEjq0JPofKKdu9_oYwVdi5O5L8JGz_xl6E"
method_name = "getUpdates"
url = 'https://api.telegram.org/bot{0}/{1}'.format(token,method_name)

user_id = '602595803'
method_name = "sendmessage"
msg = "안녕하세요!!!"
msg_url = 'https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}'.format(token,method_name,user_id,msg)
print(msg_url)
print(requests.get(msg_url))
```

- id 값을 json에서 가져오기