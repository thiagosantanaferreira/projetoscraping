# projetoscraping
1. scrapy startproject 'nomeProjeto'
2. scrapy  genspider 'nomeQualquer' url -> https://lista.mercadolivre.com.br/tenis-de-corrida
3. etapas : request, parser, next_page
4. terminal scrapy -> scrapy shell
5. erro 403(acesso não autorizado)
6. USER_AGENT = 
7. Crawled (200)-> acesso permitido
8. response -> resposta da requisição -> response.text retorno o html
9. products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element').get() retorna apenas 1 elemento
10. products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get() retorna apenas o texto 
11. salvando a pesquisa -> scrapy crawl mercadolivre -o data.jsonl