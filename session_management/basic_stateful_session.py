import os
import uuid
import asyncio
from dotenv import load_dotenv
from pprint import pprint

# pip install google-genai
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from qa_agent.agent import qa_agent  # your Agent from qa_agent/agent.py

async def main():
    # pip install python-dotenv
    load_dotenv()

    # Create an in-memory session service
    session_service = InMemorySessionService()

    APP_NAME = "BrandonBot"
    USER_ID = "brandon_hancock"

    # Define initial state with user information
    initial_state = {
        "username": "Brandon",
        "favorite_color": "Blue",
        "favorite_food": "Pizza",
        "favorite_movie": "The Matrix",
        "favorite_tv_show": "Game of Thrones",
    }

    # Create a new session (NOTE: await!)
    session_id = str(uuid.uuid4())
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session_id,
        state=initial_state,
    )

    # Create a runner with our agent and session service
    runner = Runner(
        agent=qa_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    # Create a message to send to the agent
    message = types.Content(
        role="user",
        parts=[types.Part(text="What is Brandon's favorite TV show?")],
    )

    # Run the agent (async generator)
    final_response = None
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session_id,
        new_message=message,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            final_response = event.content.parts[0].text

    print("Session ID:", session_id)
    print("\nAgent Response:")
    print(final_response)

    # Fetch the final session state from the service (also async)
    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session_id,
    )

    print("\nSession State Exploration:")
    if session and hasattr(session, "state"):
        pprint(session.state)
    else:
        print("No session state found.")


if __name__ == "__main__":
    asyncio.run(main())
