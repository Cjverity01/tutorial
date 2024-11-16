from sanic import Sanic
from sanic.response import html
from sanic.request import Request
from sanic_jinja2 import SanicJinja2

# Initialize the Sanic app
app = Sanic("ConfigFormatterApp")

# Configure Sanic
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Automatically reload templates on changes

# Initialize the Jinja2 templating engine
jinja = SanicJinja2(app)

# Home route: Show the configuration form
@app.route('/')
async def config_form(request):
    return await jinja.render('config_form.html', request)

# Submit route: Handle form submission 
