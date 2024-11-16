from sanic import Sanic
from sanic.response import html, json

app = Sanic(__name__)

@app.route('/')
async def home(request):
    # Render the HTML template as a response
    return html('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cj's Commisions Modmail Configuration</title>
    <style>
        /* Base styles for both light and dark mode */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: #333;
        }

        /* Light mode background color */
        body.light-mode {
            background-color: #ffffff;
            color: #333;
        }

        /* Dark mode background color */
        body.dark-mode {
            background-color: #181818;
            color: #ccc;
        }

        .container {
            width: 80%;
            max-width: 1000px;
            margin: 50px auto;
            padding: 30px;
            background-color: #fff;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            border-radius: 12px;
        }

        .container.dark-mode {
            background-color: #2b2b2b;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }

        .form-section {
            background-color: #f8f9fa;
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 30px;
        }

        .form-section.dark-mode {
            background-color: #333;
        }

        .form-section input[type="text"] {
            width: 100%;
            padding: 14px;
            margin: 15px 0;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
        }

        .form-section input[type="text"].dark-mode {
            background-color: #444;
            color: #eee;
            border: 1px solid #666;
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
        }

        .form-section input[type="submit"].dark-mode {
            background-color: #1a8c59;
        }

        .message {
            background-color: #e7f4e4;
            color: #2d6a4f;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 40px;
            text-align: center;
        }

        .message.dark-mode {
            background-color: #2a3d34;
            color: #b1e0b4;
        }

        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 16px;
            color: #888;
        }

        .footer.dark-mode {
            color: #bbb;
        }

        pre {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            font-size: 16px;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
        }

        pre.dark-mode {
            background-color: #333;
            color: #ccc;
        }

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
            font-size: 20px;
        }

        .toggle-button:hover {
            background-color: #45a049;
        }

        /* Remove blue color from headings and labels */
        h1, h2, h3, label {
            color: inherit;
        }
    </style>
</head>
<body class="light-mode">

    <!-- Button to toggle between light and dark modes -->
    <button class="toggle-button" onclick="toggleTheme()">
        <!-- Light mode icon (sun) -->
        <img src="https://img.icons8.com/ios-filled/50/000000/sun.png" id="theme-icon" alt="Sun/Moon" width="30px"/>
    </button>

    <div class="container">
        <!-- Display the custom message -->
        <div class="message">
            <h2>Welcome to Cj's Commisions Modmail Hosting</h2>
        </div>

        <div class="form-section">
            <p style="font-size: 18px; font-weight: bold;">Thank you for subscribing to our Modmail Hosting Service! Please follow the information below and send the generated code to support!</p>
            <h3>Modmail Bot Configuration</h3>
            <p>Please fill out the form below with the necessary details for us to deploy your bot.</p>
        </div>

        <!-- Configuration form section -->
        <div class="form-section">
            <h3>Modmail Bot Configuration</h3>
            <p>Please fill out the form below with the necessary details for us to deploy your bot.</p>

            <form action="/submit" method="post" id="configForm">
                <label for="token">Bot Token <span style="color: red;">*</span>:</label>
                <input type="text" id="token" name="token" placeholder="Enter your bot token" required>

                <label for="guild_id">Guild ID <span style="color: red;">*</span>:</label>
                <input type="text" id="guild_id" name="guild_id" placeholder="Enter the server (guild) ID" required>

                <label for="owners">Owners <span style="color: red;">*</span>:</label>
                <input type="text" id="owners" name="owners" placeholder="Enter bot owner(s) ID" required>

                <label for="log_url">Log URL <span style="color: red;">*</span>:</label>
                <input type="text" id="log_url" name="log_url" placeholder="Enter your log URL" required>

                <label for="modmail_guild_id">Modmail Guild ID (Optional):</label>
                <input type="text" id="modmail_guild_id" name="modmail_guild_id" placeholder="Enter Modmail Guild ID (optional)">

                <input type="submit" value="Generate Configuration">
            </form>
        </div>

        <!-- Button to show the generated configuration -->
        <button id="showConfigBtn" style="display:none;" onclick="showConfig()">Show Generated Configuration</button>

        <!-- Placeholder for generated config -->
        <div id="generatedConfig" style="display:none;">
            <h3>Generated Configuration:</h3>
            <pre id="configOutput"></pre>
        </div>

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
            const themeIcon = document.getElementById('theme-icon');

            // Toggle classes for light and dark mode
            body.classList.toggle('dark-mode');
            container.classList.toggle('dark-mode');
            formSection.classList.toggle('dark-mode');
            message.classList.toggle('dark-mode');
            footer.classList.toggle('dark-mode');
            button.classList.toggle('dark-mode');

            // Change button icon based on mode
            if (body.classList.contains('dark-mode')) {
                themeIcon.src = "https://img.icons8.com/ios-filled/50/FFFFFF/moon.png";  // Moon icon for dark mode
            } else {
                themeIcon.src = "https://img.icons8.com/ios-filled/50/000000/sun.png";  // Sun icon for light mode
            }

            // Apply dark mode styling to inputs and buttons
            inputs.forEach(input => input.classList.toggle('dark-mode'));
            submitButton.classList.toggle('dark-mode');
        }

        // Function to show the generated configuration
        function showConfig() {
            const form = document.getElementById("configForm");
            const showConfigBtn = document.getElementById("showConfigBtn");
            const generatedConfig = document.getElementById("generatedConfig");
            const configOutput = document.getElementById("configOutput");

            // Simulate generating the config from form data (replace with actual logic)
            const configData = {
                token: document.getElementById("token").value,
                guild_id: document.getElementById("guild_id").value,
                owners: document.getElementById("owners").value,
                log_url: document.getElementById("log_url").value,
                modmail_guild_id: document.getElementById("modmail_guild_id").value
            };

            // Format the config as a string
            const formattedConfig = `
Bot Token: ${configData.token}
Guild ID: ${configData.guild_id}
Owners: ${configData.owners}
Log URL: ${configData.log_url}
Modmail Guild ID: ${configData.modmail_guild_id}
            `;

            // Display the generated configuration
            configOutput.textContent = formattedConfig;

            // Show the config and the button
            showConfigBtn.style.display = "none";
            generatedConfig.style.display = "block";
        }
    </script>

</body>
</html>''')

# POST route to handle form submission
@app.route('/submit', methods=['POST'])
async def submit(request):
    # Extract data from the form
    token = request.form.get('token')
    guild_id = request.form.get('guild_id')
    owners = request.form.get('owners')
    log_url = request.form.get('log_url')
    modmail_guild_id = request.form.get('modmail_guild_id', '')

    # Format the configuration
    formatted_config = f"""
Bot Token: {token}
Guild ID: {guild_id}
Owners: {owners}
Log URL: {log_url}
Modmail Guild ID: {modmail_guild_id}
    """

    # Return the page with the generated configuration
    return html(f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Cj's Commisions Modmail Configuration</title>
            <style>
                /* Styles here */
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Generated Configuration:</h2>
                <pre>{formatted_config}</pre>
            </div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
