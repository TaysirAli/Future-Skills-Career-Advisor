class Carreira:
    def __init__(self, nome, competencias_necessarias):
        self.nome = nome
        self.competencias_necessarias = competencias_necessarias  # dict

    def calcular_afinidade(self, competencias_user):
        afinidade = 0
        for comp, nivel_minimo in self.competencias_necessarias.items():
            if comp in competencias_user:
                afinidade += min(competencias_user[comp], nivel_minimo)
        return afinidade
