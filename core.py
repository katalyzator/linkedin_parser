from config import LINKEDIN_PASSWORD, LINKEDIN_EMAIL
from linkedin_client import LinkedinHelper

api = LinkedinHelper(LINKEDIN_EMAIL, LINKEDIN_PASSWORD)

results = api.search_companies('the cheese merchant')

for item in results:
    print(item.get('name'))
    print(item.get('headline'))
    print(item.get('subline'))
    company_id = item.get('urn').split(':')[-1]
    print(f'https://www.linkedin.com/company/{company_id}/')
    print('---------------------------------------------')

# company = api.get_company('3177376')
# print(company)
