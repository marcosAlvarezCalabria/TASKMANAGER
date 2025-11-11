from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def create_simple_task(task):
    if not client:
        return ["error: Anthropic client is not initialized."]

    try:
        prompt = f"""Break down the following task into 3 simple steps:

Task: {task}

Response format (use dashes):
- step one
- step two
- step three

Respond with only the list of steps using dashes (-)."""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=300,
            temperature=0.7,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = message.content[0].text.strip()

        subtasks = []

        for line in content.split('\n'):
            line = line.strip()
            if line and line.startswith('-'):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)

        return subtasks if subtasks else ["No subtasks generated"]

    except Exception as e:
        return [f"error: {str(e)}"]
