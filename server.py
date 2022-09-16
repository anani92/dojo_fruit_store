from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print(request.form)

    return render_template("index.html")

@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    print(request.form)
    sb = request.form['strawberry']
    rb = request.form['raspberry']
    app = request.form['apple']
    first_n = request.form['first_name']
    last_n = request.form['last_name']
    count = int(sb) + int(rb) + int(app)
    print(count)
    print(f"Charging {first_n} {last_n} for {count} fruits")
    return render_template("checkout.html", apple=app, strawberry=sb, raspberry=rb, student_id = request.form['student_id'], first_name = first_n, last_name = last_n)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)