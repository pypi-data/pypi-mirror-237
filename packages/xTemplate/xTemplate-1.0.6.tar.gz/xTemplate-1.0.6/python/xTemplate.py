import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import time
import logging
import ctypes
from psycopg2 import Error
from python.xPostgreSQL import Config as PostgreSQLConfig
from python.xConfigparser import Config as Config
from colorama import init, Fore, Back, Style

class DatabaseConnector:
    def __init__(self, db, host, user, pw, port, schemas):
        self.db = db
        self.host = host
        self.user = user
        self.pw = pw
        self.port = port
        self.schemas = schemas

    def connect(self):
        try:
            # PostgreSQLConfigクラスを使用してデータベースに接続
            connection = PostgreSQLConfig(self.db, self.host, self.user, self.pw, self.port, self.schemas)
            return connection
        except (Exception, Error) as error:
            # データベースへの接続中にエラーが発生した場合はRuntimeErrorを発生させる
            raise RuntimeError(f"データベースへの接続エラー: {error}")

class EmailNotifier:
    def __init__(self, smtp_server,smtp_port,sender):
        self.smtp_server=smtp_server
        self.smtp_port=smtp_port
        self.sender = sender

    def get_files_in_folders(folder_paths):
        file_paths = []
        file_names = []
        for folder_path in folder_paths:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_paths.append(os.path.join(root, file))
                    file_names.append(file)
        return file_paths, file_names

    def send_email(self,subject,header,body,footer,recipients,recipients_cc):
        try:
            # Email details
            smtp_server = self.smtp_server
            smtp_port = self.smtp_port
            sender = self.sender

            # Create a MIME text object
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = ';'.join(recipients)
            if recipients_cc!='':
                msg['CC'] = ';'.join(recipients_cc)

            table_html = ''
            if body != '':
                table_html = body
            
            # Create the email body as HTML
            message = header
            message += f'<html><body>{table_html}</body></html>'
            message += footer

            # Attach the email body
            msg.attach(MIMEText(message, 'html'))

            # Connect to the SMTP server
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                try:    
                    server.sendmail(sender, recipients, msg.as_string())
                    return 1
                except Exception as e:
                    print('An error occurred:', str(e))
                    return 0
                finally:
                    # Disconnect from the SMTP server
                    server.quit()
        except Exception as e:
            # Email通知の送信中にエラーが発生した場合はRuntimeErrorを発生させる
            raise RuntimeError(f"Email通知の送信エラー: {e}")


class Template:
    def __init__(self,config_file):
        # Configクラスを使用して設定ファイルから設定を読み込む
        self.config_file = config_file
        self.db = None
        self.host = None
        self.user = None
        self.pw = None
        self.port = None
        self.schemas = None
        self.log = None
        self.console_title = None
        self.smtp_server = None
        self.smtp_port = None
        self.sender = None
        self.recipient = None
        self.recipient_cc = None
        self.subject = None
        self.message_header = None
        self.message_header2 = None
        self.message_footer = None
        self.message_footer2 = None
        try:
            self.config = Config(self.config_file)

            self.db = self.config.get('DB', 'db')
            self.host = self.config.get('DB', 'host')
            self.user = self.config.get('DB', 'user')
            self.pw = self.config.get('DB', 'pw')
            self.port = self.config.get('DB', 'port')
            self.schemas = self.config.get('DB', 'schemas')

            self.smtp_server = self.config.get('EMAIL', 'smtp_server')
            self.smtp_port = self.config.get('EMAIL', 'smtp_port')
            self.sender = self.config.get('EMAIL', 'sender')
            self.recipient = self.config.get('EMAIL', 'recipient')
            self.recipient_cc = self.config.get('EMAIL', 'recipient_cc')
            self.subject = self.config.get('EMAIL', 'subject')
            self.message_header = self.config.get('EMAIL', 'message_header')
            self.message_header2 = self.config.get('EMAIL', 'message_header2')
            self.message_footer = self.config.get('EMAIL', 'message_footer')
            self.message_footer2 = self.config.get('EMAIL', 'message_footer2')

            self.log = self.config.get('PARAM', 'log')
            self.console_title = self.config.get('PARAM', 'console_title')

        except Exception as e:
            print(f"Exception error: {str(e)}")


        # DatabaseConnectorおよびEmailNotifierの初期化
        self.database_connector = DatabaseConnector(
            self.db,
            self.host,
            self.user,
            self.pw,
            self.port,
            self.schemas
        )
        self.email_notifier = EmailNotifier(
            self.smtp_server,
            self.smtp_port,
            self.sender
        )

        # DatabaseConnectorおよびEmailNotifierの初期化
        # self.database_connector = DatabaseConnector(
        #     self.config.get('DB', 'db'),
        #     self.config.get('DB', 'host'),
        #     self.config.get('DB', 'user'),
        #     self.config.get('DB', 'pw'),
        #     self.config.get('DB', 'port'),
        #     self.config.get('DB', 'schemas')
        # )
        # self.email_notifier = EmailNotifier(
        #     self.config.get('EMAIL', 'smtp_server'),
        #     self.config.get('EMAIL', 'smtp_port'),
        #     self.config.get('EMAIL', 'sender')
        # )

        # その他の変数の初期化...
        self.console_title = self.console_title

        console_handle = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.kernel32.SetConsoleTitleW(self.console_title)

        init(autoreset=True)                                            # autoreset=Trueを設定して、Coloramaのテキストリセットを有効にします。
        logging.basicConfig(filename=self.log, level=logging.INFO, encoding="utf-8")

    def db_fetchall(self,query):
        try:
            # データベースへの接続
            db_connection = self.database_connector.connect()
            # クエリの実行
            return db_connection.fetchall(query)

        except Exception as error:
            # エラーが発生した場合はエラーハンドリングを実行
            print("ERROR2:", error)
            self.handle_error(error)

    def db_commit(self,query):
        try:
            # データベースへの接続
            db_connection = self.database_connector.connect()
            # クエリの実行
            return db_connection.commit(query)

        except Exception as error:
            # エラーが発生した場合はエラーハンドリングを実行
            print("ERROR2:", error)
            self.handle_error(error)

    def db_commit_values(self,query,values):
        try:
            # データベースへの接続
            db_connection = self.database_connector.connect()
            # クエリの実行
            return db_connection.commit_values(query,values)

        except Exception as error:
            # エラーが発生した場合はエラーハンドリングを実行
            print("ERROR2:", error)
            self.handle_error(error)

    def db_commit_many(self, query, values):
        try:
            # データベースへの接続
            db_connection = self.database_connector.connect()
            # クエリの実行
            return db_connection.commit_many(query, values)

        except Exception as error:
            # エラーが発生した場合はエラーハンドリングを実行
            print("ERROR2:", error)
            self.handle_error(error)

    def run_interval(self):
        while True:
            print("システムを起動しています")
            if not self.in_process_flag:
                self.in_process_flag = True
                try:
                    self.main()
                finally:
                    self.in_process_flag = False
            interval = int(self.interval)
            time.sleep(interval)
 
    def handle_error(self, error):
        print("Error2:", error)
        logging.basicConfig(filename="error.log", level=logging.ERROR)
        # 現在の日時を取得
        now = datetime.datetime.now()
        # エラーログを記録
        logging.error(now.strftime("%Y-%m-%d %H:%M:%S") + " " + str(error))

    def print(self, OKNG,info):
        now = datetime.datetime.now()
        if OKNG == "OK":
            # OKの場合のメッセージ
            message = f" {Fore.WHITE}{Back.YELLOW}{Style.BRIGHT}{now.strftime('%Y-%m-%d %H:%M:%S')}{Back.BLACK} {info} {Style.NORMAL}"
        else:
            # NGの場合のメッセージ
            message = f" {now.strftime('%Y-%m-%d %H:%M:%S')}{Fore.WHITE}{Back.RED}{Style.BRIGHT} {info} {Style.NORMAL}"

        print(message)

    
    def logging(self,info):
        now = datetime.datetime.now()
        log_message = f" {now.strftime('%Y-%m-%d %H:%M:%S')} {info}"
        logging.info(log_message)

    def send_email(self, message_body):
        recipient = self.recipient.split(';')
        recipient_cc = self.recipient_cc.split(';')
        subject = self.subject
        message_header = f"{self.message_header}<br><br>"
        message_header += f"<font style='color:blue;font-weight:bold;font-size:18px'>{self.message_header2}</font><br><br>"
        message_footer = f"<br><br>{self.message_footer}<br><br>{self.message_footer2}"
        # Email通知の送信
        self.email_notifier.send_email(subject, message_header,message_body, message_footer, recipient, recipient_cc)



