import multiprocessing
import secrets
import threading
import traceback
import faker
from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask
from flask import request
import datetime
import os
import random
from faker import Faker

INFINITY_FILENAME = 'infinity.log'
APACHE_FILENAME = 'tomcat_access.txt'
PERF_FILENAME = 'infinity-perf.log'
LOG_DIRECTORY = '/var/log/'
LOG_FOLDER_NAME = 'loggerman'
FULL_PATH = LOG_DIRECTORY + LOG_FOLDER_NAME
INFI_REC_COUNT = ""
TOMCAT_REC_COUNT = ""
PERF_REC_COUNT = ""

app = Flask(__name__)
faker = Faker()


@app.route('/')
def index():
    goblin = request.args.get("goblin", "")
    global INFI_REC_COUNT
    global TOMCAT_REC_COUNT
    global PERF_REC_COUNT
    INFI_REC_COUNT = request.args.get("infinty_rec_count", "")
    TOMCAT_REC_COUNT = request.args.get("tomcat_rec_count", "")
    PERF_REC_COUNT = request.args.get("perf_rec_count", "")

    if goblin:
        baker = multi_log_tasker(goblin)
    else:
        baker = ""
    return (
            """<form action="" method="get">
                Enter start to generate logs : <input type="text" name="goblin">
                <br>Enter no of tomcat events required per 10secs interval : <input type="number" name="tomcat_rec_count"\n>
                <br>Enter no of infinity events required per 10secs interval : <input type="number" name="infinty_rec_count"\n>
                <br>Enter no of perf events required per 10secs interval : <input type="number" name="perf_rec_count"\n>                
                <br><input type="submit" value="submit">
            </form>"""
            + "status: "
            + baker
    )


def log_filecheck():
    files_list = [INFINITY_FILENAME, APACHE_FILENAME, PERF_FILENAME]
    path = os.path.join(LOG_DIRECTORY, LOG_FOLDER_NAME)
    if not os.path.isdir(path):
        try:
            os.mkdir(path, 0o777)
        except OSError:
            print("error while creating the APP Directory")
            exit(0)
    else:
        pass

    for i in files_list:
        try:
            with open(os.path.join(LOG_DIRECTORY + LOG_FOLDER_NAME, i), 'w') as temp_file:
                print("File creation done - %s", i)
            temp_file.close()
        except Exception:
            print("file creation error %s", i)
            exit(1)


def infinity_log_producer():
    message_ml1 = """Plugin.IETLProductModelLoaderPlugin etlOptionCovTermPattern - NameAmount of InsurancePublic ID :nullCode :FM_EDPHardwareAmtOfInsLmtDisplayName :
                    (ETLOptionCovTermPattern) {ID=-34256, BeanVersion=null, ClausePattern=-35035, Code=FM_EDPHardwareAmtOfInsLmt, ColumnName=ChoiceTerm1, CovTermType=Option, ModelType=Limit, Name=Amount of Insurance, PatternID=FM_EDPHardwareAmtOfInsLmt, PublicID=null, Subtype=ETLOptionCovTermPattern, ValueType=money}"""
    message_ml2 = """ Server.Database.Upgrade Skipping non-applicable Version Trigger at minor version 197 - Verifies that the maui-dbupgrade-config.properties file can be opened, read, and that the properties and values are in the following formats:
 - AccountContact.MapSubtype.Property = Value
 - PolicyContact.MapSubtype.Property = Value
 - PolicyContactRole.Column.Property.Scope = All or CSV Value
 - PolicyContactRole.Column.Property.Value = Entity.Column
 Where the Entity is PolicyContact, AccountContact or Contact. """
    message_ml3 = """RateBook [RateBook] [su] [[farm_package_ontario:00007]] java.net.ConnectException: Connection timed out (Connection timed out)
	at java.net.PlainSocketImpl.socketConnect(Native Method)
	at java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:344)
	at java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:200)
	at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:182)
	at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:392)
	at java.net.Socket.connect(Socket.java:596)
	at sun.security.ssl.SSLSocketImpl.connect(SSLSocketImpl.java:630)
	at sun.security.ssl.BaseSSLSocketImpl.connect(BaseSSLSocketImpl.java:160)
	at sun.net.NetworkClient.doConnect(NetworkClient.java:180)
	at sun.net.www.http.HttpClient.openServer(HttpClient.java:463)
	at sun.net.www.http.HttpClient.openServer(HttpClient.java:558)
	at sun.net.www.protocol.https.HttpsClient.<init>(HttpsClient.java:264)
	at sun.net.www.protocol.https.HttpsClient.New(HttpsClient.java:367)
	at sun.net.www.protocol.https.AbstractDelegateHttpsURLConnection.getNewHttpClient(AbstractDelegateHttpsURLConnection.java:191)
	at sun.net.www.protocol.http.HttpURLConnection.plainConnect(HttpURLConnection.java:999)
	at sun.net.www.protocol.https.AbstractDelegateHttpsURLConnection.connect(AbstractDelegateHttpsURLConnection.java:177)
	at sun.net.www.protocol.http.HttpURLConnection.getInputStream(HttpURLConnection.java:1367)
	at sun.net.www.protocol.https.HttpsURLConnectionImpl.getInputStream(HttpsURLConnectionImpl.java:268)
	at java.net.URL.openStream(URL.java:1070)
	at wmic.util.download.URLFileRetriever.storeFile(URLFileRetriever.gs:34)
	at wmic.datachange.ratebook.RateBookDetails.downloadRateBook(RateBookDetails.gs:54)
	at wmic.datachange.ratebook.RateBookDetails.getFilePath(RateBookDetails.gs:41)
	at wmic.datachange.ratebook.load.AutoLoadNewRateBookBase$block_0_$block_0_.invoke(AutoLoadNewRateBookBase.gs:36)
	at gw.lang.enhancements.CoreArrayEnhancement.each(CoreArrayEnhancement.gsx:236)
	at wmic.datachange.ratebook.load.AutoLoadNewRateBookBase$block_0_.invoke(AutoLoadNewRateBookBase.gs:30)
	at gw.lang.function.Function1.invokeWithArgs(Function1.java:13)
	at __proxy.generated.blocktointerface.ProxyForTransaction.BlockRunnable.run(Unknown Source)
	at gw.transaction.Transaction.runWithNewBundle(Transaction.java:46)
	at com.guidewire.pl.system.bundle.TransactionUtil.runWithNewBundle(TransactionUtil.java:39)
	at gw.transaction.Transaction.runWithNewBundle(Transaction.java:61)
	at wmic.datachange.ratebook.load.AutoLoadNewRateBookBase.loadBooks(AutoLoadNewRateBookBase.gs:28)
	at wmic.datachange.ratebook.load.AutoLoadNewRateBookBase.execute(AutoLoadNewRateBookBase.gs:19)
	at program_.__Program__9183.evaluate(Unknown Source)
	at gw.internal.gosu.parser.GosuProgram.runProgram(GosuProgram.java:421)
	at gw.internal.gosu.parser.GosuProgram.evaluate(GosuProgram.java:253)
	at gw.internal.gosu.parser.GosuProgram_Proxy.evaluate(gw.internal.gosu.parser.GosuProgram_Proxy:2)
	at gw.internal.gosu.parser.Expression.evaluate(Expression.java:61)
	at gw.internal.gosu.parser.expressions.Program.evaluate(Program.java:72)
	at com.guidewire.pl.domain.history.impl.DataChangeImpl$1.run(DataChangeImpl.java:81)"""

    messages_list = ["Plugin.CSIOOutbound [Plugin.CSIOOutbound] [sys] [CSIOResendPolicyProcess_WMIC.doWork] CSIO "
                     "Resend Policy Process - found 0 CSIO Policy Resend Requests",
                     "Plugin [Plugin] [unknown] [createSourceFromHTTPRequest] SSOAuthentication - UserId extracted from HTTP "
                     "header: null",
                     "Plugin [Plugin] [unknown] [createSourceFromHTTPRequest] Creating a null UserNameAuthenticationSource",
                     "Plugin [Plugin] [unknown] [authenticate] SSO login failed for user null: not authorized to use application",
                     "Server.Workflow Workflow stats writer wrote 0 rows(from Tue Oct 05 23:04:24 CDT 2021 to Wed Oct 06 00:04:24 CDT 2021)",
                     "Server.RunLevel Memory usage: 9311.902 MB used (both active and stale objects), 2976.096 MB free, 12288.000 MB total, 12288.000 MB max. --  Please read Memory usage logging in the System Administration Guide for information on how to interpret these numbers.",
                     message_ml1, message_ml2, message_ml3]
    print("started generating infinity logs")
    infintyfile_path = LOG_DIRECTORY + LOG_FOLDER_NAME + '/' + INFINITY_FILENAME
    infi_count = int(INFI_REC_COUNT)
    log_levels = ['INFO', 'ERROR', 'WARN', 'DEBUG']
    with open(infintyfile_path, 'a') as file:
        for i in range(infi_count):
            try:
                file.write(str(
                    "\n" + f"ste30pc0        " + datetime.datetime.now().strftime(
                        "%y-%m-%d %H:%M:%S,%p "+random.choice(log_levels)+" "+random.choice(messages_list))
                ))
            except Exception:
                traceback.print_exc()
        file.close()  # This close() is important


def perf_log_producer():
    print("started generating perf logs")
    perf_file_path = LOG_DIRECTORY + LOG_FOLDER_NAME + '/' + PERF_FILENAME
    perf_count = int(PERF_REC_COUNT)
    with open(perf_file_path, 'a') as file:
        for i in range(perf_count):
            try:
                file.write(str(
                    "\n" + f"[RequestId = @" + secrets.token_hex(
                        4) + "]" + " " + "[Event = AFTER]" + "[Date = " + datetime.datetime.now().strftime(
                        "[%b %d, %Y]") + "]" + "[Time = " + datetime.datetime.now().strftime(
                        "%H:%M:%S %p") + "]" + "[ServerId = ste30pc0][ServerLocalName = localhost][ServerIP = " + faker.ipv4() +
                    "][ServerPort = 8443][URL = /PolicyCenter.do][sessionid = _NONE][eventsource = _NONE][page = "
                    "Login:LoginScreen:_msgs][userid = _NONE] "
                    "[SEPARATOR = SEPARATOR][Size = 6539][Application = 12][Filter = 0][TotalFilter = 12][Response = "
                    "0][Writer = 0]"))
            except Exception:
                traceback.print_exc()
        file.close()  # This close() is important


def tomcat_log_producer():
    messages_list = ['"GET /ping HTTP/1.1" 200 1 "-" "Wawanesa User-Agent" 0 - "10.100.91.188" 0',
                     '"HEAD / HTTP/1.0" 200 - "-" "-" 0 - "-" 0',
                     '"GET /PolicyCenter.do HTTP/1.1" 200 6539 "-" "Wget/1.14 (linux-gnu)" 13 '
                     '5E9FB533459DA01580208CF2F3E7738A "-" 13"']
    print("started generating apache logs")
    apachefile_path = LOG_DIRECTORY + LOG_FOLDER_NAME + '/' + APACHE_FILENAME
    tomcat_count = int(TOMCAT_REC_COUNT)
    with open(apachefile_path, 'a') as file:
        for i in range(tomcat_count):
            try:
                file.write(str(
                    "\n" + faker.ipv4() + " " + '-' + " " + '-' + " " + datetime.datetime.now().strftime(
                        "[%d-%b-%y:%H:%M:%S,%f]") + " " + random.choice(messages_list)))
            except Exception:
                traceback.print_exc()
        file.close()  # This close() is important


def multi_log_tasker(status):

    if status == "start":
        log_filecheck()
        scheduler = BlockingScheduler()
        scheduler.add_job(infinity_log_producer, 'interval', seconds=10)
        scheduler.add_job(tomcat_log_producer, 'interval', seconds=10)
        scheduler.add_job(perf_log_producer, 'interval', seconds=10)
        scheduler.start()
    if status == "rotate":
        files_list = [INFINITY_FILENAME, APACHE_FILENAME, PERF_FILENAME]
        Current_Date = datetime.datetime.today().strftime('%d-%b-%Y')
        for i in files_list:
            file_path = LOG_DIRECTORY + LOG_FOLDER_NAME + '/'
            with open(file_path + i, 'a') as file:
                file.close()
            os.rename(file_path + i, file_path + Current_Date + i)
        print("files rotated with date extension in names")
    if status == "exit":
        exit(0)

    return status


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80)
