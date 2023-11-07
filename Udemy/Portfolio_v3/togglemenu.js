document.addEventListener('DOMContentLoaded', function () {
    const menuIcon = document.querySelector('.menu-icon');
    const navList = document.querySelector('.nav__list');

    menuIcon.addEventListener('click', function () {
        if (window.innerWidth <= 768) {
            navList.style.display = (navList.style.display === 'none' || navList.style.display === '') ? 'block' : 'none';
        }
    });

    const navLinks = document.querySelectorAll('.nav__list a');
    navLinks.forEach(function (link) {
        link.addEventListener('click', function () {
            if (window.innerWidth <= 768) {
                navList.style.display = 'none';
            }
        });
    });
});
