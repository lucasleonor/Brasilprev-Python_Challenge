import os
import yaml

__config_path = os.environ['CONFIG_FILE']
with open(__config_path) as file:
    __data = yaml.load(file, Loader=yaml.FullLoader)

app_prefix = __data['app_prefix']
cors = __data.get('cors')

__db: dict = __data['db']
db_url: str = __db.get('url')
if db_url is None:
    db_url = __db['uri_pattern']
    # if __db.get('pass'):
    #     __db['pass'] = crypto_service.decrypt(__db['pass'])
    db_url.format(**__db)
