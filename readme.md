# Django Quiz App - C Programming Edition

Welcome to the Django Quiz App focused on C programming! This web application allows users to test their knowledge of C programming concepts through a series of 15 easy, medium, and hard questions, along with two programming challenges.

## Features

- **User Authentication:** Users can create accounts and log in to track their progress and scores.
- **Question Database:** All questions are stored in a database, making it easy to add, modify, and retrieve questions.
- **Difficulty Levels:** Questions are categorized by difficulty levels (easy, medium, hard) for a tailored learning experience.
- **Programming Challenges:** Users can tackle two programming challenges to test their coding skills.
- **Scoring System:** The app evaluates users' performance based on their answers and provides scores accordingly.
- **Leaderboard:** A leaderboard showcases the top scores of users, adding a competitive element to the quiz. # TODO

## Additional Functionality - Compiling User C Code and Running Test Cases

In addition to the quiz functionality, this app offers a unique feature: users can submit C code for programming challenges. The app compiles the submitted code and runs test cases against it to determine the number of passed test cases.

### How It Works

1. **User Submission:** Users can submit their C code solutions for the programming challenges through the app interface.
2. **Code Compilation:** The app compiles the user-submitted code using a secure compiler.
3. **Test Cases:** After compilation, the app runs predefined test cases against the compiled code.
4. **Evaluation:** The app evaluates the output of the user's code against the expected output of the test cases.
5. **Results:** Users receive feedback on the number of passed test cases, allowing them to assess the correctness of their solutions.

This feature provides users with an interactive platform to practice coding and receive instant feedback on their solutions.

## Usage

1. Clone the repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Set up the Django project and migrate the database.
4. Run the development server using `python manage.py runserver`.
5. Access the web application through your browser and start exploring the quiz and programming challenges.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to suggest improvements, report bugs, or add new features.
