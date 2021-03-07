from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    

    return render_template('form.html')

@app.route('/results')
def show_results():
    
    cheery = request.args.get("cheery")
    honest = request.args.get("honest")
    dreary = request.args.get("dreary")

    return render_template('results.html',
                            cheery=cheery,
                            honest=honest,
                            dreary=dreary)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
