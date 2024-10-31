# Real-Time Chat Application

This is a real-time chat application built with Flask and Flask-SocketIO. Users can join the chat room, set a username, and send messages that are displayed to all users in real time, complete with timestamps and message history.

## Features
- **Real-Time Messaging**: Instant message delivery using WebSockets.
- **Usernames**: Users can set a username to identify themselves in the chat.
- **Message History**: New users see previous messages upon joining.
- **Enhanced UI**: A modern and clean interface for an optimal chat experience.
- **Timestamps**: Each message is timestamped to track when it was sent.

## Technologies Used
- **Backend**: Flask, Flask-SocketIO
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Custom CSS for a polished look

## Setup Instructions
To run this project locally, follow these steps:

### Prerequisites
- Python installed on your system
- Basic knowledge of Git and Git Bash

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SamsonNg00/real-time-chat-app.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd real-time-chat-app
   ```
3. **Create and Activate a Virtual Environment**:
   - **Windows (Git Bash)**:
     ```bash
     py -m venv venv
     source venv/Scripts/activate
     ```
   - **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
4. **Install Dependencies**:
   ```bash
   pip install Flask Flask-SocketIO
   ```
5. **Run the Application**:
   ```bash
   python app.py
   ```
6. **Open Your Browser**: Visit `http://127.0.0.1:5000` to use the chat app.

## How It Works
1. Users open the application in their browser and set a username.
2. They can type and send messages, which are instantly broadcast to all connected users.
3. New users who join the chat room will see the message history.

## Future Improvements
- **Multiple Chat Rooms**: Add support for multiple chat rooms.
- **User Authentication**: Implement user login and registration for better security.
- **Persistent Storage**: Use a database to store messages persistently.
- **File Sharing**: Allow users to share files and images in the chat.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

## Contact
For any questions or feedback, please contact me via:
- **Email**: samsonnguyen00@gmail.com
- **GitHub**: [SamsonNg00](https://github.com/SamsonNg00)

