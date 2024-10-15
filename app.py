from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load configuration
def load_config():
    with open('config/default_config.json') as config_file:
        config_data = json.load(config_file)
    return config_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_config', methods=['GET'])
def get_config():
    config_data = load_config()
    return jsonify(config_data)

@app.route('/update_config', methods=['POST'])
def update_config():
    new_config = request.json
    with open('config/default_config.json', 'w') as config_file:
        json.dump(new_config, config_file, indent=4)
    return jsonify({"status": "Configuration updated"})

if __name__ == '__main__':
    app.run(debug=True)
