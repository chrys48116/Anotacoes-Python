from os import link
from random import random, randrange
from unicodedata import name
from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep
from app.lib.lib import delay, sortUserAgent

delay(8)
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.instagram.com/")

#------------------------------------------------------------------------------
#Parte de login no Instagram
#------------------------------------------------------------------------------
    page.get_by_label("Telefone, nome de usuário ou email").click()
    sleep(2)
    login = page.get_by_label("Telefone, nome de usuário ou email").fill("chrys481@gmail.com")
    sleep(1)
    page.get_by_label("Telefone, nome de usuário ou email").press("Tab")
    sleep(1)
    psw = page.get_by_label("Senha").fill("chrys200402")
    sleep(1)
    page.get_by_label("Senha").press("Enter")
    sleep(2)
    page.wait_for_url("https://www.instagram.com/accounts/onetap/?next=%2F")
    page.goto("https://www.instagram.com/accounts/onetap/?next=%2F")
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#Pop-ups
#------------------------------------------------------------------------------
    page.get_by_role("button", name="Agora não").click()
    page.wait_for_url("https://www.instagram.com/")
    page.get_by_role("button", name="Agora não").click()
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#Entranado na lista de amigos
#------------------------------------------------------------------------------
    for i in range(3):
        pessoas=[]
        scroll = randrange(1000)
        page.get_by_role("link", name="chrystian_artur").click()
        page.wait_for_url("https://www.instagram.com/chrystian_artur/")

        seguindo = page.locator('text=seguindo').click()
        page.wait_for_url("https://www.instagram.com/chrystian_artur/following/")

        sleep(1)
        nth = 0
        page.locator('role=dialog').nth(1).hover()
        sleep(1)
        for i in range(3):
            page.mouse.wheel(0, scroll)
            nth += 30

        page.get_by_role('link').nth(randrange(1,90,2))
        # page.mouse.dblclick(540, 300)
        pessoa = page.locator('h2').inner_text()
        print(pessoa)
        sleep(4)
        # page.wait_for_url("https://www.instagram.com/sassijulia/")

        page.locator('text=seguidores').click()
        sleep(4)

        page.locator('role=dialog').nth(1).hover()
        sleep(1)
        page.mouse.wheel(0, scroll)

        page.mouse.dblclick(540, 300)
        sleep(4)
        # page.wait_for_url("https://www.instagram.com/sassijulia/following/")
#------------------------------------------------------------------------------
#Voltando a lista de amigos
#------------------------------------------------------------------------------
        page.go_back()
        page.go_back()
        page.go_back()
        page.goto("https://www.instagram.com/chrystian_artur/")
#------------------------------------------------------------------------------
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
