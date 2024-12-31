# Book Management System

This project is a Django-based system for managing books, authors, categories, and user favorites. It provides models to store and interact with book-related data, including categories, authors, and user interactions like favoriting books.

## Features

- **Category Management**: Organize books into categories with optional descriptions.
- **Author Management**: Add and manage authors of books.
- **Book Management**: Store information about books, including:
  - Title
  - Author
  - PDF upload
  - Description
  - Publication date
  - Cover image upload
  - Category association
  - Download count tracking
- **Favorites**: Allow users to mark books as their favorites. A user can only favorite a book once.

## Models Overview

### Category
- `name`: Name of the category.
- `description`: Optional description of the category.

### Author
- `name`: Name of the author.

### Book
- `title`: Title of the book.
- `author`: ForeignKey linking to the `Author` model.
- `pdfLink`: FileField for uploading the book's PDF.
- `description`: Optional description of the book.
- `publicationDate`: Date of publication.
- `coverImage`: ImageField for uploading the book's cover.
- `category`: ForeignKey linking to the `Category` model.
- `download_count`: IntegerField to track downloads (default is 0).

### Favorite
- `user`: ForeignKey linking to the `CustomUser` model.
- `book`: ForeignKey linking to the `Book` model.
- Unique constraint ensures a user can only favorite a book once.
