# Atividade 2 - Jogo da Forca (Programação Assistida por IA)

## Identificação
- Nome: Renan Ribeiro
- Turma: N1 CCP
- Unidade: 02 - Programação Assistida por IA / Aula 01
- Mini-projeto escolhido: **Jogo da Forca** (nível intermediário)
- Ferramenta de IA utilizada: Claude (Anthropic)

---

## Objetivo da atividade

> "Gerencie o estado do jogo, listas e loops. Use a IA para refatorar a lógica de
> exibição das letras e tentativas."

O fluxo seguido foi o **Ciclo de Colaboração Humano-IA** do material:
`Contextualizar & Sugerir (IA)` → `Avaliar Criticamente (Humano)` →
`Refatorar & Ajustar (Humano + IA)` → `Decidir & Integrar (Humano)`.

A versão final está em [`Jogo_Da_Forca.py`](Jogo_Da_Forca.py). Este arquivo
documenta os prompts usados, o antes/depois de cada refatoração e a avaliação
crítica de cada resposta da IA.

---

## Etapa 0 - Base construída manualmente (antes da IA)

Primeiro escrevi uma versão funcional, porém "amadora", com o estado espalhado em
várias variáveis e a exibição feita por concatenação dentro de um loop.

```python
import random

palavras = ["banana", "python", "melancia"]
palavra = random.choice(palavras)
letras_certas = []
erros = 0
acabou = False

while not acabou:
    # exibição das letras: concatenação repetitiva
    exibicao = ""
    for i in range(len(palavra)):
        if palavra[i] in letras_certas:
            exibicao = exibicao + palavra[i] + " "
        else:
            exibicao = exibicao + "_ "
    print(exibicao)

    chute = input("Letra: ")

    # verificação de letra misturada com o loop principal
    achou = False
    for i in range(len(palavra)):
        if palavra[i] == chute:
            letras_certas.append(chute)
            achou = True
    if achou == False:
        erros = erros + 1

    # condição de vitória com contador manual
    certas = 0
    for i in range(len(palavra)):
        if palavra[i] in letras_certas:
            certas = certas + 1
    if certas == len(palavra):
        print("Ganhou")
        acabou = True
    if erros == 6:
        print("Perdeu")
        acabou = True
```

### Problemas identificados (avaliação crítica - humano)
- Estado do jogo espalhado em 4 variáveis soltas (`palavra`, `letras_certas`, `erros`, `acabou`).
- Exibição das letras por concatenação repetitiva (`exibicao = exibicao + ...`).
- Verificação de letra misturada com o loop principal, sem função própria.
- Vitória calculada com contador manual reinicializado a cada rodada.
- Sem validação de entrada (aceita `""`, número, duas letras, letra repetida).
- Comparações não-pythônicas (`if achou == False`, `range(len(...))`).

---

## Roteiro de Prompts (Cheat Sheet aplicado)

| Etapa | ❌ Prompt fraco (amador) | ✅ Prompt estruturado (usado na atividade) |
|---|---|---|
| Contexto/geração | "Faça um jogo da forca." | Prompt 1 (abaixo) |
| Refatoração da exibição | "Melhore esse código." | Prompt 2 (abaixo) |
| Refatoração do estado/tentativas | "Deixa mais organizado." | Prompt 3 (abaixo) |
| Debugging | "Tá dando erro." | Prompt 4 (abaixo) |

---

## Prompt 1 - Contextualização e geração da estrutura

### Prompt
```text
Atue como um dev Python sênior.

CONTEXTO:
Tenho uma versão funcional, mas amadora, de um jogo da forca de terminal
(estado em variáveis soltas, exibição por concatenação em loop, verificação
de letra dentro do loop principal). Vou colar o código abaixo.

TAREFA:
Reescreva a base de forma MODULAR:
1. Agrupe todo o estado da partida (palavra, letras certas, letras erradas)
   em uma única estrutura.
2. Separe a verificação de letras em uma função específica.
3. Isole a entrada/saída de texto das funções de regra.
4. Use type hints e uma responsabilidade por função.

FORMATO:
Código Python 3.10+, com docstrings curtas e comentário indicando o motivo
de cada decisão de refatoração.

RESTRIÇÕES:
- Sem bibliotecas externas.
- Não usar `range(len(...))` nem comparar com `== True/False`.

CRITÉRIO DE QUALIDADE:
Deve ser possível testar `verificação de letra` e `exibição` sem rodar o
loop de input.
```

### Resposta da IA (resumo)
Introduziu `@dataclass EstadoJogo` com `letras_certas` / `letras_erradas` como
`set`, `properties` para `venceu` / `perdeu` / `erros`, e as funções
`registrar_tentativa`, `montar_exibicao`, `validar_tentativa`.

### Avaliação crítica (humano)
- ✅ Estado unificado em um objeto — some com as variáveis soltas.
- ✅ `set` em vez de `list` para letras: elimina duplicatas e deixa a checagem O(1).
- ✅ Vitória vira `set(self.palavra) <= self.letras_certas` (subconjunto), sem contador.
- ⚠️ A IA não tinha tratado acentos na entrada do usuário → pedido no Prompt 3.
- **Decisão:** integrado, com ajuste dos nomes para português.

---

## Prompt 2 - Refatoração da LÓGICA DE EXIBIÇÃO DAS LETRAS

### Antes (força bruta)
```python
exibicao = ""
for i in range(len(palavra)):
    if palavra[i] in letras_certas:
        exibicao = exibicao + palavra[i] + " "
    else:
        exibicao = exibicao + "_ "
```
Concatenação repetitiva de string (cria uma string nova a cada volta) e índice
manual propenso a erro.

### Prompt
```text
Refatore esta função de exibição focando em legibilidade e no idioma da
linguagem. Evite concatenação de string em loop e índice manual. O retorno
deve ser a palavra parcialmente revelada, com as letras separadas por espaço
(ex.: "m e l _ _ _ _ a"). Comente a mudança.
```

### Depois (pythônico) — em [`Jogo_Da_Forca.py`](Jogo_Da_Forca.py)
```python
def montar_exibicao(estado: EstadoJogo) -> str:
    return " ".join(
        letra if letra in estado.letras_certas else "_"
        for letra in estado.palavra
    )
```

### Avaliação crítica (humano)
- ✅ Uma expressão declarativa substitui 6 linhas de loop.
- ✅ Sem `range(len())`: itera direto sobre os caracteres.
- ✅ `str.join` monta a string de uma vez, sem objetos intermediários.
- Testado: `melancia` com `{m,e,l}` → `m e l _ _ _ _ a`. ✔️

---

## Prompt 3 - Refatoração do ESTADO E DAS TENTATIVAS

### Antes
Contador `erros` incrementado à mão; vitória recontada a cada rodada; nenhuma
validação do palpite; acento quebrava a comparação.

### Prompt
```text
Refatore o controle de tentativas evitando mutação de estado desnecessária
e flags redundantes.

Requisitos:
1. `erros` deve ser derivado do número de letras erradas, não uma variável
   que eu incremento.
2. `venceu` e `perdeu` devem ser propriedades calculadas a partir do estado.
3. Crie `validar_tentativa(entrada, ja_tentadas)` que rejeite: entrada vazia,
   mais de um caractere, não-letra e letra repetida — retornando (ok, valor).
4. Normalize acento e maiúscula na entrada (ex.: "Á" deve valer "a").

Comente cada alteração.
```

### Depois — trechos de [`Jogo_Da_Forca.py`](Jogo_Da_Forca.py)
```python
@property
def erros(self) -> int:
    return len(self.letras_erradas)          # derivado, não incrementado

@property
def venceu(self) -> bool:
    return set(self.palavra) <= self.letras_certas

@property
def perdeu(self) -> bool:
    return self.erros >= MAX_ERROS


def validar_tentativa(entrada: str, ja_tentadas: set[str]) -> tuple[bool, str]:
    letra = normalizar(entrada)
    if len(letra) != 1:
        return False, "Digite exatamente uma letra."
    if not letra.isalpha():
        return False, "Isso nao e uma letra valida."
    if letra in ja_tentadas:
        return False, f"Voce ja tentou a letra '{letra}'."
    return True, letra


def registrar_tentativa(estado: EstadoJogo, letra: str) -> bool:
    if letra in estado.palavra:
        estado.letras_certas.add(letra)
        return True
    estado.letras_erradas.add(letra)
    return False
```

### Avaliação crítica (humano)
- ✅ `erros` deixou de ser um estado mutável → impossível "esquecer de incrementar".
- ✅ `venceu` / `perdeu` calculados: some a flag `acabou` espalhada.
- ✅ Validação centralizada em uma função testável.
- ✅ `normalizar` (via `unicodedata`) resolve acento e maiúscula de uma vez.
- Testado: `"AB"` → recusado; `"7"` → recusado; `"Á"` → aceito como `"a"`. ✔️

---

## Prompt 4 - Debugging (prompt específico, não genérico)

### Situação
Ao rodar a primeira versão da IA, `montar_exibicao` gerava `KeyError` quando
`letras_certas` ainda era `None`.

### ❌ Prompt fraco
```text
Tá dando erro na linha da exibição.
```

### ✅ Prompt estruturado
```text
Ao chamar `montar_exibicao(estado)` logo após criar `EstadoJogo(palavra=...)`,
recebo `TypeError: argument of type 'NoneType' is not iterable`, porque
`letras_certas` está como None. Como inicializar um set mutável como valor
padrão de campo em uma dataclass sem cair na armadilha do default mutável
compartilhado?
```

### Resposta aplicada
```python
from dataclasses import dataclass, field

@dataclass
class EstadoJogo:
    palavra: str
    tema: str
    letras_certas: set[str] = field(default_factory=set)
    letras_erradas: set[str] = field(default_factory=set)
```
`field(default_factory=set)` cria um `set` novo por instância — evita o bug
clássico de default mutável compartilhado entre objetos.

---

## Comparação final (antes x depois da colaboração com a IA)

| Critério | Base manual | Versão refatorada (IA + revisão) |
|---|---|---|
| Estado do jogo | 4 variáveis soltas | 1 `dataclass EstadoJogo` |
| Exibição das letras | loop + concatenação (6 linhas) | 1 comprehension com `join` |
| Verificação de letra | dentro do loop principal | função `registrar_tentativa` |
| Contagem de erros | `erros = erros + 1` manual | `property` derivada de `set` |
| Vitória | contador recalculado por rodada | `set(palavra) <= letras_certas` |
| Validação de entrada | inexistente | `validar_tentativa` (4 casos) |
| Acentos/maiúsculas | quebravam a comparação | `normalizar` com `unicodedata` |
| Testabilidade | só rodando o jogo inteiro | regras testáveis sem `input()` |

---

## Limites da automação (reflexão do material)

- **A máquina entregou:** velocidade na sintaxe pythônica (`join`, comprehension,
  `default_factory`), lembrança de idiomas esquecidos e sugestão de estrutura.
- **A máquina falhou em:** contexto — não sabia que o público é acadêmico e que
  os nomes deviam estar em português; não tratou acento até eu pedir; a primeira
  versão tinha o bug do `None`.
- **A assinatura é minha:** revisei cada sugestão, rodei os testes de mesa
  (`melancia`, entradas inválidas, vitória/derrota) e decido o que entra no commit.

> "A IA sugere a velocidade. O humano garante a direção e a arquitetura."

---

## Como executar

```bash
python "Jogo_Da_Forca.py"
```

## Verificação feita

```text
- sortear_palavra('Frutas') -> ('melancia', 'Frutas')            OK
- adivinhar m,e,l,a,n,c,i -> "m e l a n c i a", venceu = True     OK
- chutes z,x,q contam como 3 erros, perdeu = False               OK
- validar_tentativa("AB")  -> (False, "Digite exatamente...")    OK
- validar_tentativa("7")   -> (False, "Isso nao e uma letra...") OK
- validar_tentativa("Á")   -> (True, "a")                        OK
```
