from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)  # 啟用跨源資源共享

# 獎項池（可調整機率）
prize_pool = [
    ("A賞", 5),
    ("B賞", 10),
    ("C賞", 20),
    ("銘謝惠顧", 65)
]

# 把獎項機率轉為權重抽籤用
prizes = [p[0] for p in prize_pool]
weights = [p[1] for p in prize_pool]

@app.route("/draw", methods=["GET"])
def draw():
    result = random.choices(prizes, weights=weights, k=1)[0]
    # 可加上時間記錄
    return jsonify({
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == '__main__':
    app.run(debug=True)
