// scripts.js
document.addEventListener('DOMContentLoaded', function () {
    // const aboutUsSection = document.querySelector('.aboutUsSection');
    const servicesSection = document.querySelector('.servicesSection');
    if (servicesSection) {
        function updateParallax() {
            const scrollPosition = window.scrollY;
            const speed = 0.35; // Adjust for parallax speed
            const sectionHeight = servicesSection.offsetHeight;

            // Adjust the starting position by subtracting an offset
            const offset = sectionHeight * 0.5; // Adjust 0.5 to control the offset
            const backgroundPositionY = (scrollPosition * speed - offset) % sectionHeight;

            servicesSection.style.backgroundPosition = `center ${backgroundPositionY}px`;
        }

        window.addEventListener('scroll', updateParallax);
        updateParallax(); // Initial parallax update
    }
    // if (aboutUsSection) {
    //     function updateParallax() {
    //         const scrollPosition = window.scrollY;
    //         const speed = 0.15;
    //         const sectionHeight = aboutUsSection.offsetHeight; // Get the height of the section
    //         const offset = sectionHeight * 0.40; // Adjust 0.5 to control the offset 
    //         const backgroundPositionY = (scrollPosition * speed - offset) % sectionHeight;

    //         aboutUsSection.style.backgroundPosition = `center ${backgroundPositionY}px`;
    //     }

    //     window.addEventListener('scroll', updateParallax);
    //     updateParallax(); // Initial parallax update
    // }
});

// document.addEventListener('wheel', function(event) {
//     event.preventDefault();
  
//     const maxScrollSpeed = 60;
//     const scrollDirection = Math.sign(event.deltaY);
  
//     // Introduce a velocity variable
//     let velocity = scrollDirection * maxScrollSpeed; 
  
//     // Use requestAnimationFrame for smoother animation
//     function updateScroll() {
//       window.scrollBy({
//         top: velocity,
//         behavior: 'smooth' 
//       });
  
//       // Gradually decrease velocity (simulate friction)
//       velocity *= 0.4; // Adjust this value for stronger/weaker deceleration
  
//       // Stop animation when velocity is sufficiently small
//       if (Math.abs(velocity) > 0.5) { 
//         requestAnimationFrame(updateScroll);
//       }
//     }
  
//     requestAnimationFrame(updateScroll);
//   });
// Get the elements
// Get the elements
document.addEventListener('DOMContentLoaded', (event) => {
    const openButton = document.querySelector('.contactUsBox a'); // Select the <a> tag inside .contactUsBox
    const popup = document.getElementById('contact-form-popup');
    const closeButton = document.querySelector('.close-button'); 
    
    // Open the popup
    openButton.onclick = function(event) {
        event.preventDefault(); // Prevent the default link behavior
        popup.style.display = 'block';
        // Fetch the contact form using AJAX (same as before)
        fetch('/contact') 
        .then(response => response.text())
        .then(html => {
            popup.querySelector('.popup-content').innerHTML = html;

            // Add event listener to the close button here
            const closeButton = document.querySelector('.close-button');
            closeButton.onclick = function() {
                popup.style.display = 'none';
            }

        });
    }
    
    
    // Close the popup when clicking outside of it (same as before)
    window.onclick = function(event) {
        if (event.target == popup) {
            popup.style.display = 'none';
        }
    }
});