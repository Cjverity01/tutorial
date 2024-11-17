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
            width: 90%;
            max-width: 700px;
            margin: 20px auto;
            background-color: #333;
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"] {
            width: calc(100% - 20px);
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 5px;
            border: 1px solid #555;
            font-size: 14px;
            box-sizing: border-box;
        }
        input[type="text"]:focus {
            border-color: #4CAF50;
            outline: none;
        }
        input[type="submit"] {
            width: 100%;
            padding: 12px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
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
        .output pre {
            white-space: pre-wrap;
            word-wrap: break-word;
            margin: 0;
            color: #eee;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Modmail Configuration</h1>
        <form method="post" action="/submit">
            <label for="token">Bot Token <span style="color: red;">*</span>:</label>
            <input type="text" id="token" name="token" required>

            <label for="guild_id">Guild ID <span style="color: red;">*</span>:</label>
            <input type="text" id="guild_id" name="guild_id" required>

            <label for="owners">Owners <span style="color: red;">*</span>:</label>
            <input type="text" id="owners" name="owners" required>

            <label for="log_url">Log URL <span style="color: red;">*</span>:</label>
            <input type="text" id="log_url" name="log_url" placeholder="Enter base log URL" required>

            <label for="staff_server">Staff Server (Optional):</label>
            <input type="text" id="staff_server" name="staff_server">

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
    staff_server = request.form.get("staff_server", "").strip()

    # Append '.cjscommisions.xyz/' to the log URL if it is not already present
    if not log_url.endswith(".cjscommisions.xyz/"):
        log_url = f"{log_url}.cjscommisions.xyz/"

    # Generate the configuration
    formatted_output = f"""
TOKEN={token}
GUILD_ID={guild_id}
OWNERS={owners}
LOG_URL={log_url}
    """

    # Include Staff Server in output only if provided
    if staff_server:
    formatted_output += f"MODMAIL_GUILD_ID={staff_server}\n"

    # Re-render the page with the generated configuration
    return html(html_template.render(formatted_output=formatted_output))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
