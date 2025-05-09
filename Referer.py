from playwright.sync_api import sync_playwright


def test_example(page):
    # Переход на страницу
    page.goto("https://u3.cespdev.mss.bi.zone/login")
    page.locator("[data-test-id='login-login']").fill("admin")
    page.locator("[data-test-id='login-password']").fill("admin")
    page.locator("[data-test-id='login-submit']").click()
    page.get_by_role("link", name="Журнал сообщений").click()
    page.locator("[data-test-id=\"\\30 \"]").click()  # Возможно, это ID для первого элемента
    page.locator("[data-test-id='messages-grid-side-bar-expand-button']").click()
    #Первая часть кода. Дальше мы нажимаем на кнопку и выбираем поп-ап

    #Это кнопки, их мы по очереди подставляем в функцию test_example(page)
    def PickButton()
    page.locator("[data-test-id='virustotal-copy-block-button']").first.click()
    page.locator("[data-test-id=\"virustotal-copy-block-button\"]").nth(2).click()
    page.locator(".VirustotalContainer-sc-1dnvydz-6 > .sc-bypJrT").first.click()
    page.locator(".CopyContainer-sc-1rlf97d-0 > button").first.click()

    #После того, как мы выполнили test_example(page) c одной из кнопок def PickButton(), мы с этой кнопкой открываем попап следующей функцией и
    def PopUp(page):
    with page.expect_popup() as page1_info:
        page.locator("[data-test-id='Popover-virus-button']").click()  # Открытие ссылки
    # Получение новой страницы (VirusTotal)
    page1 = page1_info.value
    # Перехват запросов на новой странице

    def check_referer_header(request):
        print(f"Request Headers: {request.headers}")
    page1.on("request", check_referer_header)
    page1.wait_for_load_state("networkidle")


def run(playwright):
    # Запуск браузера
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Вызов функции теста
    test_example(page)

    # Закрытие браузера
    context.close()
    browser.close()


# Запуск скрипта
with sync_playwright() as playwright:
    run(playwright)
