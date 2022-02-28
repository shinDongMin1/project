const tooglebtn = document.querySelector(".navbar-tooglebtn");
const main_menu = document.querySelector(".main-menu");
const sub_menu = document.querySelector(".sub-menu");

tooglebtn.addEventListener('click', () => {
    main_menu.classList.toggle('active');
    sub_menu.classList.toggle('active');
});