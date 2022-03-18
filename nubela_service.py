import requests


class NubelaService:
    API_KEY = 'e2565859-ef37-4e54-9e69-5b21ce7730bd'

    @classmethod
    def _fetch(cls, url: str, params: dict = None) -> dict:
        header_dic = {'Authorization': 'Bearer ' + cls.API_KEY}

        response = requests.get(url,
                                params=params,
                                headers=header_dic)

        return response.json()

    @staticmethod
    def _format_company_url(company_id: str):
        return f'https://www.linkedin.com/company/{company_id}/'

    @staticmethod
    def _format_person_url(person_id: str):
        return f'https://www.linkedin.com/in/{person_id}/'

    @classmethod
    def get_company_profile(cls, company_id: str) -> dict:
        api_url = 'https://nubela.co/proxycurl/api/linkedin/company'
        company_url = cls._format_company_url(company_id=company_id)
        params = {
            'categories': 'include',
            'funding_data': 'include',
            'extra': 'include',
            'exit_data': 'include',
            'acquisitions': 'include',
            'url': company_url,
            'use_cache': 'if-present',
        }

        return cls._fetch(url=api_url, params=params)

    @classmethod
    def get_company_employees(cls, company_id: str) -> dict:
        api_url = 'https://nubela.co/proxycurl/api/linkedin/company/employees/'
        company_url = cls._format_company_url(company_id=company_id)
        params = {
            'page_size': '1000',
            'employment_status': 'current',
            'url': company_url,
        }

        return cls._fetch(url=api_url, params=params)

    @classmethod
    def get_person_profile(cls, person_id: str) -> dict:
        api_url = 'https://nubela.co/proxycurl/api/v2/linkedin'
        person_url = cls._format_person_url(person_id=person_id)

        params = {
            'url': person_url,
            'use_cache': 'if-present',
            'skills': 'include',
            'inferred_salary': 'include',
            'extra': 'include',
        }

        return cls._fetch(url=api_url, params=params)


if __name__ == '__main__':
    company_id = 'enviropack-ltd'
    # company_profile = NubelaService.get_company_profile(company_id=company_id)
    # print(company_profile)

    # company_employees = NubelaService.get_company_employees(company_id=company_id)
    # print(company_employees)

    person_id = 'aibek-raiymbekov'
    person_profile = NubelaService.get_person_profile(person_id=person_id)
    print(person_profile)
