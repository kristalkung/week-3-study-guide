from flask import Flask, render_template, session, request, flash, redirect

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


    if cheery and honest and dreary:
        msg = "Cheery, honest, and dreary"
    elif cheery and honest and not dreary:
        msg = "cheery and honest"
    elif cheery and not honest and not dreary:
        msg = "cheery"
    elif cheery and not honest and dreary:
        msg = "cheery and dreary"
    elif not cheery and honest and dreary:
        msg = "honest and dreary"
    elif not cheery and honest and not dreary:
        msg = "honest"
    elif not cheery and not honest and dreary:
        msg = "dreary"
    else:
        flash('Pick something!')
        return redirect('/form')
        # flash message isn't showing up

    return render_template('results.html',
                            msg=msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
