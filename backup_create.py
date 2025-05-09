import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto('https://develop.cespdev.mss.bi.zone/')
    context = await browser.new_context()
    await page.locator("[data-test-id=\"login-login\"]").click()
    await page.locator("[data-test-id=\"login-login\"]").fill("admin")
    await page.locator("[data-test-id=\"login-password\"]").click()
    await page.locator("[data-test-id=\"login-password\"]").fill("admin")
    await page.locator("[data-test-id=\"login-submit\"]").click()
    await page.get_by_role("link", name="Система").click()
    await page.locator("[data-test-id=\"System-button-create\"]").click()
    await page.locator("[data-test-id=\"System-input-create-backup\"]").click()
    await page.locator("[data-test-id=\"System-input-create-backup\"]").fill("123123123123132")
    async with page.expect_download() as download_info:
        await page.locator("[data-test-id=\"System-button-create-modal\"]").click()
    download = await download_info.value

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())