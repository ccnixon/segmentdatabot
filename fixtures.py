import random as r

user_agent_list = ['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.7.01001)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.5.01003)','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0','Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8','Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko/20100101 Firefox/11.0','Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.0.3705)','Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0.1','Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)','Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)','Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1','Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1','Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.02 Bork-edition [en]'] 

event_props = {
  'Visited Social Media': {
    'site': r.choice(['Instagram', 'Facebook', 'YouTube', 'Twitter'])
  },

  'Shared Article': {
    'media': r.choice(['Twitter', 'Facebook', 'Email'])
  },

  'Purchased Subscription': {
    'plan': r.choice(['Digital', 'Print', 'All Access'])
  },

  'Commented on Article': {}
}

pages = [
  {
    'category': '',
    'name': 'Home',
    'context': {
      'page': {
        'path': '/', 
        'title': 'PEOPLE.com | Celebrity News, Exclusives, Photos, and Videos', 
        'url': 'http://people.com/'
      },
      'ip': '69.91.163.173',
      'userAgent': r.choice(user_agent_list)
    },
    'properties': {
      'path': '/',
      'referrer': '',
      'search': '',
      'title': 'PEOPLE.com | Celebrity News, Exclusives, Photos, and Videos',
      'url': 'http://people.com/'
    }
  },
  {
    'category': 'Subscription',
    'name': '',
    'context': {
      'page': {
        'path': 'storefront/subscribe-to-people', 
        'title': 'Special Offer from PEOPLE Magazine!', 
        'url': 'https://subscription.people.com/storefront/subscribe-to-people/site/pe-chop384nextgenrcboxlp0216.html'
      },
      'ip': '69.91.163.173',
      'userAgent': r.choice(user_agent_list)
    },
    'properties': {
      'path': 'storefront/subscribe-to-people',
      'referrer': '',
      'search': '',
      'title': 'Special Offer from PEOPLE Magazine!',
      'url': 'https://subscription.people.com/storefront/subscribe-to-people/site/pe-chop384nextgenrcboxlp0216.html'
    }
  },
  {
    'category': 'TV',
    'name': 'Article',
    'author': 'Jordan Runtagh',
    'context': {
      'page': {
        'path': 'tv/kim-kardashian-west-dream-kardashian-first-visit/', 
        'title': 'Kim Kardashian Has Already Met Her Niece Dream Kardashian: Source', 
        'url': 'http://people.com/tv/kim-kardashian-west-dream-kardashian-first-visit/'
      },
      'userAgent': r.choice(user_agent_list),
      'ip': '69.91.163.173'
    },
    'properties': {
      'path': 'tv/kim-kardashian-west-dream-kardashian-first-visit/',
      'referrer': '',
      'search': '',
      'title': 'Kim Kardashian Has Already Met Her Niece Dream Kardashian: Source',
      'url': 'http://people.com/tv/kim-kardashian-west-dream-kardashian-first-visit/'
    }
  },
  {
    'category': 'Sports',
    'name': 'Article',
    'author': 'Gerald Green',
    'context': {
      'page': {
        'path': 'sports/steph-curry-trades-autographed-jerseys-with-leukemia-patient/', 
        'title': 'Steph Curry Gives Signed Jersey to Boy with Leukemia', 
        'url': 'http://people.com/sports/steph-curry-trades-autographed-jerseys-with-leukemia-patient/'
      },
      'userAgent': r.choice(user_agent_list),
      'ip': '69.91.163.173'
    },
    'properties': {
      'path': 'tv/kim-kardashian-west-dream-kardashian-first-visit/',
      'referrer': '',
      'search': '',
      'title': 'Kim Kardashian Has Already Met Her Niece Dream Kardashian: Source',
      'url': 'http://people.com/tv/kim-kardashian-west-dream-kardashian-first-visit/'
    }
  },
  {
    'category': 'Music',
    'name': 'Article',
    'author': 'Chris Nixon',
    'context': {
      'page': {
        'path': 'music/amas-2016-kylie-jenner-dog-bambi-labor/', 
        'title': 'AMAs 2016: Why Kylie Jenner Didn\'t Attend the AMAs', 
        'url': 'http://people.com/music/amas-2016-kylie-jenner-dog-bambi-labor/'
      },
      'userAgent': r.choice(user_agent_list),
      'ip': '69.91.163.173'
    },
    'properties': {
      'path': 'music/amas-2016-kylie-jenner-dog-bambi-labor/',
      'referrer': '',
      'search': '',
      'title': 'AMAs 2016: Why Kylie Jenner Didn\'t Attend the AMAs',
      'url': 'http://people.com/music/amas-2016-kylie-jenner-dog-bambi-labor/'
    }
  }
]