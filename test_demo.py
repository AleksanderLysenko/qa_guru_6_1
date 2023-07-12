from selene import be
from selene.support.shared import browser


def test_hard():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id=firstName]').type('Alex')
    browser.element('[id=lastName]').type('Lys')
    browser.element('[id=userEmail]').type('example@yandex.ru')
    browser.element('.custom-radio [for=gender-radio-1]').click()
    browser.element('[id=userNumber]').type('1234567890')
    browser.element('[id=dateOfBirthInput]').click()
    browser.element('[class="react-datepicker__year-select"]').click().type("1992").click()
    browser.element('[class="react-datepicker__month-select"]').click().type("January").click()
    browser.element('[aria-label="Choose Sunday, January 5th, 1992"]').click()
    browser.element('[id=subjectsInput]').type('economics').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[id=currentAddress]').type('godovikova 9')
    browser.element('[id=react-select-3-input]').type('NCR').press_enter()
    browser.element('[id=react-select-4-input]').type('Merrut').press_enter()
    browser.element('[id=submit]').should(be.visible).press_enter()
    browser.element('[id=closeLargeModal]').press_enter()