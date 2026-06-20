"""Interactive CLI for the AI assistant."""

from __future__ import annotations

import sys

from chatbot.assistant import AIAssistant

BANNER = """
╔══════════════════════════════════════╗
║         AI Assistant Chatbot         ║
╚══════════════════════════════════════╝

Type your message and press Enter.
Commands: /help  /reset  /quit  (or /exit)
"""


def print_help() -> None:
    print(
        """
Commands:
  /help   Show this help message
  /reset  Clear conversation history
  /quit   Exit the chatbot (also /exit)

Just type normally to chat with the assistant.
"""
    )


def run_cli() -> None:
    try:
        assistant = AIAssistant()
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        print(
            "\nCreate a .env file from .env.example and set your OPENAI_API_KEY.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(BANNER)

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        command = user_input.lower()
        if command in ("/quit", "/exit"):
            print("Goodbye!")
            break
        if command == "/help":
            print_help()
            continue
        if command == "/reset":
            assistant.reset()
            print("Conversation history cleared.\n")
            continue

        print("Assistant: ", end="", flush=True)
        try:
            reply = assistant.chat(user_input)
            print(reply)
        except Exception as exc:
            print(f"Sorry, something went wrong: {exc}", file=sys.stderr)
        print()
