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
async def index(request):
    # Serve a simple HTML form for submission
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
