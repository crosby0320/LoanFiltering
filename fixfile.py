import string

maxlinesread = 300
theOrderOfStuff = [
    ["loan_amnt", "funded_amnt", "funded_amnt_inv", "term", "int_rate", "installment", "grade",
     "emp_length", "home_ownership", "annual_inc", "loan_status", "delinq_2yrs",
     "fico_range_low", "fico_range_high", "inq_last_6mths", "mths_since_last_delinq",
     "mths_since_last_record", "open_acc", "pub_rec", "revol_bal", "revol_util", "total_acc",
     "out_prncp", "out_prncp_inv", "total_pymnt", "total_pymnt_inv", "total_rec_prncp",
     "total_rec_int", "total_rec_late_fee", "mths_since_last_major_derog", "acc_now_delinq",
     "tot_coll_amt", "tot_cur_bal", "open_acc_6m", "open_act_il", "open_il_12m", "open_il_24m",
     "mths_since_rcnt_il", "total_bal_il", "il_util", "open_rv_12m", "open_rv_24m", "max_bal_bc",
     "all_util", "total_rev_hi_lim", "inq_fi", "total_cu_tl", "inq_last_12m", "acc_open_past_24mths",
     "avg_cur_bal", "bc_open_to_buy", "bc_util", "chargeoff_within_12_mths", "delinq_amnt",
     "mo_sin_old_il_acct", "mo_sin_old_rev_tl_op", "mo_sin_rcnt_rev_tl_op", "mo_sin_rcnt_tl",
     "mort_acc", "mths_since_recent_bc", "mths_since_recent_bc_dlq", "mths_since_recent_inq",
     "mths_since_recent_revol_delinq", "num_accts_ever_120_pd", "num_actv_bc_tl",
     "num_actv_rev_tl", "num_bc_sats", "num_bc_tl", "num_il_tl", "num_op_rev_tl",
     "num_rev_accts", "num_rev_tl_bal_gt_0", "num_sats", "num_tl_120dpd_2m", "num_tl_30dpd",
     "num_tl_90g_dpd_24m", "num_tl_op_past_12m", "pct_tl_nvr_dlq", "percent_bc_gt_75",
     "pub_rec_bankruptcies", "tax_liens", "tot_hi_cred_lim", "total_bal_ex_mort",
     "total_bc_limit", "total_il_high_credit_limit", "revol_bal_joint", "sec_app_fico_range_low",
     "sec_app_fico_range_high", "sec_app_earliest_cr_line", "sec_app_inq_last_6mths", "sec_app_mort_acc"],

    ["id", "member_id", "sub_grade", "emp_title", "verification_status", "issue_d", "pymnt_plan", "url",
     "desc", "earliest_cr_line", "last_pymnt_d", "purpose", "title", "zip_code", "addr_state", "initial_list_status",
     "recoveries",
     "collection_recovery_fee", "last_fico_range_high", "last_fico_range_low", "collections_12_mths_ex_med",
     "last_pymnt_amnt", "next_pymnt_d", "last_credit_pull_d", "policy_code", "application_type",
     "annual_inc_joint", "dti_joint", "verification_status_joint", "dti", "sec_app_open_acc", "sec_app_revol_util",
     "sec_app_open_act_il", "sec_app_num_rev_accts", "sec_app_chargeoff_within_12_mths",
     "sec_app_collections_12_mths_ex_med", "sec_app_mths_since_last_major_derog", "hardship_flag",
     "hardship_type", "hardship_reason", "hardship_status", "deferral_term", "hardship_amount",
     "hardship_start_date", "hardship_end_date", "payment_plan_start_date", "hardship_length",
     "hardship_dpd", "hardship_loan_status", "orig_projected_additional_accrued_interest",
     "hardship_payoff_balance_amount", "hardship_last_payment_amount", "disbursement_method",
     "debt_settlement_flag", "debt_settlement_flag_date", "settlement_status", "settlement_date",
     "settlement_amount", "settlement_percentage", "settlement_term\n"],

    []
]
listOfIndexes = [[], [], []]


class allDataInfo:
    titles = []
    data = []

    def __init__(self):
        self.titles = ""

    def addInTheTitles(self, t):
        self.titles = t.split(",")

    def addDataToList(self, d):
        self.data.append(d)


class LoadData:
    datavector = []

    def __init__(self, dataimputtingin):
        self.datavector = self.readinstringdatatoarray(dataimputtingin)

    @staticmethod
    def readinstringdatatoarray(datacommingin):
        vector = datacommingin.split(",")
        return vector


def readFile(nameOfFile):
    allstuff = allDataInfo()
    with open(nameOfFile) as f:
        count = 0
        for line in f:
            if count == 1:
                allstuff.addInTheTitles(line)
            elif count > 1:
                allstuff.addDataToList(LoadData(line))
            if count == maxlinesread:
                break
            count += 1
    return allstuff


def checkIfLegit():
    for a in xrange(len(data.data)):
        # if a not in {}:
        for column in xrange(len(listOfIndexes[0])):
            if data.data[a].datavector[listOfIndexes[0][column]] == "":
                data.data[a].datavector[listOfIndexes[0][column]] = 0
            else:
                try:
                    data.data[a].datavector[listOfIndexes[0][column]] = float(
                        data.data[a].datavector[listOfIndexes[0][column]])
                except:
                    print '!!!!!!!cant convert to float: {0} title: {1} index: {2}'.format(
                        data.data[a].datavector[listOfIndexes[0][column]], data.titles[listOfIndexes[0][column]],
                        listOfIndexes[0][column])
                    exit()


def findOutWhatToRead():
    count = 0
    for columnIndex in xrange(len(data.titles)):
        if data.titles[columnIndex] in theOrderOfStuff[0]:
            # print "keep" , data.titles[i]
            listOfIndexes[0].append(columnIndex)
        elif data.titles[columnIndex] in theOrderOfStuff[1]:
            # print "No" , data.titles[i]
            listOfIndexes[1].append(columnIndex)
        else:
            # print "IDK what to do " ,data.titles[i]
            count += 1
            listOfIndexes[2].append(columnIndex)
        if count == 10:
            break
    for columnIndex in listOfIndexes[2]:
        print '{0} {1:20}  : '.format(columnIndex, data.titles[columnIndex]),
        for jj in xrange(0, 6):
            print '{0}'.format(data.data[jj].datavector[columnIndex]),
        print ""
    if len(listOfIndexes[2]) != 0:
        exit()


def printForProgrammer():
    for ii in xrange(len(listOfIndexes[0])):
        print '{0:4} {1:20} : '.format(listOfIndexes[0][ii], data.titles[listOfIndexes[0][ii]]),
        for jj in xrange(0, 8):
            print ' {0:8}'.format(data.data[jj].datavector[listOfIndexes[0][ii]]),
        print ""


def formatData():
    for colunmIndex in xrange(len(listOfIndexes[0])):
        for loanIndex in xrange(len(data.data)):
            ######################################################################################
            if data.titles[listOfIndexes[0][colunmIndex]] == "term":

                if data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == " 36 months":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 36
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == " 60 months":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 60
                else:
                    print "old value:", data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]], "from : ", \
                        data.titles[
                            listOfIndexes[0][colunmIndex]]
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = '?'

            ######################################################################################
            elif data.titles[listOfIndexes[0][colunmIndex]] == "int_rate" or data.titles[
                listOfIndexes[0][colunmIndex]] == "revol_util":
                data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = data.data[loanIndex].datavector[
                    listOfIndexes[0][colunmIndex]].replace("%", "")

            ######################################################################################
            elif data.titles[listOfIndexes[0][colunmIndex]] == "grade":
                if data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "A":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 10
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "B":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 9
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "C":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 8
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "D":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 7
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "E":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 6
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "F":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 5
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "G":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 4
                else:
                    print "old value:", data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]], "from : ", \
                        data.titles[
                            listOfIndexes[0][colunmIndex]]
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = '?'

            elif data.titles[listOfIndexes[0][colunmIndex]] == "emp_length":
                if "years" in data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] or "year" in \
                        data.data[loanIndex].datavector[
                            listOfIndexes[0][colunmIndex]]:
                    l = string.maketrans('', '')
                    nodigs = l.translate(l, string.digits)
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = data.data[loanIndex].datavector[
                        listOfIndexes[0][colunmIndex]].translate(l, nodigs)
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "n/a":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 0
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == " Audit":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 0
                else:
                    print "old value:", data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]], "from : ", \
                        data.titles[
                            listOfIndexes[0][colunmIndex]]
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = '?'


            elif data.titles[listOfIndexes[0][colunmIndex]] == "home_ownership":
                if data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "RENT":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 5
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "MORTGAGE":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 7.5
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "OWN":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 10
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "AUDIT":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 0
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == " Med D Support":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 0
                else:
                    print "old value:", data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]], "from : ", \
                        data.titles[
                            listOfIndexes[0][colunmIndex]]
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = "?"

            elif data.titles[listOfIndexes[0][colunmIndex]] == "loan_status":
                if data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "Current":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 1
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "Fully Paid":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 1
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "Default":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 1
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "Charged Off":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 1
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "Late (16-30 days)":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 1
                elif data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] == "Late (31-120 days)":
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 1
                else:
                    print "old value:", data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]], "from : ", \
                        data.titles[
                            listOfIndexes[0][colunmIndex]]
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = "?"

            elif data.titles[listOfIndexes[0][colunmIndex]] == "annual_inc":
                if "years" in data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]]:
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 0

            elif data.titles[listOfIndexes[0][colunmIndex]] == "delinq_2yrs":
                if "AZ" in data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]]:
                    data.data[loanIndex].datavector[listOfIndexes[0][colunmIndex]] = 0


#################################################################################################
#################################################################################################
###################################        Main     #############################################
#################################################################################################
#################################################################################################

data = readFile("AllLoanStats_2016Q4.csv")

for i in xrange(len(data.data)):
    for j in xrange(len(data.data[i].datavector)):
        data.data[i].datavector[j] = data.data[i].datavector[j].replace("\"", "")

for i in xrange(len(data.titles)):
    data.titles[i] = data.titles[i].replace("\"", "")

findOutWhatToRead()

formatData()

print "======================================================================================="
printForProgrammer()
print "======================================================================================="
checkIfLegit()
