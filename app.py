from sanic import Sanic
from sanic.response import json
import logging

# Initialize the Sanic app
app = Sanic("ModmailApp")

# Serve a simple HTML form for submission
@app.route('/')
async def index(request):
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Modmail Bot Configuration</title>
        </head>
        <body>
            <h2>Submit your configuration</h2>
            <form action="/submit" method="post">
                <label for="token">Bot Token:</label>
                <input type="text" id="token" name="token" required><br><br>

                <label for="guild_id">Guild ID:</label>
                <input type="text" id="guild_id" name="guild_id" required><br><br>

                <label for="owners">Owners:</label>
                <input type="text" id="owners" name="owners" required><br><br>

                <label for="log_url">Log URL:</label>
                <input type="text" id="log_url" name="log_url" required><br><br>

                <label for="modmail_guild_id">Modmail Guild ID (Optional):</label>
                <input type="text" id="modmail_guild_id" name="modmail_guild_id"><br><br>

                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    """

@app.route('/submit', methods=["POST"])
async def submit(request):
    # Log the form data to check if it's being received
    print("Form Data Received:", request.form)

    # Extract form data
    token = request.form.get('token')
    guild_id = request.form.get('guild_id')
    owners = request.form.get('owners')
    log_url = request.form.get('log_url')
    modmail_guild_id = request.form.get('modmail_guild_id')

    # Process the form data and generate the configuration
    generated_config = f"""
    Bot Token: {token}
    Guild ID: {guild_id}
    Owners: {owners}
    Log URL: {log_url}
    Modmail Guild ID: {modmail_guild_id}
    """

    # Respond with the generated config (you can format it however you'd like)
    return json({"generated_config": generated_config})

# Run the app with the appropriate configurations
if __name__ == '__main__':
    # Run Sanic app on port 8080
    app.run(host='0.0.0.0', port=8080, debug=True)
