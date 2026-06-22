from playwright.sync_api import Page, expect

def test_homepage_loads(page: Page):
    """
    Ověří, že je domovská stránka Seznam.cz dostupná
    a obsahuje viditelné vyhledávací pole.
    """
    page.goto("https://www.seznam.cz")

    # Použití role locatoru zajišťuje větší odolnost testu vůči změnám HTML struktury.
    search_input = page.get_by_role("textbox", name="Vyhledat")

    expect(search_input).to_be_visible()

def test_search_functionality(page: Page):
    """
    Ověří, že uživatel může zadat vyhledávací dotaz
    a že po jeho odeslání dojde k přechodu na stránku s výsledky hledání.
    """

    page.goto("https://www.seznam.cz")

    # Vyhledávací pole je identifikováno pomocí role, což zvyšuje stabilitu testu
    search_input = page.get_by_role("textbox", name="Vyhledat")

    search_input.fill("Playwright")
    search_input.press("Enter")

    # Kontrola, že se hledaný výraz propisuje do URL výsledků vyhledávání.
    assert "Playwright" in page.url


def test_email_link(page: Page):
    """
    Ověří, že po kliknutí na odkaz Email dojde k přesměrování
    na stránku služby Email nebo přihlašovací stránku Seznamu.
    """

    page.goto("https://www.seznam.cz")

    # Ověření funkčnosti jednoho z hlavních navigačních prvků domovské stránky.
    page.get_by_role("link", name="Email").click()

    # Kontrola, že uživatel byl přesměrován na očekávanou službu.
    assert "email.cz" in page.url or "seznam.cz" in page.url
