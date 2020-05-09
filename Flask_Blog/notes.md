# Flask notes

@app.route("/endpoint") is called when a user accesses that endpoint. The return is HTML in string.

To return complex HTML, use render_template(). It takes an HTML template and can access variables within it.

Use {{ variable }} to use the argument 'variable' and you can use . access like {{ variable.property }} to access a dictionary's properties.

With jinja there is inheritance in templates. You can make templates with blocks in them, and then have other tempaltes inherit ("extend") them and implement the block.

We're using Bootstrap to make the web page look pretty. The most basic element is the Bootstrap 'container' which we are using to wrap the body content.

We're using url_for for our static/main.css stylesheet to generate href. In register.html, we use it where we pass 'login' into url_for in an href to reference the login function in flaskblog.py. This is supposed to be better than directly linking the href to "/login".

In href, a '#' sign is a dummy link that doesn't go anywhere. Can be used where you want to implement a feature in the future.