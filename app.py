from sanic import Sanic
from sanic.response import html, json
from sanic.request import Request

app = Sanic(__name__)

@app.route('/')
async def index(request):
    # HTML for the form with the light/dark mode toggle
    return html("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Modmail Bot Configuration</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
            /* Base styles for both light and dark mode */
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                color: #333;
                transition: background-color 0.3s ease, color 0.3s ease;
            }
            .container {
                width: 80%;
                max-width: 1000px;
                margin: 50px auto;
                padding: 30px;
                background-color: #fff;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
                border-radius: 12px;
                transition: background-color 0.3s ease;
            }
            h1, h2 {
                color: #1e2a48;
                text-align: center;
            }
            h3 {
                color: #4c6a92;
            }
            .form-section {
                background-color: #f8f9fa;
                padding: 30px;
                border-radius: 12px;
                margin-bottom: 30px;
                box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease;
            }
            .form-section input[type="text"] {
                width: 100%;
                padding: 14px;
                margin: 15px 0;
                border: 1px solid #ddd;
                border-radius: 8px;
                box-sizing: border-box;
                font-size: 16px;
            }
            .form-section input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                padding: 18px 25px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 18px;
                width: 100%;
                transition: background-color 0.3s ease;
            }
            .form-section input[type="submit"]:hover {
                background-color: #45a049;
            }
            .message {
                background-color: #e7f4e4;
                color: #2d6a4f;
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 40px;
                text-align: center;
                font-size: 18px;
            }
            .footer {
                text-align: center;
                margin-top: 50px;
                font-size: 16px;
                color: #888;
            }

            /* Light mode */
            body.light-mode {
                background-color: #f4f7fc;
                color: #333;
            }
            .container.light-mode {
                background-color: #fff;
            }

            /* Dark mode */
            body.dark-mode {
                background-color: #181818;
                color: #ccc;
            }
            .container.dark-mode {
                background-color: #2b2b2b;
            }
            .form-section.dark-mode {
                background-color: #333;
            }
            .form-section input[type="text"].dark-mode {
                background-color: #555;
                color: #eee;
                border: 1px solid #666;
            }
            .form-section input[type="submit"].dark-mode {
                background-color: #1a8c59;
            }
            .message.dark-mode {
                background-color: #2a3d34;
                color: #b1e0b4;
            }
            .footer.dark-mode {
                color: #bbb;
            }

            /* Button styling */
            .toggle-button {
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                position: absolute;
                top: 20px;
                right: 20px;
                font-size: 16px;
                transition: background-color 0.3s ease;
            }
            .toggle-button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body class="light-mode">
        <button class="toggle-button" onclick="toggleTheme()">🌞</button>
        <div class="container">
            <!-- Display the custom message -->
            <div class="message">
                <h2>Submit your configuration</h2>
            </div>
            <!-- Configuration form section -->
            <div class="form-section">
                <h3>Modmail Bot Configuration</h3>
                <p>Please fill out the form below with the necessary details for us to deploy your bot.</p>
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
                    <input type="submit" value="Generate Configuration">
                </form>
            </div>
            <!-- Display the formatted config output if available -->
            {% if generated_config %}
            <div class="form-section">
                <h3>Generated Configuration:</h3>
                <pre>{{ generated_config }}</pre>
            </div>
            {% endif %}
        </div>
        <div class="footer">
            <p>Powered by Cj's Commissions</p>
        </div>

        <script>
            // Function to toggle between light and dark mode
            function toggleTheme() {
                const body = document.body;
                const container = document.querySelector('.container');
                const formSection = document.querySelector('.form-section');
                const inputs = document.querySelectorAll('input[type="text"]');
                const submitButton = document.querySelector('input[type="submit"]');
                const message = document.querySelector('.message');
                const footer = document.querySelector('.footer');
                const button = document.querySelector('.toggle-button');

                body.classList.toggle('dark-mode');
                container.classList.toggle('dark-mode');
                formSection.classList.toggle('dark-mode');
                message.classList.toggle('dark-mode');
                footer.classList.toggle('dark-mode');
                button.classList.toggle('dark-mode');

                if (body.classList.contains('dark-mode')) {
                    button.textContent = "🌙";
                } else {
                    button.textContent = "🌞";
                }

                inputs.forEach(input => input.classList.toggle('dark-mode'));
                submitButton.classList.toggle('dark-mode');
            }
        </script>
    </body>
    </html>
    """)

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

    # Render the same form page with the generated configuration
    return html(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Modmail Bot Configuration</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
            /* Include styles here... */
        </style>
    </head>
    <body class="light-mode">
        <button class="toggle-button" onclick="toggleTheme()">🌞</button>
        <div class="container">
            <div class="message">
                <h2>Submit your configuration</h2>
            </div>
            <div class="form-section">
                <h3>Modmail Bot Configuration</h3>
                <p>Please fill out the form below with the necessary details for us to deploy your bot.</p>
                <form action="/submit" method="post">
                    <label for="token">Bot Token:</label>
                    <input type="text" id="token" name="token" value="{token}" required><br><br>
                    <label for="guild_id">Guild ID:</label>
                    <input type="text" id="guild_id" name="guild_id" value="{guild_id}" required><br><br>
                    <label for="owners">Owners:</label>
                    <input type="text" id="owners" name="owners" value="{owners}" required><br><br>
                    <label for="log_url">Log URL:</label>
                    <input type="text" id="log_url" name="log_url" value="{log_url}" required><br><br>
                    <label for="modmail_guild_id">Modmail Guild ID (Optional):</label>
                    <input type="text" id="modmail_guild_id" name="modmail_guild_id" value="{modmail_guild_id}"><br><br>
                    <input type="submit" value="Generate Configuration">
                </form>
            </div>
            <div class="form-section">
                <h3>Generated Configuration:</h3>
                <pre>{generated_config}</pre>
            </div>
        </div>
        <div class="footer">
            <p>Powered by Cj's Commissions</p>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
