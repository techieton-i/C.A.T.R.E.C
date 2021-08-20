const menuBtn = document.querySelector(".menu-btn");
const hamBurger = document.querySelector('.menu-btn_burger');
const nav = document.querySelector('.r-nav');
const menuNav = document.querySelector('.nav');


let showMenu = false;

menuBtn.addEventListener('click', () => {
    if(!showMenu){
        hamBurger.classList.add('open');
        nav.classList.add('open');
        menuNav.classList.add('open');

        showMenu = true;
    }else{
        hamBurger.classList.remove('open');
        nav.classList.remove('open');
        menuNav.classList.remove('open');


        showMenu = false;
    }
});