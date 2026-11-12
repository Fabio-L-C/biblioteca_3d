# Espadachim de fantasia

## Versão preferida

A **v005 em T-pose com textura Meshy N1** é a versão padrão da galeria para avaliação. A preferência anterior do usuário pela v004/N1 está preservada; a v005 ainda aguarda sua avaliação. Rig e deformações continuam não validados.

[v005 — GLB](exports/v005/chr_001_anime_espadachim_v005.glb): 477.916 triângulos, cor 2048×2048 embutida, quatro referências em T-pose, Meshy 7.1 Ultra 2K e sem remesh. [Corpo inteiro](previews/textured_v005_front.png), [rosto](previews/textured_v005_head_front.png), [mão](previews/textured_v005_hand.png).

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
| attempt_005 | Quatro novas vistas em T-pose, Ultra 2K, sem pose_mode, N1 | Braços horizontais e dedos separados; v005 em avaliação |

As diferenças reforçam a hipótese de que a normalização de pose interfere nas mãos, mas as gerações estocásticas não provam causalidade definitiva.

## Diretriz de qualidade

Usar quatro imagens por personagem e os melhores modelos e estratégias para a tarefa, independentemente do custo relativo. A API Multi-Image reconstrói geometria pelas imagens e não oferece prompt de forma. A textura multivista não aceita prompt textual simultâneo; a [especificação](prompts/meshy_quality_v003.txt) foi preservada sem declarar envio de um campo inexistente.

## Consumo confirmado

Nesta rodada: 25 créditos da tentativa 003 + 25 da geometria 004 + 15 da textura 8K + 10 da comparação N1 = 75 créditos. Consumo acumulado do projeto: 135. Saldo final consultado: 1.055 créditos (615 mensais e 440 permanentes), em 2026-11-12.

## Rodada T-pose

Tentativa 005: 25 créditos de geometria e 10 de textura N1. Acumulado: 170. Saldo confirmado: 1.020 (580 mensais + 440 permanentes). Originais e quatro PNGs preservados. Sem rig ou teste de deformações.

Inspeção final corrigida após as imagens do usuário: há prolongamentos geométricos indevidos sob ambas as orelhas, semelhantes a lóbulos duplicados ou apêndices. O defeito exige correção da malha; alterar somente a cor não resolve. A causa exata da reconstrução ainda não foi isolada. Olhos e mãos continuam suavizados. A versão permanece em avaliação.
