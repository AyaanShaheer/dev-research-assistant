"""
Custom tools for the Dev Research Assistant
"""
from typing import Dict, Any

def save_research_note(topic: str, content: str, source: str = "") -> Dict[str, Any]:
    """
    Save a research note for future reference.
    
    Args:
        topic: The topic or category of the note
        content: The actual note content
        source: Optional URL or source reference
    
    Returns:
        Confirmation message
    """
    # In a real implementation, this would save to a database
    # For now, we'll just return a confirmation
    return {
        "status": "success",
        "message": f"Research note saved for topic: {topic}",
        "topic": topic,
        "content": content,
        "source": source
    }

def format_code_snippet(code: str, language: str = "python") -> str:
    """
    Format code snippets for better readability.
    
    Args:
        code: The code to format
        language: Programming language (python, javascript, etc.)
    
    Returns:
        Formatted code string
    """
    return f"``````"
