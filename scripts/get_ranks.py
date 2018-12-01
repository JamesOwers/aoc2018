#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 05:46:57 2017

@author: kungfujam
"""
import json
import pandas as pd
from collections import defaultdict
import requests
import sys
#from tabulate import tabulate


SESSION = '53616c7465645f5fe926c66dd23945dc581ba7ae0a70847d939e7069709e002ccf631901d6f0c925c7b82b6456cf46a4'  # get from the browser
PROJECT_HOME = '/Users/kungfujam/git/aoc2017'
LEADER_URL = 'https://adventofcode.com/2017/leaderboard/private/view/222021.json'


def load_leaderboard():
    try:
        with open('{}/leaderboard.json'.format(PROJECT_HOME)) as f:
            f_str = f.read().replace('\r\n', '').replace('\n', '')
            leaderboard = json.loads(f_str)
        print('Read local json...\n\n')
    except:
        resp = requests.get('{}'.format(LEADER_URL),
                            cookies = {'session': SESSION})
        leaderboard = json.loads(resp.text)
        with open('{}/leaderboard.json'.format(PROJECT_HOME), 'w') as f:
            json.dump(leaderboard, f)
        print('Downloaded json from website...\n\n')
    return leaderboard


def get_day_times(leaderboard, days):
    day_times = defaultdict(dict)
    for member_id in leaderboard['members']:
        name = leaderboard['members'][member_id]['name']
        times = leaderboard['members'][member_id]['completion_day_level']
        for day in days:
            if day in times:
                tt = {star: times[day][star]['get_star_ts']
                      for star in times[day]}
                day_times[int(day)][name] = tt
    return day_times


def day_times_df(day_times):
    reform = {(outerKey, innerKey): values 
              for outerKey, innerDict in day_times.iteritems() 
              for innerKey, values in innerDict.iteritems()}
    df = pd.DataFrame.from_dict(reform)
    df = df.stack(0)  # bring star nr from col to index
    df = df.swaplevel(0, 1)  # swap day and star nr index
    df.index.rename(('Day', 'Star Nr'), inplace=True)
    df.columns.name = 'Name'
    return df.sort_index()


def load_days(days=None):
    leaderboard = load_leaderboard()
    if days is None:
        days = [str(ii) for ii in range(1, 26)]
    elif not isinstance(days, list):
        days = [days]
    day_times = get_day_times(leaderboard, days)
    for day in days:
        pass 
    return day_times    
    

def main(days=None):
    day_times = load_days(days)
    df = day_times_df(day_times)
#    print(tabulate(df, headers='keys', tablefmt='psql'))
    print(df)
    return df   
    
    
if __name__ == '__main__':
    args = sys.argv
    df = main(days=args)