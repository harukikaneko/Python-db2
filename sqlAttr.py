from mrtEnv import PLN_DBSCHEMA, IF_DBSCHEMA
import tableInfoAttr

# GET_PART_CODE_0 = u"SELECT DISTINCT "+tableInfoAttr.PART_MIG_T1_C1+u","+tableInfoAttr.PART_MIG_T1_C2+u" FROM " + \
# IF_DBSCHEMA + u"."+tableInfoAttr.PART_MIG_T1 + \
#    " where "+tableInfoAttr.PART_MIG_T1_C3+u" = 'CX'"

GET_PART_CODE_1 = u"SELECT DISTINCT pm." + tableInfoAttr.PART_MIG_T1_C1 + u", pm." + tableInfoAttr.PART_MIG_T1_C2 + u", pf." + tableInfoAttr.PART_MIG_T2_C1 + u" FROM" + \
    u" ( SELECT "+tableInfoAttr.PART_MIG_T1_C1+","+tableInfoAttr.PART_MIG_T1_C2+u" FROM "+IF_DBSCHEMA+u"."+tableInfoAttr.PART_MIG_T1+u" WHERE "+tableInfoAttr.PART_MIG_T1_C3 + u"= 'CX' ) AS pm " + \
    u"INNER JOIN "+IF_DBSCHEMA+u"."+tableInfoAttr.PART_MIG_T2+u" AS pf ON pm."+tableInfoAttr.PART_MIG_T1_C2+u" = pf."+tableInfoAttr.PART_MIG_T1_C2 + \
    u" ORDER BY pm."+tableInfoAttr.PART_MIG_T1_C1 + \
    u", pm."+tableInfoAttr.PART_MIG_T1_C2+u", pf."+tableInfoAttr.PART_MIG_T2_C1


"""
GET_PROC_DIM_1 = u"SELECT " + tableInfoAttr.PROC_MIG_T1_C1 + u", " + tableInfoAttr.PROC_MIG_T1_C2 + u", " + \
    tableInfoAttr.PROC_MIG_T1_C3 + u" FROM "+IF_DBSCHEMA+u"." + tableInfoAttr.PROC_MIG_T1 + \
    u" ORDER BY "+tableInfoAttr.PROC_MIG_T1_C1 + \
    u", " + tableInfoAttr.PROC_MIG_T1_C2
"""

GET_PROC_DIM_1 = u"SELECT DISTINCT pf.PR_PROC_LINE_CODE, pf.PR_PROC_ORDER, pf.PR_PROC_CODE, pm.PR_PROC_NAME FROM "+IF_DBSCHEMA+u".PROCFROW_PR AS pf LEFT OUTER JOIN " + \
    IF_DBSCHEMA + \
    u".PROC_MSTR_PR AS pm ON pf.PR_PROC_CODE = pm.PR_PROC_CODE WHERE pf.PR_PROC_LINE_CODE IN ('3CD0','3D80','G550') ORDER BY pf.PR_PROC_LINE_CODE, pf.PR_PROC_ORDER"
