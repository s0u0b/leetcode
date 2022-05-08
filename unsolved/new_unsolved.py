import argparse
from pathlib import Path
import sys

sys.path.append('..')
from crawler.crawler import Crawler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('problem_id', help='question frontend id', type=int)
    parser.add_argument("-v", "--version", help='another solution')
    parser.add_argument("-va", "--validator", action='count', help='validator')
    args = parser.parse_args()
    problem_id = args.problem_id

    with Crawler() as crawler:
        problem = crawler.get_problem_by_id(problem_id)
        if problem:
            file = crawler.get_file_name(problem)
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
                question_frontend_id = crawler.get_frontend_id(problem)
                question_title = crawler.get_title(problem)
                difficulty = crawler.get_difficulty(problem)
                url = crawler.get_url(problem)
                topic_tags = crawler.get_topic_tags(problem)
                code = crawler.get_python_code(problem)
                test_cases = crawler.get_test_cases(problem)
                print('"""', file=file)
                print(f'Problem:\n'
                      f'    {question_frontend_id}. {question_title}\n'
                      f'Difficulty:\n'
                      f'    {difficulty}\n'
                      f'URL:\n'
                      f'    {url}\n'
                      f'Tags:\n'
                      f'    {topic_tags}\n'
                      f'"""\n'
                      f'\n'
                      f'\n'
                      f'{code}\n'
                      f'\n'
                      f'\n'
                      f'{test_cases}\n'
                      f'\n', file=file)
                if args.validator:
                    function_name = crawler.get_function_name(problem)
                    parameter_names = crawler.get_parameter_names(problem)
                    print(f'def validator({function_name}, inputs, expected):\n'
                          f'    {parameter_names} = inputs\n'
                          f'    output = {function_name}({parameter_names})\n'
                          f'    assert output == expected, (output, expected)\n'
                          f'\n', file=file)


if __name__ == '__main__':
    main()
