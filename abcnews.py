import scrapy

class AbcnewsSpider(scrapy.Spider):
    name = "abcnews"
    allowed_domains = ['abcnews.go.com']
    start_urls = [
        'https://abcnews.go.com/Sports/mckenzie-milton-released-hospital-watch-american-title-game/story?id=59544456',
        'https://abcnews.go.com/Sports/wireStory/cfp-hopeful-oklahoma-beats-texas-big-12-59547578',
        'https://abcnews.go.com/Sports/wireStory/latest-championship-saturday-starts-texas-td-59544264',
        'https://abcnews.go.com/Sports/wireStory/chiefs-set-oakland-game-hunt-wonders-59544491',
        'https://abcnews.go.com/Sports/wireStory/norvells-28-points-rallies-zags-past-creighton-103-59547680',
        'https://abcnews.go.com/Sports/wireStory/nats-work-bryce-harper-looms-offseason-59546909',
        'https://abcnews.go.com/Sports/wireStory/chiefs-raiders-seahawks-49ers-top-nfl-rivalries-sour-59542856',
        'https://abcnews.go.com/Sports/wireStory/column-keys-turnarounds-seahawks-colts-texans-59522641',
        'https://abcnews.go.com/Sports/wireStory/franz-takes-super-race-beaver-creek-snowy-foggy-59547434',
        'https://abcnews.go.com/Sports/wireStory/austrias-schmidhofer-wins-2nd-straight-lake-louise-downhill-59548142',
        'https://abcnews.go.com/Sports/wireStory/jets-harrison-overcame-years-bullying-achieve-dreams-59539579',
    ]
    global visited_url
    visited_url = set()

    def parse(self, response):
        global visited_url
        if response.url not in visited_url:
            visited_url.add(response.url)
            #print ("\t" + response.url)
            # write code to process the items.
            body1 = response.css('div.article-copy p::text').extract()
            body2 = ''
            
            for eachString in body1:
                body2 += eachString
            

            title1 = response.css('h1::text').extract()
            title2 = ''

            for eachString in title1:
                title2 += eachString

            title2 = title2.strip()


            author1 = response.css('div.author::text').extract()
            author2 = ''

            for eachString in author1:
                author2 += eachString

            author2 = author2.strip()

    
            date1 = response.css('span.timestamp::text').extract()
            date2 = ''

            for eachString in date1:
                date2 += eachString
                
            date2 = date2.strip()

            yield {
                'url': response.url,
                'body': body2,
                'title': title2,
                'author': author2,
                'date': date2,
            }
            
            links = response.css('article.news-feed-item h1 a::attr(href)').extract()
            for item in links:
                if item.find("/Sports/") is 0:
                    #print ("\t\t" + item)
                    yield response.follow (item, callback=self.parse)

