from search import semantic_search
from llm import summarize

question = "Why are customers unhappy with delivery?"

context = semantic_search(question)

print("Retrieved context:")
for c in context:
    print("-", c)

answer = summarize(context, question)

print("\nLLM Answer:")
print(answer)
