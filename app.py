from flask import Flask, jsonify
import random
from rejection_reasons import rejection_reasons

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    """Return nothing for the root path."""
    return ""

@app.route('/no', methods=['GET'])
def get_rejection():
    """Return a random rejection reason."""
    return jsonify({"reason": random.choice(rejection_reasons)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
