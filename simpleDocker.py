 #!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
def massage():
    print('--------\033[1;31;40mDebian服务器配置\033[0m--------')
    print('\033[1;32;40m24\033[0m:Debian更新组件')
    print('\033[1;32;40m23\033[0m:Debian安装Docker')
    print('\033[1;32;40m25\033[0m:Debian定时重启Docker')
    print('\033[1;32;40m28\033[0m:SWAP一键脚本')
    print('\033[1;32;40m8\033[0m:Debian系统开通指定端口')
    print('--------\033[1;31;40mDocker原版节点命令\033[0m--------')
    print('\033[1;32;40m3\033[0m:创建原版容器-单端口/多端口')
    print('\033[1;32;40m4\033[0m:创建原版容器-单端口/多端口-解锁Netflix')
    print('--------\033[1;31;40mDocker端口偏移节点命令\033[0m--------')
    print('\033[1;32;40m1\033[0m:创建新版容器-端口偏移')
    print('\033[1;32;40m2\033[0m:创建新版容器-端口偏移-解锁Netflix')
    print('--------\033[1;31;40mV2ray节点对接命令\033[0m--------')
    print('\033[1;32;40m11\033[0m:V2ray对接')
    print('---------\033[1;31;40mDocker命令\033[0m---------')
    print('\033[1;32;40m5\033[0m:删除指定容器')
    print('\033[1;32;40m6\033[0m:重启Docker')
    print('---------\033[1;31;40mCentOS服务器配置\033[0m---------')
    print('\033[1;32;40m12\033[0m:CentOS关闭防火墙')
    print('\033[1;32;40m17\033[0m:CentOS安装BBR')
    print('\033[1;32;40m13\033[0m:CentOS安装Docker')
    print('\033[1;32;40m14\033[0m:CentOS安装wget')
    print('\033[1;32;40m15\033[0m:CentOS安装curl')
    print('\033[1;32;40m16\033[0m:CentOS安装vim')
    print('---------\033[1;31;40m其他服务器配置命令\033[0m---------')
    print('\033[1;32;40m18\033[0m:编辑CF-DDNS')
    print('\033[1;32;40m19\033[0m:运行CF-DDNS')
    print('\033[1;32;40m20\033[0m:CF-DDNS定时检测')
    print('\033[1;32;40m0\033[0m:退出程序')
    try:
        result = input('----请选择:')
        return result
    except:
        print('\n您没有选择正确的选项：')
        sys.exit()

Num  = massage()
if Num == 1:#运行容器新版端口偏移
    name = raw_input('请输入容器名称(默认chaoqiang):')
    if len(name) ==0:
        name = 'chaoqiang'
    node = raw_input('请输入节点ID(默认100):')
    if len(node) == 0:
        node = '100'  
    port_web = raw_input('请输入网站偏移端口(默认11111):')
    if len(port_web) == 0:
        port_web = '11111' 

    port_ob = raw_input('请输入端口偏移量(默认0):')
    if len(port_ob) == 0:
        port_sev =  port_web
    else:
        port_sev = int(port_web) + int(port_ob)
        print '节点端口为:',port_sev
        port_sev = str(port_sev) 
    url = raw_input('请输入网站地址(默认https://chaoqiangtstudio.com):')
    if len(url) == 0:
        url = 'https://chaoqiangtstudio.com'
    os.system('docker run -d --name='+name+' \
        -e NODE_ID='+node+' \
        -e MU_SUFFIX=cloudfront.com \
        -e MU_REGEX=%5m%id.%suffix \
        -e API_INTERFACE=modwebapi \
        -e WEBAPI_URL='+url+' \
        -e SPEEDTEST=0 \
        -e WEBAPI_TOKEN=ChaoQiang \
        --log-opt max-size=50m \
        --log-opt max-file=3 \
        -p '+port_sev+':'+port_web+'/tcp \
        -p '+port_sev+':'+port_web+'/udp  \
        --restart=always jiaowoxiaotete/docker-new')
    sys.exit()

if Num == 2:#运行容器新版端口偏移-解锁Netflix
    name = raw_input('请输入容器名称(默认chaoqiang):')
    if len(name) ==0:
        name = 'chaoqiang'
    node = raw_input('请输入节点ID(默认100):')
    if len(node) == 0:
        node = '100'
    port_web = raw_input('请输入网站偏移端口(默认11111):')
    if len(port_web) == 0:
        port_web = '11111'                
    port_ob = raw_input('请输入端口偏移量(默认0):')  
    if len(port_ob) == 0:
        port_sev = port_web
    else:
        port_sev = int(port_web) + int(port_ob)
        print '节点端口为:',port_sev
        port_sev = str(port_sev)
    dns = raw_input('请输入DNS服务器地址(默认172.81.99.87):')  
    if len(dns) == 0:
        dns = '172.81.99.87'  
    url = raw_input('请输入网站地址(默认https://chaoqiangtstudio.com):')  
    if len(url) == 0:
        url = 'https://chaoqiangtstudio.com'
    os.system('docker run -d --name='+name+' \
        -e NODE_ID='+node+' \
        -e MU_SUFFIX=cloudfront.com \
        -e MU_REGEX=%5m%id.%suffix \
        -e API_INTERFACE=modwebapi \
        -e WEBAPI_URL='+url+' \
        -e SPEEDTEST=0 \
        -e WEBAPI_TOKEN=ChaoQiang \
        --log-opt max-size=50m --log-opt max-file=3 \
        -p '+port_sev+':'+port_web+'/tcp \
        -p '+port_sev+':'+port_web+'/udp \
        -e DNS_1='+dns+' \
        -e DNS_2='+dns+' \
        --restart=always jiaowoxiaotete/docker-new')
    sys.exit()

elif Num == 3:#运行容器原版
    name = raw_input('请输入容器名称(默认chaoqiang):')
    if len(name) ==0:
        name = 'chaoqiang'
    node = raw_input('请输入节点ID(默认100):')
    if len(node) == 0:
        node = '100'
    url = raw_input('请输入网站地址(默认https://chaoqiangtstudio.com):')  
    if len(url) == 0:
        url = 'https://chaoqiangtstudio.com'
    os.system('docker run -d --name='+name+' \
    -e NODE_ID='+node+' \
    -e SPEEDTEST=0 \
    -e MU_SUFFIX=cloudfront.com \
    -e MU_REGEX=%5m%id.%suffix \
    -e API_INTERFACE=modwebapi \
    -e WEBAPI_URL='+url+' \
    -e WEBAPI_TOKEN=ChaoQiang \
    --network=host \
    --log-opt max-size=50m \
    --log-opt max-file=3 \
    --restart=always jiaowoxiaotete/docker-old')
    print('%s节点添加成功'% node)
    sys.exit()

elif Num == 4:#运行容器原版解锁Netflix
    name = raw_input('请输入容器名称(默认chaoqiang):')
    if len(name) ==0:
        name = 'chaoqiang'
    node = raw_input('请输入节点ID(默认100):')
    if len(node) == 0:
        node = '100'
    dns = raw_input('请输入DNS服务器地址(默认172.81.99.87-日本):')  
    if len(dns) == 0:
        dns = '172.81.99.87'
    url = raw_input('请输入网站地址(默认https://chaoqiangtstudio.com):')  
    if len(url) == 0:
        url = 'https://chaoqiangtstudio.com'
    os.system('docker run -d --name='+name+' \
    -e NODE_ID='+node+' \
    -e SPEEDTEST=0 \
    -e MU_SUFFIX=cloudfront.com \
    -e MU_REGEX=%5m%id.%suffix \
    -e API_INTERFACE=modwebapi \
    -e WEBAPI_URL='+url+' \
    -e WEBAPI_TOKEN=ChaoQiang \
    --network=host \
    --log-opt max-size=50m \
    --log-opt max-file=3 \
    -e DNS_1='+dns+' \
    -e DNS_2='+dns+' \
    --restart=always jiaowoxiaotete/docker-old')
    sys.exit()

elif Num == 5:#删除指定容器
    name = raw_input('请输入容器名称(默认chaoqiang):')
    if len(name) == 0:
        name = 'chaoqiang'
    os.system('docker rm -f '+name)
    sys.exit()

elif Num == 6: #重启Docker
    os.system('systemctl restart docker')
    sys.exit()

elif Num == 7:#偏移量计算
    port = input('请输入节点服务器开通端口(必填):')
    port = port - 11111
    print('您的偏移量为%d'% port)
    sys.exit()

elif Num == 8:#端口防火墙
    port = raw_input('请输入节点服务器开通端口(必填):')
    os.system('/sbin/iptables -I INPUT -p tcp --dport '+port+' -j ACCEPT')
    os.system('/sbin/iptables -I INPUT -p udp --dport '+port+' -j ACCEPT')
    sys.exit()

elif Num == 9:#V2ray免费版一键对接
    url = raw_input('请输入对接网址(默认https://chaoqiangtstudio.com):')
    if len(url) ==0:
        url = 'https://chaoqiangtstudio.com'
    else:
        print('您的对接网址为：%s'% url)
    token = raw_input('请输入对接Token(默认ChaoQiang):')
    if len(token) == 0:
        token = 'ChaoQiang'  
    else:
        print('你的Token为：%s'% token)
    nodeid = raw_input('请输入节点ID:')  
    if len(nodeid) == 0:
        sys.exit()  
    os.system('wget -N --no-check-certificate \
        https://raw.githubusercontent.com/NS-Sp4ce/V2Ray-With-SSpanel/master/install-release.sh')
    os.system('bash install-release.sh --panelurl '+url+' --panelkey '+token+' --nodeid '+nodeid)
    #增加开机自启功能
    os.system('systemctl enable v2ray && systemctl restart v2ray')
    sys.exit()

elif Num == 10:#V2ray付费版一键对接 脚本内已经开启了开机自启功能
    os.system('wget -N --no-check-certificate \
        https://gist.github.com/Indexyz/3b541518e16aadc314af4b6e82e628bc/raw/bf959d40f3df630f8a8d0dc44413c34d2626503c/webapi.sh && \
        chmod +x webapi.sh && \
        bash webapi.sh')
    sys.exit()

elif Num == 11:#V2ray Docker对接SSP
    os.system('rm -rf v2ray-agent && mkdir v2ray-agent && \
        cd v2ray-agent && \
        curl https://raw.githubusercontent.com/jiaowoxiaotete/v2ray-sspanel-v3-mod_Uim-plugin/master/install.sh -o install.sh && \
        chmod +x install.sh && \
        bash install.sh')
    sys.exit()

elif Num == 12:#Centos 关闭防火墙
    os.system('systemctl stop firewalld.service && \
        systemctl disable firewalld.service')
    sys.exit()

elif Num == 13:#Centos 安装CentOS
    os.system('docker version > /dev/null || curl -fsSL get.docker.com | bash && \
        service docker restart && \
        systemctl enable docker && \
        crontab -l > docker.cron && \
        echo \'0 4 * * * docker restart $(docker ps -q)\' >> docker.cron && \
        crontab docker.cron && \
        systemclt enable docker')
    sys.exit()

elif Num == 14:#Centos 安装wget
    os.system('yum -y install wget')
    sys.exit()

elif Num == 15:#Centos 更新curl
    os.system('yum update nss curl')
    sys.exit()

elif Num == 16:#Centos 安装vim
    os.system('yum install vim -y')
    sys.exit()

elif Num == 17:#BBR加速
    os.system('wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh" && \
        chmod +x tcp.sh && ./tcp.sh')
    sys.exit()

elif Num == 18:#编辑CF-DDNS
    os.system('wget  -N --no-check-certificate \
        https://raw.githubusercontent.com/yulewang/cloudflare-api-v4-ddns/master/cf-v4-ddns.sh && vi cf-v4-ddns.sh')
    sys.exit()

elif Num == 19:#运行CF-DDNS
    os.system('chmod +x cf-v4-ddns.sh && bash cf-v4-ddns.sh')
    sys.exit()

elif Num == 20:#CF-DENS定时检测
    os.system('crontab -l > cf.cron && \
        echo \'*/2 * * * * /root/cf-v4-ddns.sh >/dev/null 2>&1\' >> cf.cron && \
        crontab cf.cron')
    sys.exit()

elif Num == 21:#运行CF-DDNS
    os.system('systemctl stop v2ray && systemctl disable v2ray')
    sys.exit()

elif Num == 22:#Brook手动安装
    port_a = raw_input('请输入转发机端口:')
    abroad_ip = raw_input('请输入被转发机IP:')
    port_b = raw_input('请输入被转发机端口:')
    os.system('cd /root && \
        mkdir brook && \
        cd brook && \
        brook_ver=$(wget -qO- "https://github.com/txthinking/brook/tags"| grep "/txthinking/brook/releases/tag/"| head -n 1| awk -F "/tag/" \'{print $2}\'| sed \'s/\\">//\') && \
        echo ${brook_ver} && \
        wget -N --no-check-certificate "https://github.com/txthinking/brook/releases/download/${brook_ver}/brook" && \
        chmod +x brook && \
        nohup ./brook relay -l :port_a -r abroad_ip:port_b > /dev/null 2>&1 &')
    sys.exit()

elif Num ==23:#Debian安装Docker
    os.system('curl -sSL https://get.docker.com/ | sh && \
    systemctl start docker && \
    systemctl enable docker.service')
    sys.exit()

elif Num == 24:#Debian 更新组件
    os.system('apt-get update && \
        apt-get install curl vim python-pip iperf3 && \
        pip install speedtest-cli')
    sys.exit()

elif Num == 25:#Debian Docker 定时重启
    os.system('crontab -l > docker.cron')
    os.system('echo \'0 4 * * * docker restart $(docker ps -q)\' >> docker.cron')
    os.system('crontab docker.cron')
    print('Docker定时重启任务添加成功！')
    sys.exit()

elif Num == 26:#安装宝塔
    os.system('yum install -y wget && \
        wget -O install.sh http://download.bt.cn/install/install_6.0.sh && \
        sh install.sh')
    sys.exit()

elif Num == 27:#安装iptable
    os.system('wget -qO natcfg.sh http://arloor.com/sh/iptablesUtils/natcfg.sh && bash natcfg.sh')
    sys.exit()

elif Num == 28:#SWAP一键脚本
    os.system('wget  -N --no-check-certificate https://raw.githubusercontent.com/jiaowoxiaotete/Addswap/master/swap.sh && bash swap.sh')
    sys.exit()

elif Num == 0:
    sys.exit() 

else:
    print('\n对不起没有该功能！！！\n')
