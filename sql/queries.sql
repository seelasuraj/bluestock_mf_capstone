SELECT 
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM fact_sip_inflows
ORDER BY month;
SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;
SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;
SELECT
    category,
    COUNT(*) AS number_of_funds
FROM dim_fund
GROUP BY category
ORDER BY number_of_funds DESC;
SELECT
    transaction_type,
    AVG(amount_inr) AS average_amount
FROM fact_transactions
GROUP BY transaction_type;
SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;
SELECT
    risk_grade,
    AVG(return_5yr_pct) AS avg_return,
    AVG(sharpe_ratio) AS avg_sharpe
FROM fact_performance
GROUP BY risk_grade
ORDER BY avg_return DESC;