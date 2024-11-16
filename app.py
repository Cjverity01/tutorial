from sanic import Sanic
from sanic.response import json
import logging

# Initialize the Sanic app
app = Sanic("ModmailApp")

# Configure logging to reduce output
logging.basicConfig(level=logging.WARNING)  # Set log level to WARNING
logger = logging.getLogger('sanic')
logger.setLevel(logging.WARNING)  # Set logger level for Sanic

# Disable Sanic's request/response logging
app.config['ACCESS_LOG'] = False

@app.route('/')
async def test(request):
    # Just a sample route to confirm the server works
    return json({"message": "Hello, World!"})

# Example of a form submission route (adjust as needed)
@app.route('/submit', methods=["POST"])
async def submit(request):
    # Here you would handle the form submission and configuration generation
    token = request.form.get('token')
    guild_id = request.form.get('guild_id')
    owners = request.form.get('owners')
    log_url = request.form.get('log_url')
    modmail_guild_id = request.form.get('modmail_guild_id')

    # You would process the form data here and generate the configuration
    generated_config = f"Bot Token: {token}\nGuild ID: {guild_id}\nOwners: {owners}\nLog URL: {log_url}\nModmail Guild ID: {modmail_guild_id}"

    # Respond with generated config (you can format it however you'd like)
    return json({"generated_config": generated_config})

# Run the app with the appropriate configurations
if __name__ == '__main__':
    # Run Sanic app with reduced log verbosity and debug mode off
    app.run(host='0.0.0.0', port=8000, debug=False)
