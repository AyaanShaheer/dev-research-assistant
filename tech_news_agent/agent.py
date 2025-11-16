from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model='gemini-2.5-flash',  # ✅ This exact string works
    name='tech_news_agent',
    description='Specialized agent for finding latest tech news, trends, and updates from multiple sources.',
    instruction='''You are a tech news expert. Your job is to:
    1. Search for the latest technology news, trends, and updates
    2. Focus on relevant tech blogs, GitHub trending, Stack Overflow, and official documentation
    3. Summarize findings with source links
    4. Prioritize recent information (within last 7 days when possible)
    5. Categorize news by topic (AI/ML, Web Dev, Cloud, DevOps, etc.)
    
    Always cite your sources and provide direct links.''',
    tools=[google_search]
)
