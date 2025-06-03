from mcp.server.fastmcp import FastMCP

# Get port from environment variable (Render sets this)
port = int(os.environ.get("PORT", 8001))
# Initialize FastMCP server through SSE
mcp = FastMCP("theme-park-server", port=port)

@mcp.tool()
def get_themepark_location(name: str) -> str:
    """
    Gets the location of the theme park

    Args:
        name: Name of the theme park

    Returns:
        string with the location of the theme park if found, error message if not found
    """
    locations = {
        "Wonderla": "Bangalore, India",
        "Queensland": "Chennai, India"
    }
    return locations.get(name, "Location not found")

@mcp.tool()
def get_weather(location: str):
    """
    Finds the weather info for the given location

    Args:
        location: Location for which the weather info has to be found out

    Returns:
        json string with weather info 
    """
    weather_data = {
        "Bangalore, India": {"temperature": "25°C", "condition": "Sunny"},
        "Chennai, India": {"temperature": "35°C", "condition": "Sunny"}
    }
    return weather_data.get(location, {"temperature": "Unknown", "condition": "Unknown"})

@mcp.tool()
def send_email(to: str, subject: str, body: str) -> bool:
    """
    Sends the email to the email address of the mentioned user along with the subject and description

    Args:
        to: To email address
        subject: Subject of the email
        body: Description content of the email

    Returns:
        A boolean True if the email is sent successfully False if the email sending is failed
    """
    return True  # Assume email is sent successfully

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='sse', host='0.0.0.0')
