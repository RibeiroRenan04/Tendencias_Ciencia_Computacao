"""
Jogo da Forca (Hangman) - Unidade 02 / Aula 01 - Programacao Assistida por IA.

Atividade pratica: mini-projeto de nivel intermediario.
O objetivo da atividade e construir a base do jogo e usar a IA para refatorar
a logica de exibicao das letras e das tentativas.

Este arquivo ja e a VERSAO REFATORADA. As decisoes de refatoracao e os prompts
usados estao documentados em `Prompts_Jogo_Da_Forca.md`.

Principios de refatoracao aplicados (baseados no material da aula):
1. Estado do jogo isolado em uma estrutura unica (dataclass) em vez de varias
   variaveis soltas mutando dentro do loop.
2. Verificacao de letras separada em uma funcao especifica (`registrar_tentativa`).
3. Logica de exibicao das letras tornada declarativa com list comprehension e
   `str.join`, no lugar de concatenacao repetitiva em loop.
4. Condicoes de vitoria/derrota expressas com operacoes de conjunto (set),
   eliminando contadores manuais e flags redundantes.
5. Funcoes pequenas, com type hints e uma responsabilidade cada.

Autor: Renan Ribeiro - Turma N1 CCP
"""

from __future__ import annotations

import random
import unicodedata
from dataclasses import dataclass, field

# --------------------------------------------------------------------------- #
# Configuracao
# --------------------------------------------------------------------------- #

MAX_ERROS: int = 6

BANCO_DE_PALAVRAS: dict[str, tuple[str, ...]] = {
    "Frutas": ("banana", "morango", "abacaxi", "melancia", "framboesa", "caju"),
    "Paises": ("brasil", "portugal", "japao", "canada", "argentina", "egito"),
    "Linguagens": ("python", "javascript", "kotlin", "rust", "elixir", "golang"),
    "Animais": ("elefante", "jacare", "tucano", "capivara", "tubarao", "coruja"),
}

# Estagios do boneco: indice = numero de erros (0 a MAX_ERROS).
ESTAGIOS_FORCA: tuple[str, ...] = (
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========""",
)


# --------------------------------------------------------------------------- #
# Estado do jogo
# --------------------------------------------------------------------------- #

@dataclass
class EstadoJogo:
    """Agrupa todo o estado de uma partida em um unico objeto."""

    palavra: str
    tema: str
    letras_certas: set[str] = field(default_factory=set)
    letras_erradas: set[str] = field(default_factory=set)

    @property
    def erros(self) -> int:
        """Numero de tentativas erradas ja feitas."""
        return len(self.letras_erradas)

    @property
    def tentativas_restantes(self) -> int:
        return MAX_ERROS - self.erros

    @property
    def venceu(self) -> bool:
        """Venceu quando toda letra da palavra ja foi descoberta."""
        return set(self.palavra) <= self.letras_certas

    @property
    def perdeu(self) -> bool:
        return self.erros >= MAX_ERROS

    @property
    def acabou(self) -> bool:
        return self.venceu or self.perdeu

    @property
    def letras_tentadas(self) -> set[str]:
        return self.letras_certas | self.letras_erradas


# --------------------------------------------------------------------------- #
# Regras do jogo (funcoes puras, faceis de testar)
# --------------------------------------------------------------------------- #

def normalizar(texto: str) -> str:
    """Remove acentos e coloca em minusculo, para comparar letras com seguranca."""
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return sem_acento.strip().lower()


def sortear_palavra(tema: str | None = None) -> tuple[str, str]:
    """Retorna (palavra, tema). Sorteia o tema tambem quando nenhum e informado."""
    tema_escolhido = tema or random.choice(list(BANCO_DE_PALAVRAS))
    palavra = random.choice(BANCO_DE_PALAVRAS[tema_escolhido])
    return normalizar(palavra), tema_escolhido


def montar_exibicao(estado: EstadoJogo) -> str:
    """
    Monta a palavra parcialmente revelada.

    Refatoracao da 'logica de exibicao das letras': de um loop com concatenacao
    (`saida += letra + ' '`) para uma unica expressao declarativa.
    """
    return " ".join(
        letra if letra in estado.letras_certas else "_"
        for letra in estado.palavra
    )


def validar_tentativa(entrada: str, ja_tentadas: set[str]) -> tuple[bool, str]:
    """
    Valida o palpite do jogador.

    Retorna (ok, valor): se `ok` for True, `valor` e a letra normalizada;
    caso contrario, `valor` e a mensagem de erro a ser exibida.
    """
    letra = normalizar(entrada)
    if len(letra) != 1:
        return False, "Digite exatamente uma letra."
    if not letra.isalpha():
        return False, "Isso nao e uma letra valida."
    if letra in ja_tentadas:
        return False, f"Voce ja tentou a letra '{letra}'."
    return True, letra


def registrar_tentativa(estado: EstadoJogo, letra: str) -> bool:
    """
    Verificacao de letras isolada em uma funcao especifica.

    Atualiza o estado e retorna True se a letra pertence a palavra.
    """
    if letra in estado.palavra:
        estado.letras_certas.add(letra)
        return True
    estado.letras_erradas.add(letra)
    return False


# --------------------------------------------------------------------------- #
# Interface de texto (I/O isolado do resto da logica)
# --------------------------------------------------------------------------- #

def mostrar_estado(estado: EstadoJogo) -> None:
    print(ESTAGIOS_FORCA[estado.erros])
    print(f"\nTema: {estado.tema}")
    print(f"Palavra: {montar_exibicao(estado)}")
    erradas = ", ".join(sorted(estado.letras_erradas)) or "-"
    print(f"Letras erradas: {erradas}")
    print(f"Tentativas restantes: {estado.tentativas_restantes}\n")


def ler_palpite(estado: EstadoJogo) -> str:
    """Le da entrada ate receber um palpite valido e ainda nao tentado."""
    while True:
        ok, valor = validar_tentativa(input("Chute uma letra: "), estado.letras_tentadas)
        if ok:
            return valor
        print(f"  -> {valor}")


def escolher_tema() -> str | None:
    temas = list(BANCO_DE_PALAVRAS)
    print("Escolha um tema:")
    print("  0 - Aleatorio")
    for indice, nome in enumerate(temas, start=1):
        print(f"  {indice} - {nome}")

    while True:
        escolha = input("Opcao: ").strip()
        if escolha == "0":
            return None
        if escolha.isdigit() and 1 <= int(escolha) <= len(temas):
            return temas[int(escolha) - 1]
        print("  -> Opcao invalida.")


def mostrar_resultado(estado: EstadoJogo) -> None:
    print(ESTAGIOS_FORCA[estado.erros])
    if estado.venceu:
        print(f"\nParabens! Voce acertou a palavra: {estado.palavra.upper()}")
    else:
        print(f"\nVoce perdeu! A palavra era: {estado.palavra.upper()}")


# --------------------------------------------------------------------------- #
# Loop principal
# --------------------------------------------------------------------------- #

def jogar_partida(tema: str | None) -> None:
    palavra, tema_final = sortear_palavra(tema)
    estado = EstadoJogo(palavra=palavra, tema=tema_final)

    print("\n=== JOGO DA FORCA ===")
    while not estado.acabou:
        mostrar_estado(estado)
        letra = ler_palpite(estado)
        if registrar_tentativa(estado, letra):
            print(f"  -> Boa! A palavra tem a letra '{letra}'.\n")
        else:
            print(f"  -> A palavra nao tem a letra '{letra}'.\n")

    mostrar_resultado(estado)


def main() -> None:
    while True:
        tema = escolher_tema()
        jogar_partida(tema)
        if input("\nJogar de novo? (s/n): ").strip().lower() != "s":
            print("Ate a proxima!")
            break


if __name__ == "__main__":
    main()
