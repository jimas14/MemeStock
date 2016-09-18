from pytrends.request import TrendReq

google_username = 'memestocks9000'
google_password = 'memesrule1'

pytrend = TrendReq(google_username, google_password, custom_useragent=None)

payload = {
	'q' : 'harambe',
	'date': 'today 7-d'
}

trend = pytrend.trend(payload)

print(trend)

df = pytrend.trend(payload, return_type='dataframe')

print(df)