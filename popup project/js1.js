var popupoverlay = document.querySelector(".popup-overlay");
var popupbox = document.querySelector(".popup-box");
var addpopupbtn = document.getElementById("add-popup-btn");

addpopupbtn.addEventListener("click", function() {
    popupoverlay.style.display = "block";
    popupbox.style.display = "block";
});

// Selecting cancel button
var cancelpopup = document.getElementById("cancel-popup");
cancelpopup.addEventListener("click", function(event) {
    event.preventDefault();
    popupoverlay.style.display = "none";
    popupbox.style.display = "none";
});

// Select container, add-book, book-title-input, book-author-input, book-description-input
var container = document.querySelector(".container");
var addbook = document.getElementById("add-book");
var booktitleinput = document.getElementById("Book-title-input");
var bookauthorinput = document.getElementById("Book-author-input");
var bookdescriptioninput = document.getElementById("Book-description");

addbook.addEventListener("click", function(event) {
    event.preventDefault();
    var div = document.createElement("div");
    div.setAttribute("class", "bookcontainer");
    div.innerHTML = `
        <h2>${booktitleinput.value}</h2>
        <h5>${bookauthorinput.value}</h5>
        <p>${bookdescriptioninput.value}</p>
        <button class="delete-book">Delete</button>
    `;
    
    // Append the new book container to the main container
    container.append(div);

    // Add an event listener to the new delete button
    var deleteBtn = div.querySelector(".delete-book");
    deleteBtn.addEventListener("click", function() {
        div.remove();
    });

    // Clear input fields
    booktitleinput.value = "";
    bookauthorinput.value = "";
    bookdescriptioninput.value = "";

    // Hide popup
    popupoverlay.style.display = "none";
    popupbox.style.display = "none";
});
