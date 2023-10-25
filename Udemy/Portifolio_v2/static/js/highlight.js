document.addEventListener("DOMContentLoaded", function () {
    highlightCurrentSection();
});

function highlightCurrentSection() {
    var currentSection = getCurrentSection();

    if (currentSection) {
        var sidebarLinks = document.querySelectorAll('.sidebar__list__item');
        sidebarLinks.forEach(function (link) {
            link.classList.remove('sidebar__active__link');
        });

        var currentSectionId = currentSection.id;

        var activeLink = document.querySelector('a[href="#' + currentSectionId + '"]');
        if (activeLink) {
            activeLink.classList.add('sidebar__active__link');
        }
    }
}
