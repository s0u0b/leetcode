import json
import re
import requests
from pathlib import Path

test_case_formatter = '''
    (
        ({},
        ),
        {},
    ),'''


class Crawler:
    def __init__(self):
        self.user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (HTML, like Gecko) ' \
                          r'Chrome/44.0.2403.157 Safari/537.36 '

    def __enter__(self):
        self.session = requests.Session()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.session.close()

    def get_problem_by_slug(self, slug):
        url = "https://leetcode.com/graphql"
        params = {
            'operationName': "getQuestionDetail",
            'variables': {'titleSlug': slug},
            'query':
                '''query getQuestionDetail($titleSlug: String!) {
                    question(titleSlug: $titleSlug) {
                        questionFrontendId
                        questionTitle
                        titleSlug
                        content
                        difficulty
                        codeSnippets {
                            langSlug
                            code
                        }
                        topicTags {
                            name
                        }
                    }
                }'''
        }
        json_data = json.dumps(params).encode('utf8')
        headers = {
            'User-Agent': self.user_agent,
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Referer': 'https://leetcode.com/problems/' + slug
        }
        resp = self.session.post(url, data=json_data, headers=headers, timeout=10)
        content = resp.json()
        question = content['data']['question']
        question['url'] = 'https://leetcode.com/problems/' + slug
        return question

    def update_local_problem_json(self):
        print('Download problems.json')
        url = "https://leetcode.com/api/problems/all/"
        headers = {'User-Agent': self.user_agent, 'Connection': 'keep-alive'}
        resp = self.session.get(url, headers=headers, timeout=10)
        question_list = json.loads(resp.content.decode('utf-8'))
        with open('../problems.json', 'w', encoding='utf-8') as f:
            json.dump(question_list, f, ensure_ascii=False, indent=4)

    def get_problem_slug_by_id(self, question_id, update_if_not_exist=True):
        if not Path('../problems.json').exists():
            print("Can't found problems.json, download it")
            self.update_local_problem_json()
            update_if_not_exist = False
        with open('../problems.json', 'r', encoding='utf-8') as f:
            question_list = json.load(f)

        stat_status_pairs = question_list['stat_status_pairs']
        for question in stat_status_pairs:
            if question_id == question['stat']['frontend_question_id']:
                if question['paid_only']:
                    print('Paid problem')
                    return None
                return question['stat']['question__title_slug']
        if update_if_not_exist:
            print("Can't found question id in problems.json, download it again")
            self.update_local_problem_json()
            print('Try to find again')
            self.get_problem_slug_by_id(question_id, update_if_not_exist=False)
        else:
            print('Question id not found')
            return None

    def get_problem_by_id(self, question_id):
        problem_slug = self.get_problem_slug_by_id(question_id)
        if problem_slug:
            return self.get_problem_by_slug(problem_slug)
        else:
            return None

    def parse_inputs(self, inputs):
        last_comma = 0
        last_equal = 0
        input_list = []
        for i, c in enumerate(inputs):
            if c == ',':
                last_comma = i
            if c == '=':
                if inputs[last_equal + 1:last_comma]:
                    input_list += [inputs[last_equal + 1:last_comma].strip()]
                last_equal = i
        else:
            input_list += [inputs[last_equal + 1:].strip()]
        return ', '.join(input_list)

    def escape(self, string):
        return string.replace('\n', '').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace(
            '&quot;', '"').replace('&#39;', "'").replace('true', 'True').replace('false', 'False').replace('\t', '    ')

    def get_test_cases(self, problem):
        problem_content = problem['content']
        inputs_and_output_list = re.findall(r'<strong>Input:</strong>(.*?)<strong>Output:</strong>(.*?)\n',
                                            problem_content,
                                            re.DOTALL)
        test_cases = ''
        for inputs_and_output in inputs_and_output_list:
            inputs, output = inputs_and_output
            inputs = self.escape(inputs)
            output = self.escape(output)
            test_cases += test_case_formatter.format(self.parse_inputs(inputs), output)
        test_cases = 'tests = [' + test_cases + '\n]'
        return test_cases

    def get_python_code(self, problem):
        code_snippets = problem['codeSnippets']
        for code_snippet in code_snippets:
            if code_snippet['langSlug'] == 'python3':
                if 'List' in code_snippet['code']:
                    code_snippet['code'] = 'from typing import List\n\n\n' + code_snippet['code']
                return code_snippet['code'].replace('\t', '    ')

    def get_file_name(self, problem):
        question_frontend_id = problem['questionFrontendId'].rjust(5, '0')
        title_slug = problem['titleSlug'].replace('-', '_')
        file_name = '_'.join([question_frontend_id, title_slug])
        return 'a' + file_name + '.py'

    def get_difficulty(self, problem):
        return problem['difficulty']

    def get_title(self, problem):
        return problem['questionTitle']

    def get_frontend_id(self, problem):
        return problem['questionFrontendId']

    def get_url(self, problem):
        return problem['url']

    def get_topic_tags(self, problem):
        topic_tags = problem['topicTags']
        tags = []
        for topic_tag in topic_tags:
            tags.append(topic_tag['name'])
        return ', '.join(tags)
