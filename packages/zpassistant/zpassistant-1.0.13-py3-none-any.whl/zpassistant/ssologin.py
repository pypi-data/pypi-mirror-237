import base64
import datetime
import os
import threading
import requests

import time
import http.cookiejar
import urllib.parse
import re
from urllib.parse import urlparse
import getpass


def get_protocol_and_domain(url):
    parsed_url = urlparse(url)
    protocol = parsed_url.scheme
    domain = parsed_url.netloc
    protocol_and_domain = f"{protocol}://{domain}"
    return protocol_and_domain

def base64_decode(s):
    decoded_bytes = base64.b64decode(s)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string

def base64url_encode(s):
    encoded_bytes = base64.urlsafe_b64encode(s.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def redirect(url):
    if re.search(r'redirectUrl=(\S*)', url):
        all_path = re.search(r'redirectUrl=(\S*)', url).group(1)
        third_path = ''
        if re.search(r'state=(\S*)', url):
            third_path = re.search(r'state=(\S*)', url).group(1)
        elif re.search(r'goto=(\S*)', url):
            third_path = re.search(r'goto=(\S*)', url).group(1)
        else:
            # 处理没有state或goto的情况
            pass
        if third_path:
            decode_third = urllib.parse.unquote(third_path)
            try:
                # 进行解密操作，防止重复加密
                decode_third = base64_decode(decode_third)
            except:
                # 解密失败，不处理
                pass
            # 加密third_path
            encode_third = base64url_encode(decode_third)
            all_path = all_path.replace(third_path, encode_third)
        # 加密redirectUrl
        next_jump = '/nextJump.html?nextJump=' + base64url_encode(all_path)
        return next_jump
    else:
        return '/nextJump.html?nextJump=/'

class SsoLoginUtil:
    def __init__(self,sso_url = None):
        self.browser_type_map = {
            "chrome": self.init_chrome,
            "edge": self.init_edge,
            "firefox": self.init_firefox,
            "safari": self.init_safari,
        }
        self.installed_browser = None
        self.work_folder = ".zpsso"
        # 读取环境变量 ZPSSO_FOLDER_NAME
        self.url =os.getenv("ZPSSO_URL",sso_url)
        self.session = requests.Session() 
        self.base_cookie_jar = http.cookiejar.LWPCookieJar(filename=self.get_cookie_path())
        self.session.cookies = self.base_cookie_jar
        if os.path.exists(self.base_cookie_jar.filename):
            self.base_cookie_jar.load()
        
        self.get_or_update_version()

    def clearCookie(self):
        self.session.cookies.clear()

    def get_cookie_path(self):
        cookie_dir = self.get_or_create_work_dir()
        if not os.path.exists(cookie_dir):
            os.makedirs(cookie_dir)
        return cookie_dir + '/cookies.txt'
    
    # 获取pypi最新版本, 如果版本不一致,提示更新
    def get_or_update_version(self):
        from datetime import datetime, timedelta
        lastupdateTimeFile = os.path.abspath(self.get_or_create_work_dir() + "/lastupdatetime")
        if os.path.exists(lastupdateTimeFile):
            with open(lastupdateTimeFile,"r") as f:
                lastUpdatetime = f.read().strip()
            file_time = datetime.strptime(lastUpdatetime, '%Y-%m-%d %H:%M:%S')
            current_time = datetime.now()
            time_diff = current_time - file_time
            if time_diff <= timedelta(days=3):
                return
        current_time = datetime.now()
        # 将当前时间转换为字符串
        current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
        # 替换文件中的时间
        with open(lastupdateTimeFile, 'w') as file:
            file.write(current_time_str)
        version_path = os.path.abspath(self.get_or_create_work_dir() + "/update_failed.log")
        try:
            # 读取更新信息
            version = None
            if os.path.exists(version_path):
                with open(version_path, "r", encoding="utf-8") as fh:
                    version = fh.read()
                    print("package version is : " + version)
            if version is not None:
                # 说明尝试更新失败,不执行更新操作
                print("\033[31m auto update failed , please try update by : pip3 install -i https://pypi.org/simple --upgrade zpassistant")
                return
            import pkg_resources
            for i in range(3):
                version = pkg_resources.get_distribution("zpassistant").version
                # 读取远端版本
                url = "https://pypi.org/pypi/zpassistant/json"
                response = requests.get(url,timeout=1)
                if response.status_code == 200:
                    data = response.json()
                    latest_version = data["info"]["version"]
                    if latest_version != version:
                        # 使用红色字体打印
                        print("\033[31m latest version is : " + latest_version + ",will update your package: pip3 install -i https://pypi.org/simple --upgrade zpassistant")
                        # 执行安装指令
                        os.system("pip3 install -i https://pypi.org/simple --upgrade zpassistant")
                        # 绿色字体
                        print("\033[32m update success,please retry your cammond")
                    else:
                        break
        except Exception as e:
            print("get or update version failed , ignore")
            # 写入更新失败到文件中
            with open(version_path, "w", encoding="utf-8") as fh:
                fh.write(str(e))

    def base_cookie_check(self,url):
        # 校验是否超时
        base_cookie_jar = self.base_cookie_jar
        if base_cookie_jar.filename is not None and os.path.exists(base_cookie_jar.filename):
            base_cookie_jar.load()
            if not self.check_cookie_jar_expire(base_cookie_jar):
                self.refresh_cookie(url)
                return True
            else:
                print("cookie 过期,重新登录")
                base_cookie_jar.clear()
        return False
    
    def session_cookie_expired_check(self):
        # 创廳new_cookie_jar对象
        session_cookie_jar = self.base_cookie_jar
        # 校顶是否超时
        if session_cookie_jar.filename is not None and os.path.exists(session_cookie_jar.filename):
            session_cookie_jar.load(ignore_expires=True)
            all_cookies = session_cookie_jar._cookies
            # 遍历 cookie 对象的列表
            for domain in all_cookies:
                for path in all_cookies[domain]:
                    for name in all_cookies[domain][path]:
                        cookie = all_cookies[domain][path][name]
                        # 检查 cookie 是否已过期
                        if cookie.is_expired():
                            return (session_cookie_jar,True)
            return  (session_cookie_jar,False)
        return (session_cookie_jar,True)

    def get_or_create_work_dir(self):
        user_home = os.path.expanduser("~")
        folder_name = self.work_folder
        config_path = os.path.join(user_home, folder_name)
        if not os.path.exists(config_path):
            os.makedirs(config_path)
            print(f"文件夹 '{folder_name}' 已创建在用户主目录下。")
        return os.path.abspath(config_path)


    def check_cookie_jar_expire(self,cookie_jar):
        for cookie in cookie_jar:
            if cookie.name == "INNER_AUTHENTICATION":
                return False
        return True

    def get_current_session(self,url):
        # 获取 session cookie
        if self.base_cookie_check(url=url):
            self.refresh_cookie(url=url)
            return self.session
        return None

    def login(self,url, userName = None, password=None,type = None):
        session = self.get_current_session(url)
        if session :
            return session
        return self.ssoLoginByUserNamePassword(url=url,userName=userName,password=password,type=type)

    def refresh_cookie(self,url):
        session = self.session
        portal_address = urllib.parse.quote(url)
        url = 'https://zsg.zhaopin.com/changeUrl.html?redirectUrl=https://zpsso.zhaopin.com/cas/login?service=https%3A%2F%2Fzsg.zhaopin.com%2Fcas%2Fclient%2Fauth?state=' + portal_address
        headers = {
            'Referer': url,
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        }
        response = session.get(get_protocol_and_domain(url) +  redirect(url), allow_redirects=True,headers= headers)
        if response.status_code == 200:
                for cookie in session.cookies:
                    self.base_cookie_jar.set_cookie(cookie)
                self.base_cookie_jar.save()
                return session
        
    def ssoLoginByUserNamePassword(self,url, userName = None, password=None,type = None):
        if userName is None:
            userName = input("请输入ERP用户名: ")
        if password is None:
            password = getpass.getpass("请输入ERP密码：")
        # 密码去除前后空格,base64加密
        password = password.strip()
        password = base64.b64encode(str(password).encode("utf-8")).decode()
        portal_address = urllib.parse.quote(url)
        headers = {
            'Referer': self.url,
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
        }
        session = self.session
        data = f"path={portal_address}&username={userName}&password={password}&hideDing=true&loginthrid=&ct="
        response = session.post(self.url, data=data, headers=headers, allow_redirects=True)
        if response.status_code == 200:
            headers = {
                'Referer': response.url,
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            }
            response = session.get(get_protocol_and_domain(response.url) +  redirect(response.url), allow_redirects=True,headers= headers)
            if response.status_code == 200:
                for cookie in session.cookies:
                    self.base_cookie_jar.set_cookie(cookie)
                self.base_cookie_jar.save()
                return session
        raise Exception("登录失败" + response.text)

if (__name__ == "__main__"):
    SsoLoginUtil("https://zpsso.zhaopin.com/login").login("https://jenkins.dev.zhaopin.com:443/securityRealm/commenceLogin?from=/")