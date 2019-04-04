from selenium import webdriver
import re, time, csv
def getCharList(xpathId):
    charList = []
    for chars in map(lambda x: x.get_attribute('innerHTML'), driver.find_elements_by_xpath('//*[@id="descripton' + xpathId + 'Span"]/ul/li')):
        i = chars.index(' ')
        char = chars[i + 1:]
        if char == 'babies': char = 'baby'
        elif char[-1] == 's': char = char[:-1]
        elif char[-3:] == 'men': char = char[:-3] + 'man'
        elif char == 'homeless people': char = 'homeless person'
        charList.append((int(chars[:i]), char))
    return charList
def addWeights(charList, jaywalk, passenger):
    weight = 0
    for char in charList:
        productWeight = char[0]*charWeight[char[1]]
        if jaywalk and char[0] not in ['dog', 'cat']: weight += 0.291920196*productWeight
        else: weight += productWeight
    if passenger: weight *= 5.976440283
    return weight
driver, charWeight, side, floutText, passengerText, writer = webdriver.Chrome(), {'man': 1, 'woman': 1, 'pregnant woman': 1, 'baby': 2.255379727, 'elderly man': 0.09317147, 'elderly woman': 0.09317147, 'boy': 5.660293394, 'girl': 5.660293394, 'homeless person': 0.561489098, 'large woman': 0.106958749, 'large man': 0.106958749, 'criminal': 0.211613543, 'male executive': 1.117429247, 'female executive': 1.117429247, 'female athlete': 50.03391293, 'male athlete': 50.03391293, 'female doctor': 11.1128903, 'male doctor': 11.1128903, 'dog': 0.432911022, 'cat': 0.300093252}, ['left', 'right'], 'Note that the affected pedestrians are flouting the law by crossing on the red signal.', 'In this case, the self-driving car with sudden brake failure will swerve and crash into a concrete barrier.', csv.writer(open('mmresults.csv', 'w', newline = ''))
driver.get('http://moralmachine.mit.edu/')
driver.find_element_by_xpath('//*[@id="langen"]').click()
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
driver.find_element_by_xpath('//*[@id="play"]').click()
while True:
    for i in range(13):
        while True:
            try:
                for s in side: driver.find_element_by_xpath('//*[@id="' + s + 'button"]').click()
                break
            except: time.sleep(1)
        descripton = list(map(lambda x: driver.find_element_by_xpath('//*[@id="descripton' + x + 'Span"]').get_attribute('innerHTML'), side))
        charList, jaywalk, passenger = list(map(list, [map(getCharList, side), map(lambda x: True if re.search('<\/ul>(.*)', descripton[x]).group(1) == floutText else False, range(2)), map(lambda x: True if re.search('(.*) This will result in', descripton[x]).group(1) == passengerText else False, range(2))]))
        weight = list(map(lambda x: addWeights(charList[x], jaywalk[x], passenger[x]), range(2)))
        if weight[1] > weight[0]: driver.find_element_by_xpath('//*[@id="canvas_images0"]').click()
        else: driver.find_element_by_xpath('//*[@id="canvas_images1"]').click()
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="noSurvey"]').click()
            break
        except:
            if driver.find_elements_by_xpath('//*[@id="yesSurvey"]'): break
            else: time.sleep(1)
    writer.writerow([''] + [re.search('xlink:href="http:\/\/avgame.s3-accelerate\.amazonaws\.com\/images\/results\/all\/(.*)_walking\.svg"', driver.find_element_by_xpath('//*[@id="most' + superlative + '"]').get_attribute('innerHTML')).group(1) for superlative in ['Saved', 'Killed']])
    j = 0
    for row in list(zip(*[list(map(lambda x: float(re.search('x="(\d+\.?\d+)"', x.get_attribute('outerHTML')).group(1)), driver.find_elements_by_xpath('//*[@class="results-pip-' + resultsPip + '"]'))) for resultsPip in ['you', 'others']])):
        writer.writerow((j,) + row)
        j += 1
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    for optout in ['', 'tryagain']: driver.find_element_by_xpath('//*[@id="' + optout + 'optout"]').click()
