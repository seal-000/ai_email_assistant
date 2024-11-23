# AI-Email Assistant
AI-Email assistant, is a web application built with Django that helps users in writting professional emails in a short time

## Table of Contents
  1. [Features](#features)
  2. [Tech Stack](#tech-stack)
  3. [Project Structure](#project-structure)
  4. [Demo](#demo)

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

### Home Page  
**Description**: A clean and intuitive interface for users to start their email creation journey.  
**Screenshot**:  
![Home Page](link_to_home_page_image)
![wave-login](https://github.com/user-attachments/assets/23fa8acc-9552-4cd5-830b-43d1b55eed97)

---

### Login Page  
**Description**: Secure login with Google or email authentication, featuring a dynamic wave effect.  
**Screenshot**:  
![image](https://github.com/user-attachments/assets/6de590e3-1237-4669-bf39-aa84265817a2)

---

### AI Rephrasing Interface  
**Description**: Enter plain text, and the assistant transforms it into a professional email.  
**Screenshot**:  
![Rephrasing Interface](link_to_rephrasing_interface_image)

---

### History Page  
**Description**: A detailed log of past rephrased emails with timestamps for easy reference.  
**Screenshot**:  
![History Page](link_to_history_page_image)

