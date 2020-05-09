from flaskblog import app

'''
Only true when running the script directly.
Means you can start the server by running 
this script rather than do 'flask run'
'''
if __name__ == '__main__':
	app.run(debug=True)