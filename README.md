# Anki IA

This project uses Python and requires a virtual environment to run correctly.

### 🐍 Set up the virtual environment:

```bash
python3 -m venv ankia
source ankia/bin/activate
pip install -r requirements.txt
```

### 🧠 Ollama (LLM Backend)

You need to run [Ollama](https://ollama.com) in a separate terminal:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run gemma3:4b
```

### ▶️ Running the Project

Once Ollama is running, execute the script:

```bash
python3 main.py
```

### 💬 Prompt sent to Ollama:

> "50 most used irregular verbs with a sentence example in past tense and past participle, one line per verb."

