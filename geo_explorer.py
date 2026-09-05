import argparse

class GeoExplorer:
    def __init__(self):
        self.knowledge_base = {
            "brasil": {"capital": "Brasília", "continente": "América do Sul"},
            "japao": {"capital": "Tóquio", "continente": "Ásia"},
            "franca": {"capital": "Paris", "continente": "Europa"}
        }

    def consultar(self, pais: str) -> str:
        pais_fmt = pais.lower().strip()
        if pais_fmt in self.knowledge_base:
            dados = self.knowledge_base[pais_fmt]
            return f"[Agente Geo-Explorer]: A capital de {pais.capitalize()} é {dados['capital']} e fica no continente {dados['continente']}."
        return f"[Agente Geo-Explorer]: Desculpe, não tenho informações sobre o país '{pais}' na minha base de dados atual."

def main():
    parser = argparse.ArgumentParser(description="Geo-Explorer: Seu Agente de IA para Geografia")
    parser.add_argument("--pais", type=str, help="Nome do país para consultar", required=True)
    args = parser.parse_args()
    
    agente = GeoExplorer()
    print(agente.consultar(args.pais))

if __name__ == "__main__":
    main()
