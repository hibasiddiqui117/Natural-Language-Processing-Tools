def extract_entities(sentence):
    entities = []
    words = sentence.split()

    # Define some simple rules for entity recognition
    for word in words:
        if word[0].isupper():
            entities.append((word, "PERSON"))  # Assume capitalized words are persons
        elif word.lower() in ["company", "organization", "corporation"]:
            entities.append((word, "ORGANIZATION"))  # Assume these words indicate organizations
        # Add more rules as needed for other entity types

    return entities

def main():
    while True:
        input_text = input("Enter a sentence (or 'exit' to quit): ")
        if input_text.lower() == 'exit':
            break

        entities = extract_entities(input_text)
        print("Entities found:")
        for entity, entity_type in entities:
            print(f"{entity}: {entity_type}")

if __name__ == "__main__":
    main()
