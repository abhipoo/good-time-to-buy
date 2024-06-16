from bsedata.bse import BSE
import csv
import datetime
import psycopg2
import json

b = BSE()

# # Create scrip codes seed file for creating static dimension
# api_response = b.getScripCodes()
# with open("scrip_codes_seed.csv", "w", newline="") as f:
#     w = csv.writer(f)
#     w.writerow(['scrip_code', 'company_name']) #write header
#     w.writerows(api_response.items()) #write rows

# Create daily change file
#q = b.getQuote('524348')

#query_date = datetime.date.today()
query_date = datetime.date(2024, 6, 12)
#query_date = datetime.date(2024, 6, 13)
#query_date = datetime.date(2024, 6, 14)
q = b.getBhavCopyData(query_date)
#print(q)

connection = psycopg2.connect("dbname=postgres user=gttb password=gttbpass port=5433")
cursor = connection.cursor()

print(type(q))

print(type(json.dumps(q)))

query_sql = """
insert into raw_bhavcopy (created_datetime, bhav_date, bhav_json_response) 
values ('{0}', '{1}', '{2}');
""".format(datetime.datetime.now(), query_date, json.dumps(q).replace("'",""))

cursor.execute(query_sql)
connection.commit()
