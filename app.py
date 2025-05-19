from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    msg = data.get('message', '').lower()
    if 'hej' in msg:
        reply = 'Hej! Hur kan jag hjälpa dig?'
    else:
        reply = 'Jag förstår inte, kan du prova igen?'
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
