from flask import Flask, request, jsonify
from utils import analyze_user_agent, check_request_frequency, block_suspicious_ip, is_ip_blocked, check_honeypot_access

app = Flask(__name__)

@app.before_request
def before_request():
    if is_ip_blocked():
        return jsonify({"error": "Your IP has been blocked due to suspicious activity."}), 403
    
    if check_honeypot_access():
        block_suspicious_ip()
        return jsonify({"error": "Honeypot accessed. Your IP has been blocked."}), 403
    
    if analyze_user_agent() or check_request_frequency():
        block_suspicious_ip()
        return jsonify({"error": "Suspicious activity detected. Your IP has been blocked."}), 403

@app.route('/')
def index():
    return 'Welcome to the secure website!'

@app.route('/honeypot')
def honeypot():
    return 'Honeypot! You should not be here.'

if __name__ == "__main__":
    app.run(debug=True)
