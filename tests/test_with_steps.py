import allure
from selene import browser, have, by
from selene.support.shared.jquery_style import s

def test_with_steps():
    with allure.step("Открытие гитхаб"):
        browser.open("https://github.com")

    with allure.step("Поиск репозитория"):
        s(".header-search-button").click()
        s('#query-builder-test').type("shakeawwake/qaguru_python_9_9").press_enter()

    with allure.step("Переход по ссылке"):
        s(by.link_text("shakeawwake/qaguru_python_9_9")).click()

    with allure.step("Открытие вкладки Issues"):
        s("#issues-tab").click()

    with allure.step("Проверка наличия нужного Issue"):
        s('#issue_1_link').should(have.exact_text('Test me'))