let nav;
let mobileNav, mobileNavButton, mobileNavClose;

nav = document.querySelector('.nav');
navDropdown = document.querySelector('.nav__dropdown');
navMenu = document.querySelector(".nav__menu");


mobileNav = document.querySelector(".mobile-nav");
mobileNav.appendChild(navMenu.cloneNode(true));
mobileNavButton = document.querySelector(".nav__menu-button");
mobileNavClose = document.querySelector(".mobile-nav__close");
let mobileNavMenu = mobileNav.children[1];




mobileNavButton.addEventListener("click", ()=>{
    mobileNav.style.zIndex = 11;
    mobileNav.style.backgroundColor = "rgba(14, 27, 49, 0.7)";
    mobileNavButton.style.opacity = 0;
    mobileNavMenu.classList.add('mobile-menu__active');
});



mobileNavClose.addEventListener("click",()=>{
    mobileNav.style.zIndex = -10;
    mobileNavButton.style.opacity = 1;
    mobileNavMenu.classList.remove('mobile-menu__active');
});

// let navDropdown;
// navDropdown = document.querySelector('.nav__dropdown');
// console.log(navDropdown);

console.log(navDropdown);

window.addEventListener("scroll",()=>{
    navDropdown.classList.toggle('nav__dropdown--theme',window.scrollY > 0);
    nav.classList.toggle('nav--sticky',window.scrollY > 0);
    mobileNavClose.classList.toggle('mobile-nav__sticky',window.scrollY > 0);
});

// ===================end mobile menu==================== 

// password validation ===============


// password validation end===============



// =============comunity page ===============



// ===============end community page===============
