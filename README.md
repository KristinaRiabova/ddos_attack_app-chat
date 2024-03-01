![banner](https://zn.ua/img/article/4846/30_main.jpeg)



############################################################
#                                                          #
#                      DDOS ATTACKER                       #
#                                                          #
############################################################

Welcome to DDOS ATTACKER - your comprehensive platform for exploring and understanding Distributed Denial of Service (DDoS) attacks!

## Introduction

DDOS ATTACKER offers an environment for DDoS attacks. Whether you're a cybersecurity enthusiast, a network security professional, or an IT student, this tool empowers you to delve into the intricate dynamics of DDoS attacks in a safe and controlled setting.

**Please Note:** DDOS ATTACKER is intended for educational and research purposes only. Under no circumstances should this tool be used to launch attacks against systems or networks. Use of this tool to attack other servers or networks may result in severe legal consequences.

############################################################
#                     Features                               #
############################################################

- **User Authentication**: Enable users to register, log in, and manage their profiles securely.
- **Profile Management**: Users can update their profiles, including adding a bio and profile picture.
- **DDoS Attack Simulation**: Provides a simulation environment for testing DDoS attack scenarios.
- **Real-time Communication**: Utilizes WebSocket integration for real-time messaging between clients and the server.
- **MongoDB Integration**: Implements MongoDB as the database solution for flexibility and scalability.

############################################################
#                      Installation                         #
############################################################

1. Clone the repository:
`/git clone https://github.com/KristinaRiabova/ddos_attack_app-chat.git/`


2. Install dependencies:
`/pip install -r requirements.txt/`


4. Run migrations:
`/python manage.py migrate/`


6. Start the development server:
`/python manage.py runserver/`


############################################################
#                          Usage                            #
############################################################

1. Open [http://localhost:8000/](http://localhost:8000/) in your web browser.
2. Follow the instructions to register or log in.
3. Explore the different features such as profile management and launching DDoS attacks.

############################################################
#                        Endpoints                          #
############################################################

- **Registration**: `/registration/` (POST)
- **Login**: `/login/` (POST)
- **Profile Creation**: `/profile_created/` (GET)
- **Profile Update**: `/update_profile/` (POST)
- **Profile Deletion**: `/delete_profile/` (POST)
- **DDoS Attack**: `/ddos/` (GET)

############################################################
#                      Documentation                        #
############################################################

### Logging
Utilizes Python logging for comprehensive event tracking and error reporting.

### User Authentication and Registration
- **Login View (login_view):** Validates user credentials against MongoDB and Django authentication systems.
- **Registration View (registration_view):** Enables users to create accounts with unique profiles.

### Profile Management
- **Profile Creation View (profile_created_view):** Displays user profiles post-login.
- **Profile Update View (update_profile):** Allows users to modify their profile details.
- **Profile Deletion View (delete_profile):** Facilitates the removal of user profiles.

### DDoS Attack Simulation
- **DDoS View (ddos):** Simulates DDoS attacks with threading for multiple HTTP requests.

### Error Handling
Robust error handling mechanisms ensure smooth operation and recovery from unforeseen scenarios.

### Caching
Django's caching mechanism enhances performance by storing responses from external HTTP requests.

Experience the world of DDoS attacks responsibly with DDOS ATTACKER!


WebSocket Integration: Enables real-time communication between clients and the server. Implemented using Django Channels library. Facilitates instant message delivery without requiring page reloads.
Template Customization: Enhances user experience through visually appealing and user-friendly interfaces. Forms for user authentication, registration, and other functionalities. Applies styling and responsive design principles for consistency across devices.

The ChatConsumer class is the WebSocket consumer handling connections, message reception, and broadcasting. It inherits from AsyncWebsocketConsumer provided by Django Channels. connect() method accepts WebSocket connections. receive() method handles incoming messages and broadcasts them to other connected clients.
URL patterns are defined to route WebSocket connections to the ChatConsumer. WebSocket connections are routed through the AuthMiddlewareStack for authentication. Configuration is done in the ProtocolTypeRouter within the routing.py file.

JavaScript WebSocket client establishes a connection with the server. Functions handle sending and receiving messages. Event listeners manage user interactions such as message submission. Auto-responses and notifications are implemented for user engagement.

# Database Integration Documentation

For this project, MongoDB was chosen as the database solution due to several reasons:

Flexibility: MongoDB is a NoSQL database, offering a flexible schema design that allows for easy adaptation to changing data requirements.

Ease of Use: MongoDB's query language is intuitive and easy to understand, simplifying database operations and development tasks.


## Entity Models:

UserProfile Model:

Stores user information such as username, email, and password.

Profile Model:

Represents additional profile information associated with each user, such as a bio field.


# More information about API Endpoints:

## Registration Endpoint:

URL: /registration/

Method: POST

Parameters: username, email, password

Functionality: Creates a new user profile and saves it to the database.

## Login Endpoint:

URL: /login/

Method: POST

Parameters: username, password

Functionality: Authenticates the user and logs them into the system.

## Profile Creation Endpoint(after registration):

URL: /profile_created/

Method: GET

Functionality: Retrieves the user profile information after successful login.

## Profile Update Endpoint(update your bio):

URL: /update_profile/

Method: POST

Parameters: bio,profile picture

Functionality: Updates the bio information of the user's profile and picture of the profile.

## Profile Deletion Endpoint:

URL: /delete_profile/

Method: POST

Functionality: Deletes the user's profile from the system.

## DDoS Endpoint:

URL: /ddos/

Method: GET

Functionality: Renders a page for launching DDoS attacks (for testing purposes).

# Logging, Error Handling, Caching, and Performance

## Logging:

Logging is implemented using the Python logging module.

Logs are categorized into different levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

Two loggers are configured: one for general logging and another for error logging.

General logs are written to both the console and a file named logfile.log.

Error logs are written to a separate file named error.log.


## Error Handling:

Error handling middleware captures exceptions that occur during request processing.

When an exception is encountered, it logs the error message and returns a JSON response with the error message and a 500 status code.

## Performance Optimization:

Performance monitoring is implemented to measure the time taken for processing the request in the launch_attack view.

The start time is recorded before processing the request, and the end time is recorded after the request processing is complete.

The total time taken for processing the request is calculated and logged.

## Caching:

Caching is used to store responses from GET requests made during a DDoS attack.

Responses are stored in the cache with a timeout of 60 seconds.

Before making a new request, the view checks the cache for a stored response. If found, it returns the cached response instead of making a new request.


# Guide for Future Developers(Logging, Error Handling, Caching, and Performance):


## Logging:

Familiarize yourself with the logging module and the configuration specified in the LOGGING dictionary.

Ensure that logging statements are clear and informative, providing insights into the application's behavior.

## Error Handling:

Understand how error handling middleware captures and processes exceptions.

Ensure that error messages are logged appropriately, and meaningful responses are returned to clients.

## Caching:

Understand the caching mechanism used in the application and its impact on performance.

Monitor cache usage and ensure that caching settings are optimized for the application's requirements.

## Performance Optimization:

Review performance monitoring implementations to understand how performance metrics are measured.

Identify critical areas for optimization and consider implementing performance enhancements where necessary.

# Experience the world of DDoS attacks responsibly with DDOS ATTACKER!

CASE DIAGRAM(UML)





<img width="261" alt="image" src="https://github.com/KristinaRiabova/ddos_attack_app-chat/assets/103763577/f3db273d-f5e6-4bc1-acc5-065509f490ea">
