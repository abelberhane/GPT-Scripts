# Role-prompt: Write a Python script that connects to a database and retrieves information safely with comprehensive error handling. The code should demonstrate how to catch multiple types of exceptions, potentially define custom exceptions, and ensure the program does not crash upon encountering an error. It should also log meaningful error messages for debugging purposes.

import sys
import logging

# Setting up basic configuration for logging error messages
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConnectionError(Exception):
    """A custom exception used to report errors in database connectivity."""
    pass

def connect_to_database():
    """
    Simulates connecting to a database. For the sake of this example, we'll use a dummy function that raises an error to simulate a connection failure.
    """

    # Here, we simulate a connection error by explicitly raising a built-in exception. In a real-world scenario, this could be an actual database connectivity operation that might fail for any number of reasons.
    raise ConnectionError("Failed to connect to the database.")

def query_database():
    """
    Simulates a database query. For this example, we're using a dummy function that raises an error to simulate a query failure.
    """

    # This represents a database query operation that fails, raising another built-in exception. The specificity of exceptions allows for precise error handling, one of the key benefits of using role-prompts.
    raise ValueError("Query is malformed.")

def main():
    """Main function to demonstrate error handling in action."""
    try:
        # Attempt to connect to the database
        connect_to_database()
    except ConnectionError as e:
        # Catching a specific exception ensures that the program can respond to different errors in a context-appropriate way, a core advantage of role-prompting.
        logger.error(f"Database connection failed: {e}")
        sys.exit(1)  # Exit with an error code

    try:
        # Attempt to query the database
        query_database()
    except ValueError as e:
        # Catching distinct exceptions allows GitHub Copilot to understand the need for handling different types of errors separately, providing more meaningful responses.
        logger.error(f"Database query failed: {e}")
        sys.exit(1)  # Exit with an error code

    except Exception as e:
        # A general exception clause like this is a safeguard, ensuring that even unexpected errors won't crash the program. This resilience is a direct result of the comprehensive error handling stipulated in the role-prompt.
        logger.error(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit with an error code

# Execute the script
if __name__ == "__main__":
    main()
