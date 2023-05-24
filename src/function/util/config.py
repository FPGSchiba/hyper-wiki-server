import os
import yaml


def get_data_dir():
    while 'src' not in os.listdir('.'):
        os.chdir('..')
    if 'data' in os.listdir('.'):
        return os.path.join(os.getcwd(), 'data')
    else:
        raise FileNotFoundError('Could not find data directory!')


class Config:
    def __init__(self):
        self.data_dir = get_data_dir()
        with open(os.path.join(self.data_dir, 'config.yaml'), 'r+', encoding='utf-8') as config_file:
            data = yaml.load(config_file, yaml.Loader)
        for key in data:
            if type(data[key]) == dict:
                self.load_data(data[key], key)
            else:
                setattr(self, key, data[key])

    def load_data(self, data, prevKey):
        for key in data:
            if type(data[key]) == dict:
                self.load_data(data[key], f'{prevKey}_{key}')
            else:
                if type(data[key]) == str:
                    setattr(self, f'{prevKey}_{key}', data[key].replace('{data-dir}', self.data_dir))
                else:
                    setattr(self, f'{prevKey}_{key}', data[key])
