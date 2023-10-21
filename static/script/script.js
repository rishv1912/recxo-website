 // Get references to the mobile menu toggle button and the mobile menu element
 const mobileMenuToggle = document.getElementById("menu-toggle");
 const mobileMenu = document.getElementById("mobile-menu");
 
 // Add a click event listener to the mobile menu toggle button
 mobileMenuToggle.addEventListener("click", function () {
   // Toggle the "active" class on the mobile menu element
   mobileMenu.classList.toggle("active");
 });
 