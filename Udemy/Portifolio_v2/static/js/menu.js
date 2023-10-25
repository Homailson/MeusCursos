function toggleMenu() {
    var navbarList = document.querySelector('.navbar__list');
    navbarList.classList.toggle('show-menu');
}

function closeMenu() {
    var navbarList = document.querySelector('.navbar__list');
    navbarList.classList.remove('show-menu');
}

window.addEventListener('resize', function () {
    var navbarList = document.querySelector('.navbar__list');
    if (window.innerWidth > 1020) {
        navbarList.classList.remove('show-menu');
    }


    var currentSection = getCurrentSection();
    if (currentSection) {
        currentSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
});

function getCurrentSection() {
    var sections = document.querySelectorAll('section');
    var closestSection = null;
    var closestDistance = Infinity;

    sections.forEach(function (section) {
        var rect = section.getBoundingClientRect();
        var distance = Math.abs(rect.top);

        if (distance < closestDistance) {
            closestDistance = distance;
            closestSection = section;
        }
    });

    return closestSection;
}