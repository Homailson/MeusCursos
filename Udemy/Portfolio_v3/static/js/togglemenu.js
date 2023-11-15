function toggleMenu() {
    var navList = document.getElementById("nav__list");
    if (window.innerWidth <= 540) {
        if (navList.classList.contains('nav__hidden')) {
            navList.classList.remove('nav__hidden');
        } else {
            navList.classList.add('nav__hidden');
        }

        // Adiciona/remove uma classe para controlar a visibilidade
        document.body.classList.toggle('menu-visible');
        
        // Dispara manualmente o evento de rolagem após abrir ou fechar o menu
        var event = new Event('scroll');
        window.dispatchEvent(event);
    }
}


