from flask import Flask,request, jsonify,make_response

app = Flask(__name__)

colors=[
	{
		"color": "red",
		"value": "#f00"
	},
	{
		"color": "green",
		"value": "#0f0"
	},
	{
		"color": "blue",
		"value": "#00f"
	},
	{
		"color": "cyan",
		"value": "#0ff"
	},
	{
		"color": "magenta",
		"value": "#f0f"
	},
	{
		"color": "yellow",
		"value": "#ff0"
	},
	{
		"color": "black",
		"value": "#000"
	}
]

@app.get('/colors')
def hello_world():
    return jsonify({"colors":colors})


@app.post("/update")
def update():
    colors.append({
"color": "white",
"value": "#000000"
})
    response = make_response(jsonify({"colors":colors}), 200)
    return response

if __name__ == "__main__":
    app.run(debug=True)
