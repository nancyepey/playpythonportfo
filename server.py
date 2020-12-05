import os
from flask import Flask, render_template, url_for, request, redirect
#render_template (it comes with flask) allows us to send the html file
#importing csv module
import csv



app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')


#creating routes dynamically
@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

# @app.route('/index.html')
# def home():
# 	return render_template('index.html')


# @app.route('/works.html')
# def works():
# 	return render_template('works.html')


# @app.route('/about.html')
# def about():
# 	return render_template('about.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')



def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n {email}, {subject}, {message} ')


# def write_to_csv(data):
# 	with open('./database.csv', mode='a', newline='',) as database2:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# 		csv_writer.writerow([email,subject,message])



def write_to_csv(data):
  with open('database.csv', newline='', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	try:
	    	# print(data)
	    	write_to_csv(data)
	    	# with open('database.txt', 'a') as f:
			   #  f.writelines(f'{data}\n')
	    	return redirect('./thankyou.html')
    	except:
    		return 'did not save to database'
    else:
    	return 'something went wrong please Try again!'



# @app.route('/')
# def hello_world():
#     return 'Hello, It\'s Nancy the Billionaire Problem Solver :)!'

# @app.route('/favicon.ico')
# def blog():
#     return 'These are my thoughts on blogs'

# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs'


# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'this is my dog'
