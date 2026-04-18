from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mi App</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }
            h1 {
                font-size: 3rem;
                color: #333;
                display: block;
            }
        </style>
    </head>
    <body>
        <h1>¡Bienvenidos :)!</h1>
        <br>
        <h2> Introducción a la Programación y Computación 1 - 770 Seccion D </h2>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)