# Optional script if you want to use muliple .txt files to create your embeddings.
# After getting those txt files with 02_create_vector_db.py, run this script to get a single .json file containing all your data
import json
import os

def merge_json_files(directory):
    merged_data = list()
    for filename in os.listdir(directory):
        if filename.endswith(".json") and filename != "merged.json":
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                data = json.load(file)
                merged_data.extend(data)
    return merged_data

# Merge JSON files
merged_json = merge_json_files("knowledge_pool")

output_file_path = "knowledge_pool/merged.json"

with open("knowledge_pool/merged.json", "w") as output_file:
    json.dump(merged_json, output_file, indent=4)

print(f"Merged JSON saved to {output_file_path}")