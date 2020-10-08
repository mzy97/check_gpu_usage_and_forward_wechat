# check_gpu_usage_and_forward_wechat
服务器GPU监控程序，当有GPU空闲时自动推送到微信端，抢卡快人一步。

## Description

使用pynvml读取显卡当前信息，判断是否有卡空闲，如果有空闲推送至微信，帮助用户更快的抢卡。

依赖python包：

pynvml

blessed

apscheduler

requests

argparse

logging

## User Guide

使用check_gpu_main.py 启动监控脚本

可以使用screen或者tmux工具将其置于后台运行

使用方法：

```bash
python check_gpu_main.py --key_of_notify [your own Key] --check_freq '*|*|*/1'
```

参数：

- --key_of_notify（必选）：“Server酱”的推送Key，用于推送到微信账号
- -define_threshold：定义卡显存阈值，低于该阈值推送微信通知，以MB为单位
- —check_freq：间隔多长时间检查一次，或者定时运行。例如，“*|*|*/10“ 为每10分钟检查一次。该参数遵循crontab的时间设置规则。
- —log_file：设置log输出文件路径（have bug）

Server酱的key获取请参考：

[http://sc.ftqq.com/3.version](http://sc.ftqq.com/3.version)

corntab时间设置请参考：

[https://crontab.guru](https://crontab.guru/)

## 其他

core.py 是一个非常强大的文件，可以从其中取用当前机器所有GPU的状态（显存占用，占用进程的用户，风扇转速等信息），可以使用playground.ipynb进行游玩
