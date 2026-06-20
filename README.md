# Personal Codex — AI Assistant Chatbot

A conversational AI assistant you can run from the terminal. It remembers context within a session, answers questions clearly, and can help with coding, writing, brainstorming, and everyday tasks.

## Features

- Interactive chat in the terminal
- Conversation memory across the session
- Works with OpenAI, Google Gemini, Anthropic, local models, or any OpenAI-compatible API
- No account required — use [Ollama](https://ollama.com) for fully local, free operation
- Built-in commands: `/help`, `/reset`, `/quit`

## Prerequisites

- Python 3.10+
- **Either** an API key from [OpenAI](https://platform.openai.com/), Google Gemini, etc.
- **Or** [Ollama](https://ollama.com) installed for local models

## Setup

1. Clone the repository and enter the project folder:

   ```bash
   cd personal_codex
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Configure your provider in `.env`:

   ```bash
   cp .env.example .env
   ```

### Option A: Local (free, no internet required)

Install [Ollama](https://ollama.com) and pull a small model:

```bash
ollama pull qwen2.5:1.5b
```

Then edit `.env` to:

```
OPENAI_API_KEY=ollama
OPENAI_BASE_URL=http://localhost:11434/v1
OPENAI_MODEL=qwen2.5:1.5b
```

### Option B: Cloud provider (OpenAI, Gemini, etc.)

Set your API key and the provider's base URL in `.env`. Example for Gemini:

```
OPENAI_API_KEY=your-gemini-key
OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
OPENAI_MODEL=gemini-2.0-flash
```

## Usage

Start the chatbot:

```bash
python main.py
```

Example session:

```
You: What is a binary search tree?
Assistant: A binary search tree is a tree data structure where each node has at most two children...

You: /reset
Conversation history cleared.

You: /quit
Goodbye!
```

## Configuration

| Variable           | Default        | Description                          |
|--------------------|----------------|--------------------------------------|
| `OPENAI_API_KEY`   | —              | Your API key (required)              |
| `OPENAI_BASE_URL`  | OpenAI default | Custom API base URL (optional)       |
| `OPENAI_MODEL`     | `gpt-4o-mini`  | Model to use for responses           |

## Project Structure

```
personal_codex/
├── chatbot/
│   ├── __init__.py
│   ├── assistant.py   # Core AI assistant logic
│   └── cli.py         # Interactive terminal interface
├── main.py            # Entry point
├── requirements.txt
├── .env.example
└── README.md
```

## Programmatic Usage

You can also use the assistant in your own scripts:

```python
from dotenv import load_dotenv
from chatbot import AIAssistant

load_dotenv()
assistant = AIAssistant()
reply = assistant.chat("Explain recursion in one sentence.")
print(reply)
```
