# AI-Email Assistant
AI-Email assistant, is a web application built with Django that helps users in writting professional emails in a short time

## Table of Contents
  1. [Features](#features)
  2. [Tech Stack](#tech-stack)
  3. [Project Structure](#project-structure)
  4. [Demo](#demo)
  5. [Installation](#installation)
  6. [Usage](#usage)
  7. [Contributing](#contributing)
  8. [License](#license)

## Features
- **User Authentication**: Secure login using Auth0, with Google and email-based authentication.
- **AI-Powered Rephrasing**:Transform plain text into professionally worded emails using a custom Hugging Face model.
- **Responsive Design**: Optimized for all devices with Tailwind CSS.
- **Personalized User Experience**: User-specific session management and history tracking.
- **Database Integration**: Scalable and secure data storage with PostgreSQL.
- **Dynamic Animations**: Engaging UI elements such as the wave effect for login screens.
- **History Tracking**: View past rephrased emails with timestamps.




## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Database**: PostgreSQL
- **API Integration**: Hugging Face (for AI-based text rephrasing)
- **Authentication**: Auth0 (Google Login and Email/Password support)



## Project Structure
```plaintext
ai_email_assistant/
│
├── email_app/                
│   ├── __init__.py
│   ├── forms.py              
│   ├── migrations/           
│   │   ├── __init__.py
│   │   └── 0001_initial.py  
│   ├── models.py             
│   ├── settings.py           
│   ├── templates/            
│   │   ├── history.html
│   │   └── index.html
│   ├── urls.py               
│   ├── utils/                
│   │   └── huggingface.py    
│   ├── views.py              
│   └── wsgi.py               
│
├── __pycache__/             
├── .gitignore                
├── manage.py                 
├── README.md                 
├── requirements.txt          
```
## Demo



### Login Page  
**Description**: Secure login with Google or email authentication.  
**Screenshot**:  
<img src="https://github.com/user-attachments/assets/28ab5c14-41bf-4a9d-9b27-58ec31696720" alt="Screenshot 1" width="35%">

---
### Home Page  
**Description**: A clean and intuitive interface for users to start their email creation journey, featuring a dynamic wave effect.  
**Screenshot**:  

<img src="https://github.com/user-attachments/assets/629485fd-e2a4-4b71-b166-537ff5a578ba" alt="Screen" width="45%">

---

### AI Rephrasing Interface  
**Description**: Enter plain text, and the assistant transforms it into a professional email.  
**Screenshot**:  
<img src="https://github.com/user-attachments/assets/6d17f0fd-f769-4899-a9bc-d97f62eec706" alt="Screenshot 2" width="50%">


---

### History Page  
**Description**: A detailed log of past rephrased texts with timestamps for easy reference.  
**Screenshot**:  


<div style="display: flex; align-items: center; justify-content: space-around;">
  <img src="https://github.com/user-attachments/assets/4f81056d-ba1e-4c75-957b-3e449e5a590c" alt="Screenshot 3" width="45%">
  <img src="https://github.com/user-attachments/assets/42308350-b45a-4567-b593-b594569002fb" alt="Screenshot 2024-11-24 014054" width="40%">
</div>



## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- A registered Auth0 account

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/seal-000/ai_email_assistant.git
   cd ai-mail-assistant
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables: Create a ```.env``` file with the following:
   ```bash
   
   AUTH0_CLIENT_ID=your-auth0-client-id
   AUTH0_CLIENT_SECRET=your-auth0-client-secret
   AUTH0_DOMAIN=your-auth0-domain

   DB_NAME=your-database-name
   DB_PASSWORD=your-database-password
   DB_HOST=your-database-host
   DB_PORT=your-database-port

   HUGGING_FACE_API_KEY=your-hugging-face-key
   
   ```

5. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
6. Start the development server:
   ```bash
   python manage.py runserver 3000
   ```
   

## Usage


### Login and Session

1. Navigate to the home page (```/```).
2. Login using Google or email credentials via Auth0.

### Rephrase Emails

1. After login in, use the form to input text.
2. Submit the form to get a professionally rephrased text.


### View History 

1. Access ```/history``` to review previously rephrased text along with original text and timestamps.


## Contributing

Contributions are welcome!
1. Fork the repository.
2. Create a new feature branch:
```bash
git checkout -b feature-name
```
3. Commit your changes and push to your fork.
4. Submit a pull request with a detailed explanation of your changes.


## License
This project is licensed under the MIT License. See the ```LICENSE``` file for details.

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)



