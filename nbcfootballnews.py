import scrapy

class NbcfootballnewsSpider(scrapy.Spider):
    name = "nbcfootballnews"
    allowed_domains = ['profootballtalk.nbcsports.com']
    start_urls = [
        'https://profootballtalk.nbcsports.com/2018/12/01/colts-already-strong-offensive-line-gets-joe-haeg-back/',
        'https://profootballtalk.nbcsports.com/2018/12/01/josh-adams-pops-on-on-eagles-injury-report/',
        'https://profootballtalk.nbcsports.com/2018/12/01/colin-kaepernick-supporters-plan-to-rock-the-probowlvote/',
        'https://profootballtalk.nbcsports.com/2018/12/01/will-someone-claim-kareem-hunt-on-waivers/',
        'https://profootballtalk.nbcsports.com/2018/12/01/cowboys-address-mystery-man-on-saints-sideline/',
        'https://profootballtalk.nbcsports.com/2018/12/01/nfl-may-have-overcorrected-post-ezekiel-elliott/',
        'https://profootballtalk.nbcsports.com/2018/12/01/nfl-fines-shaq-lawson-33425-for-fight-with-leonard-fournette/',
        'https://profootballtalk.nbcsports.com/2018/12/01/bears-downgrades-dont-include-trubisky/',
        'https://profootballtalk.nbcsports.com/2018/12/01/dolphins-extend-nick-oleary-through-2019/',
        'https://profootballtalk.nbcsports.com/2018/12/01/packers-ceo-im-not-ready-to-give-up-on-the-season/',
        'https://profootballtalk.nbcsports.com/2018/11/30/week-13-injury-report-roundup-6/',
        'https://profootballtalk.nbcsports.com/2018/11/30/nfl-still-needs-real-time-video-official/',
        'https://profootballtalk.nbcsports.com/2018/11/30/nfc-playoff-picture-cowboys-win-boosts-the-rams/',
        'https://profootballtalk.nbcsports.com/2018/11/29/pfts-week-13-picks-9/',
        'https://profootballtalk.nbcsports.com/2018/11/28/saints-rams-and-chiefs-can-clinch-playoff-berths-this-week/',      
    ]
    global visited_url
    visited_url = set()

    def parse(self, response):
        global visited_url
        if response.url not in visited_url:
            visited_url.add(response.url)
            # write code to process the items.
            body1 = response.css('div.entry-content p *::text').extract()
            body2 = ''
            
            for eachString in body1:
                body2 += eachString
            

            title1 = response.css('h1.entry-title::text').extract()
            title2 = ''

            for eachString in title1:
                title2 += eachString

            title2 = title2.strip()


            author1 = response.css('span.byline::text').extract()
            author2 = ''

            for eachString in author1:
                author2 += eachString

            author2 = author2.strip()

       
            date1 = response.css('span.entry-date::text').extract()
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
            links = response.css('   ').extract()
            for item in links:
                if item.find("   ") is 0:
                    yield response.follow (item, callback=self.parse)
           `'''

