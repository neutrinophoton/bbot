from bbot.modules.templates.subdomain_enum import subdomain_enum import subdomain_enum_apikey
class whoisxml(subdomain_enum_apikey):
    flags = ["subdomain-enum", "passive", "safe"]
    watched_events = ["DNS_NAME"]
    produced_events = ["DNS_NAME"]
    meta = {
        "description": "Query whoisxml database for Subdomains",
        "created_date": "2025-04-18",
        "author": "@neutrinophoton",
        "auth_required": True,
    }
    base_url = "https://subdomains.whoisxmlapi.com"
    options = {"api_key": ""}
    options_desc = {"api_key": "Whoisxmlapikey"}

    def request_url(self, query):
        url = f"{self.base_url}/api/v1?apiKey={self.api_key}&domainName={self.helpers.quote(query)}"
        return self.api_request(url)

 def parse_results(self, r, query):
    j = r.json()
    if isinstance(j, dict):
        for entry in j.get("result", {}).get("records", []):
            subdomain = entry.get("domain", "")
            if subdomain:
                yield subdomain
