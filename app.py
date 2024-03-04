from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return 'a'#render_template('result.html', input_text=user_input)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port = 3000)
