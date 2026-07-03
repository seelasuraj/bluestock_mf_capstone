import os
import glob
import pandas as pd

# Define the path where the raw files are located
raw_data_path = os.path.join("Data", "Raw")

print("=" * 60)
print("             STARTING DATA INGESTION & RUNNING PROFILE             ")
print("=" * 60)

# Check if the directory actually exists before moving forward
if not os.path.exists(raw_data_path):
    print(f"ERROR: Cannot find the directory '{raw_data_path}'. Check your folder names.")
    exit()

# Find all CSV files inside Data/Raw
csv_files = glob.glob(os.path.join(raw_data_path, "*.csv"))

if not csv_files:
    print(f"No CSV files found in '{raw_data_path}'. Double-check that they pasted correctly.")
    exit()

print(f"Found {len(csv_files)} files to profile.\n")

# Store datasets in a dictionary to use them later for joins
datasets = {}

# --- TASK 3: LOAD AND PROFILE EACH CSV ---
for file in csv_files:
    file_name = os.path.basename(file)
    print(f"\nProcessing File: {file_name}")
    print("-" * 40)
    
    try:
        # Load the dataset
        df = pd.read_csv(file)
        datasets[file_name] = df
        
        # 1. Print Shape
        print(f"Dimensions (Rows, Columns): {df.shape}")
        
        # 2. Print Data Types
        print("\nColumn Data Types:")
        print(df.dtypes)
        
        # 3. Print Head (First 5 rows)
        print("\nFirst 5 Rows:")
        print(df.head(5))
        
        # 4. Human note on basic anomalies
        missing_data = df.isna().sum().sum()
        duplicates = df.duplicated().sum()
        
        print("\nQuick Quality Check:")
        if missing_data > 0 or duplicates > 0:
            print(f"  -> Total missing values: {missing_data}")
            print(f"  -> Total duplicate rows: {duplicates}")
        else:
            print("  -> Looking good! No missing values or duplicates found.")
            
    except Exception as e:
        print(f"Something went wrong while reading {file_name}: {e}")
        
    print("\n" + "="*50)


# --- TASK 6: EXPLORE FUND MASTER ---
print("\n" + "=" * 60)
print("                   EXPLORING FUND MASTER STRUCTURE                 ")
print("=" * 60)

# Target the specific master file from the 10 provided datasets
master_file_name = "01_fund_master.csv"

if master_file_name in datasets:
    master_df = datasets[master_file_name]
    print(f"Analyzing unique values inside '{master_file_name}':\n")
    
    # Updated to 'risk_category' to match the actual CSV column naming structure
    target_columns = ['fund_house', 'category', 'sub_category', 'risk_category']
    
    for col in target_columns:
        if col in master_df.columns:
            unique_items = master_df[col].dropna().unique()
            print(f"🔹 Unique '{col}' counts ({len(unique_items)} items):")
            print(list(unique_items))
            print()
        else:
            print(f"⚠️ Column '{col}' not found in the master file.")
else:
    print(f"Warning: Could not run exploration because '{master_file_name}' is missing.")


# --- TASK 7: VALIDATE AMFI CODES ---
print("\n" + "=" * 60)
print("                     AMFI CODE VALIDATION REPORT                   ")
print("=" * 60)

history_file_name = "02_nav_history.csv"

if master_file_name in datasets and history_file_name in datasets:
    m_df = datasets[master_file_name]
    h_df = datasets[history_file_name]
    
    # We expect 'amfi_code' or 'scheme_code' to build the relationship
    # Let's dynamically look for whatever tracking column name is present
    m_code_col = [c for c in m_df.columns if 'code' in c.lower() or 'amfi' in c.lower()]
    h_code_col = [c for c in h_df.columns if 'code' in c.lower() or 'amfi' in c.lower()]
    
    if m_code_col and h_code_col:
        master_col = m_code_col[0]
        history_col = h_code_col[0]
        
        # Get unique values as sets to do clean difference operations
        unique_master_codes = set(m_df[master_col].dropna().unique())
        unique_history_codes = set(h_df[history_col].dropna().unique())
        
        # Find any code in master that isn't present in history records
        unmatched_codes = unique_master_codes - unique_history_codes
        
        print(f"Total Unique AMFI codes in Master: {len(unique_master_codes)}")
        print(f"Total Unique AMFI codes in NAV History: {len(unique_history_codes)}")
        print("-" * 40)
        
        if len(unmatched_codes) == 0:
            print("✅ SUCCESS: Every single AMFI code in the fund_master matches a record in nav_history.")
        else:
            print(f"❌ DATA QUALITY ISSUE: Found {len(unmatched_codes)} code(s) in master missing from history file.")
            print(f"Sample unmatched codes: {list(unmatched_codes)[:5]}")
    else:
        print("Could not find an AMFI/Scheme code relationship tracking column in the files.")
else:
    print(f"Skipping validation. Ensure both '{master_file_name}' and '{history_file_name}' exist.")

print("\n" + "=" * 60)
print("                       INGESTION COMPLETED                         ")
print("=" * 60)