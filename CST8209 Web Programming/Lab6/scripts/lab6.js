//lab6 JavaScript file

book1 = {
    author: "William Shakespeare",
    title: "The Tempest",
    genre: "Historical Fiction"
};

book2 = {
    author: "Stephen King",
    title: "The Shining",
    genre: "Horror"
};

book3 = {
    author: "Anne Frank",
    title: "The Diary of Anne Frank",
    genre: "Non-Fiction"
};

book = {
    title: '',
    author: '',
    genre: ''
};

function addBooks(bookArray) {
     var bookTitle = prompt("Enter in a title");
     var bookAuthor = prompt("Enter in a Author");
     var bookGenre = prompt("Enter in a Genre");

     bookArray.push({title:bookTitle , author:bookAuthor, genre:bookGenre});
     return bookArray;
}

function displayRecomendations (bookArray){
    var bookList = document.getElementById("bookList");
    for (i=0; i < bookArray.length; i++){
      var h2 = document.createElement("h2");
      var ulEle = document.createElement("ul");
      var liEle = document.createElement("li");
      var bookText = document.createTextNode(bookArray[i].title + "," + " Written By: "
       + bookArray[i].author + "," + " Genre: " + bookArray[i].genre);

      bookList.appendChild(h2);
      h2.innerHTML = "Book: " + (i+ 1);
      h2.appendChild(ulEle);
      ulEle.appendChild(liEle);
      liEle.appendChild(bookText);
    }
}

var bookArray = new Array();
bookArray[0] = book1;
bookArray[1] = book2;
bookArray[2] = book3;

for (var i = 3; i <= 5; i++) {
    addBooks(bookArray);
}
displayRecomendations(bookArray);
