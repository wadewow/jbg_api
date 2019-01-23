# coding:utf-8
import configparser


class ReadConfig:
    """
    :introduce: 读取config.ini文件的配置信息
    :method: get_api_hosts()、get_database_config()、get_url()
    """

    def __init__(self):
        """
        :init:获取配置文件句柄
        """
        self.config = configparser.ConfigParser()
        self.config.read('../ConfigurationFolder/config.ini')
        self.email_config = configparser.ConfigParser()
        self.email_config.read('../ConfigurationFolder/email.ini')

    def get_url(self, url_name):
        """
        :param url_name: url名
        :return: 返回接口的url地址
        """
        hosts = self.config.get('HOSTS', 'hosts')
        url_sections = self.config['URL']
        try:
            if url_name == 'SetFollow':
                url = ''.join([hosts, url_sections[url_name]])
                return url
            elif url_name == 'FollowList':
                url = ''.join([hosts, url_sections[url_name]])
                return url
            elif url_name == 'DisableFollow':
                url = ''.join([hosts, url_sections[url_name]])
                return url
            elif url_name == 'GetPassSafeMobile':
                url = ''.join([hosts, url_sections[url_name]])
                return url
            elif url_name == 'SendVerificationCode':
                url = ''.join([hosts, url_sections[url_name]])
                return url
            elif url_name == 'CheckVerificationCode':
                url = ''.join([hosts, url_sections[url_name]])
                return url
            elif url_name == 'SendSMSMessage':
                url = ''.join([hosts, url_sections[url_name]])
                return url
            elif url_name == 'QueryOrder':
                url = ''.join([hosts, url_sections[url_name]])
                return url
            elif url_name == 'MyTradeList':
                url = ''.join([hosts, url_sections[url_name]])
                return url
            elif url_name == 'RoleDetail':
                url = ''.join([hosts, url_sections[url_name]])
                return url
            else:
                return 'url输入不正确'
        except Exception as e:
            print(f'url输入不正确:{e}')

    def get_database_config(self):
        """
        :return:返回数据库配置信息
        """
        host = self.config.get("DATABASE", 'host')
        port = self.config.get("DATABASE", 'port')
        user = self.config.get("DATABASE", 'user')
        password = self.config.get("DATABASE", 'password')
        db = self.config.get("DATABASE", 'db')
        return host, port, user, password, db

    def get_email_config(self):
        """
        :return: 邮件配置信息
        """
        email = {}
        receiver = []
        sender_addr = self.email_config['sender']['address']
        password = self.email_config['sender']['password']
        receivers = self.email_config['receivers']
        email['sender_addr'] = sender_addr
        email['password'] = password
        for i in receivers:
            receiver.append(receivers[i])
        email['receivers'] = receiver
        return email


if __name__ == '__main__':
    url = ReadConfig().get_email_config()
    print(url)


