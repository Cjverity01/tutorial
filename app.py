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

# Home route: Show the configuration form with a custom message
@app.route('/')
async def config_form(request):
    # Your custom message to be displayed
    message = "Thank you for subscribing to our Modmail Hosting service. Please do the form below for us to deploy your bot."
    return jinja.render('config_form.html', request, message=message)

# Submit route: Handle form submission and display the formatted result
@app.route('/submit', methods=['POST'])
async def submit_config(request: Request):
    # Print form data for debugging
    print(request.form)  # <-- Debugging line

    # Extract form data (key-value pairs)
    token = request.form.get('token', [None])[0]
    guild_id = request.form.get('guild_id', [None])[0]
    owners = request.form.get('owners', [None])[0]  # <-- Fixed line
    log_url = request.form.get('log_url', [None])[0]
    modmail_guild_id = request.form.get('modmail_guild_id', [None])[0]

    # Prepare formatted output (KEY=VALUE format)
    config_output = []
    if token:
        config_output.append(f"TOKEN={token}")
    if guild_id:
        config_output.append(f"GUILD_ID={guild_id}")
    if owners:
        config_output.append(f"OWNERS={owners}")
    if log_url:
        config_output.append(f"LOG_URL={log_url}")
    if modmail_guild_id:  # Only include MODMAIL_GUILD_ID if provided
        config_output.append(f"MODMAIL_GUILD_ID={modmail_guild_id}")

    # Join the list into a single string with line breaks
    formatted_output = "\n".join(config_output)

    # Return the result to the template
    return jinja.render('config_form.html', request, formatted_output=formatted_output)

# Ensure app runs only when executed directly (not imported as a module)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # Debug enabled
