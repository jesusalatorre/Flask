from flask import Flask 
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
	return redirect('https://jesusalatorre.github.io/About/')

if __name__=='__main__':
	app.run(debug=True)