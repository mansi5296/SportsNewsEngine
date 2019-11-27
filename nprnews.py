import scrapy

class NprnewsSpider(scrapy.Spider):
    name = "nprnews"
    allowed_domains = ['www.npr.org']
    start_urls = [
        'https://www.npr.org/2018/10/30/662120808/klay-thompson-breaks-nbas-3-point-record-held-by-teammate-stephen-curry',
        'https://www.npr.org/2018/11/17/668582123/not-my-job-we-quiz-orlando-magic-star-aaron-gordon-on-actual-magic',
        'https://www.npr.org/2018/11/14/667936235/suzy-whaley-pga-of-americas-first-female-president-outlines-her-vision-for-golf',
        'https://www.npr.org/2018/11/05/664578266/usa-gymnastics-dumped-as-organizers-of-olympic-athletes-after-sexual-abuse-scand',
        'https://www.npr.org/2018/11/05/664232524/no-athletes-will-not-shut-up-and-dribble-and-they-never-have',
        'https://www.npr.org/2018/11/04/664215594/kenyas-mary-keitany-and-lelisa-desisa-of-ethiopia-win-new-york-city-marathon',
        'https://www.npr.org/2018/11/02/663594281/nfl-cheerleader-kneels-during-national-anthem',
        'https://www.npr.org/2018/10/31/662801623/hall-of-fame-slugger-willie-mccovey-dies-at-age-80',
        'https://www.npr.org/2018/10/31/662757630/u-of-maryland-says-it-will-part-ways-with-head-football-coach-dj-durkin',
        'https://www.npr.org/2018/10/30/662271054/after-players-death-u-of-maryland-president-will-retire-but-football-coach-remai',
        'https://www.npr.org/2018/11/28/671488865/that-s-how-i-found-out-i-was-dead-soccer-club-fakes-player-s-demise-poorly',
    ]
    global visited_url
    visited_url = set()

    def parse(self, response):
        global visited_url
        if response.url not in visited_url:
            visited_url.add(response.url)
            # write code to process the items.
            body1 = response.css('div.storytext p::text').extract()
            body2 = ''
            
            for eachString in body1:
                body2 += eachString
            

            title1 = response.css('div.storytitle h1::text').extract()
            title2 = ''

            for eachString in title1:
                title2 += eachString

            title2 = title2.strip()


            author1 = response.css('div.byline p *::text').extract()
            author2 = ''

            for eachString in author1:
                author2 += eachString

            author2 = author2.strip()

       
            date1 = response.css('div.dateblock span::text').extract()
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
            '''
            links = response.css(' ').extract()
            for item in links:
                if item.find(" ") is 0:
                    yield response.follow (item, callback=self.parse)
            '''

