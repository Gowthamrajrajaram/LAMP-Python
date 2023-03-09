from configparser import ConfigParser
config=ConfigParser()
config.read('configparser.ini')
print(config.sections())
print(list(config.sections()))
print(config('client'))
# config['account']
print(config.get['account']['id'])
