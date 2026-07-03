import os
import requests
import pandas as pd

# Destination folder matching your project layout
output_dir = os.path.join("Data", "Raw")
os.makedirs(output_dir, exist_ok=True)

# Key schemes required by the assignment guidelines
target_schemes = {
    125497: "hdfc_top_100_live",
    119551: "sbi_bluechip_live",
    120503: "icici_bluechip_live",
    118632: "nippon_large_cap_live",
    119092: "axis_bluechip_live",
    120841: "kotak_bluechip_live"
}

print("=" * 60)
print("             STARTING LIVE MFAPI DATA EXTRACTION            ")
print("=" * 60)

for code, name in target_schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    print(f"📡 Requesting AMFI Code {code} ({name})...")
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            raw_json = response.json()
            nav_records = raw_json.get('data', [])
            
            if nav_records:
                # Convert list of NAV dictionaries to a clean DataFrame
                df = pd.DataFrame(nav_records)
                
                # Attach identification columns for easier relational linking later
                df['amfi_code'] = code
                
                # Save out to flat file storage
                file_path = os.path.join(output_dir, f"{name}.csv")
                df.to_csv(file_path, index=False)
                print(f"✅ Saved {len(df)} price lines to {file_path}")
            else:
                print(f"⚠️ Empty payload returned for code: {code}")
        else:
            print(f"❌ HTTP Error {response.status_code} received.")
            
    except Exception as e:
        print(f"❌ Connection or parsing failed: {e}")
    print("-" * 40)

print("\n🚀 All live requests processed successfully!")
print("=" * 60) 