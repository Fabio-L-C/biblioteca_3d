# Espadachim de fantasia

## Versão preferida

O usuário preferiu a **v004 com textura Meshy N1**. Ela é a versão padrão da galeria. A preferência é visual; rig e deformações continuam não validados.

## Versões atuais para avaliação

| Versão | Modelo de textura | Resolução verificada | Observação |
| --- | --- | --- | --- |
| [v003](exports/v003/chr_001_anime_espadachim_v003.glb) | Meshy 7 | Cor 8K; PBR 4K | Mais detalhe nos olhos e materiais; ainda há irregularidades nas sobrancelhas e no limite cabelo/pele |
| [v004](exports/v004/chr_001_anime_espadachim_v004.glb) | Meshy N1 | Cor 2K, sem PBR | Cor mais limpa e menos vazamentos; olhos suavizados |

Ambas usam a geometria de attempt_004: Meshy 7.1 Ultra 2K com quatro vistas, sem remesh e sem normalização automática da pose. A mão aberta e os cinco dedos separados foram conferidos em close.

Estado: review. A maior resolução não significa aprovação de qualidade. Sem rig, teste de deformação ou otimização para jogo. As primeiras versões foram reprovadas pelo usuário e continuam preservadas.

## Prévias

- [Corpo inteiro — 8K PBR](previews/textured_v003_front.png).
- [Rosto — 8K PBR](previews/textured_v003_head_front.png).
- [Mão — 8K PBR](previews/textured_v003_hand.png).
- [Rosto — N1](previews/textured_n1_compare_head_front.png).
- [Quatro referências](references/README.md).
- [Metadados e tarefas](metadata.json).

## Comparações de geração

| Tentativa | Configuração | Resultado da inspeção |
| --- | --- | --- |
| attempt_001 | Meshy 7, 3 vistas, remesh 30 mil, textura 2K | Reprovada: bloco junto à orelha e qualidade insuficiente |
| attempt_002 | Meshy 7, 3 vistas, sem remesh, textura 4K | Reprovada: qualidade ainda insuficiente |
| attempt_003 | Meshy 7.1 Ultra 2K, 4 vistas, normalização A-pose | Melhor geometria facial, mas dedos fundidos; sem textura |
| attempt_004 | Mesmas 4 vistas e Ultra, sem pose_mode | Mãos abertas e dedos separados; duas texturas comparadas |

As diferenças reforçam a hipótese de que a normalização de pose interfere nas mãos, mas as gerações estocásticas não provam causalidade definitiva.

## Diretriz de qualidade

Usar quatro imagens por personagem e os melhores modelos e estratégias para a tarefa, independentemente do custo relativo. A API Multi-Image reconstrói geometria pelas imagens e não oferece prompt de forma. A textura multivista não aceita prompt textual simultâneo; a [especificação](prompts/meshy_quality_v003.txt) foi preservada sem declarar envio de um campo inexistente.

## Consumo confirmado

Nesta rodada: 25 créditos da tentativa 003 + 25 da geometria 004 + 15 da textura 8K + 10 da comparação N1 = 75 créditos. Consumo acumulado do projeto: 135. Saldo final consultado: 1.055 créditos (615 mensais e 440 permanentes), em 2026-11-12.
