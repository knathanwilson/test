
from flask import Flask, request, redirect, Response, make_response, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return 'this is working???'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
