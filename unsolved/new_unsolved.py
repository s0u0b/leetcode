import argparse
from pathlib import Path
import sys
sys.path.append('..')
from crawler.crawler import Crawler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('problem_id', help='question frontend id', type=int)
    parser.add_argument("-v", "--version", help='another solution')
    args = parser.parse_args()
    problem_id = args.problem_id

    with Crawler() as crawler:
        problem = crawler.get_problem_by_id(problem_id)
        if problem:
            file_name = crawler.get_file_name(problem)
            if args.version:
                file_name = file_name.replace('.py', '_' + args.version + '.py')
            if Path('', file_name).exists():
                print(f'Unsolved file {file_name} exist')
                return
            if Path('../solutions', file_name).exists():
                print(f'Solution {file_name} exist')
                return
            else:
                file_path = Path('', file_name)
                file_path.touch(exist_ok=True)
                print(f'Create {file_path} successfully')

            with open(file_path, 'w') as file:
                print('"""', file=file)
                question_frontend_id = crawler.get_frontend_id(problem)
                question_title = crawler.get_title(problem)
                print(f'Problem:\n    {question_frontend_id}. {question_title}', file=file)
                difficulty = crawler.get_difficulty(problem)
                print(f'Difficulty:\n    {difficulty}', file=file)
                url = crawler.get_url(problem)
                print(f'URL:\n    {url}', file=file)
                print('"""', file=file)
                code = crawler.get_python_code(problem)
                print(code, file=file)
                test_cases = crawler.get_test_cases(problem)
                print(test_cases, file=file)


if __name__ == '__main__':
    main()
