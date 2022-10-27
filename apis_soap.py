import requests
import xmltodict

apiUrl = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

isoWanted = input("Digite o país/ISO: ")

payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
                    <CapitalCity xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
                    <sCountryISOCode>"""+isoWanted+"""</sCountryISOCode>
                    </CapitalCity>
                </soap:Body>
			</soap:Envelope>"""

headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
response = requests.request("POST", apiUrl, headers=headers, data=payload)

gen = xmltodict.parse(response.text)

print(f"A capital de {isoWanted} é " + gen["soap:Envelope"]["soap:Body"]["m:CapitalCityResponse"]["m:CapitalCityResult"])