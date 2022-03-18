import random
from time import sleep

from linkedin_api import Linkedin
from linkedin_api.utils.helpers import get_id_from_urn


def default_evade():
    sleep(random.randint(2, 5))


class LinkedinHelper(Linkedin):
    def _fetch(self, uri, evade=default_evade, base_request=False, **kwargs):
        """GET request to Linkedin API"""
        evade()

        url = f"{self.client.API_BASE_URL if not base_request else self.client.LINKEDIN_BASE_URL}{uri}"
        return self.client.session.get(url, **kwargs)

    def search_companies(self, keywords=None, **kwargs):
        filters = ["resultType->COMPANIES"]

        params = {
            "filters": "List({})".format(",".join(filters)),
            "queryContext": "List(spellCorrectionEnabled->true)",
        }

        if keywords:
            params["keywords"] = keywords

        data = self.search(params, **kwargs)

        results = []
        for item in data:
            if item.get("type") != "COMPANY":
                continue
            results.append(
                {
                    "urn": item.get("targetUrn"),
                    "urn_id": get_id_from_urn(item.get("targetUrn")),
                    "name": item.get("title", {}).get("text"),
                    "headline": item.get("headline", {}).get("text"),
                    "subline": item.get("subline", {}).get("text"),
                }
            )

        return results
