from google.adk.agents.llm_agent import Agent

qa_agent = Agent(
    model="gemini-2.5-flash",
    name="qa_agent",
    description="An agent that answers questions about user preferences.",
    instruction="""
You are a helpful assistant that answers questions about the user's preferences.

The user's name is {username}.

The user has the following preferences:
- Favorite color: {favorite_color}
- Favorite food: {favorite_food}
- Favorite movie: {favorite_movie}
- Favorite TV show: {favorite_tv_show}

When answering:
- Use ONLY the information above.
- Respond in plain natural language.
- Do NOT write code or tools.
- If something is not listed above, say you don't know.
"""
)
