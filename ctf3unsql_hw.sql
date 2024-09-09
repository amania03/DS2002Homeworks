#1easyquestion
SELECT name FROM country WHERE continent = 'South America';
#2easyquestion
SELECT population FROM country WHERE name = 'Germany';
#3easyquestion
SELECT name FROM city WHERE countrycode = (SELECT code FROM country WHERE name = 'Japan');
#4easyquestion
SELECT name, population FROM country WHERE continent = 'Africa' ORDER BY population DESC LIMIT 3;
#5easyquestion
SELECT name, lifeExpectancy FROM country WHERE population BETWEEN 1000000 AND 5000000;
#6mediumquestion
SELECT country.name FROM country JOIN countrylanguage ON country.code = countrylanguage.countrycode WHERE countrylanguage.language = 'French' AND countrylanguage.isofficial = 'T';
#7easyquestion
SELECT Album.Title FROM Album JOIN Artist ON Album.ArtistId = Artist.ArtistId WHERE Artist.Name = 'AC/DC';
#8easyquestion
SELECT FirstName, LastName, Email FROM Customer WHERE Country = 'Brazil';
#9easyquestion
SELECT Name FROM Playlist;
#10mediumquestion
SELECT Name FROM Playlist; SELECT COUNT(*) AS TotalTracks FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId WHERE Genre.Name = 'Rock';
#11mediumquestion
SELECT e.FirstName, e.LastName FROM Employee e JOIN Employee m ON e.ReportsTo = m.EmployeeId WHERE m.FirstName = 'Nancy' AND m.LastName = 'Edwards';
#mediumquestion12
SELECT c.FirstName, c.LastName, SUM(i.Total) AS TotalSales FROM Invoice i JOIN Customer c ON i.CustomerId = c.CustomerId GROUP BY c.FirstName, c.LastName ORDER BY TotalSales DESC;







#CreateProductstable
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Description TEXT,  -- Description of the product (e.g., ingredients, cultural significance)
    ProductType VARCHAR(50),  -- e.g., Makeup, Skincare
    Price DECIMAL(10, 2),
    Stock INT
);

#CreateCustomerTable
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100)
);

#CreateOrdersTable
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    OrderDate DATE,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

#InsertDataIntoProductsTable
INSERT INTO Products (ProductID, ProductName, Description, ProductType, Price, Stock) VALUES
(1, 'Kohl', 'Traditional eye makeup used across the Middle East, made with finely ground lead sulfide', 'Makeup', 12.99, 100),
(2, 'Moroccan Rouge', 'A vibrant lip and cheek stain made from natural pigments, popular in Moroccan beauty routines', 'Makeup', 14.50, 50),
(3, 'Argan Oil', 'Rich moisturizing oil extracted from the kernels of argan trees, native to Morocco', 'Skincare', 25.00, 80),
(4, 'Rosewater Mist', 'A hydrating facial mist infused with rose petals, commonly used in Middle Eastern skincare', 'Skincare', 18.00, 40),
(5, 'Henna Powder', 'Natural henna powder used for body art and hair treatments, derived from the henna plant', 'Bodycare', 10.00, 60);

#InsertDataIntoCustomersTable
INSERT INTO Customers (CustomerID, FirstName, LastName, Email) VALUES
(1, 'Amani', 'Akkoub', 'amani@gmail.com'),
(2, 'Fatima', 'Hassan', 'fatima.hassan@gmail.com'),
(3, 'Layla', 'Ali', 'layla.ali@gmail.com'),
(4, 'Zahra', 'Karim', 'zahra.karim@gmail.com'),
(5, 'Yasmin', 'Nasser', 'yasmin.nasser@gmail.com');

#InsertDataIntoOrdersTable
INSERT INTO Orders (OrderID, CustomerID, ProductID, OrderDate, Quantity) VALUES
(1, 1, 1, '2024-09-01', 2),
(2, 2, 3, '2024-09-02', 1),
(3, 3, 2, '2024-09-03', 3),
(4, 4, 4, '2024-09-03', 1),
(5, 5, 5, '2024-09-04', 1);

#querie1ListProductsAndStockLevels
SELECT ProductName, ProductType, Stock 
FROM Products;

#querie2FindOrdersMadeFromSpecificCustomer
SELECT Orders.OrderID, Products.ProductName, Orders.Quantity, Orders.OrderDate
FROM Orders
JOIN Products ON Orders.ProductID = Products.ProductID
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE Customers.FirstName = 'Amani' AND Customers.LastName = 'Akkoub';


#querie3GetTotalRevenuePerCustomer
SELECT Customers.FirstName, Customers.LastName, SUM(Orders.Quantity * Products.Price) AS TotalSpent
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
JOIN Products ON Orders.ProductID = Products.ProductID
GROUP BY Customers.FirstName, Customers.LastName;

# SQLQueriesDevelopedWithAssistanceFromChatGPTandPart1OfHW
