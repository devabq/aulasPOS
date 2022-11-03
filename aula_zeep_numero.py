import zeep

wsdl_url = "https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

number = int(input("Digite o número a ser palavrificado: "))

result = client.service.NumberToWords(
    ubiNum=number
)
print(f"{number} escreve-se: {result}")