import requests
from bs4 import BeautifulSoup
import sys
print(sys.executable)


url = 'https://ece.gatech.edu/current-student/undergraduate/electrical-engineering-degree-requirements'
response = requests.get(url)
html_content = response.text
question = 'What classes are requried to graduate with an ECE masters degree?'
#print(html_content)

soup = BeautifulSoup(html_content, 'html.parser')

degree_requirements = soup.find_all('table')

cleaned_data = [table.text.strip() for table in degree_requirements]
# print(cleaned_data)
# print(len(cleaned_data))

file_path = 'degree_requirements.txt'  # Define the file name and path

cleaned_data = ' '.join(cleaned_data)
cleaned_data = cleaned_data.split('\n')
with open(file_path, 'w') as file:
    file.write('{"text": "### Human: ' + question)
    file.write('### Assistant: ')
    for i in cleaned_data:
        if not i == '':
            print(i)
            file.write(i)
    file.write('"}')
    
print(f"Data has been saved to '{file_path}'")

print(i)

