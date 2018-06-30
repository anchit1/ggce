tippy('#about-header', {
  html: '#about-header-menu',
  arrow: true,
  interactive: true,
  interactiveBorder: 2,
  placement: 'bottom',
  theme: 'dropdown',
});

tippy('#courses-header', {
  html: '#courses-header-menu',
  arrow: true,
  interactive: true,
  interactiveBorder: 2,
  placement: 'bottom',
  theme: 'dropdown',
});


// modifies the header on scoll
window.onscroll = () => {
  myFunction();
}

const header = document.getElementById('header2-container');
const sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > 10) {
    header.classList.add('sticky');
  } else {
    header.classList.remove('sticky');
  }
}

// Add a spacer at the top of the page that is equal to the header height
addSpacer();
window.addEventListener('load', () => {
  window.addEventListener('resize', addSpacer);
  console.log(typeof(document.getElementById('header-nav-container').scrollHeight))
});


function addSpacer() {
  const header = document.getElementById('header-nav-container').scrollHeight;
  document.getElementById('spacer').style.height = (header-1) + 'px';
}

// Displays the location of the college in google maps
function initMap() {
  const ggce = { lat: 23.127263, lng: 79.876509};
  const map = new google.maps.Map(
    document.getElementById('map'), { zoom: 15, center: ggce }
  );
  const marker = new google.maps.Marker({position: ggce, map: map});
}