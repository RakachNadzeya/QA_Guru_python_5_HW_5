import os
from selene.support import by
from selene import be, have
from selene import browser


def test_fill_out_the_form():
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').type('Nadzeya')
    browser.element('[id="lastName"]').type('Rakach')
    browser.element('[id="userEmail"]').type('test.email@gmail.com')
    browser.element(by.xpath("//*[@id='genterWrapper']//label[.='Female']")).click()
    browser.element('[id="userNumber"]').type('1231231231')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element(by.xpath("//select[@class='react-datepicker__month-select']/option[.='September']")).click()
    browser.element(by.xpath("//option[@value='1988']")).click()
    browser.element(by.xpath("//div[@class='react-datepicker__day react-datepicker__day--020']")).click()
    browser.element(by.xpath("//*[@id='subjectsContainer']//input")).type('English').press_enter()
    browser.element(by.xpath("//label[.='Reading']")).click()
    browser.element('[id="uploadPicture"]').type(os.getcwd() + "/1570735001190494352.jpg")
    browser.element('[id="currentAddress"]').type('Poland, Gdańsk, Wilcza 1')
    browser.element('[id="state"]').click().element(by.xpath("//*[.='Haryana']")).click()
    browser.element('[id="city"]').click().element(by.xpath("//*[.='Karnal']")).click()
    browser.element('[id="submit"]').click()
    browser.element(by.xpath("//div[@class='modal-content']")).should(be.present)
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Nadzeya Rakach', 'Student Email test.email@gmail.com', 'Gender Female', 'Mobile 1231231231',
        'Date of Birth 20 September,1988', 'Subjects English', 'Hobbies Reading', 'Picture 1570735001190494352.jpg',
        'Address Poland, Gdańsk, Wilcza 1', 'State and City Haryana Karnal'))
