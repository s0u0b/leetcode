import json
import re
from pathlib import Path

import requests

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
        self.problem = {}

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

    def set_problem_by_id(self, question_id):
        problem_slug = self.get_problem_slug_by_id(question_id)
        if problem_slug:
            self.problem = self.get_problem_by_slug(problem_slug)
        else:
            self.problem = None

    def escape(self, string):
        return string.replace(
            '\n', '').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace(
            '&quot;', '"').replace('&#39;', "'").replace('true', 'True').replace('false', 'False').replace(
            '\t', '    ').replace('null', 'None')

    @property
    def test_cases(self):
        problem_content = self.problem['content']
        inputs_and_output_list = re.findall(r'<strong>Input:</strong>(.*?)<strong>Output:</strong>(.*?)\n',
                                            problem_content,
                                            re.DOTALL)
        test_cases = ''
        for inputs_and_output in inputs_and_output_list:
            inputs, output = inputs_and_output
            inputs = self.escape(inputs)
            output = self.escape(output)
            test_cases += test_case_formatter.format(self.parse_input_test_case(inputs), self.parse_output_test_case(output))
        test_cases = 'tests = [' + test_cases + '\n]'
        return test_cases

    @property
    def python_snippet(self):
        code_snippets = self.problem['codeSnippets']
        for code_snippet in code_snippets:
            if code_snippet['langSlug'] == 'python3':
                return code_snippet['code']

    @property
    def python_code(self):
        code_snippet = self.python_snippet
        if 'List' in code_snippet:
            code_snippet = 'from typing import List\n\n\n' + code_snippet
        return code_snippet.replace('\t', '    ')

    @property
    def function_name(self):
        code_snippet = self.python_snippet
        code_snippet = re.split('class Solution:', code_snippet)[1]
        function_name = re.findall(r'def (\w+)', code_snippet)[-1]
        return function_name

    @property
    def parameter_names(self):
        problem_content = self.problem['content']
        inputs_and_output_list = re.findall(r'<strong>Input:</strong>(.*?)<strong>Output:</strong>(.*?)\n',
                                            problem_content,
                                            re.DOTALL)[0]

        inputs, output = inputs_and_output_list
        inputs = self.escape(inputs)
        parameter_names = self.parse_parameter_names(inputs)
        return parameter_names

    def parse_test_case_and_parameter_names(self, inputs):
        last_comma = last_equal = 0
        input_list = []
        parameter_list = []
        output_list = []
        for i, c in enumerate(inputs):
            if c == ',':
                if inputs[last_comma + 1:last_equal]:
                    parameter_list += [inputs[last_comma + 1:last_equal].strip()]
                last_comma = i
            if c == '=':
                if inputs[last_equal + 1:last_comma]:
                    input_list += [inputs[last_equal + 1:last_comma].strip()]
                    output_list += [inputs[last_equal + 1:last_comma].strip()]
                last_equal = i
        else:
            input_list += [inputs[last_equal + 1:].strip()]
            output_list += [inputs[last_equal + 1:].strip()]
            parameter_list += [inputs[last_comma + 1:last_equal].strip()]
        input_list = ', '.join(input_list)
        parameter_list = ', '.join(parameter_list)
        return {'input_list': input_list, 'parameter_list': parameter_list, 'output_list': output_list}

    def parse_output_test_case(self, outputs):
        output_test_case = self.parse_test_case_and_parameter_names(outputs)['output_list']
        if len(output_test_case) > 1:
            print(f'Multiple output example: {", ".join(output_test_case)}, pick first')
        return output_test_case[0]

    def parse_input_test_case(self, inputs):
        return self.parse_test_case_and_parameter_names(inputs)['input_list']

    def parse_parameter_names(self, inputs):
        return self.parse_test_case_and_parameter_names(inputs)['parameter_list']

    @property
    def file(self):
        question_frontend_id = self.problem['questionFrontendId'].rjust(5, '0')
        title_slug = self.problem['titleSlug'].replace('-', '_')
        file = '_'.join([question_frontend_id, title_slug])
        return 'a' + file + '.py'

    @property
    def difficulty(self):
        return self.problem['difficulty']

    @property
    def title(self):
        return self.problem['questionTitle']

    @property
    def frontend_id(self):
        return self.problem['questionFrontendId']

    @property
    def url(self):
        return self.problem['url']

    @property
    def topic_tags(self):
        topic_tags = self.problem['topicTags']
        tags = []
        for topic_tag in topic_tags:
            tags.append(topic_tag['name'])
        return ', '.join(tags)
