# Fluxo de geração e organização

## Fontes de informação

| Arquivo | Responsabilidade |
| --- | --- |
| catalog.json | Índice: ID, nome, estilo, função, status e caminho do personagem |
| characters/<id>/metadata.json | Dados do personagem, arquivos e histórico de tentativas |
| characters/<id>/README.md | Ficha legível, decisões e avaliação |
| docs/credits.md | Situação financeira informada e resumo de consumo |
| CHANGELOG.md | Alterações relevantes do projeto |

Ao mudar nome, estilo, função ou status, atualizar o catálogo e a ficha com base nos metadados. Os caminhos do catálogo são relativos à raiz; os caminhos em metadata.json são relativos à pasta do personagem. Usar barras / nos registros.

## Identidade e pastas

Cada personagem é independente e fica em characters/<id>/. O ID é estável; mesmo que contenha o estilo inicial, não deve ser renomeado só porque a classificação mudou. Não criar subpastas por estilo.

| Pasta do personagem | Conteúdo |
| --- | --- |
| references/ | Frente, perfil e costas, em arquivos separados |
| prompts/ | Prompts e instruções utilizados |
| source/attempt_001/ | Downloads originais da primeira tentativa |
| source/attempt_002/ | Downloads originais de uma nova tentativa |
| working/ | Arquivos editáveis e revisões |
| exports/v001/ | Primeira entrega, com modelo, texturas e dependências |
| previews/ | Capturas e imagens para consulta |

Criar attempt_NNN e vNNN somente quando houver a tentativa ou exportação correspondente. .gitkeep preserva uma pasta vazia; removê-lo ao adicionar conteúdo real nessa pasta.

## Tentativa, operação e versão

- Tentativa: uma nova geração de geometria para o personagem; recebe attempt_001, attempt_002 etc.
- Operação: uma tarefa da plataforma, como gerar geometria, texturizar ou fazer remesh. Uma tentativa pode ter várias operações e IDs de tarefas.
- Versão: uma revisão ou entrega de um modelo existente; recebe v001, v002 etc. Uma nova edição no Blender não é uma nova tentativa de geração.

Se a plataforma repetir ou refizer uma operação paga, preservar o histórico e seu ID. Associar cada exportação à tentativa que a originou. Não sobrescrever downloads originais.

## Pose obrigatória

Todas as próximas referências e gerações devem usar **T-pose**: braços estendidos horizontalmente na altura dos ombros. Frente, perfil esquerdo, costas e perfil direito devem mostrar a mesma pose. Validar mãos, ombros e cotovelos no resultado 3D.

Quando as referências já estiverem em T-pose, preservá-las sem normalização automática. Se for necessário especificar ou corrigir a pose na ferramenta, usar pose_mode t-pose e revisar o resultado. Não usar A-pose nas novas gerações. Os registros das tentativas anteriores permanecem com a pose realmente utilizada.

## Sequência de trabalho

1. Criar a ficha e metadata.json com status planned; adicionar a entrada ao catálogo.
2. Definir conceito e preparar imagens. Registrar procedência e prompts exatos. Manter um personagem adulto, corpo inteiro e fundo limpo por imagem.
3. Preparar e conferir quatro vistas: frente, perfil esquerdo, costas e perfil direito, com mesma roupa, cabelo, proporções, escala, iluminação, pose e orientação das mãos. Regenerar referências divergentes antes de enviar.
4. Marcar references_ready após a revisão. Escolher os melhores modelos e recursos de qualidade atuais para a tarefa, independentemente do custo relativo. Registrar método e custo real.
5. Ao iniciar geração, criar o registro de tentativa e salvar o ID da tarefa retornado. Marcar generating. Antes de repetir uma solicitação interrompida, consultar a tarefa existente.
6. Ao concluir, preservar os arquivos originais em source/attempt_NNN/, registrar seus caminhos e marcar review. Em caso de falha, registrar o erro e marcar needs_work; não inventar arquivos ou reembolso.
7. Inspecionar geometria antes de texturizar quando houver etapas separadas. Registrar cada operação e seu custo conhecido.
8. Fazer ajustes em working/, preservar versões e exportar para exports/vNNN/ conforme a finalidade.
9. Verificar arquivos e dependências na ferramenta de destino. Para animação, testar rig e deformações. Registrar a avaliação e suas limitações.
10. Marcar approved somente para um uso documentado e validado. Atualizar ficha, catálogo, resumo de créditos e changelog.

## Histórico de tentativas

Cada entrada de attempts deve registrar: id, created_at, provider, interface, model, method, parameters, prompt_files, reference_files, status, operations, output_files e review_notes.

Cada operação em operations registra: type, task_id, status, estimated_credits, actual_credits e notes. Valores desconhecidos usam null. Preservar parâmetros reais retornados/utilizados; não preencher dados técnicos por suposição.

Exports em files.exports devem identificar version, source_attempt e paths. Não adicionar caminhos de arquivos que ainda não existem. Os demais grupos de files contêm listas de caminhos relativos à pasta do personagem.

## Estados

| Estado | Significado |
| --- | --- |
| planned | Conceito registrado, produção ainda não preparada |
| references_ready | Referências revisadas e prontas para geração |
| generating | Tarefa de geração em processamento |
| review | Resultado disponível e aguardando avaliação |
| needs_work | Falha ou problemas que exigem correção |
| approved | Adequado ao uso documentado após validação |
| archived | Fora da produção ativa, com histórico preservado |

Esses estados descrevem o personagem; cada tentativa e operação também preserva seu próprio resultado. A aprovação da arquitetura do projeto não equivale à aprovação de um modelo.

## Critérios de avaliação

Verificar silhueta, rosto, mãos, pés, costas, fusões entre membros, fidelidade visual, materiais e dependências. Registrar topologia, polígonos, escala, textura e rig apenas quando inspecionados. T-pose não garante deformação adequada. Se não houver ferramenta para abrir ou testar o modelo, manter a validação pendente e registrar a limitação.

## Seleção de qualidade — diretriz de 2026-11-12

- Quatro imagens por geração de personagem; manter frente como primeira entrada.
- Referências consistentes têm prioridade; checar dedos separados e rotação dos punhos entre vistas.
- Geometria detalhada: no momento Meshy 7.1 + geometry_resolution 2k (Ultra), sem remesh. Não confundir esse valor com resolução de textura.
- Textura: escolher o modelo conforme o tipo de defeito. Meshy 7 permite detalhe e PBR até 8K; N1 prioriza cor limpa para estilo e poucas costuras, mas opera em 2K e pode suavizar rostos. Comparações devem ser documentadas, sem presumir que o maior número de pixels sempre vence.
- Prompts e imagens devem ser combinados apenas onde suportado. Multi-Image não aceita prompt de geometria; textura multivista não pode ser combinada com texture_prompt na mesma requisição.
- Preservar geometria de alta qualidade; criar otimizações em versões derivadas, nunca substituir originais.
- A escolha de melhor modelo e consumo superior ao plano inicial já foi autorizada pelo usuário. Não comprar créditos ou renovar assinatura automaticamente.

Fontes: https://docs.meshy.ai/en/api/models e https://docs.meshy.ai/en/api/multi-image-to-3d (consultadas em 2026-11-12).

## Preservação de pose e mãos

Na comparação entre attempt_003 e attempt_004, a geração sem pose_mode preservou a mão aberta e cinco dedos separados. A geração com a-pose automática resultou em dedos fundidos. Como as gerações são estocásticas, isso não prova causalidade, mas orienta a preservação de pose: quando as quatro referências já estão na T-pose obrigatória, omitir normalização automática e conferir as mãos em close antes de texturizar. Essa comparação é histórica e não autoriza A-pose em novas gerações.
