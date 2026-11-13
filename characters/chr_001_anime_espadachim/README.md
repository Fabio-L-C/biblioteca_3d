# Espadachim de fantasia

## Versão preferida

A **v006 em T-pose, com as orelhas corrigidas localmente**, é a versão padrão da galeria para avaliação. Textura Meshy N1 preservada. Versões anteriores mantidas; rig e deformações continuam não validados.

[v006 — GLB](exports/v006/chr_001_anime_espadachim_v006.glb): 477.066 triângulos, textura 2K embutida. [Frente](previews/textured_v006_head_front.png), [três quartos](previews/textured_v006_head_threequarter.png) e [perfil](previews/textured_v006_ear_right.png).

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

## Correção local v006 — 2026-11-13

Os apêndices sob as duas orelhas foram removidos da malha v005, com fechamento e suavização locais no Blender 5.2. As novas superfícies usam UV de pele adjacente. Não foram introduzidas bordas abertas; geometria fora da região das orelhas preservada na comparação com precisão de 1e-5. Arquivo editável e [relatório](working/ear_repair_v006/repair_report.json) preservados.

Correção sem geração ou textura paga: 0 créditos Meshy. v005 e originais inalterados. A qualidade geral de olhos/mãos e a adequação à animação continuam em avaliação.

## Preparação do teste de rig — 2026-11-13

[Cópia local](working/rig_test_v007/rig_input.glb) com 299.000 triângulos, preparada no Blender em separado. v006 detalhada preservada e ainda padrão da galeria. Usuário autorizou explicitamente o envio; rig gerado por 5 créditos, com dedos e animações de caminhada/corrida. Preparação local não consumiu créditos. [Detalhes](working/rig_test_v007/README.md).

## Rig v007 — 2026-11-13

Cópia experimental da v006 com 299.000 triângulos e rig Meshy de 66 articulações, incluindo dedos. Altura de 1,7 m solicitada. Textura N1 embutida preservada. A v006 detalhada continua como padrão da galeria.

- [T-pose com rig](exports/v007/chr_001_anime_espadachim_v007.glb).
- [Caminhada](exports/v007/chr_001_anime_espadachim_v007_walk.glb).
- [Corrida](exports/v007/chr_001_anime_espadachim_v007_run.glb).

Na galeria, selecione v007 · Caminhada ou v007 · Corrida. A animação inicia automaticamente; use o botão para pausar. Rig e movimentos abertos no Blender 5.2; aprovação para produção e teste no motor de jogo continuam pendentes. Arquivos originais GLB/FBX preservados em source/attempt_005/rig_v007/.

Custo confirmado: 5 créditos, incluindo os dois movimentos. Total do projeto: 175. Saldo consultado em 13/11: 1.015 (575 mensais + 440 permanentes).

Validação v007: T-pose e duas poses por ciclo abertas no Blender 5.2, sem vértices do personagem sem peso ou coordenadas inválidas. Túnica/bolsa seguem a malha com pesos; sem simulação de tecido, teste facial ou validação no motor. Modelo permanece em avaliação. [Prévia da caminhada](previews/rig_v007_walk_1.png) e [corrida](previews/rig_v007_run_0.png).

## Animações reunidas v008 — 2026-11-13

[GLB com caminhada e corrida](exports/v008/chr_001_anime_espadachim_v008.glb), com a mesma malha de 299.000 triângulos, textura 2K e rig de 66 articulações da v007. Na galeria, escolha **v008 · Rig · Caminhada + Corrida** e alterne no campo **ANIMAÇÃO**; a troca não recarrega o modelo. A v006 detalhada permanece como padrão.

[Arquivo Blender editável](working/animation_bundle_v008/chr_001_anime_espadachim_v008.blend), salvo em T-pose, com as ações Caminhada e Corrida preservadas.

A integração preservou exatamente os bytes dos dados geométricos, da textura e dos samplers dos clipes originais. Blender 5.2 importou os dois movimentos; checagem numérica de nove posições por clipe, com coordenadas finitas e sem vértices sem peso. Isso não substitui teste visual de todas as transições, tecido ou validação em um motor. [Relatório de integração](working/animation_bundle_v008/merge_report.json) e [validação Blender](working/animation_bundle_v008/blender_validation.json).

Créditos desta revisão: 0. Consumo acumulado permanece 175; último saldo consultado em 13/11: 1.015.
