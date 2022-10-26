

class TestPage:

    def test_open_page(self, open_google):
        google_page = open_google
        searching_text = 'Think24.ru'
        searching_page = google_page.search_and_open_searching_page(searching_text)
        assert searching_text.lower() in searching_page.current_url, 'Открыта не та страница'
