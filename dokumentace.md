# 3 Automatizované testy
## Testovací Dokumentace

***Autor:*** Barbora Poláková

***Popis:*** Projekt obsahuje automatizované UI testy webové stránky Seznam.cz vytvořené pomocí frameworku Playwright v Pythonu.

***Použité technologie:***
- Python 3.x
- Playwright
- pytest
- pytest-playwright

***Tetstovací prostředí:***
- Notebook Asus
- Operační systém Linux

## Testovací scénáře

***TC001:*** Dostupnost stránky
- Cíl: Načtení domovské stránky a zobrazení vyhledávacího pole.
- Očekávaný výsledek: Stránka se bez problému načte a zobrazí se vyhledávací pole.
- Poznámky: Test ověřuje zda je stránka Seznam.cz dostupná a zobrazuje se vyhledávací pole. Neověřuje obsah stránky ani funkčnost vyhledávání.

***TC002:*** Hlavní funkcionalita vyhledávání
- Cíl: Ověření že uživatel může zadat vyhledávací dotaz a zobrazí se výsledek vyhledávání.
- Testovací data: "Playwright"
- Očekávaný výsledek: Po odeslání dotazu se stránka načte s výsledky.
- Poznámky: k ověření fukčnosti vyhledávání používá test dotaz "Playwright" a kontrola probíhá pomocí URL.

***TC003:*** Navigace na službu Email
- Cíl: Ověřit funkčnost odkazu Email na domovské stránce.
- Očekávaný výsledek: Po kliknutí na odkaz Email je uživatel přesměrován na službu Email nebo přihlašovací stránku Seznamu.
- Poznámky: Test ověřuje funkčnost odkazu Email na domovské stránce.

## Tabulka testovacích scénářů


| ID testu | Název testu | Cíl testu | Očekávaný výsledek |
|----------|-------------|-----------|--------------------|
| TC01 | Dostupnost stránky | Načtení domovské stránky a zobrazení vyhledávacího pole. | Stránka se bez problému načte a zobrazí se vyhledávací pole. |
| TC02 | Hlavní funkcionalita vyhledávání | Ověření že uživatel může zadat vyhledávací dotaz a zobrazí se výsledek vyhledávání.| Po odeslání dotazu se stránka načte s výsledky. |
| TC03 | Navigace na službu Email | Ověřit funkčnost odkazu Email na domovské stránce. | Po kliknutí na odkaz Email je uživatel přesměrován na službu Email nebo přihlašovací stránku Seznamu.|


