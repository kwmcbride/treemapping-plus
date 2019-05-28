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

## Authors

* **Kevin McBride** - [Github Page](https://github.com/kwmcbride)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* I thank the creators and contributors of squarify

