from flask import Flask, request, jsonify
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)  # 啟用跨源資源共享

# 每個活動的獎池設定
event_prize_pools = {
    "event1": [
        ("A賞", 5),
        ("B賞", 10),
        ("C賞", 20),
        ("銘謝惠顧", 65)
    ],
    "event2": [
        ("S賞", 3),
        ("A賞", 12),
        ("B賞", 30),
        ("再接再厲", 55)
    ]
}

@app.route("/draw", methods=["POST"])
def draw():
    data = request.get_json()
    event = data.get("event", "event1")  # 預設 event1

    if event not in event_prize_pools:
        return jsonify({"error": "Invalid event"}), 400

    pool = event_prize_pools[event]
    prizes = [p[0] for p in pool]
    weights = [p[1] for p in pool]
    result = random.choices(prizes, weights=weights, k=1)[0]

    return jsonify({
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == '__main__':
    app.run(debug=True)
