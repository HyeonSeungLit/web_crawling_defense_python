# web_crawling_defense_python
웹 크롤링 방어 시스템 구축하십시오! (python)

# 웹 크롤링 방어 시스템

이 프로젝트는 웹사이트의 데이터를 무단으로 수집하는 크롤러를 탐지하고 차단하는 시스템입니다. 다양한 사용자 에이전트를 분석하고 의심스러운 활동을 탐지하는 로직을 구현합니다.

## 기능
- 사용자 에이전트 분석
- 요청 빈도 분석
- 의심스러운 IP 차단
- 크롤링 방어 전략 (예: rate limiting, honeypot)

## 설치 방법

필요한 모듈을 설치하려면 `requirements.txt` 파일을 사용하세요:
pip install -r requirements.txt

##Redis 설정
이 프로젝트는 요청 빈도와 IP 차단을 관리하기 위해 Redis를 사용합니다. Redis 서버를 로컬에서 실행하거나, 필요한 경우 redis.StrictRedis 설정을 변경하세요.


## Redis 설치 및 실행
Redis가 설치되어 있지 않다면, Redis를 설치하고 실행해야 합니다. 다음 명령어를 사용하여 설치 및 실행할 수 있습니다:
```bash
sudo apt-get update
sudo apt-get install redis-server
sudo service redis-server start

## 실행 방법
app.py 파일을 실행하여 웹 서버를 시작할 수 있습니다:

