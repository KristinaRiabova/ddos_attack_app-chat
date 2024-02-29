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





CASE DIAGRAM(UML)
<img width="261" alt="image" src="https://github.com/KristinaRiabova/ddos_attack_app-chat/assets/103763577/f3db273d-f5e6-4bc1-acc5-065509f490ea">

