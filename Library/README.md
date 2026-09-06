# library

This is a simple package that stores the title of the book and name of the author for you.

## How to install library:


```

pip install personal_library

```


## Here is how to load the package:

```python
from library_script import library

lib = library()

lib.add_book("Harry Potter and The Chamber of Secrets", "J.K Rowling")
lib.show_book()
```

## You can also store these books in a txt file and view them:

```python

file_name = "example.txt"
lib.save(file_name)
lib.load(file_name)
```

###### Note that the package only supports english titles  as of the current release.
