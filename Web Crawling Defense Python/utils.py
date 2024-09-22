import time
import redis
from flask import request, jsonify

# Redis 설정
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# 사용자 에이전트 분석
def analyze_user_agent():
    user_agent = request.headers.get('User-Agent', '').lower()
    suspicious_agents = ['curl', 'wget', 'scrapy', 'httpclient']
    return any(agent in user_agent for agent in suspicious_agents)

# 요청 빈도 분석
def check_request_frequency():
    ip = request.remote_addr
    current_time = time.time()
    request_times = redis_client.lrange(ip, 0, -1)
    
    # 요청 빈도 계산
    request_times = [float(t) for t in request_times if float(t) > current_time - 60]
    redis_client.delete(ip)
    for t in request_times:
        redis_client.rpush(ip, t)
    
    redis_client.rpush(ip, current_time)
    return len(request_times) > 100  # 예: 1분에 100번 이상 요청 시 의심

# 의심스러운 IP 차단
def block_suspicious_ip():
    ip = request.remote_addr
    redis_client.setex(f"blocked:{ip}", 3600, 'blocked')  # 1시간 동안 차단

# 차단된 IP 확인
def is_ip_blocked():
    ip = request.remote_addr
    return redis_client.exists(f"blocked:{ip}")

# Honeypot URL 설정
HONEYPOT_URLS = ['/honeypot', '/hidden']

# Honeypot 접근 여부 확인
def check_honeypot_access():
    path = request.path
    return path in HONEYPOT_URLS
