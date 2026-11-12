# Instruções para agentes — Biblioteca 3D

## Escopo

Este projeto é um repositório para gerar, documentar, avaliar e guardar modelos 3D de personagens. Trabalhe dentro da estrutura existente e preserve o acervo e as alterações do usuário.

Leia README.md e CHANGELOG.md antes de modificar o projeto. Leia também a ficha e os metadados do personagem em que estiver trabalhando. Instruções específicas de um subdiretório complementam estas orientações.

## Idioma e documentação

- Escreva documentação e atualizações ao usuário em português brasileiro.
- Use nomes técnicos e identificadores de API em sua forma original.
- Prompts podem ser escritos em inglês para a ferramenta; preserve o texto exato usado e registre uma descrição em português.
- Use Markdown em UTF-8, caminhos relativos nos documentos e datas ISO 8601 nos registros.
- Atualize CHANGELOG.md quando houver alterações relevantes, sem apresentar planos como trabalho concluído.

## Organização do acervo

- Cada personagem tem um ID estável e uma pasta em characters/<id>/.
- Siga as convenções do README.md e o fluxo de docs/generation_workflow.md.
- Use metadata.json como fonte dos dados do personagem. Mantenha catalog.json e a ficha coerentes ao mudar nome, estilo, função ou status.
- Caminhos no catálogo são relativos à raiz; caminhos nos metadados são relativos à pasta do personagem.
- Estilo é uma classificação; não mova ou renomeie pastas só para mudar o estilo.
- Separe originais por source/attempt_NNN/ e entregas por exports/vNNN/. Crie essas pastas apenas quando houver trabalho correspondente.
- Diferencie nova geração (tentativa), tarefa da plataforma (operação) e revisão de um resultado existente (versão).
- Registre custos por operação em metadata.json e resuma em docs/credits.md, sem duplicar a contabilização.
- Crie apenas os arquivos e subdiretórios necessários à tarefa atual.
- Preserve downloads originais em source/; edições ficam em working/ e versões de uso em exports/.
- Use versões incrementais v001, v002 etc. Não sobrescreva resultados anteriores sem autorização correspondente.
- Registre referências, prompts, parâmetros, tarefas e arquivos produzidos por tentativa.
- Guarde as imagens de cada vista separadamente; não envie uma ficha com vários personagens ou ângulos como se fosse uma única vista.

## Decisões atuais

- Coleção inicial de personagens fictícios adultos em anime, semi-realista, realista, low poly, cartoon e chibi.
- Meta inicial: quatro personagens por estilo, totalizando 24, sujeita ao orçamento e à avaliação do piloto.
- Primeiro teste: personagem anime adulto. Depois, completar o piloto de seis estilos.
- Prioridade definida pelo usuário: qualidade visual acima da economia de créditos. Selecionar os melhores modelos atuais de geometria e textura para a tarefa, verificando documentação e recursos disponíveis. Modelos e estratégias podem mudar para melhorar qualidade dentro do trabalho autorizado.
- Usar quatro imagens de referência por personagem: frente, perfil esquerdo, costas e perfil direito. As vistas devem ser consistentes e salvas individualmente.
- Não reduzir qualidade, resolução, número de vistas ou geometria para economizar créditos. Custos continuam registrados, sem comprar créditos ou renovar planos automaticamente.
- Preservar a malha detalhada; otimização para jogos somente em versão separada e depois da validação visual.
- Sempre que a API aceitar a combinação, enviar as quatro vistas e o prompt. Respeitar campos mutuamente exclusivos: não afirmar que o prompt guiou uma etapa que só aceita imagens.
- T-pose obrigatória para as próximas referências e modelos: braços estendidos horizontalmente na altura dos ombros, corpo inteiro e mãos visíveis. Não usar A-pose como padrão. Evitar objetos nas mãos no piloto; acessórios complexos podem ser tratados separadamente.
- Estas são diretrizes de produção, não autorização para iniciar todas as gerações de uma vez.

## Integrações e gastos

- Antes de executar, verifique se a ferramenta realmente está disponível e conectada. Não afirme conexão, saldo ou conclusão sem evidência.
- Prefira ferramentas conectadas quando oferecerem as operações necessárias.
- Confirme o identificador do modelo, a compatibilidade do fluxo e o custo na ferramenta efetivamente usada. Site, API e MCP podem diferir.
- Registrar o motivo da escolha do modelo e os parâmetros de qualidade. A escolha dos melhores modelos e estratégias já está autorizada pelo usuário; não solicitar confirmação repetida por causa do custo de uma tentativa pertinente.
- Execute tarefas pagas dentro da autorização e do orçamento já dados pelo usuário, sem pedir confirmação repetida para a mesma ação autorizada.
- Não compre créditos, renove assinatura ou inicie lotes adicionais fora do escopo autorizado.
- O saldo de 1.190 créditos e o fim do plano em 24/12/2026 foram informados pelo usuário em 12/11/2026; não são uma consulta atual da conta.
- Os 1.000 créditos esperados em dezembro não estão confirmados. Registre créditos mensais e permanentes separadamente e confirme a data de reset.
- Custos citados no README.md são estimativas do site e não devem ser aplicados automaticamente à API ou ao MCP.
- Salve o ID retornado por uma tarefa antes de acompanhá-la. Em caso de interrupção, consulte a tarefa existente antes de criar outra e arriscar cobrança duplicada.
- Registre custo efetivo apenas quando conhecido. Não invente saldo, consumo ou reembolso.

## Referências e geração

- Verifique identidade, roupa, cabelo, escala, iluminação e pose entre as vistas.
- Se as quatro vistas forem contraditórias, corrigir ou regenerar as referências antes de enviar ao Meshy. Não substituir o conjunto por uma imagem única como estratégia de economia.
- Se gerar vistas complementares, revise-as antes da conversão para 3D.
- Quando a ferramenta permitir, avalie a geometria antes de gastar com textura.
- As quatro vistas devem representar a mesma T-pose. Quando já estiverem corretas, preservar a pose das referências sem normalização automática. Se a etapa exigir normalização, usar pose_mode t-pose e inspecionar mãos e postura; não usar a-pose. A comparação histórica attempt_003/004 permanece registrada e não altera a regra atual de T-pose.
- Validar T-pose no resultado 3D antes de aprovar a geometria. Manter os parâmetros e as poses reais das tentativas anteriores como histórico, sem reclassificá-las como T-pose.
- Não prometa topologia adequada à animação, rig funcional ou qualidade de produção só porque a geração terminou.

## Validação e rastreabilidade

- Diferencie planned, references_ready, generating, review, approved, needs_work e archived.
- Inspecione rosto, mãos, pés, silhueta, costas e fusões de membros.
- Verifique arquivos, texturas e dependências. Registre a ferramenta em que o modelo foi aberto e o que foi efetivamente testado.
- Para modelos destinados à animação, teste rig e deformações quando houver ferramentas disponíveis.
- Quando não puder abrir ou testar um arquivo, registre a limitação e mantenha a revisão pendente.
- Não invente contagem de polígonos, resolução de textura, licença ou outros metadados técnicos.
- Para mudanças apenas documentais, valide legibilidade, consistência, caminhos e codificação; não crie testes de software desnecessários.

## Segurança e preservação

- Nunca peça ao usuário para colar uma chave de API no chat.
- Nunca exiba nem versione chaves, tokens de autenticação, credenciais, dados de cobrança ou URLs assinadas temporárias.
- Não leia nem divulgue segredos durante a inspeção de arquivos de configuração.
- Registre procedência das referências e condições de uso conhecidas, sem presumir direitos não verificados.
- Não apague modelos, referências ou históricos nem publique o acervo sem autorização correspondente.
- Não faça commits, pushes ou alterações de assinatura apenas por criar documentação; siga o pedido do usuário.
