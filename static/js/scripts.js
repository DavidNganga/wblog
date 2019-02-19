const carouselSlide = document.querySelector('.carousel-slide');
const carouselImages = document.querySelectorAll('.carousel-slide image');

//Buttons
const prevBtn = document.querySelector('#prevBtn');
const nextBtn = document.querySelector('#nextBtn');


//counter
let Counter = 1;
const size = carouselImages[0].clientwidth;

carouselSlide.style.transform = 'translateX('+(-size * counter)+ 'px)';

//Button Listeners
nextBtn.adddEventListener('click',()=>{
  carouselSlide.style.transition = "transform 0.4s ease-in-out"
  counter++;

});
