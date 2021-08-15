class AnonymousSurvey():
    """Takes a survey using a random survey"""

    def __init__(self, question):
        """Store a question and prepare to store responses"""
        self.question = question
        self.response = []

    def display_question(self):
        """Displays the question"""
        print(f"The Question is:\n{self.question}")

    def store_response(self, response):
        """Stores a response"""
        self.response.append(response)

    def show_result(self):
        """Displays the result of surveys"""
        print("Survey results are:\n")
        for result in self.response:
            print(f"-{result}\n")