# Changelog

Histórico de alterações relevantes na estrutura, documentação e coleção de personagens. Datas no formato AAAA-MM-DD.

## [Unreleased]

### Prioridade de qualidade

- Comparação attempt_003/004: retirar pose_mode resultou em mãos abertas e cinco dedos separados nesta geração; hipótese de interferência da normalização registrada sem atribuição causal definitiva.
- Duas alternativas preservadas: v003 com textura Meshy 7 8K PBR e v004 com N1. Detalhe versus limpeza de cor comparados em close.
- Consumo adicional da rodada: 75 créditos; acumulado: 135. Saldo final: 1.055, sendo 615 mensais e 440 permanentes.
- Galeria com alternativa preferencial explícita e especificações por arquivo/versão, incluindo geometria sem textura.

- Diretriz do usuário incorporada ao AGENTS.md, README.md e fluxo: quatro vistas e melhores modelos/estratégias para qualidade, sem priorizar economia de créditos.
- v002 reprovada pelo usuário; quatro referências novas geradas, salvas e revisadas, incluindo correção da rotação da mão no perfil direito.
- Integração MCP 0.6.11 preparada para acesso aos modelos atuais e resolução Ultra; configuração global e chave existentes preservadas.
- Tentativa 003: geometria Meshy 7.1 Ultra 2K com quatro imagens, sem remesh; custo confirmado de 25 créditos.
- Galeria ajustada para quatro referências com rótulos de ambos os perfis.

### Segunda tentativa

- Três novas referências salvas com olhos e orelhas expostos e volumes em estilo anime 3D. Prompts preservados.
- attempt_002 gerada sem remesh e texturizada em 4K, com exportação v002 de 514.009 triângulos. Versão anterior preservada.
- Closes de cabeça e mão renderizados no Blender. Bloco retangular anterior ausente nos ângulos inspecionados; contaminação de cor nas orelhas e pouca definição dos dedos ainda presentes. Estado review, sem rig e sem otimização para jogo.
- Consumo adicional: 30 créditos. Total acumulado: 60. Saldo confirmado: 1.130 créditos.
- Galeria apresenta v002 primeiro e mostra dados técnicos conforme a tentativa da versão selecionada.

### Avaliação

- Primeiro personagem marcado como needs_work após retorno do usuário: artefato retangular junto à orelha, rosto e textura com qualidade insuficiente. Catálogo e ficha atualizados; nenhuma nova geração ou cobrança nesta avaliação.

### Adicionado

- Galeria local em index.html, integrada a catalog.json e às fichas dos personagens.
- Visualização com model-viewer 4.1.0 local, filtros, versões, download, referências ampliáveis e controles de câmera.
- Iniciador abrir_galeria.bat e servidor Python em loopback na porta 8088.
- Guia docs/gallery.md; verificações de sintaxe e HTTP concluídas. Conferência visual WebGL pendente por indisponibilidade do navegador automatizado.

- Três PNGs originais usados na geração salvos na pasta de referências do primeiro personagem: front_v001.png, left_profile_v002.png e back_v001.png. Metadados e links locais atualizados.

### Próximas etapas

- Avaliar o primeiro modelo: rosto, franja, mãos e adequação ao uso.
- Testar rig e deformações conforme a finalidade.
- Completar o piloto de seis estilos após a avaliação.

## [0.3.0] - 2026-11-12

### Adicionado

- Primeiro modelo de espadachim anime, gerado por Multi-View e texturizado em 2K; originais preservados e exportação v001 em GLB.
- Prévias de avaliação no Blender 5.2 e script scripts/render_character.py.
- Links persistentes das referências originais em references/README.md do personagem; cópias locais das imagens de entrada salvas posteriormente, com metadados preservados no Windows.
- IDs de tarefas, parâmetros e custos efetivos: 20 créditos de geometria e 10 de textura. Saldo consultado: 1.160.

### Avaliação

- Estado review: sem rig ou teste de deformações; rosto, franja e dedos precisam de revisão.

### Configuração do projeto

- Git inicializado e origin configurado em trabalho anterior para https://github.com/Fabio-L-C/biblioteca_3d.git; .gitignore para credenciais e temporários preservado.
- Meshy MCP 0.5.2 validado localmente. Nenhum commit ou push executado nesta etapa de geração.

## [0.2.0] - 2026-11-12

### Adicionado

- catalog.json com o primeiro personagem em estado planned.
- Pasta chr_001_anime_espadachim com ficha, metadados e subpastas de referências, prompts, originais, trabalho, exportações e previews.
- docs/credits.md para situação informada e registro de consumo.
- docs/generation_workflow.md para estados, tentativas, operações, versões e validação.
- Arquivos .gitkeep nas pastas vazias para preservação no Git.

### Alterado

- README.md e AGENTS.md alinhados à arquitetura aprovada por personagem.
- Estilos mantidos como classificação no catálogo, com IDs estáveis.

O cadastro inicial representa planejamento; nenhuma tarefa Meshy ou geração de imagens foi iniciada nesta alteração.

## [0.1.0] - 2026-11-12

### Adicionado

- README.md com objetivo, estrutura, convenções, plano de 24 personagens e critérios de avaliação.
- AGENTS.md com instruções para agentes, preservação de arquivos e registro de gerações.
- Este changelog para acompanhar as alterações do projeto.
- Diretórios iniciais characters/, references/, docs/ e scripts/.

### Registrado

- Saldo de 1.190 créditos informado pelo usuário e encerramento do plano em 24/12/2026.
- Expectativa não confirmada de 1.000 créditos em dezembro, sem assumir acúmulo com o saldo atual.
- Preferência inicial por Meshy 7 e referências Multi-View consistentes.
- Etapa inicial de validação com um personagem anime, seguida de um piloto de seis estilos.

Nenhuma geração, compra de créditos, configuração de integração ou validação de modelos foi executada nesta versão. O número identifica esta edição da documentação; não implica tag ou commit Git criado.
