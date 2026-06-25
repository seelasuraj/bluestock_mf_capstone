# Bluestock Mutual Fund Analytics Platform

## Data Dictionary

Project: Mutual Fund Analytics Platform  
Dataset Source: Bluestock Fintech Capstone Dataset

---

# 1. dim_fund

Source:
01_fund_master.csv

Purpose:
Stores master information about mutual fund schemes.

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Unique identifier for mutual fund scheme |
| fund_house | Text | Asset Management Company name |
| scheme_name | Text | Name of mutual fund scheme |
| category | Text | Main category of fund |
| sub_category | Text | Fund sub-category |
| plan | Text | Direct or Regular investment plan |
| launch_date | Date | Fund launch date |
| benchmark | Text | Benchmark index of fund |
| expense_ratio_pct | Float | Annual expense ratio percentage |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Float | Minimum SIP investment amount |
| min_lumpsum_amount | Float | Minimum lump sum investment |
| fund_manager | Text | Person managing the fund |
| risk_category | Text | Risk level of fund |
| sebi_category_code | Text | SEBI classification code |

---
# 2. fact_nav

Source:
02_nav_history.csv

Purpose:
Stores historical daily NAV values.

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Fund identifier |
| date | Date | NAV calculation date |
| nav | Float | Net Asset Value of fund |

---
# 3. fact_transactions

Source:
08_investor_transactions.csv

Purpose:
Stores investor purchase and redemption transactions.

| Column | Data Type | Description |
|---|---|---|
| investor_id | Text | Unique investor identifier |
| transaction_date | Date | Date of transaction |
| amfi_code | Integer | Fund identifier |
| transaction_type | Text | SIP, Lumpsum, Redemption |
| amount_inr | Float | Transaction amount in INR |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | City classification |
| age_group | Text | Investor age category |
| gender | Text | Investor gender |
| annual_income_lakh | Float | Annual income |
| payment_mode | Text | Payment method |
| kyc_status | Text | Investor KYC verification status |

---
# 4. fact_performance

Source:
07_scheme_performance.csv

Purpose:
Stores mutual fund performance metrics.

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Fund identifier |
| scheme_name | Text | Fund scheme name |
| fund_house | Text | AMC name |
| category | Text | Fund category |
| plan | Text | Investment plan |
| return_1yr_pct | Float | One year return percentage |
| return_3yr_pct | Float | Three year return percentage |
| return_5yr_pct | Float | Five year return percentage |
| benchmark_3yr_pct | Float | Benchmark three year return |
| alpha | Float | Excess return generated |
| beta | Float | Market sensitivity |
| sharpe_ratio | Float | Risk adjusted return |
| sortino_ratio | Float | Downside risk adjusted return |
| std_dev_ann_pct | Float | Annual volatility |
| max_drawdown_pct | Float | Maximum loss percentage |
| aum_crore | Float | Assets under management |
| expense_ratio_pct | Float | Fund expense ratio |
| morningstar_rating | Integer | External rating |
| risk_grade | Text | Risk classification |

---
# 5. fact_aum

Source:
03_aum_by_fund_house.csv

Purpose:
Stores Assets Under Management information.

| Column | Data Type | Description |
|---|---|---|
| date | Date | Reporting date |
| fund_house | Text | AMC name |
| aum_lakh_crore | Float | AUM in lakh crore |
| aum_crore | Float | AUM in crore |
| num_schemes | Integer | Number of schemes managed |

---
# Additional Datasets

| Dataset | Purpose |
|---|---|
| 04_monthly_sip_inflows.csv | Monthly SIP investment trends |
| 05_category_inflows.csv | Category-wise investment inflows |
| 06_industry_folio_count.csv | Industry investor folio statistics |
| 09_portfolio_holdings.csv | Fund portfolio holdings |
| 10_benchmark_indices.csv | Market benchmark index values |

---