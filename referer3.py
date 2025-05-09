from playwright.sync_api import sync_playwright

def login_and_navigate(page):
    # Переход на страницу
    page.goto("https://u3.cespdev.mss.bi.zone/login")

    # Заполнение формы логина
    page.locator("[data-test-id='login-login']").fill("admin")
    page.locator("[data-test-id='login-password']").fill("admin")

    # Нажатие кнопки отправки формы
    page.locator("[data-test-id='login-submit']").click()
    page.get_by_role("link", name="Журнал сообщений").click()

    # Выбор первого элемента и раскрытие боковой панели
    page.locator("[data-test-id=\"\\30 \"]").click()  # Возможно, это ID для первого элемента
    page.locator("[data-test-id='messages-grid-side-bar-expand-button']").click()

def pick_button_1(page):
    # Нажатие первой кнопки
    page.locator("[data-test-id='virustotal-copy-block-button']").first.click()
    pop_up(page, "[data-test-id='messages-grid-side-bar-accordion-block-messages-grid-side-bar-general-section'] [data-test-id='Popover-virus-button']")

def pick_button_2(page):
    # Нажатие второй кнопки
    page.locator("[data-test-id=\"virustotal-copy-block-button\"]").nth(2).click()
    pop_up(page, "[data-test-id='messages-grid-side-bar-accordion-block-messages-grid-side-bar-smtpCheck-section'] [data-test-id='Popover-virus-button']")

def pick_button_3(page):
    # Нажатие третьей кнопки
    page.locator("[data-test-id=\"copy-block-virus-button\"]").first.click()
    pop_up(page, "[data-test-id=\"copy-block-virus-button\']")

#def pick_button_4(page):
    # Нажатие четвертой кнопки
    #page.locator(".CopyContainer-sc-1rlf97d-0 > button").first.click()
   # pop_up(page, "[data-test-id='messages-grid-side-bar-accordion-block-messages-grid-side-bar-smtpCheck-section'] [data-test-id='Popover-virus-button']")

def pop_up(page, popup_selector):
    # Ожидание появления элемента
    page.locator(popup_selector).wait_for(timeout=60000)  # Ждем до 60 секунд

    # Ожидание появления всплывающего окна
    with page.expect_popup(timeout=60000) as page1_info:  # Увеличиваем таймаут
        page.locator(popup_selector).click()  # Открытие ссылки

    # Получение новой страницы (VirusTotal)
    page1 = page1_info.value

    # Перехват запросов на новой странице
    def check_referer_header(request):
        print(f"Request Headers: {request.headers}")

    # Подписываемся на событие "request" для проверки заголовков
    page1.on("request", check_referer_header)

    # Ждем загрузки страницы VirusTotal
    page1.wait_for_load_state("networkidle")
    print("Проверка referer для всплывающего окна завершена")

def test_example(page):
    # Логин и навигация
    login_and_navigate(page)

    # Тестирование каждой кнопки
    pick_button_1(page)
    pick_button_2(page)
    pick_button_3(page)
    #pick_button_4(page)

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