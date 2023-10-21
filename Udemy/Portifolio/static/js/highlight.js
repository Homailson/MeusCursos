function highlightCurrentSection() {
    var currentSection = getCurrentSection();

    if (currentSection) {               
        var sidebarLinks = document.querySelectorAll('.sidebar__item');
        sidebarLinks.forEach(function (link) {
            link.classList.remove('active-link');
        });
        
        var currentSectionId = currentSection.id;
                        
        var activeLink = document.querySelector('a[href="#' + currentSectionId + '"]');
        if (activeLink) {
            activeLink.classList.add('active-link');
        }
    }
}
