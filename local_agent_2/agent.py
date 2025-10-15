from zoneinfo import ZoneInfo
from google.adk.agents import Agent


def get_user_location() -> dict:
    """Retrieves the user's current geographical location.
    This function obtaining the user's current location.

    Returns:
        dict: Contains status, location details, and a descriptive message.
    """
    try:
        location = {
            "city": "Arequipa",
            "region": "Arequipa",
            "country": "Perú",
            "latitude": -16.3989,
            "longitude": -71.5350,
            "timezone": "America/Lima",
        }

        return {"status": "success", "location": location}

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"No se pudo obtener la ubicación actual: {e}",
        }


# ---------- DEFINICIÓN DEL AGENTE ----------

root_agent = Agent(
    name="geo_context_agent",
    model="gemini-2.0-flash",
    description="Agente que responde adecuadamente según la ubicación geográfica del usuario.",
    instruction=(
        "You are a context-aware assistant. First, always call 'get_user_location' to determine the user's location. Then, respond naturally and appropriately based on that geographical context. "
        # "For example, if the user is in Arequipa, Perú, you might mention the local culture, "
        # "weather, timezone, or other relevant aspects of that place in your response."
    ),
    tools=[get_user_location],
)

