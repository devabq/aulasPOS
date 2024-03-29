import zeep

# define a URL do WSDL
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# define o código do país para BR
country_code = "BR"

# faz a chamada do serviço
result = client.service.CapitalCity(
	sCountryISOCode=country_code
)
# imprime o resultado
print(f"A capital de {country_code} é {result}")

# define o código do país para US
country_code = "US"

# faz a chamada do serviço
result = client.service.CapitalCity(
	sCountryISOCode=country_code
)

# imprime o resultado
print(f"A capital de {country_code} é {result}")

country_code = "NZ"
result = client.service.CapitalCity(
	sCountryISOCode=country_code
)
print(f"A capital de {country_code} é {result}")