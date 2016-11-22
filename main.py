import analytics
import uuid
import random as r
import time
import fixtures
from faker import Faker
import sys
fake = Faker()
analytics.write_key = sys.argv[1]
print "Source WriteKey = " + analytics.write_key
user_agent_list = ['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.7.01001)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.5.01003)','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0','Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8','Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko/20100101 Firefox/11.0','Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.0.3705)','Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0.1','Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)','Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)','Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1','Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1','Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.02 Bork-edition [en]'] 
events = ['identify', 'track', 'page']


# Start loop here...
while True:
  time.sleep(r.randint(0,5))
  event = r.choice(events)
  print "Sending " + event.title() + " event"
  page = None
  payload = {
    'user_id': str(uuid.uuid4()),
    'anonymous_id': str(uuid.uuid4())
  }

  ##############
  # Track Event
  ##############
  if (event == 'track'):
    track_events = ['Purchased Subscription', 'Shared Article', 'Visited Social Media', 'Commented on Article']

    # Get event name
    event_name = r.choice(track_events)

    # analytics.track args:
      # user_id
      # event
      # properties
      # context
      # anonymous_id 

    payload['event'] = event_name
    
    # Check to see if the event is a 'Subscription'.
    # If so, return the 'Subscription' page
    if (event_name == 'Purchased Subscription'):
      page = (item for item in fixtures.pages if item["category"] == "Subscription").next()
    elif (event_name == 'Shared Article' or event == 'Commented on Article'):
      page = (item for item in fixtures.pages if item["name"] == "Article").next()
    else:
      page = r.choice(fixtures.pages)

    payload['properties'] = fixtures.event_props[event_name]
    payload['context'] = page['context']

    analytics.track(
      user_id=payload['user_id'],
      event=payload['event'],
      properties=payload['properties'],
      context=payload['context'],
      anonymous_id=payload['anonymous_id']
    )

  ##############
  # Identify Event
  ##############
  if (event == 'identify'):
    # Set page equal to the Subscription page
    page = (item for item in fixtures.pages if item["category"] == "Subscription").next()

    # Load properties
    payload['traits'] = {
      'email': fake.email(),
      'name': fake.name(),
      'state': fake.state(),
      'city': fake.city()
    }

    payload['context'] = page['context']

    analytics.identify(
      user_id=payload['user_id'],
      traits=payload['traits'],
      context=payload['context'],
      anonymous_id=payload['anonymous_id']
    )
    

  ##############
  # Page Event
  ##############
  if (event == 'page'):
    page = r.choice(fixtures.pages)

    analytics.page(
      user_id=payload['user_id'], 
      category=page['category'], 
      name=page['name'], 
      properties=page['properties'], 
      context=page['context'],
      anonymous_id=payload['anonymous_id']
    )
  print "Success!"