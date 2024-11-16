from sanic import Sanic
from sanic.response import html
from sanic.request import Request
from sanic.templating import Jinja2

app = Sanic("ConfigFormatterApp")
app.config.from_mapping(TEMPLATES_AUTO_RELOAD=True)

# Setup Jinja2 for templating
jinja = Jinja2(app)

# Home route: Show the configuration form
@app.route('/')
async def config_form(request):
    return await jinja.render('config_form.html', request)

# Submit route: Handle form submission and display the formatted result
@app.route('/submit', methods=['POST'])
async def submit_config(request: Request):
    # Extract the key-value pairs from the form
    token = request.form.get('token', [None])[0]
    guild_id = request.form.get('guild_id', [None])[0]
    owners = request.form.get('owners', [None])[0]
    log_url = request.form.get('log_url', [None])[0]
    modmail_guild_id = request.form.get('modmail_guild_id', [None])[0]

    # Prepare the formatted output (KEY=VALUE format)
    config_output = []
    if token:
        config_output.append(f"TOKEN={token}")
    if guild_id:
        config_output.append(f"GUILD_ID={guild_id}")
    if owners:
        config_output.append(f"OWNERS={owners}")
    if log_url:
        config_output.append(f"LOG_URL={log_url}")
    if modmail_guild_id:  # Only add MODMAIL_GUILD_ID if provided
        config_output.append(f"MODMAIL_GUILD_ID={modmail_guild_id}")

    # Join the list into a single string with line breaks
    formatted_output = "\n".join(config_output)

    return await jinja.render('config_form.html', request, formatted_output=formatted_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
