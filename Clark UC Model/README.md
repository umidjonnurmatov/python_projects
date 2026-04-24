# Clark Unobserved Components Model for Uzbek Potential GDP

## Project Overview

This project estimates **potential GDP** and **output gap** for Uzbekistan using the Clark (1987) Unobserved Components (UC) model. The model decomposes real GDP into:

- **Trend component** (potential GDP) - random walk with drift
- **Cycle component** (output gap) - stationary AR(2) process
- **Irregular component** (noise) - white noise

Developed as part of macroeconomic research at the Institute for Macroeconomic and Regional Studies.

## Why Clark UC Model?

| Feature | Benefit |
|---------|---------|
| Unobserved components | Separates trend from cycle statistically |
| Allows stochastic trend | GDP shocks can have permanent effects |
| AR(2) cycle | Captures business cycle persistence |
| Kalman filter estimation | Handles unobserved components optimally |

## Key Outputs

| Output | Description |
|--------|-------------|
| **Potential GDP** | Long-run sustainable output level |
| **Output Gap** | Actual GDP - Potential GDP (%) |
| **Cycle persistence** | How long shocks last |
| **Trend volatility** | Permanent shock magnitude |