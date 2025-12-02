from src import Export

entities = Export().read_from_directory()

print("Exported images:")
for entity in entities:
    print(f"- {entity}")
