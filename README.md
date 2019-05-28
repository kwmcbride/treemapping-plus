# treemapping-plus

This module provides improved treemapping functionality based on the squarify module but includes sub-categories. This module also works with pandas dataframes as input, making it easy to use existing data structures.

## Getting Started

This package requires only pandas and the package squarify. At the moment, you can simply place the Treemapping.py file into your path. It will be incorporated into a more comprehensive package in the near future.

### Prerequisites

This is a python module that additionally requires pandas and squarify:

```
pip install squarify
```

## Usage

A pandas DataFrame with a value to be mapped with at least one category for splitting.
For example, if you have a stock portfolio, you can separate it at the most basic level using the stock name or ticker.
For this task you could simply use the squarify package. However, if you have higher-level categorical information, such as sector and industry,
this is where treemapping-plus steps in.

A dataframe with the desired categories and sizing values is required. Continuing with the portfolio example, this would require a column for tickers, sector, and industry.
The sizing column would contain the value of the stock in the portfolio.

# Example

Suppose you have the following data stored in a dataframe:


| index  | ticker | sector | industry | value |
| --- | --- | --- | --- | --- |
|0 |	HON |	Industrials |	Diversified Industrials | 1500 |
|1 |	CVS |	Healthcare |	Health Care Plans | 1200| 
|2 |	XOM |	Energy |	Oil & Gas Integrated | 800 |
|3 |	JNJ |	Healthcare |	Drug Manufacturers - Major | 2000 |
|4 |	V |	Financial Services |	Credit Services | 2500 |
|5 |	PEP |	Consumer Defensive |	Beverages - Soft Drinks | 4500 |
|6 |	AVGO |	Technology |	Semiconductors | 1300 |
|7 |	HRL |	Consumer Defensive |	Packaged Foods | 2100 |
|8 |	KO |	Consumer Defensive |	Beverages - Soft Drinks | 3200 |

Using the function make_treemap, you can generate the coordinates required for plotting a treemap as done using squarify, but with subclasses! For example, you can split the dataframe into sectors, followed by splitting each sector square into industries, and finally each individual stock. In this way you can generate more coordinated treemaps.

The main function returns a dict that contains dataframes with the coordinates for each category. You can use these however you wish for plotting.

```
rects = make_treemap(dataframe, ['sector', 'industry', 'ticker'], 'value', **kwargs)
```




## Authors

* **Kevin McBride** - [Github Page](https://github.com/kwmcbride)

## License

This project is licensed under the MIT License

## Acknowledgments

* I thank the creators and contributors of squarify

