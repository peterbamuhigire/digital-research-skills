import csv
import os
import re
import json
from collections import defaultdict
from datetime import datetime

# Load ATC universe
atc_universe = set()
with open('projects/healthcare-app-clinical-data/drug-interactions/research/_atc-universe.txt', 'r') as f:
    for line in f:
        atc_code = line.strip()
        if atc_code:
            atc_universe.add(atc_code)

print(f"ATC Universe loaded: {len(atc_universe)} codes")

# Create a drug-to-ATC mapping by parsing markdown tables
drug_to_atc = {}
drug_files_dir = 'projects/healthcare-app-clinical-data/drugs/research'
for file in os.listdir(drug_files_dir):
    if 'data' in file and file.endswith('.md'):
        filepath = os.path.join(drug_files_dir, file)
        print(f"Processing {file}...")
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                # Data row in table (starts with | and contains ATC code pattern at position 0)
                if line.strip().startswith('|') and '---' not in line:
                    # Split by pipe
                    cells = [cell.strip() for cell in line.split('|')[1:-1]]
                    if len(cells) >= 9:
                        atc = cells[0]
                        inn = cells[8]

                        # Valid ATC code?
                        if re.match(r'[A-Z]\d{2}[A-Z]{2}\d{2}', atc) and inn and '[GAP' not in inn:
                            if atc not in drug_to_atc:
                                drug_to_atc[atc] = set()
                            drug_to_atc[atc].add(inn.lower())

print(f"Drug-to-ATC mapping created: {len(drug_to_atc)} unique ATCs with {sum(len(v) for v in drug_to_atc.values())} total drug names")

# Sample the mapping
if drug_to_atc:
    sample_atc = list(drug_to_atc.keys())[0]
    print(f"Sample: {sample_atc} -> {drug_to_atc[sample_atc]}")

# Parse all DDInter CSVs and filter
all_pairs = []
csv_files = [
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_A_raw.csv',
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_B_raw.csv',
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_D_raw.csv',
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_G_raw.csv',
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_H_raw.csv',
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_J_raw.csv',
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_L_raw.csv',
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_N_raw.csv',
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_P_raw.csv',
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_R_raw.csv',
    'projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_code_V_raw.csv',
]

seen_pairs = set()
for csv_file in csv_files:
    if not os.path.exists(csv_file):
        continue

    print(f"Processing {os.path.basename(csv_file)}...")
    matched = 0
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            drug_a_name = row.get('Drug_A', '').strip().lower()
            drug_b_name = row.get('Drug_B', '').strip().lower()
            severity = row.get('Level', 'UNKNOWN').upper()

            # Map severity to MAJOR/MODERATE/MINOR
            if severity not in ['MAJOR', 'MODERATE', 'MINOR']:
                if 'MAJOR' in severity or 'SEVERE' in severity:
                    severity = 'MAJOR'
                elif 'MODERATE' in severity:
                    severity = 'MODERATE'
                else:
                    severity = 'MINOR'

            # Try to find ATCs for both drugs
            atc_a = None
            atc_b = None

            # Direct match or partial match
            for atc, drug_names in drug_to_atc.items():
                if not atc_a:
                    for dn in drug_names:
                        if drug_a_name == dn or drug_a_name in dn or dn in drug_a_name:
                            atc_a = atc
                            break
                if not atc_b:
                    for dn in drug_names:
                        if drug_b_name == dn or drug_b_name in dn or dn in drug_b_name:
                            atc_b = atc
                            break
                if atc_a and atc_b:
                    break

            # Only include if both ATCs are in our universe
            if atc_a and atc_b and atc_a in atc_universe and atc_b in atc_universe:
                # Normalize pair order for deduplication
                pair_key = tuple(sorted([atc_a, atc_b]))
                if pair_key not in seen_pairs:
                    seen_pairs.add(pair_key)
                    all_pairs.append({
                        'drug_a_atc': atc_a,
                        'drug_b_atc': atc_b,
                        'drug_a_name': row.get('Drug_A', '').strip(),
                        'drug_b_name': row.get('Drug_B', '').strip(),
                        'severity': severity,
                        'mechanism': '[DDInter — see dataset for mechanism narrative]',
                        'clinical_consequence': '[DDInter — see dataset for clinical consequence narrative]',
                        'management': '[DDInter — see dataset for management narrative]',
                        'monitoring': '[DDInter — see dataset for monitoring narrative]',
                        'evidence_level': 'B',
                        'source_citations': '[ddinter-v2-2025]',
                    })
                    matched += 1

    print(f"  Matched {matched} pairs from this file")

print(f"\nTotal filtered pairs from all CSVs: {len(all_pairs)}")

# Load existing EAC pairs to avoid duplicates
existing_pairs = set()
with open('projects/healthcare-app-clinical-data/drug-interactions/research/wave1-data.md', 'r', encoding='utf-8') as f:
    for line in f:
        # Match table rows: | ddi-XXXX | ATC1 | ATC2 |
        match = re.search(r'\|\s*ddi-\d+\s*\|\s*([A-Z]\d{2}[A-Z]{2}\d{2})\s*\|\s*([A-Z]\d{2}[A-Z]{2}\d{2})\s*\|', line)
        if match:
            atc_a = match.group(1)
            atc_b = match.group(2)
            pair_key = tuple(sorted([atc_a, atc_b]))
            existing_pairs.add(pair_key)

print(f"Existing EAC pairs to avoid: {len(existing_pairs)}")

# Filter out existing pairs
new_pairs = []
for pair in all_pairs:
    pair_key = tuple(sorted([pair['drug_a_atc'], pair['drug_b_atc']]))
    if pair_key not in existing_pairs:
        new_pairs.append(pair)

print(f"New unique pairs after deduplication: {len(new_pairs)}")

# Write summary statistics
with open('projects/healthcare-app-clinical-data/drug-interactions/research/_ddinter_import_stats.txt', 'w') as f:
    f.write(f"DDInter 2.0 Bulk Import Statistics\n")
    f.write(f"Date: {datetime.now().isoformat()}\n\n")
    f.write(f"ATC Universe: {len(atc_universe)} codes\n")
    f.write(f"Drug-to-ATC mappings: {len(drug_to_atc)} unique ATCs\n")
    f.write(f"Total pairs parsed from DDInter CSVs: {len(all_pairs)}\n")
    f.write(f"Pairs deduped against EAC (52 existing): {len(new_pairs)}\n")
    f.write(f"Severity breakdown of new pairs:\n")

    severity_counts = defaultdict(int)
    for pair in new_pairs:
        severity_counts[pair['severity']] += 1

    for sev in ['MAJOR', 'MODERATE', 'MINOR']:
        f.write(f"  {sev}: {severity_counts[sev]}\n")

    f.write(f"\nTotal after import: {52 + len(new_pairs)} pairs\n")

print(f"\nStatistics written to _ddinter_import_stats.txt")
print(f"Severity breakdown:")
severity_counts = defaultdict(int)
for pair in new_pairs:
    severity_counts[pair['severity']] += 1
for sev in ['MAJOR', 'MODERATE', 'MINOR']:
    print(f"  {sev}: {severity_counts[sev]}")

# Save new pairs for integration
with open('projects/healthcare-app-clinical-data/drug-interactions/research/_new_pairs_for_import.json', 'w') as f:
    json.dump(new_pairs, f, indent=2)

print(f"Saved {len(new_pairs)} new pairs to _new_pairs_for_import.json")
