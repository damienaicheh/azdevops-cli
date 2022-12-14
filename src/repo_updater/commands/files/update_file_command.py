import os
import re
from src.repo_updater.commands.files.file_command import FileCommand
from src.repo_updater.commands.files.file_command_args import FileCommandArgs
from src.repo_updater.exceptions.repo_updater_exception import RepoUpdaterException

class UpdateFileCommand(FileCommand):

    def __init__(self, logger):
        """initializes a new instance of the class"""
        super().__init__(logger)

    def get_target_path(self, args: FileCommandArgs) -> str:
        target_path = None
        if 'target_path' in args.action.update._fields:
            target_path = args.action.update.target_path
        if not target_path or target_path.strip() == '':
            raise RepoUpdaterException('The target path is required on Update File Action.')
        return os.path.join(
            args.output, 
            args.repository.name,
            target_path
        )

    def get_pattern_regex(self, args: FileCommandArgs) -> str:
        pattern_regex = None
        if 'regex' in args.action.update.pattern._fields:
            pattern_regex = args.action.update.pattern.regex
        if (not pattern_regex or pattern_regex.strip() == ''):
            raise RepoUpdaterException('The pattern regex is required on Update File Action.')
        return pattern_regex

    def get_pattern_group_name(self, args: FileCommandArgs) -> str:
        pattern_group_name = 'replace'
        if 'group_name' in args.action.update.pattern._fields:
            pattern_group_name = str(args.action.update.pattern.group_name)
        if (not pattern_group_name or pattern_group_name.strip() == ''):
            raise RepoUpdaterException('The pattern group name is required on Update File Action.')
        return pattern_group_name

    def get_pattern_ignore_case(self, args: FileCommandArgs):
        ignore_case = None
        if 'ignore_case' in args.action.update.pattern._fields:
            ignore_case = args.action.update.pattern.ignore_case
        return re.IGNORECASE if ignore_case else 0

    def get_mode(self, args: FileCommandArgs):
        if 'mode' in args.action.update._fields:
            if not re.match(f'(at-beginning|at-the-end|delete|insert-after|insert-before|replace-with)', args.action.update.mode):
                raise RepoUpdaterException(f'The mode \'{args.action.update.mode}\' is invalid on Update File Action. possible values :at-beginning,at-the-end,delete,insert-after,insert-before,replace-with')
            return args.action.update.mode
        return 'replace'
    
    def _on_execute(self, args: FileCommandArgs) -> bool:
        """Update the files of a repository based on a regex"""
        target_path = self.get_target_path(args)
        target_path_tmp = '{}.tmp'.format(target_path)
        mode = self.get_mode(args)
        pattern_regex = None
        pattern_ignore_case = 0
        pattern_group_name = None
        processed = False
        if mode != 'at-beginning' and mode != 'at-the-end':
            pattern_regex = self.get_pattern_regex(args)
            pattern_ignore_case = self.get_pattern_ignore_case(args)
            pattern_group_name = self.get_pattern_group_name(args)
        value = args.action.update.value
        if os.path.exists(target_path) and os.path.isfile(target_path):
            with open(target_path, 'r') as read_file:
                with open(target_path_tmp, 'w') as write_file:
                    result = ''
                    if mode == 'at-beginning':
                        result += value + '\n'
                        processed = True
                    lines = read_file.readlines()
                    nb_line = 0
                    for line in lines:
                        nb_line = nb_line + 1
                        regex_result = re.search(pattern_regex, line, pattern_ignore_case) if pattern_regex else None
                        if regex_result:
                            if mode == 'delete':
                                processed = True
                            if mode == 'insert-after':
                                result += line
                                result += value + '\n'
                                processed = True
                            elif mode == 'insert-before':
                                result += value + '\n'
                                result += line
                                processed = True
                            elif mode == 'replace-with':
                                result += line.replace(regex_result.group(pattern_group_name), value)
                                processed = True
                        else:
                            result += line
                    if mode == 'at-the-end':
                        result = result.strip()+ '\n' + value
                        processed = True  
                    write_file.write(result.strip())
                os.remove(target_path)
                os.rename(target_path_tmp, target_path)
        return processed