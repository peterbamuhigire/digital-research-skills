import json
import os

# Load the new pairs
with open('projects/healthcare-app-clinical-data/drug-interactions/research/_new_pairs_for_import.json', 'r') as f:
    new_pairs = json.load(f)

# Generate table rows
table_rows = []
start_id = 53  # Continue from ddi-0052

for idx, pair in enumerate(new_pairs, start=start_id):
    interaction_id = f"ddi-{idx:04d}"

    # Handle ordering: ensure consistent order in table (A always ≤ B lexicographically)
    if pair['drug_a_atc'] <= pair['drug_b_atc']:
        atc_a, atc_b = pair['drug_a_atc'], pair['drug_b_atc']
        name_a, name_b = pair['drug_a_name'], pair['drug_b_name']
    else:
        atc_a, atc_b = pair['drug_b_atc'], pair['drug_a_atc']
        name_a, name_b = pair['drug_b_name'], pair['drug_a_name']

    row = (
        f"| {interaction_id} | {atc_a} | {atc_b} | {name_a} | {name_b} | "
        f"{pair['severity']} | {pair['mechanism']} | {pair['clinical_consequence']} | "
        f"{pair['management']} | {pair['monitoring']} | {pair['evidence_level']} | "
        f"{pair['source_citations']} | ATC/DDD 2024 | 2026-05-04 |"
    )
    table_rows.append(row)

# Write the table rows to a file
with open('projects/healthcare-app-clinical-data/drug-interactions/research/_table_rows_to_append.txt', 'w') as f:
    for row in table_rows:
        f.write(row + '\n')

print(f"Generated {len(table_rows)} table rows")
print(f"IDs range from ddi-{start_id:04d} to ddi-{start_id + len(table_rows) - 1:04d}")

# Count severity breakdown
severity_counts = {}
for pair in new_pairs:
    sev = pair['severity']
    severity_counts[sev] = severity_counts.get(sev, 0) + 1

print("\nSeverity breakdown:")
for sev in ['MAJOR', 'MODERATE', 'MINOR']:
    print(f"  {sev}: {severity_counts.get(sev, 0)}")

# Sample rows
print("\nFirst 3 sample rows:")
for row in table_rows[:3]:
    print(row[:200] + "...")
