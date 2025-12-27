import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize(context, question):
    data = "\n".join(context)

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
