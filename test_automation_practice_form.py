from selene import browser
from selene.support import by
from selene import be



def test_precondition():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.set_window_size(1400, 1500)


def test_fill_out_the_form():
    browser.element('[id="firstName"]').type('Nadzeya')
    browser.element('[id="lastName"]').type('Rakach')
    browser.element('[id="userEmail"]').type('test.email@gmail.com')
    browser.element(by.css('#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(2)')).click()
    browser.element('[id="userNumber"]').type('1231231231')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element(by.xpath("//select[@class='react-datepicker__month-select']/option[.='September']")).click()
    browser.element(by.xpath("//option[@value='1988']")).click()
    browser.element(by.xpath("//div[@class='react-datepicker__day react-datepicker__day--020']")).click()
    browser.element(by.xpath("//*[@id='subjectsContainer']//input")).type('Test subject')
    browser.element(by.xpath("//label[.='Reading']")).click()
    browser.element('[id="currentAddress"]').type('Random text')
    browser.element('[id="state"]').click().element(by.xpath("//*[.='Haryana']")).click()
    browser.element('[id="city"]').click().element(by.xpath("//*[.='Karnal']")).click()
    browser.element('[id="submit"]').click()
    browser.element(by.xpath("//div[@class='modal-content']")).should(be.present)





