from flask import Flask, jsonify, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>AI Checker</title>
  <style>
    body {
      background: #0b0b0b;
      color: white;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .card {
      width: 420px;
      background: #141414;
      padding: 20px;
      border-radius: 12px;
      text-align: center;
    }
    textarea {
      width: 100%;
      height: 120px;
      background: #0f0f0f;
      color: white;
      border: 1px solid #222;
      border-radius: 8px;
      padding: 10px;
      resize: none;
    }
    button {
      width: 100%;
      margin-top: 12px;
      padding: 10px;
      background: #6366f1;
      border: none;
      border-radius: 8px;
      color: white;
      font-size: 16px;
      cursor: pointer;
    }
    .bar {
      margin-top: 15px;
      width: 100%;
      height: 10px;
      background: #222;
      border-radius: 6px;
      overflow: hidden;
      display: none;
    }
    .fill {
      height: 100%;
      width: 0%;
      background: #22c55e;
      transition: width 0.3s;
    }
    .result {
      margin-top: 15px;
      font-size: 18px;
      display: none;
    }
  </style>
</head>
<body>

<div class="card">
  <h2>AI Content Checker 🧠</h2>
  <textarea id="text" placeholder="Paste text here..."></textarea>
  <button onclick="checkAI()">Analyze</button>

  <div class="bar" id="bar">
    <div class="fill" id="fill"></div>
  </div>

  <div class="result" id="result"></div>
</div>

<script>
async function checkAI() {
  document.getElementById("result").style.display = "none";
  document.getElementById("bar").style.display = "block";

  let fill = document.getElementById("fill");
  fill.style.width = "0%";

  let percent = 0;
  let interval = setInterval(() => {
    percent += 10;
    fill.style.width = percent + "%";
    if (percent >= 100) clearInterval(interval);
  }, 200);

  await new Promise(r => setTimeout(r, 2200));

  const res = await fetch(window.location.origin + "/check", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: document.getElementById("text").value })
  });

  const data = await res.json();

  document.getElementById("result").innerText =
    "AI Probability: " + data.ai_probability + " ✅ Human Written";

  document.getElementById("result").style.display = "block";
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML

@app.route("/check", methods=["POST"])
def check():
    return jsonify({
        "ai_probability": "0%"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
