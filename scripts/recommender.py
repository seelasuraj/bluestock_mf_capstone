import pandas as pd

# ==========================
# Load Performance Dataset
# ==========================

try:
    df = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
except FileNotFoundError:
    print("Error: Could not find data/processed/07_scheme_performance_clean.csv")
    exit()

# ==========================
# Available Risk Profiles
# ==========================

print("=" * 60)
print("      Mutual Fund Recommendation System")
print("=" * 60)

print("\nAvailable Risk Profiles:")
for risk in sorted(df["risk_grade"].dropna().unique()):
    print(f"• {risk}")

risk_input = input("\nEnter Risk Appetite: ").strip().title()

# ==========================
# Filter & Recommend
# ==========================

recommendations = (
    df[df["risk_grade"] == risk_input]
    .sort_values(by="sharpe_ratio", ascending=False)
    .head(3)
)

# ==========================
# Display Results
# ==========================

print("\n" + "=" * 75)

if recommendations.empty:
    print(f"No funds found for risk profile: {risk_input}")
else:
    print(f"Top 3 Recommended Funds for [{risk_input.upper()}] Risk Appetite:\n")

    print(
        recommendations[
            [
                "scheme_name",
                "fund_house",
                "category",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct",
                "alpha",
                "beta",
            ]
        ].to_string(index=False)
    )

print("=" * 75)