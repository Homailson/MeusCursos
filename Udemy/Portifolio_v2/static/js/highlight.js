document.addEventListener("DOMContentLoaded", function () {
    highlightCurrentSection();
});

function highlightCurrentSection() {
    var currentSection = getCurrentSection();

    if (currentSection) {
        var navbarLinks = document.querySelectorAll('.navbar__list__item');
        navbarLinks.forEach(function (link) {
            link.classList.remove('navbar__active__link');
        });

        var currentSectionId = currentSection.id;

        var activeLink = document.querySelector('a[href="#' + currentSectionId + '"]');
        if (activeLink) {
            activeLink.classList.add('navbar__active__link');
        }
    }
}
