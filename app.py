from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
  b = request.form['user_input']
  b = b.replace("^", "**")
  if b == "q":
    return "Exiting application."
  try:
    return str(eval(b))
  except (SyntaxError, NameError):
    return ("Try again, this doesn't work")

if __name__ == '__main__':
    app.run(debug=True)