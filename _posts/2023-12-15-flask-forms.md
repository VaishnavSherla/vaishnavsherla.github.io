---
layout: post
title: Forms in Flask
date: 2023-12-17 00:00:00 +0000
tags: [flask]
description: Vaishnav Sherla explains the significance of forms in Flask. Explore the fundamental approach for handling form submission using Flask's request object for both GET and POST methods.
---
## Why do we need forms?
Forms act as a communication bridge between users and web applications. By allowing users to submit data, forms serve as a means of gathering information, performing validations, and providing feedback.

## Basic Approach For Handling Form Submission
We can use the basic Flask request object for both GET and POST methods.
Take a look at the code. I have provided explanations for these methods below.

{% highlight html %}
{% raw %}
<!-- Base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %} | Forms</title>
    <style>
        body {
            background-color: #212121;
            color: white;
        }
    </style>
</head>
<body>
    <h1>NavBar</h1>
    {% block content %}
        
    {% endblock %}
    <h1>Footer</h1>
</body>
</html>{%endraw%}

{% endhighlight %} 

{% highlight html %}
{% raw %}
<!-- index.html -->
{% extends "base.html" %}

{% block title %}Forms{% endblock %}

{% block content %}
    <form action="{{ url_for('validator') }}">
        <label for="mail">Mail: </label>
        <input type="mail" name="mail">
        <br>
        <label for="password">Password: </label>
        <input type="password" name="password">
        <br>
        <br>
        <input type="submit" value="Submit">
    </form>
{% endblock %}
{% endraw %}
{% endhighlight %} 

{% highlight html %}
{% raw %}
<!-- validate.html -->
{% extends "base.html" %}

{% block title %}Response{% endblock %}

{% block content %}
    {% if mail == 'admin@gmail.com' %}
        {% if password == 'admin' %}
            <h1>You are logged in</h1>
        {% else %}
            <h1>Wrong Password</h1>
        {% endif %}
    {% else %}
        <h1>Unauthorized Access.</h1>
    {% endif %}
{% endblock %}{%endraw%}

{% endhighlight %}

{% highlight html %}
{%raw%}
<!-- form.html -->
{% extends "base.html" %}

{% block title %}Post Form{% endblock %}

{% block content %}
    <form method="POST">
        <label for="mail">Mail: </label>
        <input type="email" name="mail">
        <br>
        <label for="password">Password: </label>
        <input type="password" name="password">
        <br>
        <br>
        <input type="submit" value="Submit">
    </form>
    
    {% if response %}
        <p>{{ response }}</p>
    {% endif %}
{% endblock %}

{% endraw %}
{% endhighlight %} 

{% highlight python %}
{% raw %}
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Using Get Method.
@app.route('/validator')
def validator():
    # The request.args dictionary contains the arguments passed to the URL in the form of a dictionary
    # http://127.0.0.1:5000/validator?mail=admin%40gmail.com&password=admin
    # The get method takes in the name of the argument as a string and returns its value as a string
    
    mail = request.args.get('mail')
    password = request.args.get('password')
    return render_template('validate.html', mail=mail, password=password)

# Using Post Method.
@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        mail = request.form['mail']
        password = request.form['password']
        if mail == 'admin@gmail.com' and password == 'admin':
            return render_template('form.html', response='Logged in!')
        else:
            return render_template('form.html', response='Invalid Mail Pass!')
    return render_template('form.html', response=None)

if __name__ == '__main__':
    app.run(debug=True)

{% endraw %}
{% endhighlight %} 
- Request Object
  + GET Method
    * Upon submission of the form in index.html, the action attribute directs the data to the validator endpoint, as specified by url_for('validator').
    * This action generates a URL containing the form data as query parameters. For instance, a URL like `http://127.0.0.1:5000/validator?mail=admin%40gmail.com&password=admin` is created, encapsulating the submitted data.
    * In the Flask application, the validator view handles the incoming GET request. It extracts and processes the data from the URL parameters, retrieving information like mail and password.
    * Once the data is processed, the validator view passes this information as a context to the validate.html template for rendering.
    * Within validate.html, utilizing this context, the template generates the appropriate content, such as validation results or response messages, which is then displayed to the user on the web page.
  + POST Method
    * When the user goes to the endpoint of the form, the render_template method renders the form.html, as it is a GET request.
    * When the user submits the form, it becomes a POST request. Here, we wrote some logic which gets triggered internally within the form view, since there is no action attribute associated with the form.
    * We will validate and show the response back to the end user.

> Well, i've covered the basics of Forms in Flask. In the next post, I'll be covering the _Advanced Forms_ in Flask.