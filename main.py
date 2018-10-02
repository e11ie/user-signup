from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
	error_username = request.args.get("error_username")
	error_password = request.args.get("error_password")
	error_verify_password = request.args.get("error_verify_password")
	error_email = request.args.get("error_email")
	error = request.args.get("error")
	# check to see if username and email exist from errors
	username = ''
	email = ''
	if request.args.get("username") != None:
		username = request.args.get("username")
	if request.args.get("email") != None:
		email = request.args.get("email")
	return render_template('signup_form.html',
		error_username=error_username and cgi.escape(error_username, quote=True),
		error_password=error_password and cgi.escape(error_password, quote=True),
		error_verify_password=error_verify_password and cgi.escape(error_verify_password, quote=True),
		error_email=error_email and cgi.escape(error_email, quote=True),
		error=error and cgi.escape(error, quote=True),
		username=username and cgi.escape(username, quote=True),
		email=email and cgi.escape(email, quote=True))


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

	# check to see if these fields are empty: username, password, verify password
	if username == '':
		error_username = 'Please enter a username.'

	if password == '':
		error_password = 'Please enter a password.'

	if verify_password == '':
		error_verify_password = 'Please verify your password.'

	if username == '' or password == '' or verify_password == '':
		error= 'Please complete the required fields'
		return redirect('/?error=' + error +
			'&error_username=' + error_username +
			'&error_password=' + error_password +
			'&error_verify_password=' + error_verify_password +
			'&username=' + username +
			'&email=' + email)

	# check if username is valid 
	if not valid_len_and_char(username):
		error_username = 'Please enter a valid username.'
		error = 'Note: only characters a-z, A-Z, and 0-9, and between 3 and 20 characters in length.'
		return redirect('/?error=' + error +
			'&error_username=' + error_username +
			'&username=' + username +
			'&email=' + email)

	# check if password is valid 
	if not valid_len_and_char(password):
		error_password = 'Please enter a valid password.'
		error = 'Note: only characters a-z, A-Z, and 0-9, and between 3 and 20 characters in length.'
		return redirect('/?error=' + error +
			'&error_username=' + error_password +
			'&username=' + username +
			'&email=' + email)

	# check that password and verify_password match
	if password != verify_password:
		error_verify_password = 'Does not match the password.'
		error = 'Please make sure the password matched the verify password field.'
		return redirect('/?error=' + error +
			'&error_verify_password=' + error_verify_password +
			'&username=' + username +
			'&email=' + email)

	# check if email is valid or empty
	if email != '' and not valid_email(email):
		error_email = 'Please enter a correct email.'
		error = 'Note: No spaces, between 3 and 20 characters, and have one "@" and one "." character'
		return redirect('/?error=' + error +
			'&error_email=' + error_email +
			'&username=' + username +
			'&email=' + email)

	# if all checks passed, then render the welcome page
	return render_template('welcome.html', username=username)

# re.fullmatch
def valid_len_and_char(string):

	# Must be a between 3 and 20 characters in length
	if len(string) < 3 or len(string) > 20:
		return False
	# Must have only alphanumeric characters
	if re.search(r'\W|_', string) != None:
		return False

	return True

def valid_email(string):

	# Must be a between 3 and 20 characters in length
	if len(string) < 3 or len(string) > 20:
		return False

	# Must have no spaces
	# A valid email: has one '@' and one '.'
	regex = re.compile(r'^([^\.@\s])+@[^\.@\s]+\.[^\.@\s]+$')
	if regex.search(string) == None :
		return False

	return True

app.run()