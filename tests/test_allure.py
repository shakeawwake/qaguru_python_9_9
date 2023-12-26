import allure
from selene import browser, have, by
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "shakeawwake")
@allure.feature("Issues в репозитории")
@allure.story("Пользователь может просмотреть issue в репо")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page('https://github.com')
    searching_repo('shakeawwake/qaguru_python_9_9')
    going_to_issues()
    check_issue()



@allure.step('Открытие гитхаб {page}')
def open_main_page(page):
    browser.open(page)

@allure.step('Поиск репозитория {repo}')
def searching_repo(repo):
    s(".header-search-button").click()
    s('#query-builder-test').type(repo).press_enter()
    s(by.link_text(repo)).click()

@allure.step('Переход в Issues')
def going_to_issues():
    s("#issues-tab").click()

@allure.step('Проверка наличия нужного Issue')
def check_issue():
    s('#issue_1_link').should(have.exact_text('Test me'))