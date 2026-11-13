'use strict';
const $ = id => document.getElementById(id);
const state = {items: [], selected: null, variants: [], variant: null, libraryReady: false};
const statusNames = {planned:'Planejado',references_ready:'Referências prontas',generating:'Em geração',review:'Em avaliação',approved:'Aprovado',needs_work:'Precisa de ajustes',archived:'Arquivado'};
const styleNames = {anime:'Anime',semi_realistic:'Semi-realista','semi-realista':'Semi-realista',realistic:'Realista',realista:'Realista',low_poly:'Low poly',cartoon:'Cartoon',chibi:'Chibi'};
const labels = {front:'Frente',left_profile:'Perfil esquerdo',back:'Costas',right_profile:'Perfil direito'};
const viewer = $('viewer');
const number = n => typeof n === 'number' ? n.toLocaleString('pt-BR') : 'Não informado';
const el = (tag, cls, text) => { const node = document.createElement(tag); if(cls) node.className=cls; if(text!==undefined) node.textContent=text; return node; };
const normalize = text => String(text||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
function asset(base, relative) {
  if(typeof relative!=='string' || !relative || relative.includes('\\')) return null;
  const root = new URL('./', location.href);
  const url = new URL(base.replace(/\/$/,'')+'/'+relative, root);
  return url.origin===root.origin && url.pathname.startsWith(root.pathname) ? url.href : null;
}
function notice(text) { $('notice').textContent=text; $('notice').hidden=false; }
function message(text, {busy=false,retry=false}={}) {
  $('viewer-message-text').textContent=text;
  $('spinner').hidden=!busy; $('retry').hidden=!retry; $('viewer-message').hidden=false;
}
function getVariants(meta) {
  const result=[];
  for(const exp of [...(meta.files?.exports||[])].sort((a,b)=>Number(b.version===meta.preferred_export)-Number(a.version===meta.preferred_export)||String(b.version).localeCompare(String(a.version),undefined,{numeric:true}))) {
    for(const path of exp.paths||[]) if(/\.(glb|gltf)$/i.test(path)) result.push({path,attempt:exp.source_attempt,technical:meta.file_technical?.[path]||exp.technical,label:exp.labels?.[path]||exp.label||exp.version+' · '+(meta.status==='approved'?'Aprovado':'Para avaliação')});
  }
  for(const path of meta.files?.source||[]) if(/\.glb$/i.test(path)) result.push({path,technical:meta.file_technical?.[path],attempt:path.match(/source\/(attempt_\d+)/)?.[1],label:(/rig_v007\/rigged/i.test(path)?'Rig original':/rig_v007\/walk/i.test(path)?'Caminhada original':/rig_v007\/run/i.test(path)?'Corrida original':/geometry/i.test(path)?'Geometria original':/textured_n1/i.test(path)?'Comparação N1':'Textura original')+' · '+(path.match(/attempt_\d+/)?.[0]||'')});
  return result;
}
function preview(item) {
  const images=item.meta.files?.previews||[];
  const path=images.find(p=>/textured.*front/i.test(p))||images.find(p=>/front/i.test(p))||images[0];
  return path?asset(item.path,path):null;
}
function setOptions(id, values, labeler) {
  for(const value of [...new Set(values.filter(Boolean))].sort()) {
    const option=el('option','',labeler(value)); option.value=value; $(id).append(option);
  }
}
function renderCards() {
  const query=normalize($('search').value);
  const items=state.items.filter(item=>(!$('style-filter').value||item.meta.style===$('style-filter').value)&&(!$('status-filter').value||item.meta.status===$('status-filter').value)&&normalize([item.meta.name,item.meta.style,item.meta.role,item.meta.id].join(' ')).includes(query));
  $('cards').replaceChildren(); $('visible-count').textContent=items.length;
  if(!items.length) $('cards').append(el('p','muted','Nenhum personagem encontrado. Experimente outra busca ou filtro.'));
  for(const item of items) {
    const button=el('button','card'); button.type='button'; button.setAttribute('aria-pressed',String(state.selected?.id===item.id)); button.setAttribute('aria-label','Visualizar '+item.meta.name);
    const picture=el('div','card-image'); const src=preview(item);
    if(src) {const img=el('img');img.src=src;img.alt='Prévia de '+item.meta.name;img.loading='lazy';img.addEventListener('error',()=>{img.remove();picture.prepend(el('div','no-preview','Prévia indisponível'));},{once:true});picture.append(img);} else picture.append(el('div','no-preview','Em preparação'));
    picture.append(el('span','badge',statusNames[item.meta.status]||item.meta.status||'Sem estado'));
    const info=el('div','card-info');info.append(el('p','card-name',item.meta.name));
    const meta=el('div','card-meta');meta.append(el('span','',styleNames[item.meta.style]||item.meta.style||'Sem estilo'),el('span','',getVariants(item.meta).length?'Explorar em 3D ↗':'Sem modelo'));
    info.append(meta);button.append(picture,info);button.addEventListener('click',()=>select(item));$('cards').append(button);
  }
  return items;
}
function updateFilters() {
  const items=renderCards();
  if(!items.some(i=>i.id===state.selected?.id)) select(items[0]||null);
}
function renderSpecs(meta) {
  $('specs').replaceChildren();
  const tech=meta.technical||{};
  const specs=[['Polígonos',number(tech.polygon_count)],['Textura',tech.texture_resolution||'Não informada'],['Rig',tech.rig===true?'Disponível':tech.rig===false?'Sem rig':'Não verificado'],['Modelo gerador',meta.model||'Não informado']];
  for(const [name,value] of specs){const box=el('div');box.append(el('dt','',name),el('dd','',value));$('specs').append(box);}
}
function referenceName(meta,path) {
  const ref=(meta.provenance?.references||[]).find(r=>r.local_path===path);
  return labels[ref?.view]||path.split('/').pop();
}
function select(item) {
  state.selected=item; state.variant=null; state.variants=[]; renderCards();
  $('references').replaceChildren();$('versions').replaceChildren();$('specs').replaceChildren();$('download').hidden=true;
  $('reference-count').textContent='0';$('review').hidden=!item;$('character-status').hidden=!item;$('character-doc').hidden=!item;
  if(!item) {
    $('character-id').textContent='VISUALIZADOR';$('character-name').textContent='Nenhum personagem selecionado';
    $('concept').textContent='Escolha um personagem ou ajuste os filtros.';$('review-notes').textContent='';
    viewer.removeAttribute('src');viewer.removeAttribute('poster');state.variants=[];state.variant=null;message('Nenhum modelo selecionado.');enableControls(false);return;
  }
  const meta=item.meta;
  $('character-id').textContent=meta.id||item.id;$('character-name').textContent=meta.name;
  $('character-status').textContent=statusNames[meta.status]||meta.status;
  $('concept').textContent=meta.concept||'Conceito ainda não documentado.';
  $('character-doc').href=asset(item.path,'README.md');
  $('review-notes').textContent=meta.review_notes?.at(-1)||'Ainda não há notas de avaliação.';
  renderSpecs(meta);
  const references=(meta.files?.references||[]).filter(p=>/\.(png|jpe?g|webp)$/i.test(p));
  $('reference-count').textContent=references.length;
  $('references').classList.toggle('four-views',references.length===4);
  if(!references.length) $('references').append(el('p','muted','Referências ainda não disponíveis.'));
  for(const path of references) {
    const src=asset(item.path,path); if(!src)continue;
    const label=referenceName(meta,path);const button=el('button','reference');button.type='button';button.setAttribute('aria-label','Ampliar referência: '+label);
    const img=el('img');img.src=src;img.alt=label+' de '+meta.name;img.loading='lazy';button.append(img,el('span','',label));
    button.addEventListener('click',()=>{$('dialog-image').src=src;$('dialog-image').alt=label+' de '+meta.name;$('dialog-caption').textContent=label;$('image-dialog').showModal();});$('references').append(button);
  }
  state.variants=getVariants(meta).filter(v=>asset(item.path,v.path));
  state.variants.forEach((v,index)=>{const o=el('option','',v.label);o.value=index;$('versions').append(o);});
  if(!state.variants.length) {const o=el('option','','Sem modelo disponível');$('versions').append(o);$('versions').disabled=true;viewer.removeAttribute('src');message('Este personagem ainda não possui um modelo 3D.');enableControls(false);return;}
  $('versions').disabled=false;loadVariant(0);
}
function enableControls(enabled) {
  document.querySelectorAll('[data-orbit],#reset,#rotate,#fullscreen').forEach(n=>n.disabled=!enabled);
}
function loadVariant(index) {
  const variant=state.variants[index];if(!variant||!state.selected)return;
  state.variant=variant;const url=asset(state.selected.path,variant.path);
  viewer.pause();$('animation-controls').hidden=true;viewer.removeAttribute('animation-name');
  const attempt=state.selected.meta.attempts?.find(a=>a.id===variant.attempt);
  renderSpecs({...state.selected.meta,technical:variant.technical||attempt?.technical||state.selected.meta.technical});
  const poster=preview(state.selected);if(poster)viewer.poster=poster;else viewer.removeAttribute('poster');
  viewer.cameraOrbit='0deg 82deg 105%';viewer.cameraTarget='auto auto auto';
  viewer.removeAttribute('auto-rotate');$('rotate').setAttribute('aria-pressed','false');
  $('download').href=url;$('download').setAttribute('download',variant.path.split('/').pop());$('download').hidden=false;
  $('loaded-label').textContent=variant.path.split('.').pop().toUpperCase();
  $('stage-label').textContent=variant.label.toUpperCase();
  message(state.libraryReady?'Carregando modelo 3D…':'Preparando visualizador…',{busy:true});enableControls(false);
  viewer.src=url;
}
function updateAnimations() {
  const clips=viewer.availableAnimations||[];
  $('animations').replaceChildren();$('animation-controls').hidden=!clips.length;
  for(const clip of clips){const option=el('option','',clip);option.value=clip;$('animations').append(option);}
  if(clips.length){viewer.animationName=clips[0];viewer.currentTime=0;viewer.play();$('animation-toggle').textContent='Pausar animação';$('animation-toggle').setAttribute('aria-pressed','true');}
}
viewer.addEventListener('load',()=>{$('viewer-message').hidden=true;$('progress-bar').hidden=true;enableControls(true);updateAnimations();});
$('animations').addEventListener('change',()=>{viewer.animationName=$('animations').value;viewer.currentTime=0;viewer.play();$('animation-toggle').textContent='Pausar animação';$('animation-toggle').setAttribute('aria-pressed','true');});
$('animation-toggle').addEventListener('click',()=>{if(viewer.paused){viewer.play();$('animation-toggle').textContent='Pausar animação';$('animation-toggle').setAttribute('aria-pressed','true');}else{viewer.pause();$('animation-toggle').textContent='Reproduzir animação';$('animation-toggle').setAttribute('aria-pressed','false');}});
viewer.addEventListener('error',()=>{message('Não foi possível carregar o modelo. Verifique o arquivo e tente novamente.',{retry:true});enableControls(false);});
viewer.addEventListener('progress',event=>{const progress=event.detail.totalProgress;$('progress-bar').hidden=progress>=1;$('progress-bar').firstElementChild.style.width=(progress*100)+'%';});
$('retry').addEventListener('click',()=>{const src=viewer.src;viewer.removeAttribute('src');requestAnimationFrame(()=>{viewer.src=src;message('Carregando modelo 3D…',{busy:true});});});
$('versions').addEventListener('change',()=>loadVariant(Number($('versions').value)));
for(const id of ['search','style-filter','status-filter']) $(id).addEventListener(id==='search'?'input':'change',updateFilters);
document.querySelectorAll('[data-orbit]').forEach(button=>button.addEventListener('click',()=>{viewer.cameraOrbit=button.dataset.orbit;viewer.cameraTarget='auto auto auto';}));
$('reset').addEventListener('click',()=>{viewer.cameraOrbit='0deg 82deg 105%';viewer.cameraTarget='auto auto auto';viewer.fieldOfView='30deg';});
$('rotate').addEventListener('click',()=>{const active=$('rotate').getAttribute('aria-pressed')!=='true';$('rotate').setAttribute('aria-pressed',String(active));viewer.toggleAttribute('auto-rotate',active);});
$('background').addEventListener('click',()=>{const active=$('stage').classList.toggle('light');$('background').setAttribute('aria-pressed',String(active));$('background').textContent=active?'Fundo escuro':'Fundo claro';});
$('fullscreen').addEventListener('click',async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await $('stage').requestFullscreen();}catch{notice('Tela cheia indisponível neste navegador.');}});
$('close-dialog').addEventListener('click',()=>$('image-dialog').close());
$('image-dialog').addEventListener('click',event=>{if(event.target===$('image-dialog'))$('image-dialog').close();});
async function json(url) {const res=await fetch(url);if(!res.ok)throw new Error('HTTP '+res.status);return res.json();}
async function start() {
  enableControls(false);
  if(location.protocol==='file:') {
    notice('Para carregar os modelos e o catálogo, feche esta página e dê dois cliques em abrir_galeria.bat na pasta do projeto. Você também pode executar: py -3 scripts/serve_gallery.py');
    $('cards').replaceChildren(el('p','muted','Abra a galeria pelo iniciador local.'));
    message('Abra a galeria pelo arquivo abrir_galeria.bat.');$('character-name').textContent='Sua coleção está aqui';return;
  }
  try {
    const catalog=await json('catalog.json');
    if(!Array.isArray(catalog.characters))throw new Error('Catálogo inválido');
    const results=await Promise.allSettled(catalog.characters.map(async entry=>{
      const url=asset(entry.path,'metadata.json');if(!url)throw new Error('Caminho inválido');
      const meta=await json(url);return {...entry,meta:{...entry,...meta}};
    }));
    state.items=results.filter(r=>r.status==='fulfilled').map(r=>r.value);
    $('total-count').textContent=number(catalog.characters.length);
    if(results.some(r=>r.status==='rejected'))notice('Algumas fichas não puderam ser carregadas. Confira os caminhos e arquivos metadata.json do catálogo.');
    setOptions('style-filter',state.items.map(i=>i.meta.style),v=>styleNames[v]||v);
    setOptions('status-filter',state.items.map(i=>i.meta.status),v=>statusNames[v]||v);
    select(state.items.find(i=>getVariants(i.meta).length)||state.items[0]||null);
  } catch(error) {
    notice('Não foi possível abrir o catálogo. Confira catalog.json e execute a galeria pelo iniciador local.');
    $('cards').replaceChildren(el('p','muted','Catálogo indisponível.'));$('character-name').textContent='Catálogo indisponível';message('Não foi possível carregar a coleção.');
    console.error('Falha ao carregar catálogo:',error);
  }
}
let libraryTimer=setTimeout(()=>{if(!state.libraryReady)message('O visualizador 3D não iniciou. Verifique assets/vendor/model-viewer.min.js e o suporte WebGL do navegador.');},20000);
customElements.whenDefined('model-viewer').then(()=>{state.libraryReady=true;clearTimeout(libraryTimer);if(state.variant&&!viewer.loaded)message('Carregando modelo 3D…',{busy:true});});
start();
