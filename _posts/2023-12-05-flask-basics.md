---
layout: post
title: Flask Basics
date: 2023-12-05 00:00:00 +0000
tags: [flask]
description: Welcome to the introduction to Flask basics by Vaishnav Sherla, covering key concepts like setup, creating a Flask application, and working with dynamic routes. Get started with Flask for web development!
image: '/images/posts/flask.png'
permalink: '/flask-basics/'
---

## What is Flask?
Flask is a Python-based micro web framework that simplifies web development by providing tools and libraries to handle common tasks. It allows developers to focus on writing their application logic. 

## Setup
### Virtual Environment
Creating a virtual environment isolates your project's dependencies, making it easier to manage package versions and avoid conflicts between different projects.

Navigate to your current working Directory. Create and Activate Virtual Environment

on Windows
{% highlight bash %}
{% raw %}
python -m venv env
env\Scripts\activate
{% endraw %}
{% endhighlight %} 
on Mac/Linux
{% highlight bash %}
{% raw %}
python3 -m venv myenv
source myenv/bin/activate
{% endraw %}
{% endhighlight %} 

![Desktop View](/images/posts/flaskBasics/PowerShellError.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_If you encounter this error change terminal type to Command Promt._

Type `deactivate` to deactivate virtual environment.

### Creation of Flask Application.
Installing Flask
`pip install Flask` for Windows.
`pip3 install Flask` for Mac/Linux.

{% highlight python %}
{% raw %}
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

#127.0.0.1:5000/about or site.com/about
@app.route('/')
def about():
    return '<h1>About Us</h1>'
if __name__ == '__main__':
    app.run()
{% endraw %}
{% endhighlight %} 

To create a Flask application, we first need to grab the instance of the Flask class from the flask package. We use the `__name__` predefined name variable to represent the name of the current module.

We use the `app.route()` decorator function. Decorators are used to modify or enhance the behavior of the function. It is called when the user visits the root URL ('/'). The `def home()` function is the `view` function, which is used as a handler for different routes. When a user accesses the root URL ('/'), the function home is invoked. 

> Decorators are not only used in Python web frameworks. It's available in standard Python language. I'll write a post on decorator if required in future.
{: .prompt-info }

`def home()` it's the `view` function. They are used as handlers for different routes. When a user accesses the root URL ('/'), the function home is invoked.

`if __name__ == '__main__': app.run()` it's checks if the script being run directly(not imported as a module). if it's the main script, then app.run() will be executed, which will start the Flask development server to handle incoming requests.

![Desktop View](/images/posts/flaskBasics/01Output.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_Output_

## Debug Mode
This allows us to catch errors in our code and gives us access to the browser console. We should enable debug mode while writing code on our local machine.
To enable debug mode, we use `app.run(debug=True)`.

{% highlight bash %}
{% raw %}
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/error')
def error():
    # Intentional division by zero to trigger an error.
    res = 10/0
    return '<h1>Error</h1>'

if __name__ == '__main__':
    # change to app.run(debug=True) to enable debug mode.
    app.run()
{% endraw %}
{% endhighlight %} 

![Desktop View](/images/posts/flaskBasics/withoutDebugMode.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_Without Debug Mode_
![Desktop View](/images/posts/flaskBasics/withDebugMode.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_With Debug Mode_

## Dynamic Routes
Dynamic Routes allow you to handle URLs with variable parts. For instance, if you have a website where each user has their own profile accessible via a URL, you can use dynamic routes to handle these varying URLs without explicitly defining a route for each user.

{% highlight bash %}
{% raw %}
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

# Dynamic route handling for user profiles
@app.route('/profiles/<username>')
def userProfile(username='John'):
    return f"Welcome to {username}'s Profile."

if __name__ == '__main__':
    app.run(debug=True)
{% endraw %}
{% endhighlight %} 
We need to provide 2 things for configuring dynamic routes.
:   Route Definition with Variables, the variables are enclosed in `<variable>`
:   View Function to Handle Dynamic Routes, we need to pass the variables as arguments to the view function
`username='John'` is the default value for the username parameter.

![Desktop View](/images/posts/flaskBasics/02Output.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_Dynamic Routes Output_

> Well, i've covered the basics of creating a Flask application. In the next post, I'll be covering the _templates_ in Flask.