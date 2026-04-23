# Student Setup Guide

Welcome to the Agentic AI Bootcamp! This guide walks you through setting up your development environment and managing your exercises.

## Prerequisites

- Git installed
- Python 3.12+
- A code editor (VS Code recommended)
- GitHub account

---

## Step 1: Fork the Repository

1. Go to [https://github.com/divine-create/Agentic-AI-Bootcamp](https://github.com/divine-create/Agentic-AI-Bootcamp)
2. Click the **Fork** button (top right)
3. Select your GitHub account as the destination
4. Wait for the fork to complete

---

## Step 2: Clone Your Fork

```bash
# Clone your forked repository
git clone https://github.com/YOUR_USERNAME/Agentic-AI-Bootcamp.git
cd Agentic-AI-Bootcamp
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## Step 3: Create Exercises Branch

```bash
# Create and switch to a new branch for your exercises
git checkout -b exercises
```

This keeps your exercises separate from the course content.

---

## Step 4: Set Up Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys
# See setup/SETUP-linux.md (or mac/PC) for details
```

Your `.env` file should look like:
```
GEMINI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
```

---

## Step 5: Create Your Exercise Folder

```bash
# Replace YOUR_NAME with your name (no spaces)
mkdir exercises/your_name
cd exercises/your_name
```

This is where you'll save your exercise work.

---

## Step 6: Install Dependencies

```bash
# From the project root
cd ..
uv sync
```

Or if using pip:
```bash
pip install -r requirements.txt
```

---

## Working on Exercises

### During Class

1. Navigate to your exercise folder:
   ```bash
   cd exercises/your_name
   ```

2. Open the notebook or create your exercise file:
   ```bash
   # Open Jupyter notebook
   jupyter notebook
   ```

3. Work on the exercises

4. Save your work:
   ```bash
   git add .
   git commit -m "Completed Week X exercises"
   ```

### After Class (Pulling Updates)

When the instructor pushes new content:

```bash
# 1. Add upstream remote (first time only)
git remote add upstream https://github.com/divine-create/Agentic-AI-Bootcamp.git

# 2. Fetch latest changes
git fetch upstream

# 3. Merge updates into your exercises branch
git merge upstream/main

# 4. Resolve any conflicts if needed
# Then: git add . && git commit -m "Resolved conflicts"
```

---

## Submitting Your Work (Optional Pull Request)

If you'd like to share your work or get feedback:

### Option 1: Push to Your Fork

```bash
# Push your exercises branch to your fork
git push origin exercises
```

### Option 2: Create a Pull Request to the Main Repo

1. Go to your fork on GitHub
2. Click **Compare & pull request**
3. Set:
   - **Base repository**: `divine-create/Agentic-AI-Bootcamp`
   - **Base branch**: `main`
   - **Head repository**: `your_username/Agentic-AI-Bootcamp`
   - **Compare branch**: `exercises`
4. Add a description explaining what you completed
5. Click **Create pull request**

**Note**: Pull requests are optional. You're encouraged to submit your work for feedback or if you'd like to share notable exercises with the class.

---

## FAQ

### Q: I get merge conflicts when pulling updates
A: Don't worry! Resolve by keeping your files in `exercises/your_name/` folder. The course files in main folders are safe to merge.

### Q: How do I check my current branch?
A: `git branch`

### Q: I accidentally worked in the main branch
A: No problem! Move your work:
```bash
git checkout exercises
git checkout main -- path/to/your/files
git add .
git commit -m "Move work to exercises branch"
```

### Q: How do I back up my work?
A: Regularly push to your fork:
```bash
git push origin exercises
```

---

## Quick Reference

```bash
# Daily workflow
cd Agentic-AI-Bootcamp
git checkout exercises
git pull upstream main  # Get latest course content

# Work on exercises in your folder
cd exercises/your_name

# Save work
git add .
git commit -m "My Week X work"
git push origin exercises
```

---

Happy Learning!