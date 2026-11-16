# 🧠 AI Tutor App

[![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)](https://flutter.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=black)](https://supabase.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://choosealicense.com/licenses/mit/)

> A cross-platform AI tutor prototype built with Flutter, FastAPI and Supabase. It supports academic questions submitted through text, images and audio.

---
<img width="400" height="849" alt="image" src="https://github.com/user-attachments/assets/9d51ece3-c0e5-448a-a0ba-0a1d18a20e16" /> <img width="413" height="854" alt="image" src="https://github.com/user-attachments/assets/affc2391-828d-4e15-b908-5d1b1d5f87e8" /> <img width="402" height="845" alt="image" src="https://github.com/user-attachments/assets/843347a0-dc6c-40d4-ad77-fb20efcab58a" /> <img width="402" height="844" alt="image" src="https://github.com/user-attachments/assets/1c5daf28-8828-44e3-8cac-2902a0450ad3" /> <img width="406" height="858" alt="image" src="https://github.com/user-attachments/assets/1d265e17-aa8b-49af-b714-0fe8d774af84" /> <img width="404" height="849" alt="image" src="https://github.com/user-attachments/assets/23c6cc51-7e8c-4f7a-bfa3-93981d9619af" />





## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#-backend-setup)
  - [Frontend Setup](#-frontend-setup)
- [API Documentation](#-api-documentation)
- [Environment Configuration](#-environment-configuration)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

---

## 🎯 Overview

AI Tutor App is a comprehensive educational platform designed to revolutionize the learning experience for students. By combining cutting-edge AI technology with intuitive multi-modal input options, the application provides instant, contextually relevant answers to academic questions across various subjects and educational levels.

### Key Highlights

- **Multi-Modal Learning**: Support for text, image (OCR), and audio input
- **Personalized Experience**: Customizable subject preferences and educational levels
- **Secure & Scalable**: JWT-based authentication with cloud database infrastructure
- **Cross-Platform**: Native performance on both Android and iOS devices

---

## ✨ Features

### Core Functionality

- 🔐 **Secure Authentication**: JWT-based user registration and login system
- 🤖 **AI-Powered Q&A**: Intelligent academic assistance powered by advanced language models
- 🖼️ **Image Recognition**: OCR technology to extract and answer questions from images
- 🎙️ **Voice Input**: Convert spoken questions to text for hands-free learning
- 📚 **Customizable Learning**: Tailor responses based on subject area and educational level
- 📈 **Progress Tracking**: Comprehensive history of questions and learning journey
- 📱 **Responsive Design**: Optimized UI/UX for mobile and tablet devices
- ⚡ **Real-Time Processing**: Fast response times with efficient backend architecture

---

## 🛠 Tech Stack

### Frontend

| Technology | Purpose |
|------------|---------|
| **Flutter** | Cross-platform mobile framework |
| **Provider** | State management solution |
| **HTTP Package** | API communication |

### Backend

| Technology | Purpose |
|------------|---------|
| **FastAPI** | High-performance REST API framework |
| **SQLAlchemy** | ORM for database operations |
| **Pydantic** | Data validation and serialization |
| **JWT** | Secure token-based authentication |

### Infrastructure

| Service | Purpose |
|---------|---------|
| **Supabase PostgreSQL** | Cloud-hosted database |
| **OpenAI API** | AI-powered question answering |
| **OCR Service** | Image text extraction |

---

## 📁 Architecture

```
ai-tutor-app/
│
├── backend/                    # FastAPI Backend Service
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # Application entry point
│   │   ├── config.py          # Configuration management
│   │   │
│   │   ├── database/          # Database Layer
│   │   │   ├── __init__.py
│   │   │   ├── connection.py  # DB connection setup
│   │   │   └── crud.py        # CRUD operations
│   │   │
│   │   ├── models/            # Data Models
│   │   │   ├── __init__.py
│   │   │   ├── user.py        # User model
│   │   │   └── question.py    # Question model
│   │   │
│   │   ├── routers/           # API Endpoints
│   │   │   ├── __init__.py
│   │   │   ├── auth.py        # Authentication routes
│   │   │   ├── questions.py   # Question handling routes
│   │   │   └── users.py       # User management routes
│   │   │
│   │   ├── services/          # Business Logic
│   │   │   ├── __init__.py
│   │   │   ├── ai_service.py  # AI integration
│   │   │   ├── ocr_service.py # Image processing
│   │   │   └── auth_service.py# Authentication logic
│   │   │
│   │   └── utils/             # Utilities
│   │       ├── __init__.py
│   │       ├── security.py    # Password hashing, JWT
│   │       └── validators.py  # Input validation
│   │
│   ├── .env                   # Environment variables (not in git)
│   ├── .env.example           # Environment template
│   ├── requirements.txt       # Python dependencies
│   └── README.md              # Backend documentation
│
├── frontend/                  # Flutter Mobile Application
│   ├── lib/
│   │   ├── main.dart          # App entry point
│   │   │
│   │   ├── models/            # Data Models
│   │   │   ├── user.dart
│   │   │   └── question.dart
│   │   │
│   │   ├── providers/         # State Management
│   │   │   ├── auth_provider.dart
│   │   │   └── question_provider.dart
│   │   │
│   │   ├── screens/           # UI Screens
│   │   │   ├── auth/
│   │   │   │   ├── login_screen.dart
│   │   │   │   └── register_screen.dart
│   │   │   ├── home/
│   │   │   │   └── home_screen.dart
│   │   │   └── question/
│   │   │       └── ask_question_screen.dart
│   │   │
│   │   ├── services/          # API Services
│   │   │   ├── api_service.dart
│   │   │   └── auth_service.dart
│   │   │
│   │   ├── utils/             # Utilities
│   │   │   ├── constants.dart
│   │   │   └── validators.dart
│   │   │
│   │   └── widgets/           # Reusable Components
│   │       ├── custom_button.dart
│   │       └── input_field.dart
│   │
│   ├── assets/                # Static Assets
│   │   ├── images/
│   │   └── fonts/
│   │
│   ├── pubspec.yaml           # Flutter dependencies
│   ├── analysis_options.yaml  # Linting rules
│   └── README.md              # Frontend documentation
│
├── docs/                      # Additional Documentation
│   ├── API.md                 # API documentation
│   ├── ARCHITECTURE.md        # System architecture
│   └── DEPLOYMENT.md          # Deployment guide
│
├── .gitignore
├── LICENSE
└── README.md                  # This file
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- **Python** 3.8 or higher
- **Flutter** 3.0 or higher
- **PostgreSQL** (via Supabase account)
- **OpenAI API Key**
- **Git**

### 🖥️ Backend Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-tutor-app.git
cd ai-tutor-app/backend
```

#### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Configure Environment Variables

Create a `.env` file in the `/backend` directory:

```ini
# Database Configuration
DATABASE_URL=postgresql://postgres.USER:PASSWORD@aws-0-REGION.pooler.supabase.com:PORT/postgres

# Security
SECRET_KEY=your_super_secret_random_string_here_min_32_chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# AI Service
OPENAI_API_KEY=sk-proj-YOUR_OPENAI_API_KEY

# Application
DEBUG=True
```

> **Security Note**: Never commit the `.env` file to version control. Use `.env.example` as a template.

#### 5. Initialize Database

```bash
# Run database migrations
python -m app.database.init_db
```

#### 6. Start the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **Base URL**: `http://localhost:8000`
- **Interactive Docs**: `http://localhost:8000/docs`
- **Alternative Docs**: `http://localhost:8000/redoc`

---

### 📱 Frontend Setup

#### 1. Navigate to Frontend Directory

```bash
cd ../frontend
```

#### 2. Install Flutter Dependencies

```bash
flutter pub get
```

#### 3. Configure API Endpoint

Update `lib/utils/constants.dart` with your backend URL:

```dart
class ApiConstants {
  static const String baseUrl = 'http://localhost:8000'; // For emulator
  // static const String baseUrl = 'http://10.0.2.2:8000'; // For Android emulator
  // static const String baseUrl = 'http://YOUR_IP:8000'; // For physical device
}
```

#### 4. Run the Application

**For Android/iOS Emulator:**
```bash
flutter run
```

**For Specific Device:**
```bash
flutter devices  # List available devices
flutter run -d <device-id>
```

**For Web:**
```bash
flutter run -d chrome
```

---

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Register new user |
| POST | `/api/auth/login` | User login |
| POST | `/api/auth/refresh` | Refresh access token |

### Question Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/questions/ask` | Submit text question |
| POST | `/api/questions/ask-image` | Submit image question |
| POST | `/api/questions/ask-audio` | Submit audio question |
| GET | `/api/questions/history` | Get user question history |
| GET | `/api/questions/{id}` | Get specific question |

### User Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users/me` | Get current user profile |
| PUT | `/api/users/me` | Update user profile |
| GET | `/api/users/me/stats` | Get learning statistics |

For detailed request/response schemas, visit the interactive documentation at `/docs` when the server is running.

---

## 🔧 Environment Configuration

### Backend Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Yes | - |
| `SECRET_KEY` | JWT secret key (min 32 chars) | Yes | - |
| `ALGORITHM` | JWT algorithm | No | HS256 |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time | No | 30 |
| `OPENAI_API_KEY` | OpenAI API key | Yes | - |
| `DEBUG` | Enable debug mode | No | False |

### Frontend Configuration

Update `lib/utils/constants.dart` for environment-specific settings:

```dart
class AppConfig {
  static const String apiBaseUrl = String.fromEnvironment(
    'API_URL',
    defaultValue: 'http://localhost:8000',
  );
  
  static const int requestTimeout = 30000; // milliseconds
  static const String appVersion = '1.0.0';
}
```

---

## 🤝 Contributing

We welcome contributions from the community! Please follow these guidelines:

### Development Workflow

1. **Fork the Repository**
   ```bash
   # Click the 'Fork' button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/your-username/ai-tutor-app.git
   cd ai-tutor-app
   ```

3. **Create Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

4. **Make Your Changes**
   - Write clean, documented code
   - Follow existing code style
   - Add tests for new features

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add: AmazingFeature with comprehensive tests"
   ```

6. **Push to Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

7. **Open Pull Request**
   - Provide clear description of changes
   - Reference any related issues
   - Wait for code review

### Coding Standards

- **Python**: Follow PEP 8 guidelines
- **Dart/Flutter**: Follow official Dart style guide
- **Commits**: Use conventional commit messages
- **Documentation**: Update relevant docs with changes

### Reporting Issues

When reporting issues, please include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, versions)
- Screenshots if applicable

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 AI Tutor App Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 💬 Support

### Documentation

- [API Documentation](docs/API.md)
- [Architecture Overview](docs/ARCHITECTURE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

### Community

- **Issues**: [GitHub Issues](https://github.com/AION-2000/ai-tutor-app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/AION-2000/ai-tutor-app/discussions)
- **Email**: aionshihabshahriar@gmail.com

### Resources

- [Flutter Documentation](https://docs.flutter.dev/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Supabase Documentation](https://supabase.com/docs)

---

## 🙏 Acknowledgments

- OpenAI for providing the AI capabilities
- Supabase for database infrastructure
- Flutter and FastAPI communities for excellent frameworks
- All contributors who help improve this project

---

<p align="center">Made with ❤️ by Shihab Shahriar Aion</p>
<p align="center">
  <a href="#-ai-tutor-app">Back to Top ↑</a>
</p>
