# Referências por tentativa

## Tentativa 005 — T-pose

Quatro imagens salvas e enviadas tanto à geometria quanto à textura N1, nesta ordem:

| Vista | Arquivo |
| --- | --- |
| Frente | [t_pose_front_v001.png](t_pose_front_v001.png) |
| Perfil esquerdo | [t_pose_left_v001.png](t_pose_left_v001.png) |
| Costas | [t_pose_back_v001.png](t_pose_back_v001.png) |
| Perfil direito | [t_pose_right_v001.png](t_pose_right_v001.png) |

Braços horizontais na altura dos ombros, palmas para frente e mãos vazias. Perfis com braços vistos de ponta. Pose preservada sem normalização automática. Prompts individuais em ../prompts/t_pose_*_v001.txt.


## Tentativa 003 — qualidade prioritária

| Vista | Arquivo |
| --- | --- |
| Frente | [front_v003.png](front_v003.png) |
| Perfil esquerdo | [left_profile_v004.png](left_profile_v004.png) |
| Costas | [back_v003.png](back_v003.png) |
| Perfil direito | [right_profile_v001.png](right_profile_v001.png) |

Quatro imagens enviadas nessa ordem. Mãos abertas na frente e nas costas; nas laterais a mão fica de perfil para manter a mesma orientação. O perfil direito teve o punho corrigido antes do envio.

Especificação: [meshy_quality_v003.txt](../prompts/meshy_quality_v003.txt). Os prompts de geração das vistas estão preservados em ../prompts/. O prompt de especificação não é um parâmetro de geometria Multi-Image; a API reconstrói a malha pelas imagens.

## Tentativa 002 — preservada

- [Frente](front_v002.png).
- [Perfil esquerdo](left_profile_v003.png).
- [Costas](back_v002.png).

## Tentativa 001 — preservada

- [Frente](front_v001.png).
- [Perfil esquerdo corrigido](left_profile_v002.png).
- [Costas](back_v001.png).

Todos os PNGs usados estão preservados sem alterações posteriores. A vista lateral inicial com bolsa no lado incorreto não foi usada nas gerações.
