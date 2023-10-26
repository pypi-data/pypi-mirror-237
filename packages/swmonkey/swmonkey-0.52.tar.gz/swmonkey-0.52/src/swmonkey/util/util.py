import os
import time
import subprocess
import psutil
from swmonkey.log import logger

KEY_NAMES = [
    "\t",
    "\n",
    "\r",
    " ",
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "{",
    "|",
    "}",
    "~",
    "accept",
    "add",
    "alt",
    "altleft",
    "altright",
    "apps",
    "backspace",
    "browserback",
    "browserfavorites",
    "browserforward",
    "browserhome",
    "browserrefresh",
    "browsersearch",
    "browserstop",
    "capslock",
    "clear",
    "convert",
    "ctrl",
    "ctrlleft",
    "ctrlright",
    "decimal",
    "del",
    "delete",
    "divide",
    "down",
    "end",
    "enter",
    "esc",
    "escape",
    "execute",
    "f1",
    "f10",
    "f11",
    "f12",
    "f13",
    "f14",
    "f15",
    "f16",
    "f17",
    "f18",
    "f19",
    "f2",
    "f20",
    "f21",
    "f22",
    "f23",
    "f24",
    "f3",
    "f4",
    "f5",
    "f6",
    "f7",
    "f8",
    "f9",
    "final",
    "fn",
    "hanguel",
    "hangul",
    "hanja",
    "help",
    "home",
    "insert",
    "junja",
    "kana",
    "kanji",
    "launchapp1",
    "launchapp2",
    "launchmail",
    "launchmediaselect",
    "left",
    "modechange",
    "multiply",
    "nexttrack",
    "nonconvert",
    "num0",
    "num1",
    "num2",
    "num3",
    "num4",
    "num5",
    "num6",
    "num7",
    "num8",
    "num9",
    "numlock",
    "pagedown",
    "pageup",
    "pause",
    "pgdn",
    "pgup",
    "playpause",
    "prevtrack",
    "print",
    "printscreen",
    "prntscrn",
    "prtsc",
    "prtscr",
    "return",
    "right",
    "scrolllock",
    "select",
    "separator",
    "shift",
    "shiftleft",
    "shiftright",
    "sleep",
    "space",
    "stop",
    "subtract",
    "tab",
    "up",
    "volumedown",
    "volumemute",
    "volumeup",
    "win",
    "winleft",
    "winright",
    "yen",
    "command",
    "option",
    "optionleft",
    "optionright",
]



def run_command(sudo=False, cmd=None, passwd=None):
    if sudo:
        cmd = f'sudo -S {cmd}'
    subprocess.run(f'echo {passwd} | {cmd}', shell=True)


def count_process_instances(process_name):
    count = 0
    try:
        for process in psutil.process_iter():
            if process.name() == process_name:
                count += 1
        return count
    except Exception as e:
        logger.error(e)
        return False

def is_run_root():
    '''
    判断当前用户是否是root用户
    '''
    return os.getuid() == 0

def restart_x11_instance():
    '''
    重启X11服务
    '''
    password = os.environ.get('PASSWORD')
    if password is None and not is_run_root():
        logger.error("非root用户运行时重启x11服务需要输入sudo密码")
        raise Exception('Error: password is necessary when not run as root')
    run_command(sudo=True, cmd='systemctl restart lightdm', passwd=password)

screen_locked_check_time = time.time()
screen_lock_check_interval = 60 # 单位是秒
def check_screen_locked():
    '''
    如果系统进入锁屏状态,应当解除锁屏,或者退出程序
    '''
    global screen_locked_check_time
    # check current time, if time has passed 60 seconds, check screen lock status
    if time.time() - screen_locked_check_time < screen_lock_check_interval:
        return
    screen_locked_check_time = time.time()
    # 当配置了免密登录时, 不应该存在ukui-screensaver-checkpass进程
    if count_process_instances('ukui-screensaver-checkpass') > 0:
        logger.info("检测到系统已经进入锁屏状态,解除锁屏")
        print("检测到系统已经进入锁屏状态,解除锁屏")
        restart_x11_enabled = os.environ.get('RESTART_X11')
        if restart_x11_enabled is None:
            logger.info("没有开启重启X11服务,退出程序")
            print("没有开启重启X11服务,退出程序")
            exit(0)
        restart_x11_instance()
    

