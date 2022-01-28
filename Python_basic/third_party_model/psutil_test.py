#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import psutil

logging.getLogger().setLevel(logging.INFO)


def get_cpu_info():
    """
    psutil = process and system utilities
    :return:
    """
    cpu_number = psutil.cpu_count()
    logging.info(f'CPU Logical number: {cpu_number}')

    cpu_number = psutil.cpu_count(logical=False)
    logging.info(f'CPU physical number: {cpu_number}')

    cpu_time = psutil.cpu_times()
    logging.info(f'CPU times is: {cpu_time}')

    # 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
    for x in range(10):
        logging.info(f'{psutil.cpu_percent(interval=1, percpu=True)}')

    physical_memory = psutil.virtual_memory()
    logging.info(f'physical memory: {physical_memory}')

    swap_memory = psutil.swap_memory()
    logging.info(f'swap memory: {swap_memory}')


def get_disk_info():
    disk_partitions = psutil.disk_partitions()
    disk_usage = psutil.disk_usage('/')
    disk_io = psutil.disk_io_counters()

    logging.info(f'disk partitions: {disk_partitions}')
    logging.info(f'disk usage: {disk_usage}')
    logging.info(f'disk io: {disk_io}')


def get_network_info():
    net_io = psutil.net_io_counters()
    net_addr = psutil.net_if_addrs()
    net_stats = psutil.net_if_stats()
    net_conn = psutil.net_connections()  # under sudo

    logging.info(f'net io: {net_io}')
    logging.info(f'net addr: {net_addr}')
    logging.info(f'net stats: {net_stats}')
    res = """
    INFO:root:net io: snetio(bytes_sent=273605632, bytes_recv=2689391616, packets_sent=2382535, packets_recv=10542890, errin=0, errout=1029, dropin=0, dropout=0)
    INFO:root:net addr: {'lo0': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0',...)]}
    INFO:root:net stats: {'lo0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UN...)}

    """

    logging.info(f'net conn: {net_conn}')
    """
    INFO:root:net conn: [sconn(fd=21, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='1.....', port=52755), 
    raddr=addr(ip='1...1.1', port=443), status='ESTABLISHED', pid=9333), sconn(fd=22, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>,
    """


def get_process_info():
    process_ids = psutil.pids()
    logging.info(f'process ids are: {process_ids}')
    # INFO:root:process ids are: [0, 1, 60, 61, 64, 65, 66, 69, 70, 71, 72, 76, 78, 80, ..., 10468, 10469, 10470, 10476]

    p = psutil.Process(10501)
    p.name()  # 'Python'

    p.exe()
    # Out[10]: '/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python'

    p.cwd()
    # Out[11]: '/Users/xxxxxxxxxxx/AI'

    p.cmdline()
    res = ['/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python',
           '/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevconsole.py',
           '--mode=client',
           '--port=xxx']
    p.parent()
    # Out[13]: psutil.Process(pid=1470, name='pycharm', status='running', started='17:55:52')

    p.children()
    # Out[14]: []

    p.status()
    # Out[15]: 'running'

    p.username()
    # Out[16]: 'xxxx'

    p.create_time()
    # Out[17]: 1643352186.040108

    p.terminate()
    # Process finished with exit code 143 (interrupted by signal 15: SIGTERM)

    p.terminal()
    p.cpu_times()
    # Out[13]: pcputimes(user=1.915791744, system=0.581980928, children_user=0.0, children_system=0.0)
    p.memory_info()
    # Out[14]: pmem(rss=99749888, vms=36269252608, pfaults=35911, pageins=1)

    p.open_files()
    # Out[15]:[popenfile(path='/Users/gwendolynhai/.ipython/profile_default/history.sqlite', fd=8),
    #         popenfile(path='/Users/gwendolynhai/.ipython/profile_default/history.sqlite', fd=9)]

    p.connections()
    # Out[16]: [pconn(fd=7, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>,
    # laddr=addr(ip='xxx.0.0.1', port=xxx), raddr=addr(ip='xx.0.0.1', port=xxx), status='ESTABLISHED')]

    p.num_threads()
    # Out[18]: 4

    p.threads()
    # Out[19]:
    # [pthread(id=1, user_time=1.301841, system_time=0.308633),
    #  pthread(id=2, user_time=0.027735, system_time=0.021079),
    #  pthread(id=3, user_time=0.003955, system_time=0.013841),
    #  pthread(id=4, user_time=0.197618, system_time=0.028891)]

    p.environ()
    # Out[20]:
    # res = {'PATH': '/usr/bin:/bin:/usr/sbin:/sbin',
    #  'COMMAND_MODE': 'unix2003',
    #  'PYDEVD_LOAD_VALUES_ASYNC': 'True',
    #  'DISPLAY': '/private/tmp/com.apple.launchd.jaEYV0PpNx/org.xquartz:0',
    #  'LOG...'}
    p.terminate()
    # Process finished with exit code 143 (interrupted by signal 15: SIGTERM)

    import psutil
    psutil.test()
    # USER         PID  %MEM     VSZ     RSS  NICE STATUS  START   TIME  CMDLINE
    # root           0                              runni  Jan27         kernel_task
    # root           1                              runni  Jan27         launchd
    # root          60                              runni  Jan27         logd
    # root          61                              runni  Jan27         UserEventAgen
    # root          64                              runni  Jan27         uninstalld
    # root          65


if __name__ == '__main__':
    # get_cpu_info()
    # result
    """
    INFO:root:CPU Logical number: 16
    INFO:root:CPU physical number: 8
    INFO:root:CPU times is: scputimes(user=22864.95, nice=0.0, system=14019.33, idle=371927.57)
    INFO:root:[15.0, 0.0, 18.8, 0.0, 13.0, 0.0, 8.9, 0.0, 6.9, 0.0, 4.0, 0.0, 3.0, 0.0, 2.9, 0.0]
    INFO:root:[10.1, 0.0, 14.1, 0.0, 12.0, 1.0, 5.0, 0.0, 4.0, 1.0, 2.0, 0.0, 1.0, 0.0, 0.0, 0.0]
    INFO:root:[9.9, 0.0, 14.9, 0.0, 11.8, 0.0, 6.0, 0.0, 2.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0]
    INFO:root:[12.7, 0.0, 14.0, 0.0, 12.1, 0.0, 4.0, 0.0, 5.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 0.0]
    INFO:root:[11.1, 0.0, 17.0, 0.0, 12.9, 0.0, 3.0, 0.0, 3.0, 0.0, 1.0, 0.0, 4.0, 0.0, 1.0, 0.0]
    INFO:root:[9.0, 1.0, 13.9, 0.0, 12.0, 0.0, 4.0, 0.0, 3.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0]
    INFO:root:[10.0, 0.0, 14.0, 0.0, 11.9, 0.0, 6.9, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 0.0, 0.0]
    INFO:root:[8.9, 0.0, 12.9, 0.0, 9.1, 0.0, 5.9, 0.0, 1.0, 0.0, 10.0, 0.0, 0.0, 0.0, 1.0, 0.0]
    INFO:root:[8.9, 0.0, 14.0, 0.0, 10.9, 0.0, 4.0, 0.0, 3.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    INFO:root:[8.1, 0.0, 13.9, 0.0, 11.0, 0.0, 4.0, 0.0, 2.0, 0.0, 2.0, 0.0, 1.0, 0.0, 0.0, 0.0]
    
    INFO:root:physical memory: svmem(total=17179869184, available=6431371264, percent=62.6, used=8876556288, free=47308800, active=6393270272, inactive=6377791488, wired=2483286016)
    INFO:root:swap memory: sswap(total=2147483648, used=356777984, free=1790705664, percent=16.6, sin=96957272064, sout=321036288)

    
    Process finished with exit code 0

    """

    # get_disk_info()
    """
    INFO:root:disk partitions: [sdiskpart(device='/dev/disk1s5s1', mountpoint='/', fstype='apfs', opts='ro,local,rootfs,dovolfs,journaled,multilabel', maxfile=255, maxpath=1024), sdiskpart(device='/dev/disk1s4', mountpoint='/System/Volumes/VM', fstype='apfs', opts='rw,noexec,local,dovolfs,dontbrowse,journaled,multilabel,noatime', maxfile=255, maxpath=1024), sdiskpart(device='/dev/disk1s2', mountpoint='/System/Volumes/Preboot', fstype='apfs', opts='rw,local,dovolfs,dontbrowse,journaled,multilabel', maxfile=255, maxpath=1024), sdiskpart(device='/dev/disk1s6', mountpoint='/System/Volumes/Update', fstype='apfs', opts='rw,local,dovolfs,dontbrowse,journaled,multilabel', maxfile=255, maxpath=1024), sdiskpart(device='/dev/disk1s1', mountpoint='/System/Volumes/Data', fstype='apfs', opts='rw,local,dovolfs,dontbrowse,journaled,multilabel', maxfile=255, maxpath=1024)]
    INFO:root:disk usage: sdiskusage(total=499963174912, used=269033754624, free=230929420288, percent=53.8)
    INFO:root:disk io: sdiskio(read_count=5416732, write_count=1464400, read_bytes=115044610048, write_bytes=60473335808, read_time=2732425, write_time=729134)
    
    Process finished with exit code 0

    """

    # get_network_info()
    get_process_info()
