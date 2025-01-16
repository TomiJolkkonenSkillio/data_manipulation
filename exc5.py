def organize_words():
    try:
        # read file, words to different lines
        with open("input.txt", "r") as file:
            words = file.read().splitlines()

        # organize words by length and then alphabetically for equal lengths
        sorted_words = sorted(words, key=lambda word: (len(word), word))

        # write to file
        with open("output.txt", "w") as file:
            for word in sorted_words:
                file.write(word + "\n")

        print(f"words are written to output.txt, shortest first, and equal length words alphabetically.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    organize_words()

if __name__ == "__main__":
    main()