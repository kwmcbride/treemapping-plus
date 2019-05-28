"""Treemapping

An improved treemapping method to include sub-classes

Author: Kevin McBride
"""

import squarify as sq
import pandas as pd


def pad_rect(rect, move):
    """Returns padded rectangles given specified padding"""

    if rect['dx'] > 2:
        rect['x'] += move[0]
        rect['dx'] -= 1*move[0]
    if rect['dy'] > 2:
        rect['y'] += move[1]
        rect['dy'] -= 1*move[1]

    return rect

def make_boxes(df_data, category, size_factor, x, y, height, width, pad=[1,1], main_cat=None):
    """Generates the coordinates for the boxes of the category"""

    totals = df_data[size_factor].groupby(df_data[category]).sum()
    box_list = totals.sort_values(ascending=False).to_frame()
    box_list.columns = ['value']
    if main_cat:
        box_list['cat'] = main_cat
    box_list['norm'] = sq.normalize_sizes(box_list.value, width, height)
    box_list['rect'] = sq.squarify(box_list.norm, x, y, width, height)
    box_list['rect'] = box_list.apply(lambda row: pad_rect(row['rect'], pad), axis=1)

    return box_list

def make_sub_boxes(all_df, rect_df, size_factor, main_cat, sub_cat, pad=[1,1]):
    """Generates the boxes within each of the higher order categories"""

    rect_dict = []
    inCat = list(all_df[main_cat].unique())

    for i in inCat:

        cat_df = all_df[all_df[main_cat]==i]
        height = rect_df['rect'][i]['dy']
        width = rect_df['rect'][i]['dx']
        x = rect_df['rect'][i]['x']
        y = rect_df['rect'][i]['y']
        rect_dict.append(make_boxes(cat_df, sub_cat, size_factor, x, y, height, width, pad, i))

    return pd.concat(rect_dict)

def make_treemap(data, categories, size_factor, x=0, y=0, height=1200, width=800, pads=[1, 1]):
    """Primary function for generating treemaps with subsections

    Parameters:
    __________
    
    data : pandas DataFrame
        data containing the categories and the sizing values
    cats : list of strings
        hierarchical categories for the treemap - from highest to lowest groups (these should be columns in data)
    sizing : str
        column name of value used in sizing (should be column name in data)
    x : float
        starting value for x (usually 0)
    y : float
        starting value for y (usually 0)        
    height : int
        total width of the treemap (pixels)
    width : int
        total height of the treemap (pixels)
    pads : dict or list of two values
        key is the category, value is the padding for x and y in pixels
        i.e. : {'cat1' : [2, 5], 'cat2' : [2, 2]}
        - or -
        a general spacing for all levels : [2, 2]

    Returns:
    ________

    all_rects : pandas DataFrame
        dataframe with the box sizes as dictionaries for each entry

    """
    if not isinstance(pads, dict):
        
        pads = {c: pads for c in categories}     

    all_rects = {}
    all_rects[categories[0]] = make_boxes(data, categories[0], size_factor, x=x, y=y, height=height, width=width, pad=pads[categories[0]])

    for i in range(1,len(categories)):
            all_rects[categories[i]] = make_sub_boxes(data, all_rects[categories[i-1]], size_factor, categories[i-1], categories[i], pad=pads[categories[i]])

    return all_rects

def main():
    pass

if __name__ == '__main__':
    main()
