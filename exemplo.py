import requests
from pydantic import BaseMOdel


class PokemonSchema(BaseModel):
    name: str
    type: str




response = requests.get(f'https://pokeapi.co/api/v2/pokemon/25')
data = response.json()
data_types = data['types'] # Supondo que 'data' é o dicionario com dados
type_list = []
for type_info in data_types:
    type_list.append(type_info['type']['name'])
types = ', '.join(type_list)
print(data['name'], types)
