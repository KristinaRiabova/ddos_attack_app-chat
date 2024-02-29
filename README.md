############################################################
#                                                          #
#                      DDOS ATTACKER                       #
#                                                          #
############################################################

Welcome to DDOS ATTACKER!



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

#1. Logging

The project utilizes the Python logging module for logging events and errors. It's configured to output log messages with a level of DEBUG. Log messages are generated throughout the code to track events such as page accesses, user logins, and errors.

#2. User Authentication and Registration

Login View (login_view): Handles user login by authenticating against MongoDB and Django's authentication system.
Registration View (registration_view): Allows users to register by creating a new user profile in MongoDB and Django.

#3. Profile Management
Profile Creation View (profile_created_view): Displays the user's profile information after successful login.
Profile Update View (update_profile): Allows users to update their profile information, including the bio and profile picture.
Profile Deletion View (delete_profile): Enables users to delete their profiles from the system.

#4. DDoS Attack Simulation
DDoS View (ddos): Renders a page for launching DDoS attacks. It utilizes threading to send multiple HTTP requests to the specified target URL simultaneously.

#5. Error Handling
The code includes error handling mechanisms to gracefully manage unexpected situations and prevent application crashes. Error messages and status codes are returned to the client to communicate the nature of encountered errors.

#6. Caching
Cache Usage: The project employs Django's caching mechanism (django.core.cache) to cache responses from external HTTP requests. Cached responses are stored for a specified duration to optimize performance and reduce the load on external services.



CASE DIAGRAM(UML)
<img width="261" alt="image" src="https://github.com/KristinaRiabova/ddos_attack_app-chat/assets/103763577/f3db273d-f5e6-4bc1-acc5-065509f490ea">

