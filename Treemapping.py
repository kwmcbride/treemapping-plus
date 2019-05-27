"""Treemapping

An improved treemapping method to include sub-classes

Author: Kevin McBride
"""

import squarify as sq
import pandas as pd

def sec_add(data, desc, sizing):
    """Adds the sizing criteria for a category"""

    totals = {}
    for d in list(data[desc].unique()):

        totals[d] = data[sizing][data[desc]==d].sum()

    totals = pd.DataFrame(pd.Series(totals))
    totals = totals.sort_values(by=0, ascending=False)

    return totals

def pad_rect(rect, move):
    """Returns padded rectangles given specified padding"""

    if rect['dx'] > 2:
        rect['x'] += move[0]
        rect['dx'] -= 1*move[0]
    if rect['dy'] > 2:
        rect['y'] += move[1]
        rect['dy'] -= 1*move[1]

    return rect

def make_boxes(df_sort, cat, sizing, x, y, height, width, pad=[1,1], main_cat=None):
    """Generates the initial boxes of the main class"""

    box_list = sec_add(df_sort, cat, sizing)
    box_list.columns = ['value']
    if main_cat:
        box_list['cat'] = main_cat

    box_list['norm'] = sq.normalize_sizes(box_list.value, width, height)
    box_list['rect'] = sq.squarify(box_list.norm, x, y, width, height)

    for r in box_list['rect']:
        pad_rect(r, pad)

    return box_list


def make_sub_boxes(all_df, rect_df, sizing, main_cat, sub_cat, pad=[1,1]):
    """Generates the boxes within each of the subclasses"""

    rect_dict = {}
    inCat = list(all_df[main_cat].unique())

    for i in inCat:

        cat_df = all_df[all_df[main_cat]==i]
        
        print(i)
        print( rect_df['rect'][i]['dy'])
        
        height = rect_df['rect'][i]['dy']
        width = rect_df['rect'][i]['dx']
        x = rect_df['rect'][i]['x']
        y = rect_df['rect'][i]['y']
        rect_dict[i] = make_boxes(cat_df, sub_cat, sizing, x, y, height, width, pad, i)

    frames = []
    for dic in rect_dict:
        frames.append(rect_dict[dic])

    return pd.concat(frames)


def make_treemap(data, cats, sizing, x, y, height, width, pads):
    """Primary function for generating treemaps with subsections

    Parameters:
    __________
    
    data : pandas DataFrame
        data containing the categories and the sizing values
    cats : list of strings
        categories found as columns in data
    sizing : str
        column name of value used in sizing
    x : float
        starting value for x (usually 0)
    y : float
        starting value for y (usually 0)        
    height : int
        total width of the treemap (pixels)
    width : int
        total height of the treemap (pixels)
    pads : dict
        
        key is the category, value is the padding for x and y in pixels
        i.e. : {'cat1' : [2, 5], 'cat2' : [2, 2]}

    Returns:
    ________

    all_rects : pandas DataFrame
        dataframe with the box sizes as dictionaries for each entry

    """
    

    all_rects = {}

    for i in range(len(cats)):

        if i == 0:

            all_rects[cats[i]] = make_boxes(data, cats[i], sizing, x, y, height, width, pad=pads[cats[i]])

        else:

            all_rects[cats[i]] = make_sub_boxes(data, all_rects[cats[i-1]], sizing, cats[i-1], cats[i], pad=pads[cats[i]])

    return all_rects

def main():
    pass

if __name__ == '__main__':
    main()
