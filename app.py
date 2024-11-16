from sanic import Sanic
from sanic.response import html, json

# Initialize the Sanic app
app = Sanic("ModmailApp")

# Serve the HTML form for submission
@app.route('/')
async def index(request):
    return html("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Modmail Bot Configuration</title>
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
                    font-family: 'Arial', sans-serif;
                }

                /* Light mode */
                body.light-mode {
                    background-color: #f4f7fc;
                    color: #333;
                }
                .container.light-mode {
                    background-color: #fff;
                }
                .form-section.light-mode {
                    background-color: #f8f9fa;
                }

                /* Dark mode */
                body.dark-mode {
                    background-color: #181818;
                    color: #ccc;
                }
                .container.dark-mode {
                    background-color: #2b2b2b;
                    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
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
                .toggle-button i {
                    font-size: 20px;
                }
            </style>
        </head>
        <body class="light-mode">
            <!-- Button to toggle between light and dark modes -->
            <button class="toggle-button" onclick="toggleTheme()">
                <i id="theme-icon" class="fa fa-sun"></i> Switch to Dark Mode
            </button>

            <div class="container">
                <!-- Display the custom message -->
                <div class="message">
                    <h2>{{ message }}</h2>
                </div>

                <!-- Configuration form section -->
                <div class="form-section">
                    <h3>Modmail Bot Configuration</h3>
                    <p>Please fill out the form below with the necessary details for us to deploy your bot.</p>

                    <form action="/submit" method="post">
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

                <!-- Display the formatted config output if available -->
                {% if formatted_output %}
                    <div class="form-section">
                        <h3>Generated Configuration:</h3>
                        <pre>{{ formatted_output }}</pre>
                    </div>
                {% endif %}
            </div>

            <div class="footer">
                <p>Powered by Cj's Commissions</p>
            </div>

            <script src="https://kit.fontawesome.com/a076d05399.js"></script>

            <script>
                function toggleTheme() {
                    const body = document.body;
                    const container = document.querySelector('.container');
                    const formSection = document.querySelector('.form-section');
                    const inputs = document.querySelectorAll('input[type="text"]');
                    const submitButton = document.querySelector('input[type="submit"]');
                    const message = document.querySelector('.message');
                    const footer = document.querySelector('.footer');
                    const button = document.querySelector('.toggle-button');
                    const themeIcon = document.querySelector('#theme-icon');

                    // Toggle classes for light and dark mode
                    body.classList.toggle('dark-mode');
                    container.classList.toggle('dark-mode');
                    formSection.classList.toggle('dark-mode');
                    message.classList.toggle('dark-mode');
                    footer.classList.toggle('dark-mode');
                    button.classList.toggle('dark-mode');

                    // Change button text and icon based on mode
                    if (body.classList.contains('dark-mode')) {
                        button.textContent = "Switch to Light Mode";
                        themeIcon.classList.remove('fa-sun');
                        themeIcon.classList.add('fa-moon');
                    } else {
                        button.textContent = "Switch to Dark Mode";
                        themeIcon.classList.remove('fa-moon');
                        themeIcon.classList.add('fa-sun');
                    }

                    // Apply dark mode styling to inputs and buttons
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

    # Respond with the generated config (you can format it however you'd like)
    return json({"generated_config": generated_config})

# Run the app with the appropriate configurations
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
