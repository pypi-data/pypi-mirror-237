class InvalidChoiceException(Exception):
    def __init__(self, message="Invalid choice. Please select a valid option."):
        super().__init__(message)

class InvalidMarkdownException(Exception):
    def __init__(self, message="Invalid markdown format"):
        super().__init__(message)
