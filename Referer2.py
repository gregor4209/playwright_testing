from playwright.sync_api import sync_playwright
import time

def login_and_navigate(page):
    # Переход на страницу
    page.goto("https://u3.cespdev.mss.bi.zone/login")

    # Заполнение формы логина
    page.locator("[data-test-id='login-login']").fill("admin")
    page.locator("[data-test-id='login-password']").fill("admin")

    # Нажатие кнопки отправки формы
    page.locator("[data-test-id='login-submit']").click()
    page.get_by_role("link", name="Журнал сообщений").click()
    page.locator("[data-test-id=\"complexFilter-selector-btn\"]").click()
    page.get_by_text("Добавить условие").click()
    page.locator("xpath=/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]/button").click()
    print("НАшел")
    page.locator("xpath=/html/body/div[4]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/button").is_visible()
    page.locator(
        "xpath=/html/body/div[4]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/button").is_visible()
    print("НАшел")
    # time.sleep(300)
    #page.get_by_text("Параметр").click()
    print("НАшел")
    time.sleep(300)
    # Выбираем значение из выпадающего списка
    select_element.select_option("Количество вложений").is_visible
    page.get_by_text("Количество вложений").click()
    page.get_by_role("button", name="= равно").click()
    page.locator("[data-test-id=\"gte-select-input-content\"]").click()
    page.locator("[data-test-id=\"complexFilter-input-component-number\"]").click()
    page.locator("[data-test-id=\"complexFilter-input-component-number\"]").fill("1")
    page.locator("[data-test-id=\"condition-add-NaWIV6dIo4Zwq16k5hTy1\"]").click()
    page.locator("[data-test-id=\"YKJ5F5qsgYIofOT25m1LB-select-input\"]").click()
    page.locator("[data-test-id=\"urls_count-node\"]").click()
    page.get_by_role("button", name="= равно").click()
    page.locator("[data-test-id=\"gte-node\"] [data-test-id=\"gte-select-input-content\"]").click()
    page.locator("div").filter(has_text=re.compile(r"^ИКоличество ссылок≥ больше или равно$")).locator(
        "[data-test-id=\"complexFilter-input-component-number\"]").click()
    page.locator("div").filter(has_text=re.compile(r"^ИКоличество ссылок≥ больше или равно$")).locator(
        "[data-test-id=\"complexFilter-input-component-number\"]").fill("1")
    page.locator("[data-test-id=\"complexFilter-apply-btn\"]").click()

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
    page.locator(".VirustotalContainer-sc-1dnvydz-6 > .sc-bypJrT").first.click()
    pop_up(page, "[data-test-id='messages-grid-side-bar-accordion-block-messages-grid-side-bar-general-section'] [data-test-id='Popover-virus-button']")

def pick_button_4(page):
    # Нажатие четвертой кнопки
    page.locator(".CopyContainer-sc-1rlf97d-0 > button").first.click()
    pop_up(page, "[data-test-id='messages-grid-side-bar-accordion-block-messages-grid-side-bar-smtpCheck-section'] [data-test-id='Popover-virus-button']")

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
    pick_button_4(page)

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