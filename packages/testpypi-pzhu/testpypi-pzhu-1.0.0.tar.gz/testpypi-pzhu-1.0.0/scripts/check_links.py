from lxml import etree
import requests
import helper as helper


result = []
folders = helper.get_dirs("luxemburger-musiklexikon")
for f in folders:
    # Get xml in tei folder
    if f.endswith("/tei"):
        files = helper.get_files(f)
        if len(files) > 0:
            # Search for tei ref@target attributes 
            tei = etree.parse(files[0]).getroot()
            ns = {"tei": "http://www.tei-c.org/ns/1.0"}
            tei_list = tei.xpath("//tei:ref", namespaces=ns)
            attributes = []
            for t in tei_list:
                attributes.append(t.attrib["target"])
            if len(attributes) > 0:
                for a in attributes:
                    # Make GET request and get link with response which is not 2xx
                    try:
                        response = requests.get(a, stream=True)
                        if not(200 <= response.status_code <= 299):
                            # print(files[0].split("/")[-1], a, response)
                            # if "https://www.melusinapress.lu/read/" in a:
                            output = "{:<60}  {:120}  {:<10}".format(files[0].split("/")[-1], a, str(response))
                            print(output)
                            result.append(output)
                    except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema) as e:
                        # output = "{:<60}  {:120}  {:<10}".format(files[0].split("/")[-1], a, str(e))
                        # print(output)
                        # result.append(output)
                        pass

# Save result in txt file
with open("output.txt", "w", encoding="utf-8") as file:
    for r in result:
        file.write(r)
        file.write("\n")
