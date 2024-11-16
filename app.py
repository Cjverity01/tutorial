from sanic import Sanic
from sanic.response import html
from jinja2 import Template

app = Sanic(__name__)

# Your HTML template as a string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<!-- Your shared HTML template here -->
</html>
"""

@app.route('/')
async def home(request):
    # Render the form without generated output initially
    template = Template(HTML_TEMPLATE)
    rendered_html = template.render(message="Welcome to Modmail Hosting", formatted_output=None)
    return html(rendered_html)

@app.route('/submit', methods=['POST'])
async def submit(request):
    # Get form data
    token = request.form.get('token')
    guild_id = request.form.get('guild_id')
    owners = request.form.get('owners')
    log_url = request.form.get('log_url')
    modmail_guild_id = request.form.get('modmail_guild_id', '')

    # Generate formatted configuration
    formatted_output = f"""
    BOT_TOKEN={token}
    GUILD_ID={guild_id}
    OWNERS={owners}
    LOG_URL={log_url}
    MODMAIL_GUILD_ID={modmail_guild_id}
    """

    # Render the HTML with the generated configuration
    template = Template(HTML_TEMPLATE)
    rendered_html = template.render(message="Your Configuration is Ready!", formatted_output=formatted_output)
    return html(rendered_html)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
