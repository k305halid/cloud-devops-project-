
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <h1>Cloud DevOps Mini-Project - Version 2</h1>
    <h2>CI/CD Deployment Successful!</h2>
    <p>Application updated automatically using GitHub Actions and Docker.</p>
    """

@app.get("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

