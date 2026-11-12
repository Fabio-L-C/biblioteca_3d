# Biblioteca 3D

Repositório para criar, documentar, avaliar e guardar modelos 3D de personagens em estilos variados, com foco em reutilização em jogos e outros projetos.

## Abrir a galeria

Dê dois cliques em [abrir_galeria.bat](abrir_galeria.bat). O navegador abrirá a galeria em http://127.0.0.1:8088/, com rotação, zoom, versões e referências. Requer Python 3; mantenha a janela do servidor aberta durante o uso.

Também é possível executar `py -3 scripts/serve_gallery.py` na raiz. Consulte o [guia da galeria](docs/gallery.md).

## Estado atual

- Arquitetura por personagem aplicada em 12/11/2026, com catálogo e guias operacionais.
- Primeiro personagem gerado e em avaliação (review): chr_001_anime_espadachim.
- Versões v001 e v002 preservadas. Atual: v002 sem remesh, textura 4K e closes de avaliação no Blender 5.2. Consumo acumulado confirmado: 60 créditos; saldo consultado: 1.130.
- Plataforma planejada: Meshy.
- Modelo de geração inicialmente escolhido: Meshy 7, sujeito à disponibilidade e ao custo exibido na ferramenta utilizada.
- Estratégia: validar um personagem anime, completar um piloto de seis estilos e então ampliar a coleção.

## Plano da coleção

Todos os personagens desta coleção serão fictícios e adultos. O objetivo inicial é de 24 personagens, quatro por estilo. Quantidade e distribuição podem mudar conforme os resultados e o saldo disponível.

| Estilo | Meta | Conceito do primeiro teste |
| --- | ---: | --- |
| Anime | 4 | Espadachim adulta de fantasia |
| Semi-realista | 4 | Caçador adulto de monstros |
| Realista | 4 | Exploradora adulta |
| Low poly | 4 | Aventureiro adulto |
| Cartoon | 4 | Inventora adulta |
| Chibi | 4 | Paladina adulta com proporções estilizadas |

Os conceitos são propostas iniciais; ainda não representam modelos produzidos.

## Orçamento e prazo

| Informação | Registro |
| --- | --- |
| Saldo informado pelo usuário em 12/11/2026 | 1.190 créditos, chamados de tokens na conversa |
| Encerramento informado do plano | 24/12/2026 |
| Expectativa do usuário | Mais 1.000 créditos em dezembro, ainda não confirmados |
| Estimativa inicial para Meshy 7 com textura | 35 créditos por tentativa, baseada na tabela do site consultada em 12/11/2026 |
| Seis tentativas nessa estimativa | 210 créditos |
| 24 tentativas nessa estimativa | 840 créditos |

Esses valores não são cotações nem saldo consultado na conta. Não incluem necessariamente criação de imagens, vistas adicionais, novas tentativas, remesh, rig ou animações. Site, API e MCP podem oferecer custos e recursos diferentes. Verificar o custo real antes de iniciar tarefas.

Créditos mensais e permanentes devem ser registrados separadamente. Segundo a documentação consultada, créditos mensais não acumulam: a renovação repõe a franquia mensal. Não tratar o saldo atual mais a expectativa de dezembro como 2.190 créditos garantidos. Confirmar a próxima data de reset em Settings → Subscription; ela pode ocorrer antes do encerramento do plano.

## Estrutura

| Caminho | Finalidade |
| --- | --- |
| [index.html](index.html) | Galeria interativa dos personagens e modelos 3D |
| [abrir_galeria.bat](abrir_galeria.bat) | Iniciador local no Windows |
| assets/ | Interface e biblioteca model-viewer local |
| README.md | Objetivos, plano, orçamento e fluxo de trabalho |
| CHANGELOG.md | Histórico das alterações do projeto |
| AGENTS.md | Instruções para agentes que trabalham no repositório |
| [catalog.json](catalog.json) | Índice de personagens, estilos, funções, estados e caminhos |
| characters/ | Pastas individuais dos personagens e seus arquivos |
| references/ | Referências gerais compartilhadas e sua procedência |
| [docs/credits.md](docs/credits.md) | Situação de créditos e resumo de consumo |
| [docs/generation_workflow.md](docs/generation_workflow.md) | Organização, estados, tentativas e versões |
| scripts/ | Automações reproduzíveis, quando necessárias |

Pastas vazias são preservadas por arquivos .gitkeep. A organização é por personagem; o estilo é uma classificação no catálogo, sem subpastas de categorias.

### Organização de cada personagem

Usar characters/<id>/, com estas subpastas conforme forem necessárias:

- references/: imagens de frente, perfil e costas em arquivos separados.
- prompts/: texto exato dos prompts e instruções utilizados.
- source/attempt_001/: downloads originais de uma tentativa, preservados sem alteração.
- working/: arquivos editáveis e versões de trabalho.
- exports/v001/: uma versão destinada aos projetos de uso, com texturas e dependências.
- previews/: capturas e imagens para avaliação.

Cada personagem tem README.md e metadata.json próprios. O primeiro cadastro está em [characters/chr_001_anime_espadachim/README.md](characters/chr_001_anime_espadachim/README.md), com modelo GLB e prévias; as três referências originais estão salvas na pasta references/ do personagem. As pastas de tentativas e versões são criadas quando houver trabalho correspondente.

## Convenções

- ID estável: chr_001_anime_espadachim, chr_002_semi_realistic_cacador etc.
- Nomes de arquivos em minúsculas, sem espaços ou acentos, separados por underscore.
- Versões: chr_001_anime_espadachim_v001.glb; nunca substituir o original por uma revisão.
- Cada tentativa deve registrar prompt, referências, parâmetros e ID da tarefa, quando fornecido.
- Registrar custos estimados e efetivos separadamente; usar null para um custo desconhecido, nunca zero por suposição.
- Guardar arquivos exportados, texturas e dependências juntos; registrar procedência e condições de uso conhecidas.

## Fluxo de produção

1. Definir conceito, estilo, finalidade e complexidade do personagem.
2. Preparar uma referência frontal limpa: corpo inteiro, personagem centralizado, iluminação neutra e margem ao redor do corpo.
3. Preparar vistas complementares consistentes quando forem úteis. Conferir roupa, cabelo, proporções e pose entre frente, perfil e costas. Uma boa imagem única é preferível a várias imagens contraditórias.
4. Confirmar ferramenta, modelo, recursos disponíveis e custo. Para o piloto, preferir Meshy 7 com Multi-View quando as referências estiverem adequadas e o recurso estiver disponível.
5. Gerar a geometria, separando a textura em uma etapa posterior quando a ferramenta permitir. Registrar o ID da tarefa antes de acompanhar o processamento.
6. Inspecionar silhueta, rosto, mãos, pés, costas e separação dos membros. Texturizar as versões aprovadas quando houver separação de etapas.
7. Avaliar topologia, materiais e necessidade de remesh. Pose A ou T ajuda na preparação, mas não garante uma malha adequada à animação.
8. Testar rig e deformações se a finalidade exigir animação. Validar proporções estilizadas, especialmente chibi, antes de automatizar o rig.
9. Baixar e preservar os originais; gerar arquivos de trabalho e exportações conforme necessário.
10. Atualizar a ficha do personagem, metadados, custo efetivo e changelog.

Começar por um personagem anime. Após a avaliação, completar os outros cinco estilos. Ampliar para 24 somente com base nos resultados do piloto e no orçamento restante.

## Metadados mínimos por personagem

| Campo | Conteúdo |
| --- | --- |
| id, name, style, concept | Identidade e descrição |
| status | planned, references_ready, generating, review, approved, needs_work ou archived |
| created_at, updated_at | Datas em formato ISO 8601 |
| provider, interface, model | Plataforma, site/API/MCP e modelo efetivamente utilizados |
| attempts | Lista de tentativas com ID da tarefa, parâmetros, prompt, referências e resultado |
| estimated_credits, actual_credits | Custos da tentativa, sem presumir valores desconhecidos |
| files | Caminhos relativos dos originais, texturas, previews e exportações |
| technical | Polígonos, topologia, texturas, escala, pose e rig, quando verificados |
| provenance | Origem das referências, ferramenta geradora e condições de uso conhecidas |
| review_notes | Problemas, limitações e resultados de validação |

Um personagem pode ter várias tentativas. Uma tentativa é uma nova geração; uma versão é uma revisão ou entrega de um modelo existente. Cada tentativa pode reunir operações separadas de geometria, textura e remesh. Não somar duas vezes o mesmo gasto nem contar uma tentativa como um personagem adicional. Os caminhos do catálogo são relativos à raiz; os dos metadados são relativos à pasta do personagem. Consulte o [guia operacional](docs/generation_workflow.md) para os registros detalhados.

## Critérios de avaliação

- Fidelidade ao conceito e ao estilo desejado.
- Corpo completo e membros separados, sem fusões evidentes.
- Frente, laterais e costas coerentes.
- Texturas e arquivos associados presentes e carregando corretamente.
- Arquivo abrindo na ferramenta de destino, quando houver acesso a ela.
- Para animação: teste de rig e deformações; para jogos: avaliar malha e materiais no motor escolhido.

Aprovado significa adequado ao uso documentado. Um arquivo gerado não deve ser descrito automaticamente como pronto para jogos ou animação.

## Segurança e preservação

Não incluir chaves de API, credenciais, dados de cobrança ou URLs temporárias autenticadas nos arquivos versionados. Configurar segredos localmente e fora do conteúdo do repositório. Não publicar ou redistribuir referências e modelos sem verificar as condições aplicáveis. Antes do fim do plano, conferir os downloads e manter uma cópia de segurança do acervo.

## Documentação consultada

As páginas podem mudar; conferir os recursos e custos na interface antes de executar.

- [Créditos mensais e permanentes](https://help.meshy.ai/en/articles/9991981-how-do-meshy-credits-work)
- [Renovação e acúmulo de créditos](https://help.meshy.ai/en/articles/9991991-when-will-my-credits-reset)
- [Custos no site](https://help.meshy.ai/en/articles/10000507-how-many-credits-does-each-generation-task-cost)
- [Multi-View](https://help.meshy.ai/en/articles/12634481-how-to-use-multi-view)
- [Boas práticas para referências Multi-View](https://help.meshy.ai/en/articles/16102789-meshy-multi-view-best-practices-angles-and-images)
- [Documentação da API](https://docs.meshy.ai/en/api/multi-image-to-3d)
