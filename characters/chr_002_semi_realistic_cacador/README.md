# Caçador de monstros

Segundo personagem do piloto: homem fictício adulto, cerca de 35 anos, estilo semi-realista. Colete de couro oliva, camisa ocre, proteções de aço simétricas, calça escura e botas marrons. Sem armas ou acessórios pendentes.

Estado: **references_ready**. Quatro vistas individuais em T-pose geradas e revisadas em 2026-11-13. Nenhum modelo 3D ou tarefa Meshy confirmado; envio com falha de rede, sem ID.

## Referências

| Vista | Arquivo | Dimensões |
| --- | --- | --- |
| Frente | [front_v001.png](references/front_v001.png) | 1199 × 1312 |
| Perfil esquerdo | [left_profile_v001.png](references/left_profile_v001.png) | 1254 × 1254 |
| Costas | [back_v001.png](references/back_v001.png) | 1199 × 1312 |
| Perfil direito | [right_profile_v001.png](references/right_profile_v001.png) | 1254 × 1254 |

Revisão visual: roupa, cabelo, proporções e materiais coerentes; braços horizontais, mãos em perfil com polegares para cima e palmas preservadas para a frente do personagem. Pequenas diferenças de costura e enquadramento permanecem; não é um escaneamento calibrado. PNGs verificados estruturalmente e descomprimidos sem erro.

## Rastreabilidade

Prompts exatos em [prompts/](prompts/); procedência por vista em [metadata.json](metadata.json). Frente e costas finais correspondem aos prompts front_v002 e back_v002; os prompts iniciais também foram preservados. Imagens geradas por image_gen.imagegen nesta etapa. Condições de uso não verificadas.

O arquivo frontal herdado estava truncado no bloco IDAT e foi preservado em working/front_v001.base64 e working/front_v001_incomplete.png; não usar esses arquivos como referência.

## Próxima etapa

MCP 0.6.11 validado localmente em 2026-11-13. Seleção: Meshy 7.1, Ultra 2K, quatro vistas, sem remesh, textura ou normalização automática de pose. Estimativa da geometria: 25 créditos, confirmada no schema da ferramenta.

A solicitação falhou com `connect EACCES` na conexão HTTPS e não retornou ID. O estado remoto e o custo efetivo não foram confirmados. Registro em [working/meshy_submission_20261113.json](working/meshy_submission_20261113.json). Consultar tarefas existentes antes de reenviar para evitar duplicação. Não há geometria, textura ou rig local para avaliar.
