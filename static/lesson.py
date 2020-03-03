from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def choice(nickname, level, rating):
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="/static/style.css">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1 id="h1_top">Результаты отбора</h1>
                    <h3>Претендента на участие в миссии {}:</h3>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {} этапа отбора
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      составляет {}!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>'''.format(nickname, level, rating)


if __name__ == '__main__':
    app.run(port=8888, host='127.0.0.1')
