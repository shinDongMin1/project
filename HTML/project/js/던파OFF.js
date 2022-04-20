const tooglebtn = document.querySelector('.navbar-tooglebtn');
const menu = document.querySelector('.navbar-menu');
const icon = document.querySelector('.navbar-icon');

tooglebtn.addEventListener('click', () => {
	menu.classList.toggle('active');
	icon.classList.toggle('active'); 
});