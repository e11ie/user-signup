from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


# TODO
# if submission of signup form is not valid, reject and re-render form with feedback of what they did wrong

# TODO
# signup form is not valid if:
#	these fields are empty: username, password, verify password
#	username and/or password is not valid if: contains a space, less than 3 characters or more than 20
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


@app.route("/signup", methods=['POST'])
def signup():
	# look inside the request to figure out what the user typed
	username = request.form['username']
	password = request.form['password']
	verify_password = request.form['verify-password']
	email = request.form['email']

	# types of errors
	error = ''
	error_username = ''
	error_password = ''
	error_verify_password = ''
	error_email = ''

	# these fields are empty: username, password, verify password

	# check if username and/or password is valid 

	# check if email is valid or empty

	# if all checks passed, then render the welcome page
	return render_template('welcome.html', username=username)


def valid_username(string):
	# TODO
	# returns False if it contains a space, or less than 3 characters or more than 20
	return False

def valid_email(string):
	# TODO
	# A valid email: has one '@' and one '.', no spaces, between 3 and 20 
	# characters long
	return False

app.run()