This guide aims to help future developers understand the implemented features in the provided code.

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
