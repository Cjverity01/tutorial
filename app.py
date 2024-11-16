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

# Test route to check if the server is working
@app.route('/test')
async def test_route(request):
    return html('<h1>Server is running!</h1>')

# Home route: Show the configuration form
@app.route('/')
async def config_form(request):
    return jinja.render('config_form.html', request)

# Submit route: Handle form submission and display the formatted result
@app.route('/submit', methods=['POST'])
async def submit_config(request: Request):
    # Print form data for debugging
    print(request.form)  # <-- Debugging line

    # Extract form data (key-value pairs)
    token = request.form.get('token', [None])[0]
    guild_id = request.form.get('guild_id', [None])[0]
    owners = request.form.get('owners
