import random

def generate_random_text():
    words = ["Python", "GitHub", "Project", "Random", "Text", "Generator", "OpenAI", "Coding", "Learning", "Fun"]
    sentence = " ".join(random.choices(words, k=5))
    return sentence

if __name__ == "__main__":
    print("Random Text Generator")
    print("-" * 30)
    print(f"Generated Text: {generate_random_text()}")
