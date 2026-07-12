# Guaipecaz

Portal cidadão de Guaíba e região — notícias, rios, saúde, editais e serviços.

**Site:** https://guaipecaz.com.br/

## DNS no Registro.br

No painel do domínio **guaipecaz.com.br** → **Editar zona DNS**, adicione:

| Tipo | Nome | Destino |
|------|------|---------|
| **A** | `@` (vazio) | `185.199.108.153` |
| **A** | `@` | `185.199.109.153` |
| **A** | `@` | `185.199.110.153` |
| **A** | `@` | `185.199.111.153` |
| **CNAME** | `www` | `stanlennc.github.io` |

Salve e aguarde a propagação (minutos a 48 h). O arquivo `CNAME` na raiz do repositório já aponta para `guaipecaz.com.br`.

## GitHub Pages

Em **Settings → Pages → Custom domain**, informe `guaipecaz.com.br` e marque **Enforce HTTPS**.

## GA4

No Google Analytics, atualize a URL do site para `https://guaipecaz.com.br/`.
