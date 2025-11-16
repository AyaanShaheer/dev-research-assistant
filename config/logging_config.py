"""
Logging and observability configuration for Dev Research Assistant
"""
import logging
import sys
from datetime import datetime

def setup_logging(log_level: str = "INFO"):
    """
    Configure logging for the application with structured output.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
    """
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    simple_formatter = logging.Formatter(
        fmt='%(levelname)s: %(message)s'
    )
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, log_level.upper()))
    
    # Console handler (stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    # File handler for detailed logs
    log_filename = f"logs/dev_research_assistant_{datetime.now().strftime('%Y%m%d')}.log"
    file_handler = logging.FileHandler(log_filename, mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    
    # Add handlers
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    
    return root_logger

# Session tracking
class SessionTracker:
    """Track agent sessions for analytics and evaluation."""
    
    def __init__(self):
        self.sessions = []
    
    def log_session(self, agent_name: str, query: str, response_time: float, success: bool):
        """Log a session interaction."""
        session_data = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent_name,
            "query": query,
            "response_time_ms": response_time * 1000,
            "success": success
        }
        self.sessions.append(session_data)
        logging.info(f"Session logged: {agent_name} - {response_time:.2f}s")
    
    def get_metrics(self):
        """Get aggregated metrics from tracked sessions."""
        if not self.sessions:
            return {}
        
        total = len(self.sessions)
        successful = sum(1 for s in self.sessions if s["success"])
        avg_time = sum(s["response_time_ms"] for s in self.sessions) / total
        
        return {
            "total_sessions": total,
            "success_rate": successful / total,
            "avg_response_time_ms": avg_time
        }
