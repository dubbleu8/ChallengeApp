from flask import Flask

app = Flask(__name__)

@app.route('/')
def challenge():
    return 'Ciao Patrizio, Challenge accepted! :)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
