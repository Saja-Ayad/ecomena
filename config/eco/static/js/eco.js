// Get the button
let mybutton = document.getElementById('btn-back-to-top');

// When the user scrolls down 1000px from the top of the document, show the button
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 600 || document.documentElement.scrollTop > 600) {
        mybutton.style.display = 'block';
    } else {
        mybutton.style.display = 'none';
    }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener('click', backToTop);

function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
// for menu scroll 
var pageLink = document.querySelectorAll('.page-scroll');

pageLink.forEach(elem => {
    elem.addEventListener('click', e => {
        e.preventDefault();
        document.querySelector(elem.getAttribute('href')).scrollIntoView({
            behavior: 'smooth',
            offsetTop: 1 - 60,
        });
    });
});

// section menu active
function onScroll(event) {
    var sections = document.querySelectorAll('.page-scroll');
    var scrollPos = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;

    for (var i = 0; i < sections.length; i++) {
        var currLink = sections[i];
        var val = currLink.getAttribute('href');
        var refElement = document.querySelector(val);
        var scrollTopMinus = scrollPos + 73;
        if (refElement.offsetTop <= scrollTopMinus && (refElement.offsetTop + refElement.offsetHeight > scrollTopMinus)) {
            document.querySelector('.page-scroll').classList.remove('active');
            currLink.classList.add('active');
        } else {
            currLink.classList.remove('active');
        }
    }
};