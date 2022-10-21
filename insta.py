from asyncio import wait_for
from socket import setdefaulttimeout
from textwrap import fill
from xml.sax.xmlreader import Locator
import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from time import sleep
import os
from app.lib.lib import sortUserAgent


cls = os.system('cls')

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False,
                                timeout=0)
    context = navegador.new_context(color_scheme='dark')
    sortUserAgent()
    pagina = context.new_page()
    pagina.goto('https://www.instagram.com/', wait_until='networkidle')

    # sleep(2)
    # pagina.locator(
    #     'xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').fill('instagram')
    # sleep(2)
    # pagina.keyboard.press('Enter')
    # sleep(2)
    # pagina.locator(
    #     'xpath=//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3').click()
    pagina.locator(
        'xpath=//*[@id="loginForm"]/div/div[1]/div/label/input').fill('chrys481@gmail.com')
    pagina.locator(
        'xpath=//*[@id="loginForm"]/div/div[2]/div/label/input').fill('chrys200402')
    pagina.keyboard.press('Enter')
    pagina.locator('button:has-text("Agora não")').click()
    pagina.locator('button:has-text("Agora não")').click()
    pagina.locator('span:has-text("Pesquisar")').click()
    pagina.keyboard.insert_text('imcahu')
    sleep(3)
    pagina.keyboard.press('Enter')
    pagina.keyboard.press('Enter')
    sleep(5)
    pagina.locator('button:has-text("Seguir")').click()
    sleep(5)
    #t= pagina.locator('role="link":has-text"\imcahu\"').click()
    sleep(5)

    navegador.close()