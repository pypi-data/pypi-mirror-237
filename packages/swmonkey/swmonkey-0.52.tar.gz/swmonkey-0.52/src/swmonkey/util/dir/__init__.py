import os
import time

def get_out_dir():
    '''
    返回一个输出目录，如果用户定义了环境变量LOG_PATH，则使用用户定义的路径
    '''
    user_defined_path = os.getenv('LOG_PATH')
    if user_defined_path is not None:
        return user_defined_path
    start_time = time.time()
    if os.environ.get('START_TIME') is not None:
        start_time = float(os.environ.get('START_TIME'))

    timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(start_time))
    home_dir = os.path.expanduser('~')
    app_dir = os.path.join(home_dir, '.swmonkey')
    out_dir = os.path.join(app_dir, timestamp)
    # if out_dir does not exist, create it
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    return out_dir