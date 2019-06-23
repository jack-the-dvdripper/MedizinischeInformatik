from flask import Flask, request, render_template #import main Flask class and request object
import xml_file

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
def query_example():
    #language = request.args.get('language') #if key doesn't exist, returns None
    #framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    #website = request.args.get('website')

    return render_template('query_example.html', "python", "flask", "test")
    #return '''<h1>The language value is: {}</h1>
    #          <h1>The framework value is: {}</h1>
    #          <h1>The website value is: {}'''.format(language, framework, website)

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def index():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        formDict = request.form#.get('language')
        print(formDict.get('vorname'))
        tag = formDict.get('tag')
        monat = formDict.get('monat')
        jahr = formDict.get('jahr')
        geburtstag = tag + monat + jahr
        if isinstance(tag, str):
            print("hallo")



        normalDict = formDict.to_dict(flat=True)
        normalDict['geburtstag'] = geburtstag
        #formDict['geburtstag'] = geburtstag
        #formDict.update(*'geburtstag', **geburtstag)
        del normalDict['tag']
        del normalDict['monat']
        del normalDict['jahr']

        #if isinstance(formDict, dict):
        xml_file.create(formDict.get("name"), "100")
        xml_file.add(normalDict, formDict.get("name"), "100")
        #print(hallo)
    #    framework = request.form['framework']

    #    return '''<h1>The language value is: {}</h1>
    #              <h1>The framework value is: {}</h1>'''.format(language, framework)
    #print(xml_file.get("Kress", "100"))
    return render_template('requestTest.html')
    #return '''<form method="POST">
    #              Language: <input type="text" name="language"><br>
    #              Framework: <input type="text" name="framework"><br>
    #              <input type="submit" value="Submit"><br>
    #          </form>'''


@app.route('/login', methods=['GET', 'POST']) #allow both GET and POST requests
def login():
    if request.method == 'POST':
        formDict = request.form
        render_template('requestTest.html')
    return render_template('login.html')



if __name__ == '__main_':
    app.run(host='192.168.1.127', debug=True, port=5000) #run app in debug mode on port 5000
