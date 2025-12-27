from search import semantic_search
from llm import summarize

def is_vague(q):
    return len(q.split()) < 4

while True:
    q = input("\nQuery: ")

    if is_vague(q):
        print("Answer: I don't know.")
        continue

    context = semantic_search(q)
    answer = summarize(context, q)
    print("Answer:", answer)
