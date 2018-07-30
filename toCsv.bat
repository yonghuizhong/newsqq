if exist "newsqq.csv" del newsqq.csv
scrapy crawl links_spider -o newsqq.csv
pause