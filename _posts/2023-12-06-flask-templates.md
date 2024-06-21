---
layout: post
title: Flask Templates
date: 2023-12-06 00:00:00 +0000
tags: [flask]
description: Learn about Flask templates with Vaishnav Sherla. Explore the basics of using templates in Flask for web development.
---

## Understanding Flask Templates

Flask is built on top of Jinja2, which is a popular template engine for Python. While it's possible to return HTML code directly from the view function, as we saw in our previous blog post about Flask basics, it's not a good practice to mix presentation logic with application logic. This is where templates come in handy.

### Anatomy of File Structure

The file structure of a Flask project typically embodies distinct directories:

{% highlight bash %}
{% raw %}
myapp/
    main.py
    templates/
        base.html
        index.html
        about.html
        contact.html
    static/
        images/
            img1.png
            img2.png
        styles.css
        script.js
{% endraw %}
{% endhighlight %}


### Rendering Templates: The Heart of Display
Flask's `render_template` function is the core of rendering templates onto webpages. 
It takes a file path as an argument, and renders it onto the website when user visits certain URL.

{% highlight bash %}
{% raw %}

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

{% endraw %}
{% endhighlight %} 

Html Code 

{% highlight html %}
{% raw %}
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Templates</title>
  </head>
  <body>
    <h1>Hello From HTML</h1>
  </body>
</html>
{% endraw %}
{% endhighlight %} 

![Desktop View](/images/posts/flaskTemplates/01.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_Output of Above Code._
### The Context Object: Bridging Python and Templates
In addition to the file parameter, `render_template` also takes another parameter called the context object. 
Here we pass the list of arguments (strings, lists, dicts, bools, functions) which are further converted into a dictionary and it passes it as a context object.
{% highlight python %}
{% raw %}
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user_name = 'John'
    number_list = [1, 2, 3]
    user_data = {'username': 'Smith'}
    is_boolean = True
    return render_template('index.html', name=user_name, num_list=number_list, user=user_data, is_bool=is_boolean)

if __name__ == '__main__':
    app.run(debug=True)

{% endraw %}
{% endhighlight %} 

{% highlight html %}
{% raw %}
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
      <title>Context Obj</title>
      <style>
          body {
              background-color: #212121;
              color: white;
          }
      </style>
  </head>
  <body>
    <!-- Variable -->
    <h1>Hello, {{ name }}</h1>
    <!-- List -->
    {{ num_list[0:2] }}
    <!-- Dictionary -->
    {{ user['username'] }}
    {{ user.username }}
    <!-- Loops -->
    <ul>
        {% for num in num_list %}
            <li>{{ num }}</li>
        {% endfor %}
    </ul>
    <!-- Conditionals -->
    {% if is_bool %}
        <p>True</p>
    {% else %}
        <p>False</p>
    {% endif %}
  </body>
</html>

{% endraw %}
{% endhighlight %} 
![Desktop View](/images/posts/flaskTemplates/02.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_Output of Above Code._
### Inheritance: Simplifying Code Redundancy
Well, as we know, inheritance is a way of using the methods and attributes from a super class or parent class, which reduces the redundancy of code.

Jinja templates also support inheritance.
As we know, the navbar and footer are the same for every page on a website; rather than writing the same code in all files, we can write it once in `base.html` and import or extend it into other files.

{% highlight html %}
{% raw %}
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}|Website</title>
</head>
<body>
    <h1>NavBar</h1>
    {% block content %}
        
    {% endblock %}
    <h1>Footer</h1>
</body>
</html>{% endraw %}

{% endhighlight %} 

## Navigating and Transforming Data: UrlFor and Filters
Flask also inserts a couple of global functions and helpers into the Jinja2 context in addition to the values that are present by default. Two of these global functions are `url_for` and `filters`. `url_for` is used to generate URLs for Flask functions, i.e., we can use them to navigate by providing the view in url_for as an argument. While
`filters` are used to modify the values of variables in the templates.
### UrlFor
{% highlight html %}
{% raw %}
<!-- contact.html -->
{% raw %}{% extends 'base.html' %}

{% block title %}Contact Us{% endblock %}

{% block content %}

<p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni ex unde pariatur consequatur, dolores similique!
</p>

{# This is a comment. #}

<a href="{{ url_for('about') }}">About </a>
{% endblock %}{% endraw %}

{% endhighlight %} 
{% highlight html %}
{% raw %}
<!-- about.html -->
{% extends 'base.html' %}

{% block title %}About Us{% endblock %}

{% block content %}

<p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni ex unde pariatur consequatur, dolores similique!
</p>
<a href="{{ url_for('contactUs') }}"> Contact Us</a>
{% endblock %}

{% endraw %}
{% endhighlight %} 
{% highlight python %}
{% raw %}
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user_name = 'John'
    number_list = [1, 2, 3]
    user_data = {'username': 'Smith'}
    is_boolean = True
    return render_template('index.html', name=user_name, num_list=number_list, user=user_data, is_bool=is_boolean)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contactUs():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

{% endraw %}
{% endhighlight %} 
![Desktop View](/images/posts/flaskTemplates/03.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_Output of About Us Page._
![Desktop View](/images/posts/flaskTemplates/04.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_Output of Contact Us Page._
### Filters
As we have discussed above, Filters are used to modify the values of the variables.
Well, the Filters are represented using the pipe symbol followed by the name of the filter.
We can also create our own Filters.
{% highlight python %}
{% raw %}
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user_name = 'John'
    number_list = [1, 2, 3]
    user_data = {'username': 'Smith'}
    is_boolean = True
    return render_template('index.html', name=user_name, num_list=number_list, user=user_data, is_bool=is_boolean)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contactUs():
    return render_template('contact.html')

# Here, we are registering the filter with the name reverse.
@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

@app.route('/filters')
def filters():
    var = 'hello'
    return render_template('filters.html', var=var)

if __name__ == '__main__':
    app.run(debug=True)

{% endraw %}
{% endhighlight %} 
{% highlight html %}
{% raw %}
{% extends 'base.html' %}

{% block title %}Filters{% endblock %}

{% block content %}
{{ var|capitalize}}
<hr>
{# This is a comment. #}
{{ var|capitalize|reverse}}
{# Here, check the order of execution #}
{{ var|reverse|capitalize}}
<hr>
Output: olleH Olleh
<hr>
<a href="{{ url_for('about') }}">About </a>
{% endblock %}{%endraw%}
{% endhighlight %} 
![Desktop View](/images/posts/flaskTemplates/05.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_Output of Filters Page._
## Serving Static Files
Flask simplifies serving static files such as images, CSS, and JavaScript via the static folder. By default, Flask looks for these files in the static folder or its subfolders.

The `url_for()` function is used to generate a URL for the static file. The first argument to `url_for()` is the special endpoint name `static`, which is used by Flask to serve static files. The second argument is the filename of the static file relative to the `static` folder.

> `static` folder should only contain static files such as images, CSS, and JavaScript files. It should not contain any dynamic files, such as Python scripts or HTML files, that are generated dynamically.
{: .prompt-info }


Flask also allows you to specify a custom static folder and URL path. This can be useful if you need to serve static files from a different folder or URL path.

To specify a custom static folder and URL path, you can pass the `static_folder` and `static_url_path` parameters to the `Flask` constructor. For example, to serve static files from a folder named `public` located in the root of your Flask application and a URL path of `/public`, you can use the following code:

{% highlight python %}
{% raw %}
app = Flask(__name__, static_folder='public', static_url_path='/public')

{% endraw %}
{% endhighlight %} 

In this example, Flask will look for static files in the `public` folder instead of the default `static` folder, and will serve them under the URL path `/public` instead of the default `/static`.

{% highlight html %}
{%raw%}<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Serving Static Images</title>
    <style>
      body {
        background-color: #212121;
        color: white;
      }
      img {
        height: 40px;
      }
    </style>
  </head>
  <body>
    <h1>Hello World!</h1>
    <hr>
    <img src="../Screenshots/htmlLogo.png" alt="HTML Logo" />
    <h2>Above Image won't be Rendered.</h2>
    <hr>
    <img src="../static/htmlLogo.png" alt="HTML Logo" />
    <h2>Above and Below Image will be Rendered.</h2>
    <hr>
    <img src="{{ url_for('static', filename='htmlLogo.png') }}" alt="My Image"/>
    <hr>
  </body>
</html>

{% endraw %}
{% endhighlight %} 
{% highlight python %}
{% raw %}
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user_name = 'John'
    number_list = [1, 2, 3]
    user_data = {'username': 'Smith'}
    is_boolean = True
    return render_template('index.html', name=user_name, num_list=number_list, user=user_data, is_bool=is_boolean)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contactUs():
    return render_template('contact.html')

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

@app.route('/filters')
def filters():
    var = 'hello'
    return render_template('filters.html', var=var)

@app.route('/static')
def static_page():
    return render_template('static.html')

if __name__ == '__main__':
    app.run(debug=True)


{% endraw %}
{% endhighlight %} 
![Desktop View](/images/posts/flaskTemplates/06.png){: .dark .w-75 .shadow .rounded-10 w='1212' h='668'}
_Output of Static Page._

> Well, i've covered the templates in Flask. In the next post, I'll be covering the _Forms_ in Flask.