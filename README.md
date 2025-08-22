# learning-app

# learning-app

## Project Setup

This project consists of a React frontend and a Python backend. Follow these steps to set up and run the application.

### Prerequisites

1. **Install Node.js**
   ```bash
   brew install node
   ```

2. **Install ngrok** (optional, for exposing local server)
   ```bash
   brew install ngrok
   ```

### Frontend Setup

1. **Create React project with Vite**
   ```bash
   npm create vite@latest frontend -- --template react
   ```

2. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

3. **Install required dependencies**
   ```bash
   npm install react-router-dom@6 @clerk/clerk-react
   ```

4. **Run the frontend development server**
   ```bash
   npm run dev
   ```

### Backend Setup

1. **Create Python interpreter based on uv project**
    - Set up your IDE to use a Python interpreter based on the uv project

2. **Run the backend server**
   ```bash
   uv run .\server.py
   ```

### Useful Commands

- **Frontend**: `npm run dev` - Start development server
- **Backend**: `uv run .\server.py` - Start Python server
- **ngrok**: `ngrok http <port>` - Expose local server (optional)