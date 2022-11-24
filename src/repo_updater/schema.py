Schema = {
    'project': {
        'required': True,
        'empty': False,
        'type': 'dict',
        'schema': {
            'name' :{
                'required': True,
                'type': 'string',
                'maxlength': 254
            }
        }
    },
    'pull_request': {
        'required': True,
        'empty': False,
        'type': 'dict',
        'schema': {
            'name' :{
                'required': True,
                'type': 'string',
                'maxlength': 254
            },
            'branch' :{
                'required': True,
                'type': 'string',
                'maxlength': 254
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
                'type': 'string',
                'maxlength': 254
            },
            'pattern' :{
                'required': True,
                'empty': False,
                'type': 'string',
                'maxlength': 254
            },
            'ignore_case' :{
                'type': 'boolean'
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
        'schema': {
            'type': 'dict', 
            'schema': {
                'name' : {
                    'regex': '^(add|update|delete)$',
                    'required': True,
                    'type': 'string'
                },
                'files': {
                    'required': True,
                    'type': 'list',
                    'schema': {
                        'type': 'dict', 
                        'schema': {
                            'name' : {
                                'required': True,
                                'type': 'string',
                                'maxlength': 254
                            },
                            'pattern' : {
                                'type': 'string',
                                'maxlength': 254
                            },
                            'search' : {
                                'regex': '^(before|after|replace)$',
                                'type': 'string'
                            },
                            'value' : {
                                'type': 'string',
                                'required': True,
                            },
                            'ignore_case' : {
                                'type': 'boolean'
                            }
                        }
                    }
                }
            }
        }
    }
}