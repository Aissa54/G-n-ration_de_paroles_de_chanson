# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    return '''<h1>The language value is: {}</h1>'''.format(language)

# allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        Style = request.form.get('Style')
        Paroles = request.form.get('Paroles')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(Style, Paroles)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Style de musique: <input type="text" name="Style"></label></div>
               <div><label>Paroles: <input type="text" name="Paroles"></label></div>
               <input type="submit" value="Submit">
           </form>'''



@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
