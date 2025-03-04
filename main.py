from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-data', methods=['GET'])
def get_data():
    data = {
        "message": "GET request received successfully",
        "data": {"name": "John Doe", "age": 30}
    }
    return jsonify(data), 200

@app.route('/post-data', methods=['POST'])
def post_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    response = {
        "message": "Data received successfully",
        "data": data
    }
    return jsonify(response), 201

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

