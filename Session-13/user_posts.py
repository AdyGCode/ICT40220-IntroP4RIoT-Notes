from datetime import datetime
import time


class User:
    def __init__(self, name, email):
        self.username = name
        self.email = email
        self.posts = []

    def create_post(self, title, content):
        post = Post(title, content)
        self.posts.append(post)

    def show_posts(self):
        for post in self.posts:
            post.display_post()


class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.timestamp = datetime.now()

    def display_post(self):
        date_and_time = self.timestamp.strftime("%H:%M:%S %d %b, %Y")
        print(f"Title: {self.title} at {date_and_time}")
        print(f"Content: {self.content}")
        print()


def main():
    user_bob = User("Bob", "bob@example.com")
    user_felicia = User("Felicia", "felicia@example.com")

    user_felicia.create_post("Test Post", "Blah!")
    time.sleep(1)
    user_bob.create_post(
        "Bob Jokes", "A man with no arms and no legs in a swimming pool."
    )
    time.sleep(2)
    user_felicia.create_post("Test Post", "Blah! Blah!")

    user_felicia.show_posts()
    user_bob.show_posts()


if __name__ == "__main__":
    main()
