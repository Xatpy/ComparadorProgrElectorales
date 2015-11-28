from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.delete_all_cookies()

    url = "http://unpaiscontigo.es/programa/"
    driver.get(url)
    time.sleep(5)
    listResults = driver.find_elements_by_xpath('//h4')

    if listResults:
        print "writing results"
        with open('propuestasPodemos.txt','w+') as f:
            for result in listResults:
                f.write(result.text.encode('utf8') + '\n')
        print "end"