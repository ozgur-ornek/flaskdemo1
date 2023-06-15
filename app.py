from flask import Flask, render_template, request, flash

app=Flask(__name__)
app.secret_key="mangalAAA"

@app.route("/")
def index():
    flash("what is your name please")
    return render_template("/index.html")


@app.route("/greet", methods=["GET","POST"])
def greet():
    flash("hi "+ str(request.form['name_input'])+ ", great to see you!")
    return render_template("/index.html")

if __name__=="__main__":
    app.run(debug=True)