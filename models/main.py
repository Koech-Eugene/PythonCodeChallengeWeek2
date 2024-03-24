from author import Author
from magazine import Magazine
from articles import Article


# Test cases 
try:
    # Creating an Author instance
    author1 = Author("John Doe")
    print("Author name:", author1.name)  # Testing Author property name
except ValueError as e:
    print("Error creating Author instance:", e)

# Test Magazine class
try:
    # Creating Magazine instances
    magazine1 = Magazine("Tech Review", "Technology")
    magazine2 = Magazine("Science Today", "Science")
    print("Magazine name:", magazine1.name)  # Testing Magazine property name
    print("Magazine category:", magazine1.category)  # Testing Magazine property category
except ValueError as e:
    print("Error creating Magazine instance:", e)

# Test Article class
try:
    # Creating an Author instance
    author2 = Author("Jane Smith")
    # Creating an Article instance
    article1 = Article(author2, magazine1, "The Future of AI")
    print("Article title:", article1.title)  # Testing Article property title
    print("Article author:", article1.author.name)  # Testing Article property author
    print("Article magazine:", article1.magazine.name)  # Testing Article property magazine
except ValueError as e:
    print("Error creating Article instance:", e)

# Testing additional methods and relationships
try:
    # Creating more instances for testing relationships and methods
    article2 = author1.add_article(magazine1, "Artificial Intelligence Trends")
    article3 = author1.add_article(magazine2, "Quantum Computing Breakthroughs")
    article4 = author2.add_article(magazine1, "Machine Learning Applications")

    print("\nAuthor's articles:")
    for article in author1.articles():
        print("-", article.title)

    print("\nAuthor's magazines:")
    for magazine in author1.magazines():
        print("-", magazine.name)

    print("\nMagazine's articles:")
    for article in magazine1.articles():
        print("-", article.title)

    print("\nMagazine's contributing authors:")
    for author in magazine1.contributors():
        print("-", author.name)

    print("\nMagazine's article titles:")
    print("-", magazine1.article_titles())

    print("\nAuthors with more than 2 articles for Magazine:")
    for author in magazine1.contributing_authors():
        print("-", author.name)

    print("\nAuthor's topic areas:")
    print("-", author1.topic_areas())

except ValueError as e:
    print("Error:", e)

# Test top_publisher method
try:
    # Creating more articles for testing
    article5 = author2.add_article(magazine2, "The Evolution of Genetics")
    article6 = author2.add_article(magazine1, "Advancements in Robotics")

    # Finding the top publisher
    top_magazine = Magazine.top_publisher()
    if top_magazine:
        print("\nTop publisher:", top_magazine.name)
    else:
        print("\nNo articles found. Top publisher cannot be determined.")
except ValueError as e:
    print("Error:", e)