"""
Simple web application to test TravisCI mechanism
"""
from flask import Flask

HTML = """
<!DOCTYPE html>
<html lang="en" class="full-height">
    <head>
        <title>Home | TravisCI</title>
        <meta charset="utf-8">
        <link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='index3.css') }}">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        </head>
    <body>
        <h1>Ya no es mas integracion continua--es discontinua jojo</h1>

    </body>
</html>
"""

#  We have to disale this i pyllint, because pylint will fail our build every
#  time it encounters this "global" variable
app = Flask(__name__) # pylint: disable=invalid-name


@app.route('/')
def home():
    """ Main route to the web app
    """
    return HTML

if __name__ == '__main__':
    app.run()
