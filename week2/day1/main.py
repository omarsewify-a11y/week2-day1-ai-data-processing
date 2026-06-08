import json
import csv
from collections import Counter

# Load JSON dataset
def load_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

# Count categories
def count_categories(data):
    categories = [item["category"] for item in data]
    return Counter(categories)

# Get top 3 categories
def get_top_three(counter):
    return counter.most_common(3)

# Generate summary report
def generate_summary(counter, top_three):
    print("\n=== CATEGORY COUNT ===")
    for category, count in counter.items():
        print(f"{category}: {count}")

    print("\n=== TOP 3 CATEGORIES ===")
    for category, count in top_three:
        print(f"{category}: {count}")

# Export CSV file
def export_csv(counter, filename="summary.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Count"])

        for category, count in counter.items():
            writer.writerow([category, count])

# Main function
def main():
    data = load_data("data.json")

    category_counts = count_categories(data)
    top_three = get_top_three(category_counts)

    generate_summary(category_counts, top_three)
    export_csv(category_counts)

    print("\nCSV file 'summary.csv' generated successfully!")

# Run program
if __name__ == "__main__":
    main()
