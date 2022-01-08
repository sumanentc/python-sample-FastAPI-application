import httpx
import json
from sql_app.schemas import University

url = 'http://universities.hipolabs.com/search'


def get_all_universities_for_country(country: str) -> dict:
    params = {'country': country}
    client = httpx.Client()
    response = client.get(url, params=params)
    response_json = json.loads(response.text)
    universities = []
    for university in response_json:
        university_obj = University.parse_obj(university)
        universities.append(university_obj)
    return {country: universities}


async def get_all_universities_for_country_async(country: str, data: dict) -> None:
    params = {'country': country}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response_json = json.loads(response.text)
        universities = []
        for university in response_json:
            university_obj = University.parse_obj(university)
            universities.append(university_obj)
    data[country] = universities
