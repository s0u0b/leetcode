import argparse
from pathlib import Path
import sys

sys.path.append('..')
from crawler.crawler import Crawler

solution_formatter = '''"""
Problem:
    {frontend_id}. {title}
Difficulty:
    {difficulty}
URL:
    {url}
Tags:
    {topic_tags}
"""
{code}


{test_cases}
'''

validator_formatter = """
def validator({function_name}, inputs, expected):
    {parameter_names} = inputs
    output = {function_name}({parameter_names})
    assert output == expected, (output, expected)

"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('problem_id', help='question frontend id', type=int)
    parser.add_argument("-v", "--version", help='another solution')
    parser.add_argument("-va", "--validator", action='count', help='validator')

    args = parser.parse_args()
    problem_id = args.problem_id

    with Crawler() as crawler:
        crawler.set_problem_by_id(problem_id)
        if crawler.problem:
            file = crawler.file_name
            if args.version:
                file = file.replace('.py', f'_{args.version}.py')
            file = Path(file)

            if file.exists():
                print(f'Unsolved file {file} exist')
                return
            if Path('../solutions', file).exists():
                print(f'Solution {file} exist')
                return
            file.touch(exist_ok=True)
            print(f'Create {file} successfully')

            with open(file, 'w') as file:
                print(solution_formatter.format(
                    frontend_id=crawler.frontend_id,
                    title=crawler.title,
                    difficulty=crawler.difficulty,
                    url=crawler.url,
                    topic_tags=crawler.topic_tags,
                    code=crawler.python_code,
                    test_cases=crawler.test_cases,
                ), file=file)
                if args.validator:
                    function_name = crawler.function_name
                    parameter_names = crawler.parameter_names
                    print(validator_formatter.format(
                        function_name=function_name,
                        parameter_names=parameter_names,
                    ), file=file)


if __name__ == '__main__':
    main()
