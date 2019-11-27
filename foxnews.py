import scrapy

class FoxnewsSpider(scrapy.Spider):
    name = "foxnews"
    allowed_domains = ['www.foxnews.com']
    start_urls = [
        'https://www.foxnews.com/sports/kansas-city-chiefs-release-kareem-hunt-after-video-shows-him-pushing-kicking-a-woman',
        'https://www.foxnews.com/sports/former-patriots-tight-end-aaron-hernandez-blasted-coach-bill-belichick-for-lack-of-support',
        'https://www.foxnews.com/sports/patrick-corbins-family-tries-to-influence-free-agent-pitcher-to-sign-with-star-studded-team',
        'https://www.foxnews.com/sports/nba-star-stephen-curry-helps-rectify-girls-issue-with-signature-sneaker',
        'https://www.foxnews.com/sports/former-nfl-player-uses-lowest-point-of-his-life-to-propel-him-toward-incredible-feat',
        'https://www.foxnews.com/sports/john-cena-to-be-honored-with-muhammad-ali-legacy-award',
        'https://www.foxnews.com/sports/purdue-football-coachs-high-school-alma-mater-receives-threat-after-his-decision-to-stay-at-school',
        'https://www.foxnews.com/sports/nfl-network-reporter-kimberly-jones-leaves-hospital-after-health-scare-the-surgeons-saved-my-life',
        'https://www.foxnews.com/sports/kent-state-basketball-recruit-becomes-first-player-with-autism-to-join-division-1-school',
        'https://www.foxnews.com/sports/european-soccer-fans-left-bloodied-after-violent-rivals-throw-petrol-bombs-and-flares-into-the-stands',
        'https://www.foxnews.com/sports/irish-soccer-club-apologizes-after-falsely-reporting-players-death',
        'https://www.foxnews.com/sports/loyola-chicago-honors-sister-jean-with-her-own-final-four-ring',
    ]
    global visited_url
    visited_url = set()

    def parse(self, response):
        global visited_url
        if response.url not in visited_url:
            visited_url.add(response.url)
            #print ("\t" + response.url)
            # write code to process the items.
            body1 = response.css('div.article-body p::text').extract()
            body2 = ''
            
            for eachString in body1:
                body2 += eachString
            

            title1 = response.css('div.caption p::text').extract()
            title2 = ''

            for eachString in title1:
                title2 += eachString

            title2 = title2.strip()


            author1 = response.css('div.author-byline span span a::text').extract()
            author2 = ''

            for eachString in author1:
                author2 += eachString

            author2 = author2.strip()

       
            date1 = response.css('div.article-date time::text').extract()
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
            
            links = response.css('div.m a::attr(href)').extract()
            for item in links:
                if item.find("https://www.foxnews.com/sports/") is 0:
                    #print ("\t\t" + item)
                    yield response.follow (item, callback=self.parse)


