from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


# TODO
# if submission of signup form is not valid, reject and re-render form with feedback of what they did wrong

# TODO
# signup form is not valid if:
#	these fields are empty: username, password, verify password
#	username and/or is not valid: contains a space, less than 3 characters or more than 20
#	password and verify password do not match
#	if email is not blank, but is not a valid email: has one '@' and one '.', no spaces, between 3 and 20 
#		characters long

# TODO
# each feedback error should be next to the field it refers to

# TODO
# if there is an error, keep the username and email fields, and clear the password fields

# TODO
# if submission of signup form is valid, display a welcome page: "Welcome, [username]!"

# TODO	
# use templates (one for home page and one for the welcome page) to render the html


@app.route('/')
def index():
	return render_template('signup_form.html')


app.run()