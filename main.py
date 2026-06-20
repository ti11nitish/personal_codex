#!/usr/bin/env python3
"""Entry point for the AI assistant chatbot."""

from dotenv import load_dotenv

from chatbot.cli import run_cli


def main() -> None:
    load_dotenv()
    run_cli()


if __name__ == "__main__":
    main()
