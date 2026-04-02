import requests

def ask_ollama(message: str) -> str:
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama3",
        "messages": [
            {"role": "user", "content": message}
        ],
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["message"]["content"]

if __name__ == "__main__":
    reply = ask_ollama("Reply with exactly: OK")
    print("Model replied:\n")
    print(reply)
