# SnowPlow-Analytics
Technical test 
Support Engineer Technical Test: 

Q1. 
DNS Information:

Where is the domain registered & hosted?	
Registrar URL: https://www.ionos.com/
Datacenter: Amazon.com, Inc.
Server IP: 13.35.78.45
Location: United States of America
City: Boston
Nameservers: ns-1292.awsdns-33.org, ns-2027.awsdns-61.co.uk, ns-54.awsdns-06.com, ns-653.awsdns-17.net

What is the IP address & what company manages the emails?
Listed on most whois sites: 
52.84.64.106, 
52.84.64.245, 
52.84.64.39, 5
2.84.64.231

CMD pings 13.35.58.97
MX: aspmx.l.google.com

Q2. 
SSL certificate
Who issued the SSL certificate & when does it expire?

First Hop: 
Common name: *.snowplowanalytics.com
SANs: *.snowplowanalytics.com, snowplowanalytics.com
Valid from February 5, 2019 to March 6, 2020
Serial Number: 05a00293f5aa859faefeeebdd1af9b4f
Signature Algorithm: sha256WithRSAEncryption
Issuer: Amazon

Final Hop:
Common name: Starfield Services Root Certificate Authority - G2
Organization: Starfield Technologies, Inc.
Location: Scottsdale, Arizona, US
Valid from September 1, 2009 to June 28, 2034
Serial Number: 12037640545166866303 (0xa70e4a4c3482b77f)
Signature Algorithm: sha256WithRSAEncryption
Issuer: Starfield Technologies, Inc.



Is the certificate valid if installed for the website https://
discourse.snowplowanalytics.com? Why?

Yes it should be valid because certificate lists *.snowplowanalytics.com
which would include discourse in the asterisk.


Are the certificates installed with https://snowplowanalytics.com and https://
discourse.snowplowanalytics.com the same?

No – 
snowplowanalytics.com certificate expires Mar 06 2020 
with an AmazonS3 server type.
Serial: 05:a0:02:93:f5:aa:85:9f:ae:fe:ee:bd:d1:af:9b:4f

discourse.snowanalytics.com certificate expires on Aug 24, 2019
with a Nginx server type.
serial: 04:5e:f0:60:e5:b0:e0:58:68:bc:77:be:bd:91:c4:e1:b8:81


Q3. 
SQL ( Answered in MySQL for illustration only ) 
Example SQL will use TOP 100 instead of LIMIT 100

c = conn.cursor()

# c.execute("USE atomic;”)

c.execute("SELECT * from events where event = "+page_view+" ")


c.execute("SELECT * from events inner join contexts on events.id = context.id LIMIT 0,100")

c.execute(" INSERT INTO events_new select * from events where timestamp = 2017-10-05 00:11:54")



Q4. 
Scripting Languages

https://github.com/resilience/SnowPlow-Analytics/blob/master/cityList.py

Q5.
JSON
https://github.com/resilience/SnowPlow-Analytics/blob/master/jsonjsoff.json

Q6. 
Web Technologies (HTML & JavaScript)

<html>
	<head>
		<title>Snowplow</title>
	<link rel=”stylesheet”
	          href=” http://cdn.jsdelivr.net/npm/alertifyjs@1.11.0/build/css/alertify.min.css”
	/>
	</head>


	<body>
		<button onclick alertify.alert(Well Done!)>Click me</button>
	
	<script src=" http://cdn.jsdelivr.net/npm/alertifyjs@1.11.0/build/alertify.min.js " 	defer="defer">	
	</script>

	
	</body>
</html>
