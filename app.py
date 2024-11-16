from sanic import Sanic
from sanic.response import html

app = Sanic(__name__)

@app.route('/')
async def home(request):
    # Render the form without any generated output
    return html('''<!DOCTYPE html>
    <html lang="en">
    <!-- Your HTML content here -->
    ''')  # Place your full HTML template here.

@app.route('/submit', methods=['POST'])
async def submit(request):
    # Process form data and generate configuration
    token = request.form.get('token')
    guild_id = request.form.get('guild_id')
    owners = request.form.get('owners')
    log_url = request.form.get('log_url')
    modmail_guild_id = request.form.get('modmail_guild_id', '')

    # Create a formatted configuration (replace with your logic)
    formatted_output = f"""
    BOT_TOKEN={token}
    GUILD_ID={guild_id}
    OWNERS={owners}
    LOG_URL={log_url}
    MODMAIL_GUILD_ID={modmail_guild_id}
    """

    # Render the HTML with the formatted output
    return html(f'''<!DOCTYPE html>
    <html lang="en">
    <body>
        <!-- Your HTML content here -->
        <div class="container">
            <!-- Form Section -->
            <div class="form-section">
                <form action="/submit" method="post">
                    <input type="text" name="token" placeholder="Enter Bot Token" required>
                    <input type="text" name="guild_id" placeholder="Enter Guild ID" required>
                    <input type="text" name="owners" placeholder="Enter Owners" required>
                    <input type="text" name="log_url" placeholder="Enter Log URL" required>
                    <input type="submit" value="Generate Configuration">
                </form>
            </div>
            <!-- Conditionally display the output -->
            <div class="form-section">
                <h3>Generated Configuration:</h3>
                <pre>{formatted_output}</pre>
            </div>
        </div>
    </body>
    </html>''')
