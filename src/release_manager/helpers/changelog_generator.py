import git
import os
import re
from typing import List

regex_type = '(?P<type>(feat|fix|feat!|refactor|chore)):'
regex_commit = '\s+(?P<type>(.*?):)?(?P<message>(.*))\|(?P<date>.*)'

def process_commit_date(commit: str) -> str:
    result = ''
    regex_result = re.search(regex_commit, commit)
    if regex_result != None:
            result += regex_result.group('date')
    return result

def process_commit_message(commits_filtered) -> str:
    result = ''
    for key in commits_filtered:
        result += f'### {key} \n'
        for line in commits_filtered[key]:
            regex_result = re.search(regex_commit, line)
            if regex_result != None:
                result += f"- {regex_result.group('message')}\n"
        result += '\n'         
    return result

def add_to_dict(commits_filtered: dict, key: str, value: str) -> dict:
    if not key in commits_filtered:
        commits_filtered[key] = []
    
    commits_filtered[key].append(value)

    return commits_filtered

def process_commits(lines: List[str]) -> dict:
    commits_filtered = {}
    for line in lines:
        regex_result = re.search(regex_type, line)
        if regex_result != None:
            commit_type = regex_result.group('type')
            if (commit_type == 'feat'):
                commits_filtered = add_to_dict(commits_filtered, 'Features', line)
            elif (commit_type == 'fix'):        
                commits_filtered = add_to_dict(commits_filtered, 'Fixes', line)
            elif (commit_type == 'feat!'):        
                commits_filtered = add_to_dict(commits_filtered, 'Breaking Changes', line)
            elif (commit_type == 'docs'):        
                commits_filtered = add_to_dict(commits_filtered, 'Docs', line)
            elif (commit_type == 'chore'):        
                commits_filtered = add_to_dict(commits_filtered, 'Chore', line)   
            else:
                commits_filtered = add_to_dict(commits_filtered, 'Others', line)
        else:
            commits_filtered = add_to_dict(commits_filtered, 'Others', line)
    
    return commits_filtered

def generate_changelog(project_path: str, output: str):
    git_client = git.Git(project_path if project_path != None else os.path)
    
    tags = git_client.tag(l=True, sort='-version:refname', merge=True).split('\n')

    if len(tags):
        index = 0
        latest_tag = tags[0].strip()
        initial_commit = git_client.rev_list('--max-parents=0', 'HEAD')
        with open(os.path.join(output, 'CHANGELOG.md'), 'w') as file:
            result = '# Changelog\n'
            result += 'All notable changes to this project will be documented in this file.\n\n'
            
            for index, tag in enumerate(tags):
                current_index = index + 1
                if((current_index) < len(tags)):
                    previous_tag = tags[current_index].strip()
                else:
                    previous_tag = initial_commit
                
                logs = git_client.log('--date=short',  "--pretty=format:%s | %cd", f'{previous_tag}..{latest_tag}').split('\n')
                print(logs)
                if len(logs) and logs[0] != '':
                    result += f'## [{latest_tag}] - {process_commit_date(logs[0])}\n\n'

                    commits_filtered = process_commits(logs)
                    result += process_commit_message(commits_filtered)
                
                if((current_index) < len(tags)):
                    latest_tag = tags[current_index].strip()

            file.write(result)