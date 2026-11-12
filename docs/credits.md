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

Consumo confirmado desta primeira tentativa: 30 créditos. Saldo consultado após geometria e textura em 2026-11-12: 1.160 créditos. Estes registros não representam o histórico completo da conta.

| Data | Personagem | Tentativa | Operação / ID da tarefa | Estimativa | Custo efetivo | Fonte / situação |
| --- | --- | --- | --- | ---: | ---: | --- |
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
