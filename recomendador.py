from carreira import Carreira

class Recomendador:
    def __init__(self):
        self.carreiras = [
            Carreira("Engenheiro de IA", {
                "lógica": 8,
                "matemática": 7,
                "criatividade": 6
            }),
            Carreira("Desenvolvedor Full-Stack", {
                "lógica": 8,
                "resolução de Problemas": 7,
                "adaptabilidade": 6
            }),
            Carreira("UX/UI Designer", {
                "criatividade": 8,
                "empatia": 7,
                "Comunicação": 7
            }),
            Carreira("Analista de Dados", {
                "matemática": 8,
                "lógica": 7,
                "pensamento Analítico": 7
            })
        ]

    def recomendar(self, perfil):
        competencias_user = perfil.obter_competencias_dict()
        ranking = []

        for carreira in self.carreiras:
            afinidade = carreira.calcular_afinidade(competencias_user)
            ranking.append((carreira.nome, afinidade))

        ranking.sort(key=lambda x: x[1], reverse=True)
        return ranking[:3]
