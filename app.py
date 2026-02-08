from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>مرحباً بك! هذا أول تطبيق ويب لي على Termux 🚀</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

