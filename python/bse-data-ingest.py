from bsedata.bse import BSE
import csv

b = BSE()

# Create scrip codes seed file for creating static dimension
api_response = b.getScripCodes()
with open("scrip_codes_seed.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(['scrip_code', 'company_name']) #write header
    w.writerows(api_response.items()) #write rows

# Create daily change file
#q = b.getQuote('524348')
#print(type(q))