# projetoscraping
1. Criando o projeto: scrapy startproject 'nomeProjeto'
2. scrapy  genspider 'nomeQualquer' url -> https://lista.mercadolivre.com.br/tenis-de-corrida
3. etapas : request, parser, next_page
4. terminal scrapy -> scrapy shell
5. Em caso de erro 403(acesso não autorizado), é necessario configurar o USER_AGENT, basta buscar no browser 'my user agent'
6. USER_AGENT = ''
7. Crawled (200)-> acesso permitido
8. response -> resposta da requisição -> response.text retorno o html  -> response.css('ui-search-result__content')
-> response.text = retorna todo o HTML da url https://lista.mercadolivre.com.br/tenis-de-corrida

9. products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element').get() retorna apenas 1 elemento
10. products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get() retorna apenas o texto 
11. salvando a pesquisa -> scrapy crawl mercadolivre -o data.jsonl

# Etapa Parse:
response.css('div.ui-search-result__content')
len(response.css('div.ui-search-result__content'))
products = response.css('div.ui-search-result__content')
1. localizando a marca: products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element').get()
2. products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get()
3. scrapy crawl mercadolivre -o 'caminho para salvar'/nomeArquivo.jsonl = scrapy crawl mercadolivre -o data.jsonl

# Terminal scrapy shell
1. fetch('https://lista.mercadolivre.com.br/tenis-de-corrida')