from django.shortcuts import render, redirect, get_object_or_404
from .models import RevisionBook, CartItem
from studentrequest.models import Subject

"""This function creates the view for the store index page; right now it is kept basic as it is not final which filter/query features 
will make it to the final version"""

def books(request):
    """
     query = request.GET.get('query','')
    """

    """
    subject_id = request.GET.get('subject_id',0)
    """
    subjects = Subject.objects.all()
    books = RevisionBook.objects.all()
    """
    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    """
    
    return render(request, 'store/bookindex.html',{
        'revisionbooks': books,
        #'query': query,
        'subject' : subjects,
        #'category_id': int(category_id)
    })

def bookdetail(request, pk):
    item = get_object_or_404(RevisionBook, pk=pk)
    related_items = RevisionBook.objects.filter(category=item.subject).all()
    return render(request, 'books/bookdetail.html', {
        'revisionbook': item,
        'related_revisionbooks': related_items
    })


"""
# enumerate all the books
def book_list(request):
    revisionbook = RevisionBook.objects.all()
    return render(request, 'frontpage/bookindex.html', {'revisionbook': revisionbook})
 
# view the books currently in the cart  
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'frontpage/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, book_id):
    product = RevisionBook.objects.get(id=book_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')

"""








