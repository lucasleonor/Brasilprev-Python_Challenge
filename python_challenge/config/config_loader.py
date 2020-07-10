import os
import yaml

__config_path = os.environ['CONFIG_FILE']
with open(__config_path) as file:
    __data = yaml.load(file, Loader=yaml.FullLoader)

app_prefix = __data['app_prefix']
cors = __data.get('cors')
