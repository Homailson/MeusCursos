// When the item is activated by click, if the navList element has
// the nav__list class it will loss it, othewise will gain it
function toggleMenu() {
    var navList = document.getElementById("nav__list");
    if (window.innerWidth < 768) {
        navList.classList.toggle("nav__hidden");
    }
}

// If the screen i reduced to a size smaller than 768px add the class
// nav__hidden to navList element, otherwise remove it
window.addEventListener('resize', function () {
    var navList = document.getElementById("nav__list");
    navList.classList.toggle("nav__hidden", window.innerWidth < 768);
});