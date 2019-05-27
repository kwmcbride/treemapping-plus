# treemapping-plus
Improved Treemapping functionality based on Squarify that includes sub-categories

## Requirements

This package requires only pandas and the treemapping package squarify

## Usage

A pandas DataFrame with a value to be mapped with at least one category for splitting.
For example, if you have a stock portfolio, you can separate it at the most basic level using the stock name or ticker.
For this task you could simply use the squarify package. However, if you have higher-level categorical information, such as sector and industry,
this is where treemapping-plus steps in.

A dataframe with the desired categories and sizing values are required. Continuing with the portfolio example, this would require a column for tickers, sector, and industry.
The sizing column would contain the value of the stock in the portfolio.
