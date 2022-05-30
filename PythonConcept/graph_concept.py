import networkx as nx

def consulta_edges(id):
    import requests
    import json
    url = 'https://pokeapi.co/api/v2/'+id
    response = requests.get(url)

    response_json = response.json()
    #data_dict = json.loads(response_json)
    edges = response_json['game_indices'][0]
    name = ['game_indices'][0]['version']['name']
    return edges, name

if __name__=='__main__':
    G = nx.Graph()
    name = 'ditto'
    result = consulta_edges('pokemon/ditto')
    G.add_edge(name, result)
    print(result)
