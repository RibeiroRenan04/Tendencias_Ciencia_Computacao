# Aula 06 – Programação Assistida por Inteligência Artificial

**Texto-base:** *Vibe coding: programming through conversation with artificial intelligence* – Advait Sarkar e Ian Drosos (PPIG 2025)
**Unidade II – Programação Assistida** | Tema: Boas práticas na colaboração humano-IA

---

## Trechos/ideias que chamaram atenção

1. **Redistribuição da expertise:** o artigo conclui que o vibe coding não elimina a necessidade de conhecimento em programação; ele a redireciona para gestão de contexto, avaliação rápida de código e decisão sobre quando alternar entre IA e trabalho manual (Seções 3.7 e 5).
2. **Confiança contingente:** a confiança na IA é "granular, dinâmica e contingente", construída por verificação iterativa, e não por aceitação cega (Seção 3.8). O programador do YT21 afirma que revisa as mudanças porque isso o ajuda a "manter o controle".
3. **Context momentum:** decisões iniciais aceitas por conveniência podem prender o projeto em uma trajetória difícil de corrigir depois (Seção 3.2.2, exemplo do app de câmbio no YT18).

---

## Questão 1 – Até que ponto podemos confiar no código produzido pela IA?

A confiança deve ser **parcial e condicionada à verificação**. O artigo mostra que os modelos geram propriedades inexistentes (YT21), ignoram instruções de sistema (TW1) e produzem documentação com versões erradas de frameworks, como Next.js 14 em vez de 15 (YT22). Mesmo quem se inspira no "Karpathy canon" acaba revisando o código na prática.

**Verificações antes de aceitar código gerado por IA:**
- Leitura dos *diffs* (ao menos uma varredura rápida da estrutura, chamadas de API e identificadores);
- Execução e testes da aplicação (navegador, console, aba de rede, terminal);
- Conferência com a documentação oficial das bibliotecas usadas;
- Referência cruzada com outros arquivos do projeto (o modelo não "enxerga" dependências que estão só na cabeça do programador);
- Revisão de qualidade e manutenibilidade (TW1 recusa código "complicado demais" num repositório de 150 mil linhas).

**Riscos de aceitar sem revisão:** bugs ocultos, APIs inexistentes, dívida técnica, falhas de segurança, perda de compreensão do sistema e o *context momentum*, em que uma solução "quase certa" aceita cedo contamina gerações futuras de código. O próprio TW1 alerta que um "vibe coder médio" talvez não conseguisse corrigir o que ele corrigiu.

---

## Questão 2 – A IA reduz a necessidade de conhecimento ou transforma o tipo de conhecimento necessário?

**Transforma.** O texto é explícito: a expertise não é substituída, mas redirecionada. O programador passa de autor linha a linha para **diretor, revisor e editor**. Todos os participantes estudados eram programadores experientes, e os autores ressaltam que não é possível afirmar que não-programadores teriam o mesmo sucesso.

**Competências que ganham importância:**
- **Técnicas tradicionais:** leitura de código, depuração, interpretação de erros, arquitetura, APIs e bancos de dados;
- **Leitura "gestáltica" do código:** avaliar rapidamente se um bloco gerado "parece certo" e se usa o nível de abstração adequado;
- **Literacia em IA:** escolher modelos, gerenciar a janela de contexto, dosar a granularidade dos prompts e limitar o escopo ("faça só a fase um");
- **Visão de produto:** transformar objetivos em funcionalidades e remover o que a IA inventou sem necessidade;
- **Metacognição:** saber quando confiar, quando verificar e quando assumir o controle.

---

## Questão 3 – Quando usar a IA e quando assumir o controle manualmente?

**Critérios propostos (baseados nas Seções 3.6 e 3.7.3):**

| Situação | Abordagem | Evidência no artigo |
|---|---|---|
| Código repetitivo, estrutura inicial, grandes blocos de boilerplate | **Delegar à IA** | IA faz o "trabalho pesado" (TW1) |
| Funcionalidade nova com requisitos claros, mas detalhes a ajustar | **Colaborar**: IA gera, humano revisa e refina | TW1 aceita código "próximo" e corrige à mão |
| Ajustes pequenos (uma linha, renomear, remover botão) | **Manual** – o custo de escrever o prompt supera o da edição | YT21 e YT22 |
| Bug cuja causa o programador já identificou | **Manual** ou prompt muito específico com a correção | YT21 forma hipóteses e corrige |
| IA repete o erro após vários prompts / difícil de "guiar" | **Manual**, trocar de modelo ou reiniciar o contexto | YT15, YT22 |
| Configurações sensíveis (ambiente, banco, segurança) | **Manual com revisão cuidadosa** | YT22 edita o `.env` manualmente |

Regra geral: **quanto maior o risco e menor o tamanho da mudança, mais o controle deve ser humano.**

---

## Estudo de caso – ações antes de incorporar o código

1. **Revisar o código** por completo, entendendo o que cada parte faz (não basta "passar num teste").
2. **Verificar dependências:** existem, estão nas versões corretas, são confiáveis e necessárias?
3. **Analisar segurança:** validação de entradas, autenticação, exposição de dados e segredos.
4. **Ampliar os testes:** casos-limite, erros e testes de integração com o restante do sistema.
5. **Avaliar manutenibilidade:** padrões do projeto, legibilidade, complexidade desnecessária.
6. **Avaliar impacto:** checar arquivos e módulos relacionados que a IA pode ter ignorado.
7. **Code review por outro membro** da equipe antes do merge.

**Responsabilidades que permanecem humanas:** decisão de aceitar ou não, qualidade e segurança do que vai para produção, entendimento do sistema e responsabilidade perante usuários e equipe. Como diz o criador do YT22, "a IA é só uma ferramenta".

---

## Três boas práticas para a colaboração humano-IA

1. **Nunca aceitar sem revisar e testar** – toda saída da IA é um rascunho até ser verificada.
2. **Gerenciar o contexto e o escopo dos prompts** – tarefas pequenas, instruções específicas, documentação oficial como referência e contexto limpo ao mudar de fase.
3. **Manter o humano como responsável final** – decidir conscientemente quando delegar, colaborar ou programar manualmente.

---

## Síntese

> "Programar com IA de maneira responsável não significa apenas saber pedir código; significa também..."

...manter o domínio sobre aquilo que se entrega. O artigo de Sarkar e Drosos mostra que o *vibe coding* não elimina a expertise do programador, mas a desloca: em vez de escrever cada linha, ele passa a orientar, avaliar e corrigir o que a IA produz. Essa mudança exige ler código com rapidez e senso crítico, testar com frequência e reconhecer quando a IA se desviou da intenção original. A confiança, segundo os autores, não é concedida de antemão, mas conquistada a cada verificação. Sem esse conhecimento, aceitar código gerado vira uma aposta, com riscos de bugs, dívida técnica e falhas de segurança. Assim, a responsabilidade pelo software continua sendo humana, mesmo quando a IA escreve a maior parte dele.
