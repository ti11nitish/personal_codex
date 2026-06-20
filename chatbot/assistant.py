"""Core AI assistant with conversation memory."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any

from openai import OpenAI

DEFAULT_SYSTEM_PROMPT = """You are a helpful, friendly AI assistant. You provide clear, accurate,
and concise answers. When you are unsure about something, you say so honestly. You adapt your tone
to the user — professional when needed, casual when appropriate. You can help with coding,
writing, brainstorming, explanations, and everyday questions."""


@dataclass
class Message:
    role: str
    content: str


@dataclass
class AIAssistant:
    """Conversational AI assistant backed by an OpenAI-compatible API."""

    api_key: str | None = None
    base_url: str | None = None
    model: str = "gpt-4o-mini"
    system_prompt: str = DEFAULT_SYSTEM_PROMPT
    max_history: int = 50
    temperature: float = 0.7
    history: list[Message] = field(default_factory=list)
    _client: OpenAI | None = field(default=None, repr=False)

    def __post_init__(self) -> None:
        self.api_key = self.api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key required. Set OPENAI_API_KEY in your environment or pass api_key."
            )
        self.base_url = self.base_url or os.getenv("OPENAI_BASE_URL")
        self.model = os.getenv("OPENAI_MODEL", self.model)

    @property
    def client(self) -> OpenAI:
        if self._client is None:
            kwargs: dict[str, Any] = {"api_key": self.api_key}
            if self.base_url:
                kwargs["base_url"] = self.base_url
            self._client = OpenAI(**kwargs)
        return self._client

    def reset(self) -> None:
        """Clear conversation history."""
        self.history.clear()

    def _trim_history(self) -> None:
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history :]

    def _build_messages(self) -> list[dict[str, str]]:
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend({"role": m.role, "content": m.content} for m in self.history)
        return messages

    def chat(self, user_message: str) -> str:
        """Send a message and return the assistant's reply."""
        user_message = user_message.strip()
        if not user_message:
            return "Please enter a message."

        self.history.append(Message(role="user", content=user_message))

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self._build_messages(),
            temperature=self.temperature,
        )

        reply = response.choices[0].message.content or ""
        self.history.append(Message(role="assistant", content=reply))
        self._trim_history()
        return reply
