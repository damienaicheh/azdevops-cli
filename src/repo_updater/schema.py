Add = {
    'type': 'dict',
    'schema': {
        'add': {
            'type': 'dict',
            'schema': {
                'asset_path' : {
                    'required': True,
                    'type': 'string',
                },
                'target_path' : {
                    'required': True,
                    'type': 'string',
                },
                'ignore_case' :{
                    'type': 'boolean'
                }
            }
        }
    }
}

Delete = {
    'type': 'dict',
    'schema': {
        'delete': {
            'type': 'dict',
            'schema': {
                'source_path' : {
                    'required': True,
                    'type': 'string',
                }
            }
        }
    }
}

Update = {
    'type': 'dict',
    'schema': {
        'update': {
            'type': 'dict',
            'schema': {
                'target_path' : {
                    'required': True,
                    'type': 'string',
                },
                'pattern': {
                    'type': 'dict',
                    'schema': {
                        'regex' :{
                            'required': True,
                            'type': 'string'
                        },
                        'ignore_case' :{
                            'type': 'boolean'
                        }
                    }
                },
                'mode' : {
                    'regex': '^(insert-before|insert-after|replace-with|delete|at-beginning|at-the-end)$',
                    'type': 'string',
                },
                'value' : {
                    'required': True,
                    'type': 'string',
                }
            }
        }
    }
}

Schema = {
    'project': {
        'required': True,
        'empty': False,
        'type': 'dict',
        'schema': {
            'name' :{
                'required': True,
                'type': 'string'
            },
        }
    },
    'pull_request': {
        'required': True,
        'empty': False,
        'type': 'dict',
        'schema': {
            'name' :{
                'required': True,
                'type': 'string'
            },
            'branch' :{
                'required': True,
                'type': 'string'
            }
        }
    },
    'repository': {
        'required': True,
        'empty': False,
        'type': 'dict',
        'schema': {
            'default_branch' :{
                'required': True,
                'empty': False,
                'type': 'string'
            },
            'pattern': {
                'type': 'dict',
                'schema': {
                    'regex' :{
                        'required': True,
                        'type': 'string'
                    },
                    'ignore_case' :{
                        'type': 'boolean'
                    }
                }
            }
        }
    },
    'assets_directory' :{
        'type': 'string',
        'empty': False,
    },
    'actions': {
        'required': True,
        'type': 'list',
        'anyof_schema': [
            Add, 
            Delete,
            Update
        ]
    }
}