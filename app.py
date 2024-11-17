from sanic import Sanic
from sanic.response import html
from jinja2 import Template

app = Sanic(__name__)

# HTML template
html_template = Template('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modmail Configuration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #181818;
            color: #fff;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            max-width: 700px;
            margin: 20px auto;
            background-color: #333;
            padding: 20px;
            border-radius: 10px;
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input[type="text"], input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 5px;
            border: 1px solid #555;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .output {
            margin-top: 20px;
            background-color: #222;
            padding: 15px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Modmail Configuration</h1>
        <form method="post" action="/submit">
            <label for="token">Bot Token:</label>
            <input type="text" id="token" name="token" required>

            <label for="guild_id">Guild ID:</label>
            <input type="text" id="guild_id" name="guild_id" required>

            <label for="owners">Owners:</label>
            <input type="text" id="owners" name="owners" required>

            <label for="log_url">Log URL:</label>
            <input type="text" id="log_url" name="log_url" placeholder="Enter base log URL" required>

            <label for="staff_server">Staff Server:</label>
            <input type="text" id="staff_server" name="staff_server" required>

            <input type="submit" value="Generate Configuration">
        </form>
        {% if formatted_output %}
        <div class="output">
            <h2>Generated Configuration</h2>
            <pre>{{ formatted_output }}</pre>
        </div>
        {% endif %}
    </div>
</body>
</html>
''')

@app.route("/")
async def index(request):
    return html(html_template.render())

@app.route("/submit", methods=["POST"])
async def submit(request):
    token = request.form.get("token")
    guild_id = request.form.get("guild_id")
    owners = request.form.get("owners")
    log_url = request.form.get("log_url", "").strip()
    staff_server = request.form.get("staff_server")

    # Append '.cjscommisions.xyz/' to the log URL if it is not already present
    if not log_url.endswith(".cjscommisions.xyz/"):
        log_url = f"{log_url}.cjscommisions.xyz/"

    # Generate the configuration
    formatted_output = f"""
Bot Token: {token}
Guild ID: {guild_id}
Owners: {owners}
Log URL: {log_url}
Staff Server: {staff_server}
    """

    # Re-render the page with the generated configuration
    return html(html_template.render(formatted_output=formatted_output))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
