# pip install --no-index --find-links=https://pypi.org/simple/ lyysdk
#https://pypi.org/project/lyysdk/#description
#pip install lyypy -i https://pypi.org/simple/ --trusted-host pypi.org --upgrade
"""
python setup.py sdist bdist_wheel
twine upload dist/*
pip install --upgrade lyysdk -i https://pypi.org/simple/ --trusted-host pypi.org
"""
import time
import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
"""



"""


def lyydebug(debug, text):
    get_fun_name_cmd_text = "fun_name=str(sys._getframe().f_code.co_name)"
    fun_name = ""
    try:
        eval(get_fun_name_cmd_text)
    except Exception as e:
        print(e)
    out_txt = ("[" + fun_name + "]:" + text)
    print(out_txt)
    return out_txt


def divide_list(lst, n):
    quotient = len(lst) // n
    remainder = len(lst) % n
    result = []
    start = 0
    for i in range(n):
        if i < remainder:
            end = start + quotient + 1
        else:
            end = start + quotient
        result.append(lst[start:end])
        start = end
    return result


def get_time(f):

    def inner(*arg, **kwarg):
        s_time = time.time()
        res = f(*arg, **kwarg)
        e_time = time.time()
        print("\n<" + f.__name__ + "> 耗时：" + str(e_time - s_time))
        return res

    return inner


def 测速(开始时间, 额外说明):
    spend = datetime.now() - 开始时间
    print("\n<-" + 额外说明 + "-> 耗时: {}秒".format(spend))
    return spend


class CustomTimedRotatingFileHandler(TimedRotatingFileHandler):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def lyyf_logger(log_filename_prefix, message, if_print=False):
    """
    可以每次调用，都会自动创建当天的日志文件，日志文件名为lyylog_前缀_日期.log
    比如lyylog_lyymsg_svc_log_2023-08-24.log
    不再被占用，可以实时删除
    基本完美了
    Args:
        log_filename_prefix (_type_): _description_
        message (_type_): _description_
    """

    if if_print:
        print(message)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = None

    if handler is None:
        today = datetime.now().strftime("%Y-%m-%d")
        handler = CustomTimedRotatingFileHandler(f'lyylog_{log_filename_prefix}_{today}.log', when='midnight', interval=1, backupCount=7)
        handler.suffix = "%Y-%m-%d"
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s', "%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    with handler:
        logger.info(message)


if __name__ == "__main__":
    pass