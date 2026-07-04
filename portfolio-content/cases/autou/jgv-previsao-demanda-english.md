---
title: JGV — Demand forecasting and stock recommendation
client: JGV
category: autou
status: Production
stack: [Python, Prophet, Flask, PostgreSQL]
order: 1
gallery: jgv
---

# Case — JGV (Demand Forecasting and Stock Recommendation for an Auto Parts Chain)

**Type:** AutoU (client: JGV — multi-branch auto parts chain)
**Role:** Full Stack Developer / applied data engineer — correction and evolution of the predictive pipeline and API
**Status:** In production (automated daily execution)
**Stack:** Python, Prophet (time series), Flask (API), PostgreSQL, Sankhya ERP (Oracle SQL via API), Bubble (frontend), feature flags, Docker, Google Cloud, PowerShell/deployment CI

> Confidentiality note: AutoU client project — validate what can be made public before exposing name/details.

## Context and problem

A multi-branch auto parts chain bought and transferred stock based on the buyer's intuition about the Sankhya ERP. Result: excess items sitting idle at one branch and stockouts at another, capital tied up and lost sales — worsened by the complexity of parts with **substitutes and equivalents** (buying the "original" item when the substitute already covers demand).

## Solution

An end-to-end daily batch pipeline + recommendation management API:

- **JGV_Prediction**: syncs products, stock, movement, costs, branches and substitutes from Sankhya; computes the 7 business classification attributes; runs **Prophet per product/branch** to forecast demand; generates **purchase**, **inter-branch transfer** (behind a feature flag) and **substitute resolution** recommendations; runs automatically at a configurable daily time.
- **JGV_API (Flask)**: exposes the recommendations to the Bubble frontend, with create/accept recommendation flows integrated back into Sankhya (order generation), documented by contract for Bubble's API Connector.

## Architecture and technical decisions

- **Defensive purchase logic**: `QtdTotal_f = max(forecasted_demand − stock − pending_orders, 0)` — open orders "in transit" are deducted outside the Prophet `fit()` (they don't contaminate the model), and recommendations already accepted in the history are subtracted before saving, avoiding duplicate purchases
- **Substitute resolution at the right point**: demand aggregation between the original item and its substitutes resolved at the recommendation stage (`substitutos_resolver`), with a dedicated SQL view in Sankhya
- **Weighting by data coverage**: forecast adjusted by the days actually covered in history (`total_days`), avoiding overestimation for products with partial history
- **Feature flags** for new features (inter-branch transfer) — controlled production rollout with no deploy branch
- **Scenario tests against the cloud environment** (`test_cenarios_recomendacao_cloud.py` etc.) and scripted dev/prod schema comparison
- Sankhya integration via documented batch queries (`BATCH_QUERY_SANKHYA.md`), with a fully versioned mapping of the ERP database

## Challenges and solutions

- **Critical legacy transfer/stock bug**: investigated and fixed with a formal executive summary for the client (RESUMO_EXECUTIVO with PDF) — query diagnosis, schema fix and production validation
- **ERP as a hostile data source**: Sankhya schema mapped by hand (operation type code, invoice status, pending items) and fiscal/business rules converted into explicit, documented SQL filters
- **A model the business trusts**: every step of the calculation is reproducible and documented — the buyer can audit why the system recommended X units

## Results and impact

- Automatic daily purchase and transfer recommendations per branch, accounting for substitutes [reduction in stockouts/idle stock TO CONFIRM]
- Fixing the transfer flow eliminated phantom pending items in the ERP
- The buyer moved from spreadsheet/intuition to a queue of recommendations acceptable in one click on the front end

## Interview highlights (STAR summary)

- **S/T:** a multi-branch auto parts chain buying by intuition, substitute items ignored, and a transfer bug corrupting pending items in the ERP. **A:** I evolved the Prophet pipeline (coverage weighting, discounting pending orders outside the fit, substitute resolution), fixed the transfer flow with a formal diagnosis, and maintained the Flask API serving recommendations to the Bubble front end integrated with Sankhya. **R:** a daily production pipeline generating auditable purchase and transfer recommendations, with feature-flag rollout and the client's trust in the numbers.
