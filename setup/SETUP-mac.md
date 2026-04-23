# macOS Setup

Setup your environment for the Agentic AI Bootcamp.

## Prerequisites

- Python 3.12+
- Git
- A code editor (VS Code recommended)

## Installation

1. Install uv (Python package manager):
   ```bash
   brew install astral-sh/uv/uv
   ```

2. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Agentic-AI-Bootcamp
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

4. Set up your API keys in `.env`:
   ```
   GEMINI_API_KEY=your_key_here
   GOOGLE_API_KEY=your_key_here
   ```

## Verify Installation

Run:
```bash
python -c "import google.genai; print('Google GenAI installed')"
```