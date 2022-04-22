#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime


def os_operator():
    print(os.name)  # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
    print(os.uname())  # posix.uname_result(sysname='Darwin', nodename='GwendolyndeMacBook-Pro.local',
    # release='20.6.0', version='Darwin Kernel Version 20.6.0: Mon Aug 30 06:12:21 PDT 2021;
    # root:xnu-7195.141.6~3/RELEASE_X86_64', machine='x86_64')
    print(os.environ)   # environ({'PATH': '/Users/gwendolynhai/.sdkman/candidates/scala/current/bin:/Library/Frameworks/Python.framework/Versions/3.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/Apple/usr/bin:/Applications/Wireshark.app/Contents/MacOS', 'SDKMAN_VERSION': '5.7.3+337', 'COMMAND_MODE': 'unix2003', 'DISPLAY': '/private/tmp/com.apple.launchd.koOK2CiUZ5/org.xquartz:0', 'VERSIONER_PYTHON_VERSION': '2.7', 'SDKMAN_DIR': '/Users/gwendolynhai/.sdkman', 'LOGNAME': 'gwendolynhai', 'XPC_SERVICE_NAME': 'application.com.jetbrains.pycharm.25349469.25350412', 'PWD': '/Users/gwendolynhai/AI/Gwendolyn_s_Art/io', 'PYCHARM_HOSTED': '1', 'SCALA_HOME': '/Users/gwendolynhai/.sdkman/candidates/scala/current', 'PYCHARM_DISPLAY_PORT': '63342', 'SDKMAN_CANDIDATES_DIR': '/Users/gwendolynhai/.sdkman/candidates', '__CFBundleIdentifier': 'com.jetbrains.pycharm', 'PYTHONPATH': '/Users/gwendolynhai/AI:/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend:/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display', 'SHELL': '/bin/zsh', 'PAGER': 'less', 'LSCOLORS': 'Gxfxcxdxbxegedabagacad', 'PYTHONIOENCODING': 'UTF-8', 'SDKMAN_CANDIDATES_API': 'https://api.sdkman.io/2', 'SDKMAN_PLATFORM': 'Darwin', 'OLDPWD': '/', 'USER': 'gwendolynhai', 'ZSH': '/Users/gwendolynhai/.oh-my-zsh', 'TMPDIR': '/var/folders/5c/nc4j46jj34bdvwjddrd5vh8h0000gn/T/', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.yzVUCp3xGy/Listeners', 'XPC_FLAGS': '0x0', 'PYTHONUNBUFFERED': '1', '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 'LESS': '-R', 'LC_CTYPE': 'zh_CN.UTF-8', 'HOME': '/Users/gwendolynhai', '__PYVENV_LAUNCHER__': '/usr/local/bin/python3.7'})
    print(os.environ.get('PATH')) #/Users/gwendolynhai/.sdkman/candidates/scala/current/bin:/Library/Frameworks/Python.framework/Versions/3.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/Apple/usr/bin:/Applications/Wireshark.app/Contents/MacOS
    print(os.environ.get('x', 'default'))   # default
    """
    import os
    os.path.abspath('.')
    Out[3]: '/Users/gwendolynhai/AI'
    os.path.join('/Users/gwendolynhai/AI', 'testdir')
    Out[4]: '/Users/gwendolynhai/AI/testdir'
    os.mkdir('/Users/gwendolynhai/AI/testdir')
    os.rmdir('/Users/gwendolynhai/AI/testdir')
    """


if __name__ == '__main__':
    # os_operator()

    pwd = os.path.abspath('')

    print('      Size     Last Modified  Name')
    print('------------------------------------------------------------')

    for f in os.listdir(pwd):
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        flag = '/' if os.path.isdir(f) else ''
        print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
