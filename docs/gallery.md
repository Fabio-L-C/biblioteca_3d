# Galeria de modelos 3D

## Abrir

Dê dois cliques em abrir_galeria.bat, na raiz do projeto. É necessário Python 3 com o comando py disponível no Windows. O navegador abre em http://127.0.0.1:8088/. Mantenha a janela do servidor aberta enquanto usar a galeria; pressione Ctrl+C para encerrar.

Alternativamente, execute na raiz:

```powershell
py -3 scripts/serve_gallery.py
```

Se a porta estiver ocupada:

```powershell
py -3 scripts/serve_gallery.py --port 8089
```

Abrir index.html diretamente por file:// não permite buscar o catálogo e os modelos de forma confiável. A página mostra uma orientação para usar o iniciador.

## Recursos

- Catálogo com busca por nome, estilo, função e ID, além de filtros de estilo e estado.
- Um visualizador 3D ativo por vez, com rotação por arraste, zoom, posições de frente/lateral/costas, reenquadramento, rotação automática, fundo claro/escuro e tela cheia.
- Seletor de versões exportadas e dos GLBs originais.
- Download do arquivo selecionado, dados técnicos e nota de avaliação mais recente.
- Referências de criação ampliáveis, com suporte a fechamento por Escape.
- Estados para catálogo vazio, falha de ficha, ausência de modelo e erro de carregamento.

## Adicionar personagens

Cadastre o personagem em catalog.json com seu caminho relativo e mantenha metadata.json na pasta indicada. A galeria busca as fichas em cada abertura, sem gerar uma segunda cópia do catálogo.

Os modelos vêm de files.exports[].paths, priorizando versões em ordem decrescente, com files.source como alternativas. GLB e glTF são aceitos nas exportações; arquivos glTF precisam preservar suas dependências. As prévias vêm de files.previews e as imagens de referência de files.references. Todos esses caminhos são relativos à pasta do personagem.

Personagens planejados também aparecem, mesmo sem arquivo 3D.

## Arquivos da interface

| Arquivo | Função |
| --- | --- |
| ../index.html | Estrutura da galeria |
| ../assets/gallery.css | Estilos e layout responsivo |
| ../assets/gallery.js | Catálogo, filtros e controles |
| ../assets/vendor/model-viewer.min.js | Biblioteca 3D local, versão 4.1.0 |
| ../assets/vendor/model-viewer.LICENSE | Licença Apache-2.0 da biblioteca |
| ../scripts/serve_gallery.py | Servidor apenas em loopback, sem listagem de diretórios |
| ../abrir_galeria.bat | Iniciador Windows |

Não requer instalação npm nem compilação. Os arquivos atuais funcionam com a biblioteca armazenada no projeto; não dependem de CDN. Modelos futuros com compressão Draco ou KTX2 podem exigir decodificadores adicionais. Requer navegador com WebGL. Não publica modelos nem altera metadados pela interface.

## Validação desta implementação

Sintaxe do JavaScript e Python verificada. Servidor testado com HTML, CSS, JavaScript, biblioteca, catálogo, GLB e PNG reais. Os arquivos internos fora das rotas da galeria foram recusados. A prévia automatizada no navegador não pôde iniciar nesta sessão; renderização WebGL e interação visual ainda precisam de conferência no navegador do usuário.

Documentação da biblioteca: https://modelviewer.dev/docs/
