from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_home():
    return jsonify({
        "status": "online",
        "version": "1.0.0",
        "supported_conversions": ["celsius_to_fahrenheit"]
    })

@app.route('/convert/celsius-to-fahrenheit', methods=['POST'])
def convert_celsius_to_fahrenheit():
    data = request.get_json()
    if not data or 'celsius' not in data:
        return jsonify({"error": "Missing parameter 'celsius'"}), 400
    try:
        celsius = float(data['celsius'])
        fahrenheit = (celsius * 9/5) + 32
        return jsonify({
            "input_celsius": celsius,
            "output_fahrenheit": round(fahrenheit, 2)
        }), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid data type. 'celsius' must be a number."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
