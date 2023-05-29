bookstore_cost_price = 24.95 * 0.6
books = 60
book_cost_price = bookstore_cost_price * books
wholesale_cost_price = book_cost_price + 3 + (0.75*(books-1))
print (f"{wholesale_cost_price:.2f}")