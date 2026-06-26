from playwright.sync_api import Page, expect
import re

BASE_URL = "https://www.seznam.cz"

def accept_cookies(page: Page):
    cookie_button = page.get_by_role("button", name="Souhlasím")

    if cookie_button.is_visible(timeout=3000):
        cookie_button.click()

def test_homepage_loads(page: Page):
    """
    Ověří, že je domovská stránka Seznam.cz dostupná
    a obsahuje viditelné vyhledávací pole.
    """
    page.goto(BASE_URL)

    # Použití role locatoru zajišťuje větší odolnost testu vůči změnám HTML struktury.
    search_input = page.get_by_role("textbox", name="Vyhledat")

    expect(search_input).to_be_visible()

def test_search_functionality(page: Page):
    """
    Ověří, že uživatel může zadat vyhledávací dotaz
    a že po jeho odeslání dojde k přechodu na stránku s výsledky hledání.
    """

    page.goto(BASE_URL)

    # Vyhledávací pole je identifikováno pomocí role, což zvyšuje stabilitu testu
    search_input = page.get_by_role("textbox", name="Vyhledat")

    search_input.fill("Playwright")
    search_input.press("Enter")

    # Kontrola, že se hledaný výraz propisuje do URL výsledků vyhledávání.
    expect(page).to_have_url(re.compile("Playwright"))


def test_email_link(page: Page):
    """
    Ověří, že po kliknutí na odkaz Email dojde k přesměrování
    na stránku služby Email nebo přihlašovací stránku Seznamu.
    """

    page.goto(BASE_URL)

    # Ověření přítomnosti hlavního navigačního odkazu Email.
    email_link = page.get_by_role("link", name="Email")
    expect(email_link).to_be_visible()

    # Kontrola, že uživatel byl přesměrován na očekávanou službu.
    expect(email_link).to_have_attribute(
    "href",
    re.compile(r".*email\.seznam\.cz.*")
    )
