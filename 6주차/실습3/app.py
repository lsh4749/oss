from flask import Flask
from datetime import datetime, timezone
from pathlib import Path

app = Flask(__name__)
LOG_DIR = Path("/app/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

@app.route("/")
def home():
    # utcnow() 대신 timezone.utc를 사용하도록 수정
    msg = f"웹 사이트 접속 시간: {datetime.now(timezone.utc).isoformat()}"
    with open(LOG_DIR / "access.log", "a") as f:
        f.write(msg + "\n")
    return msg

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)