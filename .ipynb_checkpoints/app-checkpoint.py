from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['POST'])
def predict():
    # Pobierz dane JSON z żądania
    data = request.get_json()

    # Jeśli nie podano liczb, domyślnie przyjmujemy 0
    x1 = data.get('x1', 0) if data else 0
    x2 = data.get('x2', 0) if data else 0


    # Upewniamy się, że dane to liczby
    try:
        x1 = float(x1)
        x2 = float(x2)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. 'x1' and 'x2' must be numbers."}), 400

    # Model - reguła decyzyjna
    prediction = 1 if (x1 + x2) > 5.8 else 0

    # Zwróć odpowiedź
    response = {
        "prediction": prediction,
        "features": {"x1": x1, "x2": x2}
    }

    return jsonify(response)

# Obsługa błędu 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

# Obsługa błędu 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
