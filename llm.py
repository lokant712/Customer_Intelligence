import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize(context, question):
    # Convert list of dicts to a formatted string
    data = json.dumps(context, indent=2)

    prompt = f"""
Use ONLY the text inside <DATA>.
You may summarize and group similar statements.
Do NOT add new facts.
If the answer is not present, say:
"I don't know."

<DATA>
{data}
</DATA>

Question:
{question}
"""


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()
