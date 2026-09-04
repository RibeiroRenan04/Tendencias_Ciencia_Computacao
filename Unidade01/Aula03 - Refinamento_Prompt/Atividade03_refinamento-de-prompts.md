# Atividade - Refinamento de Prompts

## Identificação
- Nome: Renan Ribeiro
- Turma: N1 CCP
- Data: 03/09
- Ferramenta de IA utilizada: Claude (Anthropic)

---

## Problema escolhido

### Contexto
Um estudante do segundo semestre de Ciência da Computação já sabe usar vetores/listas e estruturas de repetição em Python, mas nunca estudou algoritmos de busca. Ele precisa entender a busca binária para uma disciplina de Estruturas de Dados e ser capaz de implementá-la sozinho.

### Problema
Como formular um prompt que faça a IA explicar o algoritmo de **busca binária** de forma didática, tecnicamente correta e aplicável (com exemplo, pseudocódigo e código), em vez de uma explicação genérica de manual?

### Objetivo
Obter, ao final do processo de refinamento, uma explicação que o estudante consiga usar para estudar sozinho: com definição clara, exemplo numérico, comparação justa com a busca linear e uma implementação em Python correta.

---

## Prompt 1 - Versão inicial

### Prompt
```text
Explique busca binária.
```

### Resultado
> A busca binária é um algoritmo de busca eficiente usado para encontrar um elemento em uma lista ordenada. Ela funciona dividindo repetidamente o intervalo de busca pela metade. Primeiro, compara-se o elemento do meio da lista com o valor procurado. Se forem iguais, a busca termina. Se o valor procurado for menor, a busca continua na metade esquerda; se for maior, continua na metade direita. Esse processo se repete até encontrar o elemento ou até que o intervalo fique vazio.
>
> A busca binária tem complexidade de tempo O(log n), o que a torna muito mais eficiente que a busca linear, que tem complexidade O(n), especialmente para listas grandes. Uma condição importante é que a lista precisa estar ordenada antes de aplicar o algoritmo.
>
> Existem implementações iterativas e recursivas da busca binária, e ela é amplamente utilizada em bancos de dados, sistemas de arquivos e bibliotecas de programação.

### Primeira impressão
- **O que funcionou?** A definição e a complexidade estão corretas.
- **O que faltou?** Exemplo numérico, pseudocódigo, código, público definido.
- **O que ficou genérico?** O texto poderia servir tanto para um recrutador quanto para um estudante — não foi adaptado a ninguém específico.
- **O que poderia ser melhor?** Estrutura em tópicos e uma aplicação prática (implementação).

---

## Etapa 3 - Análise antes do primeiro refinamento

- O objetivo ficou claro? Não — "explicar" pode significar coisas muito diferentes.
- A IA compreendeu o público? Não havia público definido.
- Houve informações excessivamente genéricas? Sim, a menção a "bancos de dados, sistemas de arquivos" é apenas decorativa.
- O nível de profundidade foi adequado? Médio, mas não calibrado para ninguém.
- A estrutura foi adequada? Não — texto corrido, sem tópicos.
- Faltaram exemplos? Sim, nenhum exemplo numérico.
- Alguma informação precisa ser verificada? A complexidade O(log n)/O(n) é padrão de literatura e está correta.

---

## Prompt 2 - Primeiro refinamento

### Alterações realizadas
- **Papel:** professor de estruturas de dados.
- **Contexto:** *(ainda não incluído nesta versão — só entra no Prompt 3)*.
- **Objetivo:** implícito em "explicar para quem nunca estudou buscas".
- **Público:** estudantes iniciantes que já sabem vetores e laços.
- **Formato:** 5 itens numerados, linguagem acessível.
- **Restrições:** limite de ~400 palavras.
- **Critérios:** *(ainda não incluídos — só entram no Prompt 3)*.

### Prompt
```text
Atue como professor de estruturas de dados.

Explique o algoritmo de busca binária para estudantes
iniciantes que já conhecem vetores e estruturas de repetição,
mas nunca estudaram algoritmos de busca.

Apresente:
1. definição;
2. pré-requisito (a lista precisa estar ordenada);
3. funcionamento passo a passo;
4. um exemplo numérico;
5. comparação com busca linear.

Utilize linguagem acessível e limite a resposta a
aproximadamente 400 palavras.
```

### Resultado
> **O que é busca binária?**
> Busca binária é um método para encontrar um valor dentro de uma lista **ordenada**, dividindo repetidamente a área de busca pela metade — como abrir um dicionário perto do meio para achar uma palavra, em vez de ler página por página.
>
> **Pré-requisito**
> A lista precisa estar ordenada. Se não estiver, o algoritmo pode devolver um resultado errado, porque ele descarta metade da lista assumindo que ela está em ordem.
>
> **Como funciona (passo a passo)**
> 1. Compare o valor procurado com o elemento do meio da lista.
> 2. Se forem iguais, encontrou o valor.
> 3. Se o valor procurado for menor, repita o processo apenas na metade esquerda.
> 4. Se for maior, repita apenas na metade direita.
> 5. Continue até encontrar o valor ou a lista ficar vazia.
>
> **Exemplo numérico**
> Lista: `[2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]`
> Procurando o número 12:
> - Meio = 23 → 12 é menor, buscar à esquerda: `[2, 5, 8, 12, 16]`
> - Novo meio = 8 → 12 é maior, buscar à direita: `[12, 16]`
> - Novo meio = 12 → encontrado!
>
> **Comparação com busca linear**
> A busca linear verifica elemento por elemento, do início ao fim, sendo mais lenta para listas grandes. A busca binária é muito mais rápida, pois elimina metade das opções a cada passo — mas só funciona em listas já ordenadas.

---

## Etapa 4 - Comparação (Prompt 1 x Prompt 2)

| Critério | Prompt 1 | Prompt 2 |
|---|---:|---:|
| Clareza | 3 | 4 |
| Precisão | 4 | 4 |
| Relevância | 3 | 4 |
| Organização | 2 | 4 |
| Adequação ao público | 2 | 4 |
| Atendimento ao objetivo | 2 | 4 |
| Utilidade prática | 2 | 3 |
| **Total** | **18** | **27** |

*(Escala: 1-Muito insatisfatório · 2-Insatisfatório · 3-Adequado · 4-Muito bom · 5-Excelente)*

O maior salto foi em **organização** e **adequação ao público** — definir papel e público forçou a IA a estruturar a resposta em vez de escrever um parágrafo corrido. A **utilidade prática** subiu pouco, porque ainda falta o código.

---

## Etapa 5 - Antes do segundo refinamento

1. **O que estava inadequado na primeira resposta?** Faltavam estrutura, público e exemplo.
2. **O que melhorou após o primeiro refinamento?** Estrutura, exemplo numérico e linguagem acessível.
3. **O que ainda pode ser melhorado?** Falta pseudocódigo, implementação em Python, tabela comparativa objetiva e um caso de uso negativo (quando não usar).
4. **Qual nova informação será adicionada?** Contexto (linguagem Python, semestre), pseudocódigo, código, tabela, critério de qualidade e perguntas de verificação.
5. **Qual informação poderá ser retirada?** Nenhuma — o Prompt 2 já estava enxuto; o Prompt 3 só complementa.
6. **Por que essas alterações podem melhorar o resultado?** Porque o objetivo real é que o estudante consiga *implementar*, não só entender conceitualmente — sem código, a resposta fica incompleta para esse fim.

## Prompt 3 - Segundo refinamento

### Hipótese de melhoria
Acredito que a resposta ficará melhor porque, ao pedir explicitamente pseudocódigo, implementação em Python, tabela comparativa e um critério de qualidade ("o estudante deve conseguir implementar sozinho"), a IA vai produzir uma resposta que serve tanto para estudar o conceito quanto para praticar — cobrindo a lacuna prática que restou no Prompt 2.

### Prompt
```text
Atue como professor de estruturas de dados especializado
em algoritmos de busca e ordenação.

CONTEXTO:
Os estudantes estão no segundo semestre, já implementaram
vetores e laços em Python, mas nunca implementaram um
algoritmo de busca.

OBJETIVO:
Fazer com que os estudantes compreendam a lógica da busca
binária e sejam capazes de implementá-la em Python.

TAREFA:
Explique o algoritmo apresentando:
1. definição em linguagem simples;
2. pré-requisito obrigatório (vetor ordenado) e por que
   ele é necessário;
3. funcionamento passo a passo com um exemplo numérico;
4. pseudocódigo comentado;
5. implementação em Python;
6. comparação entre busca binária e busca linear
   (incluindo complexidade);
7. uma situação em que a busca binária NÃO é a melhor opção.

FORMATO:
Organize a resposta com subtítulos, uma tabela comparando
as duas buscas (pré-requisito, complexidade, quando usar) e
um bloco de código Python.

RESTRIÇÕES:
- máximo de 500 palavras (o código não conta no limite);
- não usar notação matemática avançada, apenas Big-O simples;
- explicar qualquer termo técnico utilizado.

CRITÉRIO DE QUALIDADE:
Ao final, o estudante deve conseguir implementar a busca
binária sozinho e explicar por que ela é mais eficiente
que a busca linear.

Finalize apresentando duas perguntas para verificar a
compreensão do estudante.
```

### Resultado
> **Definição**
> Busca binária é um algoritmo que localiza um valor em uma lista ordenada, eliminando metade dos elementos restantes a cada comparação.
>
> **Pré-requisito: por que a lista precisa estar ordenada?**
> O algoritmo decide para qual lado ir (esquerda ou direita) comparando o valor do meio com o valor procurado. Isso só funciona se a ordem for garantida — em uma lista desordenada, a metade "descartada" poderia conter o valor certo.
>
> **Funcionamento passo a passo (exemplo numérico)**
> Lista: `[3, 9, 14, 22, 30, 41, 55, 68, 77, 90]` — procurando 41:
> 1. início=0, fim=9 → meio=4 → valor=30 → 41 é maior → buscar à direita
> 2. início=5, fim=9 → meio=7 → valor=68 → 41 é menor → buscar à esquerda
> 3. início=5, fim=6 → meio=5 → valor=41 → **encontrado!**
>
> **Pseudocódigo comentado**
> ```
> função busca_binaria(lista, alvo):
>     inicio = 0
>     fim = tamanho(lista) - 1
>     enquanto inicio <= fim:
>         meio = (inicio + fim) // 2
>         se lista[meio] == alvo:
>             retorna meio          # encontrado
>         senão se lista[meio] < alvo:
>             inicio = meio + 1     # buscar à direita
>         senão:
>             fim = meio - 1        # buscar à esquerda
>     retorna -1                    # não encontrado
> ```
>
> **Implementação em Python**
> ```python
> def busca_binaria(lista, alvo):
>     inicio, fim = 0, len(lista) - 1
>     while inicio <= fim:
>         meio = (inicio + fim) // 2
>         if lista[meio] == alvo:
>             return meio
>         elif lista[meio] < alvo:
>             inicio = meio + 1
>         else:
>             fim = meio - 1
>     return -1
> ```
>
> **Comparação: busca binária x busca linear**
>
> | Critério | Busca linear | Busca binária |
> |---|---|---|
> | Pré-requisito | Nenhum | Lista ordenada |
> | Complexidade (pior caso) | O(n) | O(log n) |
> | Quando usar | Listas pequenas ou desordenadas | Listas grandes e já ordenadas |
> | Simplicidade | Mais simples | Um pouco mais complexa |
>
> **Quando NÃO usar busca binária**
> Se a lista muda o tempo todo (muitas inserções/remoções), manter a ordenação para poder usar a busca binária pode custar mais do que o benefício — nesse caso, outra estrutura (como uma tabela hash) costuma ser melhor.
>
> **Perguntas para verificar sua compreensão**
> 1. Por que a busca binária não pode ser aplicada diretamente a uma lista desordenada?
> 2. Se uma lista tem 1.000.000 de elementos, aproximadamente quantas comparações a busca binária faz no pior caso, comparado à busca linear?

---

## Comparação final

| Critério | Prompt 1 | Prompt 2 | Prompt 3 |
|---|---:|---:|---:|
| Clareza | 3 | 4 | 5 |
| Precisão | 4 | 4 | 5 |
| Relevância | 3 | 4 | 5 |
| Organização | 2 | 4 | 5 |
| Adequação ao público | 2 | 4 | 5 |
| Atendimento ao objetivo | 2 | 4 | 5 |
| Utilidade prática | 2 | 3 | 5 |
| **Total** | **18** | **27** | **35** |

## Qual foi a melhoria?

> **Qual modificação teve maior impacto no resultado?**
> Pedir explicitamente **pseudocódigo + implementação em Python** e definir um **critério de qualidade** ("o estudante deve conseguir implementar sozinho"). Foi isso que transformou a resposta de "boa explicação teórica" (Prompt 2) para "material pronto para estudo e prática" (Prompt 3) — sem essas duas peças, o estudante ainda teria que escrever o código por conta própria, sem apoio nem verificação.

---

## Validação (checklist)

- [x] A informação pode ser confirmada? — Sim, é um algoritmo clássico documentado em qualquer livro de algoritmos.
- [x] Os conceitos apresentados existem? — Sim (busca sequencial/linear, busca binária, notação Big-O).
- [x] Os dados estão atualizados? — Não se aplica (conteúdo atemporal), mas a complexidade O(log n) é resultado matemático estável.
- [x] A resposta realmente atende ao problema? — Sim, cobre teoria, exemplo, código e comparação.
- [ ] Existem generalizações? — Uma leve: "outra estrutura (como tabela hash) costuma ser melhor" é uma heurística, não uma regra fixa; vale contextualizar em sala.
- [x] Existem afirmações sem sustentação? — Não identifiquei nenhuma.
- [ ] A IA apresentou referências? — Não, e para este conteúdo (algoritmo clássico) isso é aceitável, mas em temas mais específicos isso deveria ser cobrado no prompt.
- [x] Eu consigo explicar a resposta com minhas próprias palavras? — Sim, testando o código com o exemplo dado.

**Verificação adicional feita:** rodei mentalmente o algoritmo `busca_binaria` com a lista de exemplo e os índices batem exatamente com o passo a passo descrito; a comparação O(log n) x O(n) é um resultado padrão da literatura de estruturas de dados, não uma afirmação isolada da IA.

---

## Reflexão individual

### 1. Qual foi a principal diferença entre o prompt inicial e o prompt refinado?
O Prompt 1 pediu só o "o quê". O Prompt 3 acrescentou "para quem", "em que formato", "com que critério de qualidade" e "para quê" (implementar sozinho) — cada refinamento fechou uma lacuna de ambiguidade diferente.

### 2. Quais elementos tiveram maior impacto no resultado?
Pedir explicitamente pseudocódigo + implementação Python e definir o critério de qualidade — isso mudou a resposta de conceitual para aplicável.

### 3. Um prompt mais longo necessariamente produz uma resposta melhor? Justifique.
Não. O Prompt 3 é mais longo que o Prompt 1, mas o ganho veio de cada frase adicionar uma informação que a IA não tinha como adivinhar (contexto, formato, critério), não do tamanho em si. Um prompt longo cheio de adjetivos vagos ("bem completo", "muito detalhado") não teria o mesmo efeito, como mostra o exemplo do material de apoio sobre "Explique Python".

### 4. O que acontece quando o objetivo requisitado à IA não está claramente definido?
A IA responde ao pé da letra do que foi pedido, mas escolhe por conta própria o nível, formato e profundidade — o que pode não bater com a real necessidade de quem perguntou, como no Prompt 1 (correto, porém pouco aplicável).

### 5. Quais informações você considera indispensáveis para elaborar um bom prompt?
Público-alvo, se a resposta precisa ser conceitual ou também prática, formato esperado e um critério que permita saber se a resposta "serve" para o objetivo.

### 6. Como o refinamento de prompts pode ser útil para um profissional de Ciência da Computação?
É equivalente a escrever uma boa especificação de requisitos: quanto mais claro o "pedido" (para um colega, um sistema ou uma IA), menos retrabalho e menos ambiguidade na entrega.

### 7. Que riscos podem surgir quando confiamos em uma resposta da IA sem avaliar sua qualidade?
A resposta do Prompt 1 já estava correta, mas se estivesse errada (por exemplo, uma complexidade trocada), alguém sem base para questionar aceitaria como verdade. A fluência do texto não garante a correção do conteúdo.

### 8. Houve alguma situação em que o Prompt 3 ficou pior que o Prompt 2? Se sim, explique.
Não em termos de qualidade, mas o Prompt 3 é visivelmente mais longo e com mais seções — para alguém que só queria uma explicação rápida e conceitual (sem código), o Prompt 2 seria suficiente e mais direto. "Melhor" depende do objetivo.

### 9. Existe um ponto em que adicionar mais instruções começa a prejudicar a resposta?
Sim. Se as restrições entrarem em conflito (por exemplo, pedir "explicação muito aprofundada" e "máximo de 100 palavras" ao mesmo tempo) ou se forem exigidos formatos demais, a IA tende a cortar conteúdo de forma desigual ou ignorar parte das instruções para caber no limite.

### 10. O que você faria para verificar se a resposta tecnicamente está correta?
Rodaria o código com casos de teste (incluindo casos-limite, como valor não encontrado ou lista vazia), conferiria a definição de complexidade em uma fonte de referência (livro-texto ou documentação) e pediria a um colega ou professor para revisar a lógica antes de considerar o conteúdo validado.

---

## Take Away

> "Um bom prompt não é simplesmente um prompt longo. Ele precisa **explicitar quem vai usar a resposta, para quê, e como saber se ela está boa** — sem isso, a IA preenche essas lacunas com suposições que podem não ser as suas."

---

## Cinco recomendações

1. Antes de escrever o prompt, defina para quem é a resposta e o que você vai fazer com ela.
2. Peça um formato específico (tópicos, tabela, código) em vez de esperar que a IA adivinhe.
3. Se a tarefa é técnica, peça exemplo numérico ou código, não só a explicação conceitual.
4. Defina um critério de "pronto" (ex.: "o estudante deve conseguir implementar sozinho") — isso ajuda até você a avaliar a resposta depois.
5. Nunca trate a primeira resposta como final: compare pelo menos duas versões antes de considerar o resultado confiável.

---

## Desafio final (bônus)

Perguntas para diagnosticar "meu prompt não funcionou, a IA respondeu errado":

1. O prompt deixou claro qual era o público e o nível de profundidade esperado?
2. A informação necessária para responder corretamente estava disponível para a IA (ou era preciso conhecimento externo/atualizado que ela não tinha)?
3. O formato pedido era compatível com o tipo de conteúdo (ex.: pedir uma tabela para algo que não é tabular)?
4. Alguém verificou a resposta com uma fonte confiável, ou ela foi aceita só porque "parecia" bem escrita?
5. O erro está no conteúdo gerado, ou na forma como o resultado foi interpretado/aplicado por quem pediu?

> **Pergunta final:** o problema está no prompt, na resposta da IA, nas informações utilizadas ou na forma como o usuário avaliou o resultado?

A Engenharia de Prompt envolve aprender a investigar 

1. O problema está no prompt
O pedido ficou ambíguo, incompleto ou conflitante (ex.: faltou dizer o público, o formato, ou pediu coisas contraditórias como "resposta curta e muito detalhada"). Nesse caso, a IA não teve como adivinhar o que era esperado — a solução é refinar o prompt, como fizemos na atividade.

2. O problema está na resposta da IA
Mesmo com um prompt claro, a IA pode ter cometido um erro factual, técnico ou lógico (uma complexidade errada, um código com bug, uma afirmação sem sustentação). Aqui o prompt não é o culpado — o que resolve é validar a resposta (rodar o código, checar em fonte confiável) e, se for o caso, pedir correção apontando o erro específico.

3. O problema está nas informações utilizadas
Às vezes a IA não tinha acesso à informação necessária (dado desatualizado, específico da empresa/curso do usuário, ou algo que exigiria busca externa). Nesse caso, nem o melhor prompt do mundo resolve sozinho — é preciso fornecer o contexto/dados que faltam, ou usar uma ferramenta com acesso a informação atualizada.

4. O problema está na avaliação do usuário
Às vezes a resposta estava correta e adequada, mas quem avaliou esperava outra coisa (por exemplo, queria uma explicação superficial e recebeu uma técnica, ou vice-versa) ou não tinha base para julgar se a resposta estava certa. Aqui o "erro" é de expectativa ou de falta de critério de avaliação — não da IA