# Quizz Me: A Trivia Game with LEDs and User Feedback

"Quizz Me" is a Python-based trivia game designed to test your knowledge and provide immediate feedback through LEDs.  It retrieves questions and answers from the Open Trivia Database API ([https://opentdb.com/](https://opentdb.com/)), offering a wide range of general knowledge topics. The game uses two LEDs (green and red) to indicate correct and incorrect answers, enhancing the user experience.

## Description

"Quizz Me" consists of three main Python functions:

1.  **`main()`:**
    *   Initializes LED objects.
    *   Turns off LEDs at the start of the game.
    *   Retrieves a trivia question using the `questions()` function.
    *   Controls the LEDs based on the user's answer: green for correct, red for incorrect.

2.  **`questions()`:**
    *   Handles communication with the Open Trivia Database API.
    *   Constructs the API URL.
    *   Retrieves trivia data using the `requests` library.
    *   Parses the JSON response.
    *   Extracts the question, correct answer, and incorrect answers.
    *   Combines all answers into a single list and shuffles them to randomize the order.
    *   Displays the question and answer choices (A-D) to the user.
    *   Uses the `validate()` function to ensure the user enters a valid answer (A-D).
    *   Handles potential errors during API calls and provides informative messages to the user.

3.  **`validate()`:**
    *   Validates user input.
    *   Checks if the user's answer is a single character and within the valid answer choices (A-D).
    *   Prompts the user to re-enter a valid choice if the input is invalid.

## Design Decisions

*   **API and Question Source:** The Open Trivia Database was chosen for its extensive library of trivia questions, providing a wide range of topics for users.
*   **LED Feedback:** LEDs provide immediate visual feedback, enhancing the user experience. Green and red were chosen for their universally recognized association with correct and incorrect answers.
*   **User Input Validation:** Input validation ensures the program only accepts valid answer choices (A-D), preventing errors and maintaining game logic.
*   **Error Handling:** Error handling for API requests protects the program's functionality and provides informative error messages.
*   **Future Considerations:** While initially considering different difficulty levels (easy, medium, hard), a simpler design was chosen for this project.

## Testing and Quality Assurance

*   Mock tests were used to simulate API responses and test the interaction between the program and the API.
*   Manual testing with various valid and invalid user inputs was conducted to ensure correct program functionality.
*   Clear and concise error messages were implemented to guide users.

## Installations

*   `requests`
*   `gpiozero`

To install these libraries, you can use pip:

```bash
pip install requests gpiozero
