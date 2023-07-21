baskets ={"apple","banana","apple","gua"}
collections={"apple","pineapple","orange"}


print(collections - baskets)  # letters in  collections but not in baskets

print(baskets-collections)  #letters in baskets but not in collections

print(baskets & collections) # present in both baskets and collections

print(baskets | collections) # present on any one of them 

print(baskets ^ collections)  # present nor any pf thems  