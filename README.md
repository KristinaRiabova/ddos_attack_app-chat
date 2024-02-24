## HOW TO USE



# Firstly you need to open http://localhost:8000/ and you will see two users you need to write a secret word (Duck) to recieve a link to the website.Then when you clickk to the link you'll see registration page. After that u will have your own profile and than u will see three links (update profile, delete profile and launch ddos attack)


## All links:



http://localhost:8000/ddos/

http://localhost:8000/registration/

http://localhost:8000/login/

http://localhost:8000/

http://localhost:8000/profile/

http://localhost:8000/profile/update/

http://localhost:8000/profile/delete/


# This guide aims to help future developers understand the implemented features in the provided code.

WebSocket Integration:
Enables real-time communication between clients and the server.
Implemented using Django Channels library.
Facilitates instant message delivery without requiring page reloads.

Template Customization:
Enhances user experience through visually appealing and user-friendly interfaces.
Forms for user authentication, registration, and other functionalities.
Applies styling and responsive design principles for consistency across devices.

The ChatConsumer class is the WebSocket consumer handling connections, message reception, and broadcasting.
It inherits from AsyncWebsocketConsumer provided by Django Channels.
connect() method accepts WebSocket connections.
receive() method handles incoming messages and broadcasts them to other connected clients.

URL patterns are defined to route WebSocket connections to the ChatConsumer.
WebSocket connections are routed through the AuthMiddlewareStack for authentication.
Configuration is done in the ProtocolTypeRouter within the routing.py file.

JavaScript WebSocket client establishes a connection with the server.
Functions handle sending and receiving messages.
Event listeners manage user interactions such as message submission.
Auto-responses and notifications are implemented for user engagement.


## Database Integration Documentation

For this project, MongoDB was chosen as the database solution due to several reasons:

Flexibility: MongoDB is a NoSQL database, offering a flexible schema design that allows for easy adaptation to changing data requirements.

Ease of Use: MongoDB's query language is intuitive and easy to understand, simplifying database operations and development tasks.

# Entity Models:

UserProfile Model:

Stores user information such as username, email, and password.

Profile Model:

Represents additional profile information associated with each user, such as a bio field.


## API Endpoints:

# Registration Endpoint:

URL: /registration/
Method: POST
Parameters: username, email, password
Functionality: Creates a new user profile and saves it to the database.

# Login Endpoint:

URL: /login/
Method: POST
Parameters: username, password
Functionality: Authenticates the user and logs them into the system.

# Profile Creation Endpoint(after registration):

URL: /profile_created/
Method: GET
Functionality: Retrieves the user profile information after successful login.

# Profile Update Endpoint(update your bio):

URL: /update_profile/
Method: POST
Parameters: bio
Functionality: Updates the bio information of the user's profile.

# Profile Deletion Endpoint:

URL: /delete_profile/
Method: POST
Functionality: Deletes the user's profile from the system.

# DDoS Endpoint:

URL: /ddos/
Method: GET
Functionality: Renders a page for launching DDoS attacks (for testing purposes).

# Error Handling:

The code implements error handling mechanisms to gracefully manage unexpected situations and prevent application crashes.
Error handling techniques such as try-except blocks, conditional checks, and status code validations are employed.
HTTP status codes and descriptive error messages are returned to the client to communicate the nature of encountered errors.


Login Template (login.html):

Presents a form for user login with fields for username and password.

Registration Template (registration.html):

Provides a form for user registration with fields for username, email, age, and password.
Implements client-side validation for password requirements using JavaScript.

Index Template (index.html):

Represents the main landing page.
Contains basic layout and minimal styling for simplicity.

DDOS Attack Template (ddos.html):

Offers a form for launching a DDOS attack.
Includes fields for target, port, and duration of the attack.

CASE DIAGRAM(UML)
<img width="261" alt="image" src="https://github.com/KristinaRiabova/ddos_attack_app-chat/assets/103763577/f3db273d-f5e6-4bc1-acc5-065509f490ea">

