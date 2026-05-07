"""
Career Bot — deployed to HuggingFace Spaces.

Update self.name and place your files in the me/ folder before deploying.
See the deployment steps in 4_lab4.ipynb.
"""

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pypdf import PdfReader
import gradio as gr
import requests
import json
import os

load_dotenv(override=True)


def push(text: str):
    token = os.getenv("PUSHOVER_TOKEN")
    user = os.getenv("PUSHOVER_USER")
    if not token or not user:
        print(f"[Push skipped] {text}")
        return
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={"token": token, "user": user, "message": text},
    )


def record_user_details(email: str, name: str = "Not provided", notes: str = "Not provided") -> dict:
    """Record that a visitor provided their email and is interested in contact.

    Args:
        email: The visitor's email address
        name: The visitor's name, if they provided it
        notes: Any context about their interests worth recording
    """
    push(f"New contact: {name} — {email} — {notes}")
    return {"recorded": "ok"}


def record_unknown_question(question: str) -> dict:
    """Record a question that couldn't be answered so the owner can review it.

    Use this whenever you don't know the answer, even for trivial questions.

    Args:
        question: The question that couldn't be answered
    """
    push(f"Unanswered: {question}")
    return {"recorded": "ok"}


class CareerBot:

    def __init__(self):
        self.client = genai.Client()
        # *** CHANGE THIS ***
        self.name = "Your Name"

        self.linkedin = ""
        if os.path.exists("me/linkedin.pdf"):
            reader = PdfReader("me/linkedin.pdf")
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    self.linkedin += text

        with open("me/summary.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()

        self.config = types.GenerateContentConfig(
            system_instruction=self._build_system_prompt(),
            tools=[record_user_details, record_unknown_question],
        )

    def _build_system_prompt(self) -> str:
        prompt = (
            f"You are acting as {self.name} on their personal website. "
            f"Answer questions about {self.name}'s career, background, skills and experience. "
            f"Be professional and engaging — as if talking to a potential employer or client. "
            f"If you don't know the answer to any question, ALWAYS use record_unknown_question to log it. "
            f"When a visitor shows interest, ask for their email and record it using record_user_details.\n\n"
            f"## Summary:\n{self.summary}\n\n"
        )
        if self.linkedin:
            prompt += f"## LinkedIn Profile:\n{self.linkedin}\n\n"
        prompt += f"Always stay in character as {self.name}."
        return prompt

    def _history_to_contents(self, history: list[dict]) -> list:
        contents = []
        for msg in history:
            role = "model" if msg["role"] == "assistant" else "user"
            contents.append(
                types.Content(role=role, parts=[types.Part(text=msg["content"])])
            )
        return contents

    def _handle_tool_calls(self, response) -> list:
        result_parts = []
        for fc in response.function_calls:
            print(f"Tool called: {fc.name}", flush=True)
            tool_fn = globals().get(fc.name)
            result = tool_fn(**dict(fc.args)) if tool_fn else {"error": "unknown tool"}
            result_parts.append(
                types.Part.from_function_response(
                    name=fc.name,
                    response={"result": str(result)},
                )
            )
        return result_parts

    def chat(self, message: str, history: list[dict]) -> str:
        contents = self._history_to_contents(history)
        contents.append(types.Content(role="user", parts=[types.Part(text=message)]))

        while True:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=contents,
                config=self.config,
            )

            if not response.function_calls:
                break

            contents.append(response.candidates[0].content)
            tool_parts = self._handle_tool_calls(response)
            contents.append(types.Content(role="user", parts=tool_parts))

        return response.text


if __name__ == "__main__":
    bot = CareerBot()
    gr.ChatInterface(bot.chat, type="messages").launch()
