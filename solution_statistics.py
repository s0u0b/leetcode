import os
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path
from pprint import pprint

from mdprint import mdprint_list, mdprint


def main():
    solution_list = []

    for file in os.listdir('solutions'):
        if file.startswith('a') and file.endswith(".py"):
            solution_list.append(file)
    table_head = ['ID', 'Problem', 'Difficulty', 'Solution']
    solution_table = [table_head, ]
    difficulty_statistic = {}
    solution_id = []
    solution_tags = {}
    for solution in solution_list:
        with open(r'solutions/' + solution, 'r', encoding="utf-8") as f:
            solution_data = {
                'file': r'solutions/' + solution,
            }
            for line in f:
                if 'Problem' in line:
                    solution_data['ID'], solution_data['Problem'] = re.split(r'\.', f.readline())
                if 'Difficulty' in line:
                    solution_data['Difficulty'] = f.readline().strip()
                if 'URL' in line:
                    solution_data['URL'] = f.readline()
                if 'Tags' in line:
                    solution_data['Tags'] = f.readline()
                    break
            solution_data = {key: value.strip() for (key, value) in solution_data.items()}
            if solution_data['Difficulty'] not in difficulty_statistic.keys():
                difficulty_statistic[solution_data['Difficulty']] = 1
            else:
                difficulty_statistic[solution_data['Difficulty']] += 1
            if solution_data['ID'] not in solution_id:
                tags = [tag.strip() for tag in solution_data['Tags'].split(',')]
                for tag in tags:
                    if tag not in solution_tags.keys():
                        solution_tags[tag] = 1
                    else:
                        solution_tags[tag] += 1
                solution_id.append(solution_data['ID'])
                solution_table.append(
                    [
                        solution_data['ID'],
                        f'[{solution_data["Problem"]}]({solution_data["URL"]})',
                        solution_data['Difficulty'],
                        f'[{solution}]({solution_data["file"]})',
                    ]
                )
            else:
                for i, solution_statistic in enumerate(solution_table):
                    if solution_statistic[0] == solution_data['ID']:
                        solution_statistic[3] += f'<br>[{solution}]({solution_data["file"]})'
                        break
    total = sum([solution_statistic for solution_statistic in difficulty_statistic.values()])
    difficulty_statistic['Total'] = total
    statistic_shields = []
    difficulty_color = {'Easy': 'success', 'Medium': 'important', 'Hard': 'critical', 'Total': 'inactive'}
    for difficulty, statistic in difficulty_statistic.items():
        statistic_shields += [
            f'![](https://img.shields.io/badge/{difficulty}-{statistic}-{difficulty_color[difficulty]})']
    statistic_shields = ' '.join(statistic_shields)
    with open('README.md', 'w') as readme:
        mdprint('My leetcode solutions', heading=2, file=readme)
        mdprint(statistic_shields, file=readme)
        mdprint('<br>', file=readme)
        mdprint_list(solution_table, file=readme)


if __name__ == '__main__':
    main()
