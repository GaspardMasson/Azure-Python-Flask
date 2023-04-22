from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-Strava-Event-Type')
    if event_type == 'activity.create':
        activity_data = request.json
        # Traitez les données de la nouvelle activité ici
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False}), 400

if __name__ == '__main__':
    app.run()


#https://stravaappwebhook.azurewebsites.net/webhook