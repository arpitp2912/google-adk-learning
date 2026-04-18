from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
from datetime import datetime

def get_current_time() ->dict:
    """Tool to get the current time in YYYY-MM-DD HH:MM:SS format. Returns an error message if the time cannot be fetched."""
    try:
        return {
            "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    except Exception as e:
        return {
            "error": f"An error occurred while fetching the current time: {str(e)}"
        }


# root_agent = Agent(
#     name="basic_search_agent",
#     model="gemini-2.5-flash",
#     description="Agent to answer questions",
#     instruction="I can answer your questions by searching the internet. Just ask me anything!",
#     # google_search is a pre-built tool which allows the agent to perform Google searches.
#     tools=[google_search]
# )

root_agent = Agent(
    name="basic_search_agent",
    model="gemini-2.5-flash",
    description="AI Assistant",
    instruction="You are a helpful assistant that can use tools to answer questions. Use the get_current_time tool to get the current date and time.",
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    tools=[get_current_time]
)