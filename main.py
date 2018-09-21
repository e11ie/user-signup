from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

# page header & footer
page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>User Signup</title>
    </head>
    <body>
        <h1>User Signup</h1>
"""

page_footer = """
    </body>
</html>
"""
# TODO: inputs for username, password, verify password, and email (optional) and submit button
user_signup_form = """
<form method="post">
	<table>
		<tr>
			<td>
				<label for="username">Username</label>
			</td>
			<td>
				<input name="username" type="text" />
			</td>
		</tr>
		<tr>
			<td>
				<label for="password">Password</label>
			</td>
			<td>
				<input name="password" type="password" />
			</td>
		</tr>
		<tr>
			<td>
				<label for="verify-password">Verify Password</label>
			</td>
			<td>
				<input name="verify-password" type="password" />
			</td>
		</tr>
		<tr>
			<td>
				<label for="email">Email (optional)</label>
			</td>
			<td>
				<input name="email" type="text" />
			</td>
		</tr>
	</table>
	<input type="submit" value="Submit" />
</form>
"""

# Build Page by sandwiching content with page header and footer
def build_page_content(content_string):
	return page_header + content_string + page_footer

@app.route('/')
def index():
	return build_page_content(user_signup_form)


app.run()