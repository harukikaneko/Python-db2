#import unicodedata

import io
import sys
import ibm_db

# 環境定義
import mrtEnv

# 定数クラス
import sqlAttr
import tableInfoAttr


# DB接続
def connect_db(dbName):
    if dbName == mrtEnv.IF_DBNM:
        dbUser = mrtEnv.IF_DBUSERNM
        dbPass = mrtEnv.IF_DBPASSWD

    elif dbName == mrtEnv.PLN_DBNM:
        dbUser = mrtEnv.PLN_DBUSERNM
        dbPass = mrtEnv.PLN_DBPASSWD

    try:
        db_conn = ibm_db.connect(dbName, dbUser, dbPass)
        active = ibm_db.active(db_conn)
        print(dbName, u' activation : ', str(active))

        return db_conn
    except:
        print(u'db connect error : ', dbName)
        print(ibm_db.stmt_error())
        print(ibm_db.stmt_errormsg())
        sys.exit()


"""
# planner_db
try:
    giv_db_conn = ibm_db.connect(
        mrtEnv.PLN_DBNM, mrtEnv.PLN_DBUSERNM, mrtEnv.PLN_DBPASSWD)
    active = ibm_db.active(if_db_conn)
    print(u'pln db activation : ', str(active))
except:
    print(u'pln db connect error : ', str(active))
    print(ibm_db.stmt_error())
    print(ibm_db.stmt_errormsg())
    sys.exit()
"""
