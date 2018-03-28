'''
type_map = {'int': int,
            'str': str,
            'bool': (lambda x: (x in {'True', 'true'})),
            'bytes': (lambda x: str(x).encode())}

yaml = YAML()
with open('./matchpuller/env-settings.yaml', 'r') as f:
    env_settings = yaml.load(f)

logger.debug(env_settings)

for var in env_settings['environment']:
    name = var['name']
    t = var['type']
    default = var.get('default')
    exec_str = name + ' = env.get(' + name + ', type=' + (t if t != 'bytes' else 'str')
    if default:
        exec_str += ', default=' + str(default)
    exec_str += ')'
    if t == 'bytes':
        exec_str += '.encode()'
    exec(exec_str)
    logger.debug('initialized %s with default=%s and value=%s', name, type_map[t](default), locals()[name])
'''