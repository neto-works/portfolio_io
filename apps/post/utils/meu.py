import numpy as np


class AHP:
    """_summary_construtor da classe hp

    metodo -> informamos se o metodo é o aproximado, o geometrico ou o de autovalores
    precisao -> quantidade de números após a virgula
    alternativas -> lista com nome das alteranativas que vamos ter
    criterios ->  lista com os criterios
    subcriterios -> dic contendo os subcriterios dos criterios
    matrizes_de_preferencias-> dic contendo (creterio + sua matriz de preferencia para as alterantivas )
    log -> mostrar informações adicionais sobre os calculos

    """

    def __init__(self,metodo,precisao,alternativas,criterios,subcriterios,matrizes_de_preferencias,log=False):
        self.metodo = metodo
        self.precisao = precisao
        self.alternativas = alternativas
        self.criterios = criterios
        self.subcriterios = subcriterios
        self.matrizes_de_preferencias = matrizes_de_preferencias
        self.prioridade_globais = []
        self.log = log

    """_summary_
        Nesse metodo fazemos a soma das colunas nas respectivas linhas (soma_coluna1 -a1,a2,a3, soma_coluna2 -b1,b2,b3, soma_coluna3 -c1,c2,c3)
        Fazemos a normalização das colunas, dividimos todos os elementos da coluna pelo pela soma da coluna para normalizar(a1 = a1/soma(a1,a2,a3) e por ai endiante)
        Media das linhas ai obtemos o autovetor
    """
    @staticmethod
    def metodo_aproximado(matriz, precisao):
        soma_colunas = matriz.sum(
            axis=0
        )  # axis = 0 calculo é feito considerando colunas
        matriz_normalizada = np.divide(matriz, soma_colunas)
        media_linhas = matriz_normalizada.mean(
            axis=1
        )  # axis = 1 calculo é feito considerando linhas

        return media_linhas.round(precisao)

    @staticmethod
    def metodo_geometrico(matriz, precisao):
        media_geometrica = [np.prod(linha) ** (1 / len(linha)) for linha in matriz]
        matriz_normalizada = media_geometrica / sum(media_geometrica)
        return matriz_normalizada.round(precisao)

    @staticmethod
    def metodo_autovalor(
        matriz, precisao, numero_max_iteracao=100, autovetor_anterior=None
    ):
        matriz_quadrada = np.linalg.matrix_power(matriz, 2)  # elevar ao quadrado
        soma_linhas = np.sum(matriz_quadrada, axis=1)
        soma_coluna = np.sum(soma_linhas, axis=0)
        autovetor_atual = np.divide(soma_linhas, soma_coluna)

        if autovetor_anterior is None:
            autovetor_anterior = np.zeros(matriz.shape[0])

        diferenca = np.subtract(autovetor_atual, autovetor_anterior).round(precisao)

        if not np.any(diferenca):
            return autovetor_atual.round(precisao)
        numero_max_iteracao -= 1
        if numero_max_iteracao > 0:
            return AHP.metodo_autovalor(
                matriz_quadrada, precisao, numero_max_iteracao, autovetor_atual
            )
        else:
            return autovetor_atual.round(precisao)

    """
    argument -- 4º passo do metodo ahp que é calcular a concistencia da matriz
    """
    @staticmethod
    def calcula_concistencia(matriz):
        if (
            matriz.shape[0] and matriz.shape[1] > 2
        ):  # uma matriz precisa ser quadrada ou seja maior que 2 x 2
            lambda_max = np.real(np.linalg.eigvals(matriz).max())  # autovalor da matriz
            indice_consistencia = (lambda_max - len(matriz)) / (len(matriz) - 1)

            indice_randomico_sat = {
                3: 0.52,
                4: 0.82,
                5: 1.11,
                6: 1.25,
                7: 1.35,
                8: 1.40,
                9: 1.45,
                11: 1.49,
                11: 1.52,
                12: 1.54,
                13: 1.56,
                14: 1.58,
                15: 1.59,
            }
            razao_consistencia = indice_consistencia / indice_randomico_sat[len(matriz)]
        else:
            lambda_max = 0
            indice_consistencia = 0
            razao_consistencia = 0

        return lambda_max, indice_consistencia, razao_consistencia

    """
    argument -- 5º passo  calcular para todas as matrizes de preferencia
    """
    def calcula_prioridades_locais(self):
        vetor_prioridades_locais = {}
        for criterio in self.matrizes_de_preferencias:
            matriz = np.array(self.matrizes_de_preferencias[criterio])
            if self.metodo == "aproximado":
                prioridades_locais = self.metodo_aproximado(matriz, self.precisao)
            elif self.metodo == "geometrico":
                prioridades_locais = self.metodo_geometrico(matriz, self.precisao)
            else:
                if matriz.shape[0] and matriz.shape[1] >= 2:
                    prioridades_locais = self.metodo_autovalor(matriz, self.precisao)
                else:
                    prioridades_locais = self.metodo_aproximado(matriz, self.precisao)

            vetor_prioridades_locais[criterio] = prioridades_locais

            lambda_max, indice_consistencia, razao_consistencia = (
                self.calcula_concistencia(matriz)
            )

            if self.log:
                print(
                    "\nPrioridades locais do criterio " + criterio + ":\n",
                    prioridades_locais,
                )
                print("Soma: ", np.round(np.sum(prioridades_locais), self.precisao))
                print("Lambda_max = ", lambda_max)
                print(
                    "Indice de Consistencia " + criterio + " = ",
                    round(indice_consistencia, self.precisao),
                )
                print(
                    "Razão de Concistência " + criterio + " = ",
                    round(razao_consistencia, 2),
                )

        return vetor_prioridades_locais

    def calcula_prioridades_globais(self, prioridades, pesos, criterios):
        for criterio in criterios:
            peso = pesos[criterios.index(criterio)]
            prioridades_locais = prioridades[criterio]
            prioridade_global = np.round(peso * prioridades_locais, self.precisao)

            if criterio in self.subcriterios:
                self.calcula_prioridades_globais(
                    prioridades, prioridade_global, self.subcriterios[criterio]
                )
            else:
                self.prioridade_globais.append(prioridade_global)

                if self.log:
                    print(
                        "\nPrioridades globais do criterio " + criterio + "\n",
                        prioridade_global,
                    )
                    print("Soma: ", sum(prioridade_global).round(self.precisao))

    def resultado(self):
        prioridades = self.calcula_prioridades_locais()
        self.calcula_prioridades_globais(
            prioridades, prioridades["criterios"], self.criterios
        )
        prioridades = np.array(self.prioridade_globais)
        prioridades = prioridades.sum(axis=0).round(self.precisao)

        return dict(zip(self.alternativas, prioridades))
