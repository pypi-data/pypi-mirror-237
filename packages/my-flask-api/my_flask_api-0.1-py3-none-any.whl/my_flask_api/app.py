from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    
    # Check if data exists and contains 'a' and 'b'
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Please provide both "a" and "b" values.'}), 400

    try:
        a = float(data['a'])
        b = float(data['b'])
    except ValueError:
        return jsonify({'error': 'Please provide numeric values for "a" and "b".'}), 400

    result = add_numbers(a, b)
    return jsonify({'result': result})

def add_numbers(a, b):
    return a + b

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
