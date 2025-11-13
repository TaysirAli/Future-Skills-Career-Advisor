class Competencia:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel  # 0 a 10

    def __str__(self):
        return f"{self.nome}: {self.nivel}/10"


competencias_base = [
    "lógica", "criatividade", "comunicação", "empatia",
    "matemática", "adaptabilidade", "pensamento analítico",
    "resolução de problemas"
]

def armazenador_de_competencias(competencia):
    competencia = competencia.lower()

    if competencia not in competencias_base:
        competencias_base.append(competencia)

    return competencias_base
