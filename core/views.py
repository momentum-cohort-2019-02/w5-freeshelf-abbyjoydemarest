from django.shortcuts import render
from core.models import Book, Author, Category

# Create your views here.
def index(request):
    """View for the index(homepage) of the project. """
    #Count all of each model so we can use them moving forward
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_categories = Category.object.all().count()

    #tell it how to provide in the information each section of the dictionary is used for a different reaseon.
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_categories': num_categories,
    }

    return render(request, 'index.html', context=context)
