# Windows Setup

Setup your environment for the Agentic AI Bootcamp.

## Prerequisites

- Python 3.12+
- Git
- A code editor (VS Code recommended)

## Installation

1. Install uv (Python package manager):
   ```powershell
   powershell -ExecutionPolicy ByCommand -Command "irm | iex"
   ```

2. Clone the repository:
   ```powershell
   git clone <your-repo-url>
   cd Agentic-AI-Bootcamp
   ```

3. Install dependencies:
   ```powershell
   uv sync
   ```

4. Set up your API keys in `.env`:
   ```
   OPENAI_API_KEY=your_key_here
   ```

## Verify Installation

Run:
```powershell
python -c "import openai; print('OpenAI installed')"
```