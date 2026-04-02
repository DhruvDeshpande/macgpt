from llm import generate_command

tests = [
    "show me all pdfs on my desktop",
    "find all mp4 files in downloads larger than 500MB",
    "open the most recent pdf in downloads",
]

for t in tests:
    cmd = generate_command(t)
    print("\nRequest:", t)
    print("Command:", cmd)
