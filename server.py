from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/<int:y>")
@app.route("/<int:y>/<int:x>")
@app.route("/<int:y>/<color1>")
@app.route("/<int:y>/<int:x>/<color1>")
@app.route("/<int:y>/<int:x>/<color1>/<color2>")

def index(y=8,x=8,color1="red",color2="black"):
    return render_template("index.html", cols=y, rows=x, color1=color1,color2=color2)

if __name__ == "__main__":
    app.run(debug=True)
