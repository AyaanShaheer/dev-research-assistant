"""
Main entry point for Dev Research Assistant
This file registers all agents for the ADK web interface
"""
from tech_news_agent.agent import root_agent as tech_news_agent
from docs_search_agent.agent import root_agent as docs_search_agent
from code_debugger_agent.agent import root_agent as code_debugger_agent
from research_assistant.agent import root_agent as research_assistant

# Make agents discoverable by ADK
__all__ = [
    'tech_news_agent',
    'docs_search_agent', 
    'code_debugger_agent',
    'research_assistant'  # Main coordinator
]
