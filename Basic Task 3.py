def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        words = content.split()
        print(words)
        word_count = len(words)

        return word_count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0
    except IOError:
        print(f"Error: An issue occurred while reading the file '{file_path}'.")
        return 0
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return 0


file_path = "products.csv"
result = count_words(file_path)
if result > 0:
    print(f"The file contains {result} words.")