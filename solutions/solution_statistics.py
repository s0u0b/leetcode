import os
import re
from pathlib import Path
from pprint import pprint
from datetime import datetime, timezone, timedelta

from mdprint import mdprint_list, mdprint_dict, mdprint


def main():
    solution_list = []
    path_dir = os.path.basename(os.getcwd()) + '/'

    for file in os.listdir():
        if file.startswith('a') and file.endswith(".py"):
            solution_list.append(file)
    difficulty = {'Easy': 'green', 'Medium': 'orange', 'Hard': 'red', }
    table_head = ['ID', 'Problem', 'Difficulty', 'Solution', 'Date']
    solution_table = [table_head, ]
    solution_statistics = {}
    solution_id = []
    for solution in solution_list:
        with open(solution, 'r', encoding="utf-8") as f:
            stat_result = Path(solution).stat()
            modified = datetime.fromtimestamp(stat_result.st_mtime, tz=timezone(timedelta(hours=+8))).strftime(
                '%Y-%m-%d')
            solution_data = {
                'file': path_dir + solution,
                'date': modified
            }
            for line in f:
                if 'Problem' in line:
                    solution_data['ID'], solution_data['Problem'] = re.split(r'\.', f.readline())
                if 'Difficulty' in line:
                    solution_data['Difficulty'] = f.readline().strip()
                    solution_data['Difficulty'] = '<font color={}>{}</font>'.format(
                        difficulty[solution_data["Difficulty"]],
                        solution_data["Difficulty"])
                if 'URL' in line:
                    solution_data['URL'] = f.readline()
                    break
            solution_data = {key: value.strip() for (key, value) in solution_data.items()}
            if solution_data['Difficulty'] not in solution_statistics.keys():
                solution_statistics[solution_data['Difficulty']] = 1
            else:
                solution_statistics[solution_data['Difficulty']] += 1
            if solution_data['ID'] not in solution_id:
                solution_id.append(solution_data['ID'])
                solution_table.append(
                    [
                        solution_data['ID'],
                        f'[{solution_data["Problem"]}]({solution_data["URL"]})',
                        solution_data['Difficulty'],
                        f'[{solution}]({solution_data["file"]})',
                        solution_data["date"],
                    ]
                )
            else:
                for i, solution_statistic in enumerate(solution_table):
                    if solution_statistic[0] == solution_data['ID']:
                        solution_statistic[3] += f'<br>[{solution}]({solution_data["file"]})'
                        solution_statistic[4] += f'<br>{solution_data["date"]}'
                        break
    total = sum([solution_statistic for solution_statistic in solution_statistics.values()])
    solution_statistics['Total'] = total
    solution_statistics = [['Difficulty', 'Solved']] + [[key, value] for (key, value) in
                                                        solution_statistics.items()]
    with open('../README.md', 'w') as readme:
        mdprint('My leetcode solutions', heading=2, file=readme)
        mdprint_list(solution_statistics, file=readme)
        mdprint_list(solution_table, file=readme)


if __name__ == '__main__':
    main()
