class Article:
    def __init__(self, title, author, char_count, publication, description):
        self.title = title
        self.author = author
        self.char_count = char_count
        self.publication = publication
        self.description = description

    def get_info(self):
        return {
            "title": self.title,
            "author": self.author,
            "char_count": self.char_count,
            "publication": self.publication,
            "description": self.description,
        }

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_char_count(self, char_count):
        self.char_count = char_count

    def set_publication(self, publication):
        self.publication = publication

    def set_description(self, description):
        self.description = description


class ArticleView:
    def display_article(self, article_info):
        print("Article Information:")
        print(f"Title: {article_info['title']}")
        print(f"Author: {article_info['author']}")
        print(f"Character Count: {article_info['char_count']}")
        print(f"Publication: {article_info['publication']}")
        print(f"Description: {article_info['description']}")
        print()


class ArticleController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_article_title(self, title):
        self.model.set_title(title)

    def set_article_author(self, author):
        self.model.set_author(author)

    def set_article_char_count(self, char_count):
        self.model.set_char_count(char_count)

    def set_article_publication(self, publication):
        self.model.set_publication(publication)

    def set_article_description(self, description):
        self.model.set_description(description)

    def update_view(self):
        article_info = self.model.get_info()
        self.view.display_article(article_info)


if __name__ == "__main__":
    # Создание модели
    article = Article(
        "Использование наблюдателя состояния в задачах гидролокаци",
        "Бублей Ирина Евгеньевна",
        3648,
        "Известия Южного федерального университета. Технические науки.",
        "В работе рассмотрен подход использования наблюдателя состояния для аналитического синтеза "
        "системы управления и обработки информации в прикладных задачах гидролокации",
    )

    # Создание представления
    view = ArticleView()

    # Создание контроллера
    controller = ArticleController(article, view)

    # Отображение статьи
    controller.update_view()

    # Изменение названия статьи через контроллер
    controller.set_article_title("Использование наблюдателя состояния")

    # Обновление представления после изменения данных
    controller.update_view()
