import mutualFundClasses

# this is a sample page to add details maunally of AMC named  NJ Asset Management Private Limited
nj_amc = mutualFundClasses.amc("NJ Asset Management Private Limited")
nj_amc.add_key_info("NJ Mutual Fund","30 Apr 2021","October,21 2005","NJ Invest Private Limited"\
                    ,"NJ Trustee Private Limited","Mr. Bijon Pani","Mr. Ravi Shastri","Ms. Punam Upadhay","Mr Vineet Nayar")

nj_overnight_mf = mutualFundClasses.mutualFund("NJ Overnight Fund Direct Growth")

nj_amc.print_key_info()