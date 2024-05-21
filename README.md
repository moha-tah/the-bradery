# README

## **What We Are Expecting:**

We are expecting a basic POC (Proof of Concept) that demonstrates your knowledge of different technologies. Don’t spend too much time on minor details. You are allowed to use ChatGPT and any other AIs to assist you.

For the Python script: 
- Fetch data from [this book bank website](https://www.notion.so/https-app-qonto-com-organizations-symmetric-5500-transactions-68a02c4278d641b4a5aea5882b15a43a?pvs=21) and make a simple CRUD script in Python.
- [The API documentation can be found here](https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBookings).

For the Webapp:
- Demonstrate your knowledge of TypeScript, React, NestJS, and Prisma concepts.
- **Everything should be strongly typed.**
- **Dockerize** all services for easy deployment.
- Ensure your code is versioned with Git and follow the [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) guidelines.
- Provide a [README](README.md) file explaining how to start your project.

Make it as simple as possible; a good developer is a developer who makes the easiest choices.

<details>
<summary><strong>Python Section</strong></summary>

### What needs to be done for reading operations:

- Create a SQL database with the provider of your choice.
- Merge the firstname and the lastname into a field named `displayName` and insert it into the table.
- The table should have a primary key that serves as the unique identifier.

### What needs to be done for creation operations:

- Create a new book with the data of your choice (randomly generated or otherwise). Do not hardcode the credentials in the code.
- Once the book is created, fetch the data and insert it into a new table for newly created books.

### What needs to be done for deletion operations:

- Delete the books you created by fetching them from the table.

You can structure your scripts the way you like. Different actions can be run with different command arguments or via different files.

</details>

<details>
<summary><strong>Webapp Section</strong></summary>

### Backend:

- **User authentication**: A basic template is provided in the backend folder. It uses the passport module and the local strategy. You may use the provided code and complete the user implementation. *Don’t spend too much time on creating the user.*
- **Prisma setup**: You must set up a Prisma connection to the database you’ll create.
- **Prisma actions**: You must demonstrate your knowledge of Prisma. This includes performing some CRUD operations, creating and applying migrations, setting up a database schema, etc.
- **Tests (jest)**: You must provide a few tests.
- **API**: Implement either a REST or GraphQL API (GraphQL is a bonus).

### Frontend:

- **UI**: Simple UI with 5 pages (store home page, product page, basket page, login page, orders page).
- **Tests (jest)**: You must provide a few tests.
- **UI library**: We are using **tamagui** to help us create UIs. It can be challenging to set up. If you manage to set it up, great. If not, no worries—use any other UI library of your choice.
- **Products**: You must manage product stocks.
- **Basket**: Users must be able to add and remove products from their basket. Don’t implement a payment system; we assume users have the money to pay for everything.

### Database:

- You can have the database schema and provider you like as long as it works and follows all SQL rules.

### Evaluation Criteria:

- **Code Quality**: This is the most important criterion. Code quality includes readability, maintainability, single responsibility, and (less important) efficiency.
- **Communication**: A good developer knows how to communicate with their team and non-technical members. We expect you to roughly explain your code, the problems you encountered, and how you would explain some concepts to a non-technical person.
- **Documentation or Self-documentation**: Good code is self-documented code. If you think that your code needs some clarification, don’t hesitate to add comments.

If you are not familiar with React, you can use another technology of your choice as long as you can explain your choice.
