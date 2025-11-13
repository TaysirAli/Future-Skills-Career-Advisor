from competencia import Competencia

class Perfil:
    def __init__(self, nome):
        self.nome = nome
        self.competencias = []

    def adicionar_competencia(self, nome, nivel):
        self.competencias.append(Competencia(nome, nivel))

    def obter_competencias_dict(self):
        return {c.nome: c.nivel for c in self.competencias}
