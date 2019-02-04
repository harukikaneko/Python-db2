from mig_com import *

#import pdb

# 標準出力コードをutf-8に指定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("###########################")
print("PROC migration Start.")

select_sql = sqlAttr.GET_PROC_DIM_1
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

    # PR_PROC_LINE_CODE + _ + PR_PROC_CODE
    val_CPROCCD = ibm_db.result(select_stmt, 0) + \
        u"_" + ibm_db.result(select_stmt, 2)
    val_CLEVEL1CD = ibm_db.result(select_stmt, 0)  # PR_PROC_LINE_CODE
    val_CLEVEL2CD = ibm_db.result(select_stmt, 2)  # PR_PROC_CODE
    val_CLEVEL2NM = ibm_db.result(select_stmt, 3)  # PR_PROC_NAME
    val_CLEVEL3CD = str(ibm_db.result(select_stmt, 1))  # PR_PROC_ORDER

    if len(val_CLEVEL3CD) < 2:
        val_CLEVEL3CD = u"0" + val_CLEVEL3CD

    insert_proc_dim_sql = "insert into " + mrtEnv.PLN_DBSCHEMA + \
        u"." + tableInfoAttr.PROC_DIM + \
        u" (" + tableInfoAttr.PROC_DIM_CPROCCD + \
        u", " + tableInfoAttr.PROC_DIM_CLEVEL1CD + \
        u", " + tableInfoAttr.PROC_DIM_CLEVEL2CD + \
        u", " + tableInfoAttr.PROC_DIM_CLEVEL2NM + \
        u", " + tableInfoAttr.PROC_DIM_CLEVEL3CD + " ) " + \
        u"values ( '" + val_CPROCCD + \
        u"', '" + val_CLEVEL1CD + \
        u"', '" + val_CLEVEL2CD + \
        u"', '" + val_CLEVEL2NM + \
        u"', '" + val_CLEVEL3CD + \
        u"' )"

    try:
        ibm_db.exec_immediate(giv_db_conn, insert_proc_dim_sql)
    except:
        print("ERROR! cpart：" + val_CPROCCD)
        print(ibm_db.stmt_error())
        print(ibm_db.stmt_errormsg())


print("PART migration End.")
print("###########################")

ibm_db.close
