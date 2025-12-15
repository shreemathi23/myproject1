import string
from collections import Counter

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def analyze_text(text):
    cleaned = clean_text(text)

    words = cleaned.split()
    sentences = text.count('.') + text.count('!') + text.count('?')

    word_count = len(words)
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))

    common_words = Counter(words).most_common(5)

    print("\n--- TEXT ANALYSIS REPORT ---")
    print(f"Characters (with spaces): {char_count}")
    print(f"Characters (without spaces): {char_count_no_spaces}")
    print(f"Words: {word_count}")
    print(f"Sentences: {sentences}")
    print("\nTop 5 most common words:")
    for word, count in common_words:
        print(f"{word} → {count}")

def main():
    print("==== TEXT ANALYZER ====")
    print("1. Analyze typed text")
    print("2. Analyze text from file")

    choice = input("Choose an option: ")

    if choice == "1":
        text = input("\nEnter your text:\n")
        analyze_text(text)

    elif choice == "2":
        file_path = input("Enter file path: ")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                analyze_text(text)
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print("Error:", e)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
