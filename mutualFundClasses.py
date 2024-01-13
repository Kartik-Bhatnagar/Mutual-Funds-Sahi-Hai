class amc():#assest management company
    def __init__(self,name):
        self.amc_name = name
        
    def add_funds_list(self,fundslist):
        self.funds_list = fundslist #list of mutualFund objects

    def print_funds_list(self):
        print("The funds under {self.mf_name} are the following : ")
        for mf in self.funds_list:
            print(mf.fundName) #accessing the attribute of mutual Fund object

    def show_details(self):
        print(f"{self.amc_name} was setup on {self.setup_date}. There are total {len(self.funds_list)} funds provided by this AMC. \nFollowing is the list of the mutual funds of this amc.")
        for fund in self.funds_list:
            print(fund.fundName)  

    def add_key_info(self,mf_name,setup_date,incorp_Date,sponsor_name,trust_org,cio,md,co,iso):
        self.mf_name = mf_name
        self.setup_date = setup_date
        self.icorp_date = incorp_Date
        self.sponsor_name = sponsor_name
        self.trust_org = trust_org
        self.perosonals = {"cio":["Chief Information Officer",cio],
                           "md":["CEO or MD",md],
                           "co":["Compliance Officer",co], 
                           "iso":["Investor Service Officer",iso] 
                        }
    def print_personals(self):
        for key in self.perosonals:
            print(f"{self.perosonals[key][0]+' : ':<30}  {self.perosonals[key][1]:>30}" )
        return

    def print_key_info(self):
        print(f"{'Mutual Fund Name :':<30} {self.mf_name:>30}")
        print(f"{' Setup Date : ':<30} {self.setup_date :>30}")
        print(f"{'AMC Incorporation Date : ':<30} {self.icorp_date :>30}")
        print(f"{'Soponsor Name : ':<30} {self.sponsor_name:>30}")
        print(f"{'Trustee organisation : ':<30}{self.trust_org :>30}")
        print(f"{'Associated personal details -> ':<30}")
        self.print_personals()
        

    def add_amc_desc(self,amc_desc):
        self.amc_description = amc_desc

    def get_amc_desc(self):
        return self.amc_description    
              


class mutualFund():
    def __init__(self,name) -> None:
        self.fundName = name

    def add_info(self,minsip,rating,fund_size,risk,category,holdings):
        self.minSipAmount = minsip
        self.rating = rating
        self.fund_size = fund_size
        self.risk = risk
        self.categoty = category
    
    def add_holdings_cat(self,eq_ratio,debt_ratio,cash_ratio):#add to holdings category [equity, debt,cash]
        self.holding_cat = {"equity":eq_ratio,
                            "debt":debt_ratio,
                            "cash":cash_ratio}
    def add_equity_holdings(self,eq_holdings):
        self.holdings = eq_holdings #dictinary of holdings with their ratio
   

# make different classes based on type of mutual fund eg: index fund or tax fund etc
#! Inheritance
# class taxMutualFund(mutualFund):
#     def __init__(self,name):
#         super().__init__(self,name,minsip,category="tax-saving") 



# canara = mutualFund()
