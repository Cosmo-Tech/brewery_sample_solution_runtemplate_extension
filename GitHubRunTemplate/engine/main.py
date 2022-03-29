#!/usr/bin/env python
# -*- coding: utf-8 -*-

from investment_simulator.portfolios import growth_simulation

asset_weights = [0.5, 0.5]
asset_returns = [0.1, 0.1]
covariance = [[1.0, 0.0], [0.0, 1.0]]
steps = 10
investment_goal = 2.5

result = growth_simulation(
        asset_weightings= asset_weights,
        annual_returns=asset_returns,
        covariance=covariance,
        steps=steps,
        investment_goal=investment_goal,
    )
print(result)
