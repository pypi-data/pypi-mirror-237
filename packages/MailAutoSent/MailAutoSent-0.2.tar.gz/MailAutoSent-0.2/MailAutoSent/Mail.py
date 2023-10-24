import yagmail
import time

class Mail():
    """
    Mail class
    """
    def __init__(self,host,senders,API_token):
        super().__init__()
        self.host = host
        self.senders = senders
        self.API_token = API_token

    def log(self, content):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f'{now_time}: {content}')

    def sendmail(self, receivers, title, msg):
        """
        Send mail
        Arguments:
            msg {str} -- mail context
            title {str} -- mail title
            receivers {list} -- mail receiver
            attachment -- mail attacgmet,may add in fruture
        """
        yag = yagmail.SMTP(
            host='smtp.qq.com', user=self.senders,
            password=self.API_token, smtp_ssl=True
        )
        try:
            yag.send(receivers, title, msg)
            self.log("Success")
        except BaseException as e:
            print(e)
            self.log("Failed")

if __name__ == "__main__":
    Mail()