from flask import Flask, jsonify,request

word='HiFlask:)'

app = Flask(__name__)


@app.route('/get-word', methods=['GET'])
def get_word():
    return jsonify({"word": word})

@app.route('/set-word', methods=['POST'])
def set_word():
    global word
    word = request.json.get('word', word)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)

