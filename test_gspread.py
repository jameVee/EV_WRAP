import gspread

sa =  gspread.service_account(filename="se-02-a72d8-759b1dee5bc7.json")
sh = sa.open("Time_Auction_EV")
wks = sh.worksheet("Sheet1")

data = ["1","EV wrap",500,"30/3/2023","0:25",730]
wks.append_row(data)
