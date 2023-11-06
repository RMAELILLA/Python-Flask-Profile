from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/areaOfcirle', methods=['GET', 'POST'])
def areaOfcirle():
    result = None
    if request.method == 'POST':
        input_float = float(request.form.get('input_float', ''))
        result = 3.14 * (input_float ** 2)
    return render_template('areaOfcirle.html', result=result)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def areaOfTriangle():
    result = None
    if request.method == 'POST':
        base = float(request.form.get('base', ''))
        height = float(request.form.get('height', ''))
        result = 0.5 * base * height
    return render_template('areaOfTriangle.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
