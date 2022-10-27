import requests

apiUrl = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<CountryIntPhoneCode xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>BR</sCountryISOCode>
					</CountryIntPhoneCode>
				</soap:Body>
			</soap:Envelope>"""

headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
response = requests.request("POST", apiUrl, headers=headers, data=payload)

print(response.text)
print(response)