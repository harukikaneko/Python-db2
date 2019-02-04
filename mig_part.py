from mig_com import *

#import pdb

# 標準出力コードをutf-8に指定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# sys.exit(0)

"""
# DB接続情報
# if_db
if_db_conn = ibm_db.connect(
    mrtEnv.IF_DBNM, mrtEnv.IF_DBUSERNM, mrtEnv.IF_DBPASSWD)
active = ibm_db.active(if_db_conn)
print(u'if db activation : ', str(active))
# planner_db
giv_db_conn = ibm_db.connect(
    mrtEnv.PLN_DBNM, mrtEnv.PLN_DBUSERNM, mrtEnv.PLN_DBPASSWD)
active = ibm_db.active(if_db_conn)
print(u'pln db activation : ', str(active))
"""


print("###########################")
print("PART migration Start.")

select_sql = sqlAttr.GET_PART_CODE_1
print(select_sql)

# if db接続
if_db_conn = connect_db(mrtEnv.IF_DBNM)
# if dbからのselect実行
select_stmt = ibm_db.exec_immediate(if_db_conn, select_sql)

# planner db接続
giv_db_conn = connect_db(mrtEnv.PLN_DBNM)

i = 0
while ibm_db.fetch_row(select_stmt) != False:
    i = i+1
    sys.stdout.write("\r%d" % i)
    sys.stdout.flush()

    # pdb.set_trace()
    val_CSITECD = '241'
    val_CPARTCD = ibm_db.result(select_stmt, 0)  # PR_ITEM_NAME
    val_CPROCCD = ibm_db.result(select_stmt, 1) + \
        u"_"+ibm_db.result(select_stmt, 2)  # CPROCCD

    val_CPART = val_CSITECD + u" _" + val_CPARTCD + \
        u" _" + val_CPROCCD + u" _" + val_CSITECD

    val_CPMID = tableInfoAttr.ATTR_FLG_P
    val_CPMIDX = tableInfoAttr.ATTR_FLG_P
    val_CPEGFLG = tableInfoAttr.ATTR_FLG_Y
    val_CDSPFLG = tableInfoAttr.ATTR_FLG_Y
    val_NDSPODR = tableInfoAttr.ATTR_VALUE_9999

    insert_part_mstr_sql = "insert into " + mrtEnv.PLN_DBSCHEMA + \
        u"." + tableInfoAttr.PART_MSTR + \
        u" (" + tableInfoAttr.PART_MSTR_CPART + \
        u", " + tableInfoAttr.PART_MSTR_CPMID + \
        u", " + tableInfoAttr.PART_MSTR_CPMIDX + \
        u", " + tableInfoAttr.PART_MSTR_CPARTN + \
        u", " + tableInfoAttr.PART_MSTR_CPEGFLG + \
        u", " + tableInfoAttr.PART_MSTR_CDSPFLG + \
        u", " + tableInfoAttr.PART_MSTR_NDSPODR + \
        u", " + tableInfoAttr.PART_MSTR_CSITECD + \
        u", " + tableInfoAttr.PART_MSTR_CPARTCD + \
        u", " + tableInfoAttr.PART_MSTR_CPROCCD + \
        u", " + tableInfoAttr.PART_MSTR_CSITETCD + " ) " + \
        u"values ( '" + val_CPART + \
        u"', '" + val_CPMID + \
        u"', '" + val_CPMIDX + \
        u"', '" + val_CPARTCD + \
        u"', '" + val_CPEGFLG + \
        u"', '" + val_CDSPFLG + \
        u"', " + val_NDSPODR + \
        u", '" + val_CSITECD + \
        u"', '" + val_CPARTCD + \
        u"', '" + val_CPROCCD + \
        u"', '" + val_CSITECD + \
        u"' )"

    val_NAHEAD = tableInfoAttr.ATTR_VALUE_MINUS1
    val_CSAFE = tableInfoAttr.ATTR_VALUE_0
    val_NSAFSTKL = tableInfoAttr.ATTR_VALUE_0
    val_NSTRSTKL = tableInfoAttr.ATTR_VALUE_0
    val_CNSTN = tableInfoAttr.ATTR_FLG_Y
    val_CASAP = tableInfoAttr.ATTR_FLG_N
    val_NEXECPEN = tableInfoAttr.ATTR_VALUE_0
    val_NSTRT = tableInfoAttr.ATTR_VALUE_0
    val_NPIPELEN = tableInfoAttr.ATTR_VALUE_0
    val_NBASE = tableInfoAttr.ATTR_VALUE_0
    val_NDTERM = tableInfoAttr.ATTR_VALUE_0
    val_NATSPRIOR = tableInfoAttr.ATTR_VALUE_0
    val_CCNSFLG = tableInfoAttr.ATTR_BLANK
    val_CIGNORLOT = tableInfoAttr.ATTR_BLANK
    val_CPRMIGNORLOT = tableInfoAttr.ATTR_BLANK
    val_CNOYIELD = tableInfoAttr.ATTR_BLANK

    insert_part_inf_sql = "insert into " + mrtEnv.PLN_DBSCHEMA + \
        u"." + tableInfoAttr.PART_INF + \
        u" (" + tableInfoAttr.PART_INF_CPART + \
        u", " + tableInfoAttr.PART_INF_NAHEAD + \
        u", " + tableInfoAttr.PART_INF_CSAFE + \
        u", " + tableInfoAttr.PART_INF_NSAFSTKL + \
        u", " + tableInfoAttr.PART_INF_NSTRSTKL + \
        u", " + tableInfoAttr.PART_INF_CNSTN + \
        u", " + tableInfoAttr.PART_INF_CASAP + \
        u", " + tableInfoAttr.PART_INF_NEXECPEN + \
        u", " + tableInfoAttr.PART_INF_NSTRT + \
        u", " + tableInfoAttr.PART_INF_NPIPELEN + \
        u", " + tableInfoAttr.PART_INF_NBASE + \
        u", " + tableInfoAttr.PART_INF_NDTERM + \
        u", " + tableInfoAttr.PART_INF_NATSPRIOR + \
        u", " + tableInfoAttr.PART_INF_CCNSFLG + \
        u", " + tableInfoAttr.PART_INF_CIGNORLOT + \
        u", " + tableInfoAttr.PART_INF_CPRMIGNORLOT + \
        u", " + tableInfoAttr.PART_INF_CNOYIELD + " ) " + \
        u"values ( '" + val_CPART + \
        u"', " + val_NAHEAD + \
        u", '" + val_CSAFE + \
        u"', " + val_NSAFSTKL + \
        u", " + val_NSTRSTKL + \
        u", '" + val_CNSTN + \
        u"', '" + val_CASAP + \
        u"', " + val_NEXECPEN + \
        u", " + val_NSTRT + \
        u", " + val_NPIPELEN + \
        u", " + val_NBASE + \
        u", " + val_NDTERM + \
        u", " + val_NATSPRIOR + \
        u", '" + val_CCNSFLG + \
        u"', '" + val_CIGNORLOT + \
        u"', '" + val_CPRMIGNORLOT + \
        u"', '" + val_CNOYIELD + \
        u"' )"

    try:
        ibm_db.exec_immediate(giv_db_conn, insert_part_mstr_sql)
        ibm_db.exec_immediate(giv_db_conn, insert_part_inf_sql)
    except:
        print("ERROR! cpart：" + val_CPART)
        print(ibm_db.stmt_error())
        print(ibm_db.stmt_errormsg())


print("PART migration End.")
print("###########################")

ibm_db.close
