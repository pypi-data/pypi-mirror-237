import pandas as pd
from datetime import datetime
import os
import numpy as np
from dateutil.relativedelta import relativedelta
from pprint import pprint

def get_dict_count(unit_dict):
    add = 0
    for k in unit_dict.keys():
        add = add + unit_dict[k]
    return add

def is_teen(is_term_1, is_summer, dob):
    if pd.isnull(dob):
        return 0
    true_dob = datetime.strptime(str(dob), "%Y-%m-%d %H:%M:%S")
    if is_term_1 == 1:
        return 1 if relativedelta(datetime(2023, 5, 26), true_dob).years >= 13 and relativedelta(datetime(2023, 5, 26), true_dob).years < 20 else 0
    elif is_summer == 1:
        return 1 if relativedelta(datetime(2023, 7, 21), true_dob).years >= 13 and relativedelta(datetime(2023, 7, 21), true_dob).years < 20 else 0
    else:
        return 1 if relativedelta(datetime(2023, 9, 30), true_dob).years >= 13 and relativedelta(datetime(2023, 9, 30), true_dob).years < 20 else 0
    
def calc_age(is_term_1, is_summer, dob):
    if pd.isnull(dob):
        return np.nan 
    true_dob = datetime.strptime(str(dob), "%Y-%m-%d %H:%M:%S")
    if is_term_1 == 1:
        return relativedelta(datetime(2023, 5, 26), true_dob).years
    elif is_summer == 1:
        return relativedelta(datetime(2023, 7, 21), true_dob).years
    else:
        return relativedelta(datetime(2023, 9, 30), true_dob).years

def main(pth_in, pth_out, show_blacklist):
    if not pth_out:
        pth_out = os.getcwd()
    df = pd.read_excel(pth_in)
    df = df[~df['All Groups'].str.contains('301')]
    df['mem_unique'] = df['Membership Number'].astype(str) + df['Member Full Name']
    grps = df.groupby(['mem_unique'])
    

    units = df['Unit'].drop_duplicates().sort_values()
    units = units.astype(str).tolist()
    unit_dict = dict.fromkeys(units, 0)
    unit_dict['301'] = 0
    unit_dict['000'] = 0
    blacklist = ['000', '503', '205', '204', '411', '309']
    [unit_dict.pop(key) for key in blacklist]
    unsorted = []
    df_for_merging = pd.DataFrame(columns=['mem_unique', 'is_term_1', 'is_summer', 'is_term_2', 'used_tag'])
    for x in grps.groups:
        cur = grps.get_group(x)
        a = cur.loc[cur['All Groups'].str.contains('24')]
        b = cur.loc[cur['All Groups'].str.contains('Summer') & (cur['All Groups'].str.contains('23'))]
        c = cur.loc[(cur['All Groups'].str.contains('22')) & (cur['All Groups'].str.contains('23'))]
        prefix = None
        if a.shape[0] > 0 and a.iloc[0]['All Groups'][:3] not in blacklist:
            selected = a.iloc[0]
            prefix = selected['All Groups'][:3]
            df_temp = pd.DataFrame(data={'mem_unique': [x], 'is_term_1': [0], 'is_summer': [0], 'is_term_2': [1], 'used_tag': [selected['All Groups']]})
            df_for_merging = pd.concat([df_for_merging, df_temp], ignore_index=True)
        elif b.shape[0] > 0 and b.iloc[0]['All Groups'][:3] not in blacklist:
            selected = b.iloc[0]
            prefix = selected['All Groups'][:3]
            df_temp = pd.DataFrame(data={'mem_unique': [x], 'is_term_1': [0], 'is_summer': [1], 'is_term_2': [0], 'used_tag': [selected['All Groups']]})
            df_for_merging = pd.concat([df_for_merging, df_temp], ignore_index=True)
        elif c.shape[0] > 0 and c.iloc[0]['All Groups'][:3] not in blacklist:
            selected = c.iloc[0]
            prefix = selected['All Groups'][:3]
            df_temp = pd.DataFrame(data={'mem_unique': [x], 'is_term_1': [1], 'is_summer': [0], 'is_term_2': [0], 'used_tag': [selected['All Groups']]})
            df_for_merging = pd.concat([df_for_merging, df_temp], ignore_index=True)
        else:
            unsorted.append(cur.iloc[0]['Member Full Name'])
        if prefix not in blacklist and prefix != None:
            unit_dict[prefix] = unit_dict[prefix] + 1 
        
    df_no_dups = df.drop_duplicates(subset=['mem_unique'])
    merged = df_no_dups.merge(df_for_merging, on='mem_unique', how='inner')
    counted_students = get_dict_count(unit_dict)
    num_students = df_for_merging.shape[0]
    if counted_students != num_students:
        print(f'\n----------------------WARNING-----------------------------\nNot all students were sorted!\n\nTotal number of Students: {num_students}\nNumber of Counted Students: {counted_students}\n\nList of students not counted:\n{unsorted}\n----------------------WARNING-----------------------------\n')

    print(f'\nCount by site:\n\n')
    pprint(unit_dict)
    print(f'\nTotal: {counted_students}')

    if show_blacklist:
        print('Members not shown: \n')
        pprint(unsorted)
        unsorted = pd.Series(unsorted)
        unsorted.to_excel(f'{pth_out}/blacklist_{datetime.now()}.xlsx')


    

    merged['is_teen'] = merged.apply(lambda x: is_teen(x['is_term_1'], x['is_summer'], x['Date of Birth (Member)']), axis=1)
    merged['age_as_of_last_term_attended'] = merged.apply(lambda x: calc_age(x['is_term_1'], x['is_summer'], x['Date of Birth (Member)']), axis=1)
    merged.to_excel(f'{pth_out}/cumulative_count_{datetime.now()}.xlsx')

    df_teens = merged.loc[merged['is_teen'] == 1]
    grps = df_teens.groupby(['mem_unique'])

    unit_dict_teens = dict.fromkeys(units, 0)
    blacklist = ['000', '503', '205', '204', '411', '309']
    unit_dict_teens['000'] = 0
    [unit_dict_teens.pop(key) for key in blacklist]
    unsorted = []
    for x in grps.groups:
        cur = grps.get_group(x)
        if cur.iloc[0]['used_tag'][:3] not in blacklist:
            prefix = cur.iloc[0]['used_tag'][:3]
            unit_dict_teens[prefix] = unit_dict_teens[prefix] + 1 
    print(f'\nCount of teens by site:\n\n')
    pprint(unit_dict_teens)
    df_teens.to_excel(f'{pth_out}/teens_{datetime.now()}.xlsx')
    counted_teens = get_dict_count(unit_dict_teens)
    num_teens = df_teens.shape[0]
    if counted_teens != num_teens:
        print(f'\n----------------------WARNING-----------------------------\nNot all teens were sorted!\n\nTotal number of teens: {num_teens}\nNumber of Counted teens: {counted_teens}\n\nList of teens not counted:\n{unsorted}\n----------------------WARNING-----------------------------\n')
    print(f'\nTotal Teens: {counted_teens}')

