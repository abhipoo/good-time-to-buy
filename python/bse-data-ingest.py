from bsedata.bse import BSE
import csv

b = BSE()
#print(b)

#q = b.getQuote('524348')
#print(type(q))

api_response = b.getScripCodes()

with open("scrip_codes_seed.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(['scrip_code', 'company_name']) #write header
    w.writerows(api_response.items()) #write rows