import os
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = os.path.abspath('./venv/selenium/webdriver/chrome/chromedriver.exe')

TEST = ('AD','AE','AF')
CC = ('AD','AE','AF','AG','AI','AL','AM','AO','AQ','AR','AS','AT','AU','AW','AX','AZ',
	'BA','BB','BD','BE','BF','BG','BH','BI','BJ','BL','BM','BN','BO','BQ','BR','BS',
	'BT','BV','BW','BY','BZ','CA','CC','CD','CF','CG','CH','CI','CK','CL','CM','CN',
	'CO','CR','CU','CV','CW','CX','CY','CZ','DE','DJ','DK','DM','DO','DZ','EC','EE',
	'EG','EH','ER','ES','ET','FI','FJ','FK','FM','FO','FR','GA','GB','GD','GE','GF',
	'GG','GH','GI','GL','GM','GN','GP','GQ','GR','GS','GT','GU','GW','GY','HK','HM',
	'HN','HR','HT','HU','ID','IE','IL','IM','IN','IO','IQ','IR','IS','IT','JE','JM',
	'JO','JP','KE','KG','KH','KI','KM','KN','KP','KR','KW','KY','KZ','LA','LB','LC',
	'LI','LK','LR','LS','LT','LU','LV','LY','MA','MC','MD','ME','MF','MG','MH','MK',
	'ML','MM','MN','MO','MP','MQ','MR','MS','MT','MU','MV','MW','MX','MY','MZ','NA',
	'NC','NE','NF','NG','NI','NL','NO','NP','NR','NU','NZ','OM','PA','PE','PF','PG',
	'PH','PK','PL','PM','PN','PR','PS','PT','PW','PY','QA','RE','RO','RS','RU','RW',
	'SA','SB','SC','SD','SE','SG','SH','SI','SJ','SK','SL','SM','SN','SO','SR','SS',
	'ST','SV','SX','SY','SZ','TC','TD','TF','TG','TH','TJ','TK','TL','TM','TN','TO',
	'TR','TT','TV','TW','TZ','UA','UG','UM','US','UY','UZ','VA','VC','VE','VG','VI',
	'VN','VU','WF','WS','YE','YT','ZA','ZM','ZW'
)

countries = []
for c in CC:
	print(c + ' - started')
	driver = webdriver.Chrome(DRIVER_PATH)
	driver.get('https://www.iso.org/obp/ui/#iso:code:3166:' + c)
	wait = WebDriverWait(driver, 30)
	summary = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'core-view-summary')))
	names = summary.find_elements_by_class_name('core-view-field-name')
	values = summary.find_elements_by_class_name('core-view-field-value')

	country = {}
	for n, v in zip(names, values):
		country[n.text] = v.text

	countries.append(country)
	driver.close()
	print(c + ' - finished')
	time.sleep(10)

with open('countries.csv', 'w', newline='') as f:
	writer = csv.DictWriter(f, countries[0].keys(), extrasaction='ignore')
	
	writer.writeheader()
	writer.writerows(countries)