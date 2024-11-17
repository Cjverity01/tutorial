from sanic import Sanic
from sanic.response import html

app = Sanic(__name__)

@app.route("/", methods=["GET", "POST"])
async def home(request):
    generated_config = ""
    if request.method == "POST":
        token = request.form.get("token", "").strip()
        guild_id = request.form.get("guild_id", "").strip()
        owners = request.form.get("owners", "").strip()
        log_url = request.form.get("log_url", "").strip()
        staff_server = request.form.get("staff_server", "").strip()

        # Ensure the Log URL has the .cjscommisions.xyz/ appended
        if log_url and not log_url.endswith(".cjscommisions.xyz/"):
            log_url = f"{log_url}.cjscommisions.xyz/"

        # Build the configuration
        generated_config = f"TOKEN={token}\nGUILD_ID={guild_id}\nOWNERS={owners}\nLOG_URL={log_url}"
        if staff_server:
            generated_config += f"\nMODMAIL_GUILD_ID={staff_server}"

    return html(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Modmail Configuration</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                color: #333;
            }}
            .container {{
                width: 80%;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: #fff;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }}
            .form-section {{
                margin-bottom: 20px;
            }}
            .form-section label {{
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }}
            .form-section input[type="text"] {{
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 16px;
            }}
            .form-section input[type="submit"] {{
                display: block;
                width: 100%;
                padding: 10px;
                background: #28a745;
                color: #fff;
                border: none;
                border-radius: 4px;
                font-size: 16px;
                cursor: pointer;
            }}
            .form-section input[type="submit"]:hover {{
                background: #218838;
            }}
            pre {{
                background: #f8f8f8;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Modmail Bot Configuration</h1>
            <form method="POST" class="form-section">
                <label for="token">Bot Token <span style="color: red;">*</span></label>
                <input type="text" id="token" name="token" placeholder="Enter your bot token" required>

                <label for="guild_id">Guild ID <span style="color: red;">*</span></label>
                <input type="text" id="guild_id" name="guild_id" placeholder="Enter your guild ID" required>

                <label for="owners">Owners <span style="color: red;">*</span></label>
                <input type="text" id="owners" name="owners" placeholder="Enter bot owner(s) ID(s)" required>

                <label for="log_url">Log URL <span style="color: red;">*</span></label>
                <input type="text" id="log_url" name="log_url" placeholder="Enter your log URL" required>

                <label for="staff_server">Staff Server</label>
                <input type="text" id="staff_server" name="staff_server" placeholder="Enter your staff server ID (optional)">

                <input type="submit" value="Generate Configuration">
            </form>

            <!-- Display the generated config if available -->
            {"<h2>Generated Configuration:</h2><pre>" + generated_config + "</pre>" if generated_config else ""}
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
