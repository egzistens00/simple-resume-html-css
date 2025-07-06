from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import uuid
import datetime

app = Flask(__name__)
CORS(app)

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
table = dynamodb.Table('feedbackData')

@app.route('/')
def home():
    return "✅ Feedback API is live."

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        data = request.get_json()
        name = data.get('name')
        feedback = data.get('feedback')
        response = table.put_item(
            Item={
                'id': str(uuid.uuid4()),
                'name': name,
                'feedback': feedback,
                'timestamp': datetime.datetime.utcnow().isoformat()
            }
        )
        return jsonify({"message": "✅ Feedback stored successfully."}), 200
    except Exception as e:
        return jsonify({"error": "Failed to store feedback"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
