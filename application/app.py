from flask import Flask, request, jsonify
from flask_cors import CORS
import create_recommendation_model

app = Flask(__name__)
CORS(app)


@app.route('/song', methods=['GET'])
def recommend_songs():
    results = create_recommendation_model.recommend(request.args.get('title'))
    return jsonify({'songs': results})

if __name__ == "__main__":
    app.run(port=5000, debug=True)