import requests

url = "https://script.google.com/macros/s/AKfycbwu-VC80X8wXboRovyq16O2WRSczmmB_wCLSUrmiIpNAbwGZV4AnsBdrxRFgaYLjTFq7A/exec"
response = requests.get(url)
inner_data = response.json()
clean_data = inner_data["products"]
print(clean_data)

p_total = [p.get('Price') for p in clean_data]

q_total = [q.get('Quantity on stock ') for q in clean_data]

multiplied_list = []
for num1, num2 in zip(p_total, q_total):
    multiplied_list.append(num1 * num2)

print("Cost of all products is : ", round(sum(multiplied_list), 2))

gluten_free_list = []
for product in clean_data:
    if product['Contains Gluten'] is False:
        gluten_free_list.append(product['Price'] * product['Quantity on stock '])
print("Cost of all gluten free products is : ", round(sum(gluten_free_list), 2))
