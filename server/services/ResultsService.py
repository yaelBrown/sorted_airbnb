class ResultsService:
  def createSingleResult():
    pass

  def getNumOfResults(html):
    temp = html.find('<div class="_1h559tl">')
    start = temp + 22
    modhtml = html[start:]
    end = modhtml.find('</div>')

    t2 = html[start:(start+end)]
    t2e1 = t2.find("<span>–</span>")
    t2e2 = t2.find("of")

    return int(t2[(t2e1+15):t2e2])

  def getPhoto(html):
    t1e1 = html.find('<img class="_9ofhsl"')
    t1 = html[t1e1:]
    t2e1 = t1.find('src=')
    t2 = t1[t2e1+5:]

    t2e1 = t2.find('"')
    
    return t2[:t2e1]
    



if __name__ == "__main__":
  # num of results
  nTest = '01&amp;checkout=2021-03-29&amp;search_type=pagination&amp;place_id=ChIJB3UJ2yYAzoURQeheJnYQBlQ&amp;federated_search_session_id=3336acfc-e94a-4084-8af6-a9a9e990f996&amp;items_offset=280&amp;section_offset=2">15</a></li><li class="_i66xk8d"><a aria-label="Next" href="https://www.airbnb.com/s/Mexico-City--Mexico/homes?refinement_paths%5B%5D=%2Fhomes&amp;tab_id=home_tab&amp;checkin=2021-03-01&amp;checkout=2021-03-29&amp;search_type=pagination&amp;place_id=ChIJB3UJ2yYAzoURQeheJnYQBlQ&amp;federated_search_session_id=3336acfc-e94a-4084-8af6-a9a9e990f996&amp;items_offset=20&amp;section_offset=2" class="_1c5c8zn"><span class="_3hmsj"><svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="presentation" focusable="false" style="display: block; fill: none; height: 16px; width: 16px; stroke: currentcolor; stroke-width: 4; overflow: visible;"><g fill="none"><path d="m12 4 11.2928932 11.2928932c.3905243.3905243.3905243 1.0236893 0 1.4142136l-11.2928932 11.2928932"></path></g></svg></span></a></li></ul></nav><div class="_1vk19cb"><div class="_1h559tl">1 <span>–</span> 20 of 300+ places to stay</div></div></div><div class="_p03egf"><div class="_vzrndj">Additional fees apply. Taxes may be added.</div></div></div></div></div><div aria-hidden="false" class="_10v3f8y9"><aside aria-label="Map with interactive pins related to your search" class="_1dagk84" style="height: 100vh; padding-top: 80px; margin-top: -80px; position: sticky; top: 0px;"><div data-veloute="map/GoogleMap" style="position: relative; width: 100%; height: 100%;"><style>'

  nResults = ResultsService.getNumOfResults(nTest)

  # print(nResults)


  # photo
  pTest = '<div class="_1h6n1zu" role="img" aria-busy="false" aria-label="Centro murallas precio emergencia. Estancia larga." style="display: inline-block; vertical-align: bottom; height: 100%; width: 100%; min-height: 1px;"><img class="_9ofhsl" aria-hidden="true" alt="Centro murallas precio emergencia. Estancia larga." src="https://a0.muscache.com/im/pictures/69379915/e5a64367_original.jpg?im_w=720" data-original-uri="https://a0.muscache.com/im/pictures/69379915/e5a64367_original.jpg?im_w=720" style="object-fit: cover; vertical-align: bottom; border-radius: 0px;"><div class="_15p4g025" style="background-image: url(&quot;https://a0.muscache.com/im/pictures/69379915/e5a64367_original.jpg?im_w=720&quot;); background-size: cover; border-radius: 0px;"></div></div>'

  pResults = ResultsService.getPhoto(pTest)

  print(pResults)