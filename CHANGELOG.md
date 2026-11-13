# Changelog

Histórico de alterações relevantes na estrutura, documentação e coleção de personagens. Datas no formato AAAA-MM-DD.

## [Unreleased]

### Nova verificação da integração - 2026-11-13

- Servidor MCP local 0.6.11 inicializado; consulta `meshy_list_tasks` do caçador voltou a falhar com `connect EACCES` na conexão HTTPS. Inicialização local não confirma acesso à API.
- Verificação registrada em `working/meshy_submission_20261113.json` do personagem. Nenhum reenvio realizado; estado remoto e custo efetivo continuam desconhecidos.

### Envio do caçador bloqueado pela rede — 2026-11-13

- Quatro vistas novamente inspecionadas; MCP 0.6.11 inicializado e parâmetros Meshy 7.1 Ultra 2K confirmados na ferramenta e documentação.
- Solicitação de geometria sem remesh/textura falhou com connect EACCES, sem ID de tarefa. Estado remoto e custo efetivo desconhecidos; nenhuma geração confirmada.
- Solicitação e necessidade de consultar tarefas antes de reenviar registradas nos metadados; personagem permanece references_ready.

### Referências do caçador semi-realista — 2026-11-13

- Retomada a preparação do segundo personagem: quatro vistas individuais em T-pose geradas, revisadas visualmente e verificadas como PNGs completos.
- Arquivo frontal incompleto herdado preservado em working; conjunto válido, prompts e procedência registrados na ficha e nos metadados.
- Personagem adicionado ao catálogo como references_ready, disponível na galeria com suas referências.
- Nenhuma tarefa Meshy criada e nenhum crédito Meshy consumido. Conversão 3D pendente: integração MCP não disponível nesta sessão.

### Animações reunidas v008 — 2026-11-13

- Caminhada e corrida reunidas em um único GLB, com clipes nomeados para troca na galeria sem recarregar a malha. v006 detalhada e v007 separada preservadas.
- Integração local preserva dados binários da geometria/textura, rig e samplers originais. Script reproduzível em scripts/merge_character_animations.mjs.
- Arquivo Blender editável salvo em T-pose com ambas as ações. Blender importou os dois clipes; checagem numérica de 9 posições por clipe, coordenadas finitas e nenhum vértice sem peso. Sem validação em motor de jogo.
- Sem créditos consumidos nesta revisão; acumulado permanece 175.

### Rig e animações v007 — 2026-11-13

- Após autorização explícita de envio, gerado rig Meshy com dedos (66 articulações) na cópia local de 299.000 triângulos. Caminhada e corrida incluídas; arquivos GLB/FBX originais preservados.
- Exportação v007 com rig em T-pose e GLBs separados para cada movimento. v006 detalhada preservada como padrão.
- Galeria com rótulos por arquivo, seleção de clipes e reprodução/pausa de animações.
- Custo confirmado: 5 créditos; acumulado: 175; saldo: 1.015 (575 mensais + 440 permanentes). Teste em Blender 5.2; validação no motor de jogo e aprovação para produção pendentes.

### Preparação local para rig — 2026-11-13

- Preparada cópia separada da v006 com 299.000 triângulos, GLB com textura embutida, arquivo Blender e relatório. v006 mantida como padrão.
- Envio e remesh pago bloqueados pela revisão automática antes da execução. Remesh substituído por preparação local; envio para rig de 5 créditos aguarda autorização explícita. Rig e deformações ainda pendentes; nenhum crédito consumido.

### Correção local v006 — 2026-11-13

- Removidos apêndices geométricos sob ambas as orelhas da v005; bordas fechadas e suavizadas no Blender 5.2. UV das novas superfícies ajustada com amostra de pele adjacente.
- GLB v006 com 477.066 triângulos e textura N1 2K embutida; versão padrão da galeria para avaliação. Original, v005, arquivo editável, script e relatório preservados.
- Geometria fora da região de reparo preservada na comparação a 1e-5; nenhuma borda aberta nova. Sem rig ou teste de deformações.
- Nenhuma operação Meshy ou crédito consumido nesta revisão.

### v005 em T-pose

- Quatro novas vistas individuais em T-pose salvas, revisadas e usadas na geometria e na textura. Prompts e procedência preservados.
- Tentativa 005 retomada pelo ID existente, sem cobrança duplicada: Meshy 7.1 Ultra 2K sem remesh ou normalização de pose; textura N1 conforme preferência visual anterior.
- GLB v005 com 477.916 triângulos e cor 2K embutida, padrão da galeria para avaliação. Versões anteriores preservadas.
- T-pose e dedos separados conferidos no Blender 5.2. Diagnóstico corrigido após imagens do usuário: prolongamentos geométricos indevidos sob ambas as orelhas, além de suavização de olhos/mãos; correção da malha pendente. Sem rig ou teste de deformações; aprovação visual do usuário pendente.
- Custo: 35 créditos; acumulado: 170; saldo confirmado: 1.020 (580 mensais e 440 permanentes).

### Regra de pose

- T-pose definida pelo usuário como obrigatória para próximas referências e gerações, substituindo o padrão A-pose. AGENTS.md, README.md, fluxo e planejamento dos personagens atualizados.
- Poses e parâmetros reais das versões anteriores preservados. Nenhuma geração ou consumo de créditos nesta alteração.

### Preferência visual

- Usuário preferiu v004 (Meshy N1) à v003 (Meshy 7 8K PBR). Versão padrão e prévia do catálogo alteradas para v004, preservando as alternativas e o estado de avaliação. Nenhum crédito consumido.

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
