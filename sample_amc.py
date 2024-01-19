import mutualFundClasses
from mutualFundClasses import mutualFund

# this is a sample page to add details maunally of AMC named  NJ Asset Management Private Limited
#https://groww.in/mutual-funds/amc/nj-mutual-funds
nj_amc = mutualFundClasses.amc("NJ Asset Management Private Limited")
nj_amc.add_key_info("NJ Mutual Fund","30 Apr 2021","October,21 2005","NJ Invest Private Limited"\
                    ,"NJ Trustee Private Limited","Mr. Bijon Pani","Mr. Ravi Shastri","Ms. Punam Upadhay","Mr Vineet Nayar")

nj_overnight_mf = mutualFundClasses.mutualFund("NJ Overnight Fund Direct Growth")
nj_balanced_adv_mf = mutualFundClasses.mutualFund("MJ Balanced Advantage Fund")
nj_arb_mf = mutualFundClasses.mutualFund("NJ Arbitrage Fund")
nj_elss_mf = mutualFund("NJ ELSS Tax Saver Scheme Fund")
nj_flex_mf = mutualFund("NJ Flexi Cap Fund")

nj_amc.print_key_info()

nj_amc.add_funds_list([nj_overnight_mf,nj_balanced_adv_mf,nj_arb_mf,nj_elss_mf,nj_flex_mf])
nj_amc.print_funds_list()

#adding details 
#of 
#aj arbitage fund

nj_arb_mf.add_info(100,None,348,"Low","hybrid")

