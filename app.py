from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>KBReal Love</title>
<style>
body{margin:0;background:#080b12;color:white;font-family:Arial}
header{padding:20px;text-align:center;background:#15101c}
h1{color:#ff2378}
.card{margin:15px;padding:18px;background:#151d2b;border-radius:15px}
button{background:#ff2378;color:white;border:0;padding:12px;border-radius:10px}
input{padding:12px;border-radius:8px;border:1px solid #555;background:#0b111b;color:white;width:90%}
a{color:#ff5595}
</style>
</head>
<body>
<header>
<h1>❤️ KBReal Love</h1>
<p>Share Love • Create Memories</p>
</header>
<div class="card">
<h2>Welcome!</h2>
<p>Connect with friends and share your moments.</p>
</div>
<div class="card">
<h3>🔎 Find a TikTok Profile</h3>
<form action="/search">
<input name="username" placeholder="Enter TikTok username" required>
<br><br><button>Search</button>
</form>
</div>
<div class="card">
<h3>🎬 Share your videos</h3>
<p>Video upload will be added in the next step.</p>
</div>
<div class="card">
<h3>💬 Messages</h3>
<p>Chat feature will be added next.</p>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/search")
def search():
    from flask import request
    username = request.args.get("username", "").strip().lstrip("@")
    return f"""
    <body style="background:#080b12;color:white;font-family:Arial;padding:25px">
    <h2>🔎 TikTok Profile Search</h2>
    <p>Username: @{username}</p>
    <p>This demo does not access private TikTok data.</p>
    <a style="color:#ff5595" href="https://www.tiktok.com/@{username}">
    Open public TikTok profile</a><br><br>
    <a style="color:#ff5595" href="/">Back to KBReal Love</a>
    </body>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)
