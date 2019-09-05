# -*- coding=UTF-8 -*-
# @Description: 使用Python脚本快捷对接docker节点
# @Version: 
# @Author: 肖大人
# @Github: https://github.com/jiaowoxiaotete
# @Date: 2019-09-05 09:16:02
import os
import sys
def massage():
    os.system('clear')
    print('--------\033[1;31;40m通用命令\033[0m--------')
    print('----\033[1;32;40m1\033[0m:创建新版容器-支持单端口')
    print('----\033[1;32;40m2\033[0m:创建新版容器-支持单端口-解锁Netflix')
    print('----\033[1;32;40m3\033[0m:创建原版容器')
    print('----\033[1;32;40m4\033[0m:创建原版容器-解锁Netflix')
    print('----\033[1;32;40m5\033[0m:删除指定容器')
    print('----\033[1;32;40m6\033[0m:重启指定容器')
    print('----\033[1;32;40m7\033[0m:节点服务器端口偏移量计算')
    print('----\033[1;32;40m8\033[0m:Debian系统开通指定端口')
    print('----\033[1;32;40m0\033[0m:退出程序')
    con = 1
    while con != 0:
        con = 0
        try:
            result = input('----请选择:')
            return result
        except:
            print('\n请输入正确的数字：')
            con = 1

print(11111-12345)
Num = massage()
Num = int(Num)
if Num == 1:#运行容器新版
    name = raw_input('请输入容器名称(默认super):')
    if len(name) ==0:
        name = 'super'
    node = raw_input('请输入节点ID(默认11111):')
    if len(node) == 0:
        node = '11111'  
    port_sev = raw_input('请输入节点服务器端口(默认11111):')  
    if len(port_sev) == 0:
        port_sev = '11111'  
    port_web = raw_input('请输入网站偏移端口(默认11111):')  
    if len(port_web) == 0:
        port_web = '11111'  
    url = raw_input('请输入网站地址(默认https://super.qaqemm.xyz):')  
    if len(url) == 0:
        url = 'https://super.qaqemm.xyz'
    try:
        os.system('docker run -d --name='+name+' -e NODE_ID='+node+' -e MU_SUFFIX=cloudfront.com -e MU_REGEX=%5m%id.%suffix -e API_INTERFACE=modwebapi -e WEBAPI_URL='+url+' -e SPEEDTEST=0 -e WEBAPI_TOKEN=XiaoDaren --log-opt max-size=50m --log-opt max-file=3 -p '+port_sev+':'+port_web+'/tcp -p '+port_sev+':'+port_web+'/udp  --restart=always jiaowoxiaotete/docker-new')
    except:
        print('程序没有正确运行！\n')
if Num == 2:#运行容器新版-解锁Netflix
    name = raw_input('请输入容器名称(默认super):')
    if len(name) ==0:
        name = 'super'
    node = raw_input('请输入节点ID(默认11111):')
    if len(node) == 0:
        node = '11111'  
    port_sev = raw_input('请输入节点服务器端口(默认11111):')  
    if len(port_sev) == 0:
        port_sev = '11111'  
    port_web = raw_input('请输入网站偏移端口(默认11111):')  
    if len(port_web) == 0:
        port_web = '11111'  
    dns = raw_input('请输入DNS服务器地址(默认172.81.99.87):')  
    if len(dns) == 0:
        dns = '172.81.99.87'  
    url = raw_input('请输入网站地址(默认https://super.qaqemm.xyz):')  
    if len(url) == 0:
        url = 'https://super.qaqemm.xyz'
    try:
        os.system('docker run -d --name='+name+' -e NODE_ID='+node+' -e MU_SUFFIX=cloudfront.com -e MU_REGEX=%5m%id.%suffix -e API_INTERFACE=modwebapi -e WEBAPI_URL='+url+' -e SPEEDTEST=0 -e WEBAPI_TOKEN=XiaoDaren --log-opt max-size=50m --log-opt max-file=3 -p '+port_sev+':'+port_web+'/tcp -p '+port_sev+':'+port_web+'/udp -e DNS_1='+dns+' -e DNS_2='+dns+' --restart=always jiaowoxiaotete/docker-new')
    except:
        print('程序没有正确运行！\n')
elif Num == 3:#运行容器原版
    name = raw_input('请输入容器名称(默认super):')
    if len(name) ==0:
        name = 'super'
    node = raw_input('请输入节点ID(默认11111):')
    if len(node) == 0:
        node = '11111'
    url = raw_input('请输入网站地址(默认https://super.qaqemm.xyz):')  
    if len(url) == 0:
        url = 'https://super.qaqemm.xyz'
    try:
        os.system('docker run -d --name='+name+' -e NODE_ID='+node+' -e SPEEDTEST=0 -e MU_SUFFIX=cloudfront.com -e MU_REGEX=%5m%id.%suffix -e API_INTERFACE=modwebapi -e WEBAPI_URL='+url+' -e WEBAPI_TOKEN=XiaoDaren --network=host --log-opt max-size=50m --log-opt max-file=3 --restart=always jiaowoxiaotete/docker-old')
    except:
        print('程序没有正确运行！\n')
elif Num == 4:#运行容器原版解锁Netflix
    name = raw_input('请输入容器名称(默认super):')
    if len(name) ==0:
        name = 'super'
    node = raw_input('请输入节点ID(默认11111):')
    if len(node) == 0:
        node = '11111'
    dns = raw_input('请输入DNS服务器地址(默认172.81.99.87):')  
    if len(dns) == 0:
        dns = '172.81.99.87'
    url = raw_input('请输入网站地址(默认https://super.qaqemm.xyz):')  
    if len(url) == 0:
        url = 'https://super.qaqemm.xyz'
    try:
        os.system('docker run -d --name='+name+' -e NODE_ID='+node+' -e SPEEDTEST=0 -e MU_SUFFIX=cloudfront.com -e MU_REGEX=%5m%id.%suffix -e API_INTERFACE=modwebapi -e WEBAPI_URL='+url+' -e WEBAPI_TOKEN=XiaoDaren --network=host --log-opt max-size=50m --log-opt max-file=3 -e DNS_1='+dns+' -e DNS_2='+dns+' --restart=always jiaowoxiaotete/docker-old')
    except:
        print('程序没有正确运行！\n')
elif Num == 5:
    name = raw_input('请输入容器名称(默认super):')
    if len(name) == 0:
        name = 'super'
    os.system('docker rm -f '+name)
elif Num == 6:
    name = raw_input('请输入容器名称(默认super):')
    if len(name) == 0:
        name = 'super'
    os.system('docker restart '+name)
elif Num == 7:#偏移量计算
    port = input('请输入节点服务器开通端口(必填):')
    port = port - 11111
    print('您的偏移量为%d'% port)
elif Num == 8:#端口防火墙
    port = input('请输入节点服务器开通端口(必填):')
    os.system('/sbin/iptables -I INPUT -p tcp --dport '+port+' -j ACCEPT')
    os.system('/sbin/iptables -I INPUT -p udp --dport '+port+' -j ACCEPT')
elif Num == 0:
    sys.exit() 
else:
    print('\n对不起没有改功能！！！\n')