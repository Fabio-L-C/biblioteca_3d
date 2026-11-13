# Controle de créditos

## Situação registrada em 2026-11-12

| Item | Valor | Origem / estado |
| --- | --- | --- |
| Saldo informado | 1.190 créditos | Informado pelo usuário; não consultado na conta |
| Créditos mensais | Desconhecido | Confirmar a divisão do saldo |
| Créditos permanentes | Desconhecido | Confirmar a divisão do saldo |
| Próximo reset | Desconhecido | Consultar Settings → Subscription |
| Fim do plano | 2026-12-24 | Informado pelo usuário |
| Créditos esperados em dezembro | 1.000 | Expectativa do usuário, não confirmada |

Não somar a expectativa de dezembro ao saldo atual como disponibilidade garantida. O saldo informado não deve ser apresentado como saldo atual confirmado. As regras de renovação e os links consultados estão no [README](../README.md#orçamento-e-prazo).

## Estimativas de planejamento

A estimativa registrada para Meshy 7 com textura é de 35 créditos por tentativa no site: seis tentativas custariam 210 e 24 custariam 840. Valores consultados em 2026-11-12, sujeitos a confirmação na operação. Imagens, vistas, remesh, rig, animações e novas tentativas podem gerar custos adicionais. Não aplicar os valores do site automaticamente à API ou ao MCP.

## Registro de consumo

Consumo confirmado do projeto: 175 créditos. Saldo final consultado em 2026-11-13: 1.015 créditos, sendo 575 mensais e 440 permanentes. Estes registros não representam o histórico completo da conta.

| Data | Personagem | Tentativa | Operação / ID da tarefa | Estimativa | Custo efetivo | Fonte / situação |
| --- | --- | --- | --- | ---: | ---: | --- |
| 2026-11-13 | chr_001_anime_espadachim | attempt_005 / v007 | Rig com dedos, caminhada e corrida / 01a1d4f8-3c0f-7109-96ba-c88ee312c183 | 5 | 5 | SUCCEEDED; autorização explícita; cópia local da v006 |
| 2026-11-12 | chr_001_anime_espadachim | attempt_005 | Geometria T-pose Ultra 2K / 01a1d128-a795-759e-b047-b971b4e154f0 | 25 | 25 | SUCCEEDED; tarefa existente retomada |
| 2026-11-12 | chr_001_anime_espadachim | attempt_005 | Textura N1 T-pose / 01a1d138-9fc4-755d-8dd3-ca60d8d14e00 | 10 | 10 | SUCCEEDED; quatro referências |
| 2026-11-12 | chr_001_anime_espadachim | attempt_004 | Textura N1 comparativa / 01a1d114-742f-75dc-abd0-1e4eef179b54 | 10 | 10 | SUCCEEDED; confirmado pela API |
| 2026-11-12 | chr_001_anime_espadachim | attempt_004 | Textura Meshy 7 8K PBR / 01a1d110-c55d-76c9-97e6-c1534baf842e | 15 | 15 | SUCCEEDED; confirmado pela API |
| 2026-11-12 | chr_001_anime_espadachim | attempt_004 | Ultra 2K sem pose_mode / 01a1d10e-e646-7689-8dab-c3a4d863b7e4 | 25 | 25 | SUCCEEDED; comparação controlada |
| 2026-11-12 | chr_001_anime_espadachim | attempt_003 | Meshy 7.1 Ultra 2K / 01a1d10b-1b24-715d-9694-262be78be531 | 25 | 25 | SUCCEEDED; quatro vistas, sem remesh |
| 2026-11-12 | chr_001_anime_espadachim | attempt_002 | Retexture 4K / 01a1d0f8-7577-777f-9971-e6eb334e5a6d | 10 | 10 | SUCCEEDED; confirmado pela API |
| 2026-11-12 | chr_001_anime_espadachim | attempt_002 | Multi-image to 3D / 01a1d0f5-8ba4-74a8-82c3-8307fb5a6907 | 20 | 20 | SUCCEEDED; sem remesh |
| 2026-11-12 | chr_001_anime_espadachim | attempt_001 | Multi-image to 3D / 01a1d0cb-6bc2-7238-8216-16fd3d6a901f | 20 | 20 | SUCCEEDED; confirmado pela API |
| 2026-11-12 | chr_001_anime_espadachim | attempt_001 | Retexture / 01a1d0ce-69ea-7333-ae03-fb9ede2be19b | 10 | 10 | SUCCEEDED; confirmado pela API |

Ao executar uma operação, adicionar uma linha. Usar “desconhecido” para custo efetivo sem confirmação. Registrar gerações, texturas e outras operações separadamente; uma mesma tarefa não pode ser contabilizada duas vezes.

## Fonte dos valores

- O custo de cada operação fica no registro da respectiva tentativa em metadata.json; usar estimated_credits e actual_credits por operação, com null para valores desconhecidos.
- A tabela acima resume esses registros para leitura humana. Não somar a tabela e os metadados entre si: representam os mesmos gastos.
- Reembolsos devem citar a tarefa original e ter valor confirmado. Não presumir reembolso a partir de uma falha.
- Após consultar a conta, registrar data, saldo e evidência textual sem credenciais ou dados de cobrança. Atualizar os valores históricos sem apagar registros anteriores.
- Se houver um custo desconhecido ou renovação, não calcular saldo restante como se o consumo e a disponibilidade estivessem completos.

## Verificação de conexão — 2026-11-12

Servidor local @meshy-ai/meshy-mcp-server 0.5.2 encontrado instalado. Inicialização MCP validada, com 24 ferramentas anunciadas. Consulta autenticada de saldo concluída: 1.190 créditos. A divisão entre créditos mensais e permanentes e a data de reset continuam não verificadas. Nenhuma geração foi iniciada nesta verificação. A chave existente foi preservada e não foi registrada no projeto.

## Segunda tentativa — 2026-11-12

Geometria sem remesh: 20 créditos. Textura 4K: 10 créditos. Total desta tentativa: 30 créditos. Total confirmado do projeto: 60 créditos. Saldo após a segunda tentativa: 1.130 créditos. Sem rig ou compra de créditos.

## Saldo detalhado antes da tentativa 003 — 2026-11-12

Consulta MCP 0.6.11: total 1.130, sendo 690 mensais e 440 permanentes. Próximo reset mensal retornado pela API: 2026-11-24T11:54:46.000Z (24/11/2026 às 08:54:46 em São Paulo). Diretriz atual: priorizar qualidade sobre economia, mantendo registro do consumo.

## Rodada de qualidade com quatro vistas — 2026-11-12

Comparação geométrica: 25 + 25 créditos. Texturas: 15 (Meshy 7 8K PBR) + 10 (N1). Total desta rodada: 75. Acumulado: 135. Saldo final: 1.055 (615 mensais + 440 permanentes). Reset mensal retornado pela API: 2026-11-24T11:54:46Z. Nenhuma compra de créditos ou renovação realizada.

## T-pose — 2026-11-12

Tarefa geométrica existente retomada sem recriação. Geometria: 25 créditos; textura N1: 10. Total da tentativa 005: 35; acumulado: 170. Saldo consultado: 1.020 (580 mensais e 440 permanentes). Próximo reset: 2026-11-24T11:54:46Z.

## Rig v007 — 2026-11-13

Rig com dedos: 5 créditos. Caminhada e corrida incluídas. Redução local no Blender: sem custo Meshy. Acumulado: 175. Saldo: 1.015 (575 mensais + 440 permanentes); próximo reset retornado: 2026-11-24T11:54:46.000Z.
