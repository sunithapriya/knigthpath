from flask import Flask, request, render_template
import pathapi
import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html") 

@app.route('/path')
def path():
	s = request.args.get('start')
	e = request.args.get('end')
	start = (int(s[0]),int(s[1]))
	end = (int(e[0]),int(e[1]))
	if start:
		#return str(start)
		#return json.dumps("test")
		path = pathapi.shortestPath(start,end)
		return json.dumps(path)
	else:
		return "No valid path"


if __name__ == "__main__":
	app.run(debug=True)
