"""
FUNCTION SLIDE_LINE (ORIGINAL_LIST):
    PURPOSE: Moves all non-zero tiles to the beginning of the list (left/top) and pads the rest of the list with zeros, without performing merges.

FUNCTION MERGE_LINE (SLID_LIST, CURRENT_SCORE):
    PURPOSE: Combines adjacent, identical tiles in a list that has already been slid.
    It also updates the score when a merge occurs.

FUNCTION PROCESS_LINE (LINE, SCORE):
    PURPOSE: Executes the full movement logic (Slide, Merge, Final Slide) on a single row or column.
"""

def slide_line(original_list):
    new_list = []
    
    for value in original_list:
        if value is not 0:
            new_list.append(value)
    
    original__size = 4
    current_size = len(original_list)
    zeros_needed = original__size - current_size
    
    for i in range(1,zeros_needed+1):
        new_list.append[0]
    
    return new_list

def merge_line(list_to_merge,current_score):
    for i in range(3):
        if list_to_merge[i] is not 0 and list_to_merge[i] == list_to_merge[i+1]:
            new_value = list_to_merge[i] * 2
            list_to_merge[i] = new_value
            current_score = current_score + new_value
            list_to_merge[i+1] = 0
    return list_to_merge,current_score

def process_line(line,score):
    slid_line = slide_line(line)
    (merged_line,new_score) = merge_line(slid_line,score)
    final_line = slid_line(merged_line)

    return final_line,new_score