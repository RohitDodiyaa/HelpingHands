// Mobile Menu Toggle
document.querySelector('.mobile-menu-toggle').addEventListener('click', function() {
    document.querySelector('.main-nav').classList.toggle('active');
});

// Smooth Scrolling for Anchor Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            e.preventDefault();
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
        // If targetElement does not exist, do not prevent default, so buttons with href="#" work normally
    });
});

// Volunteer Form Submission
const volunteerForm = document.querySelector('.volunteer-form');
if (volunteerForm) {
    volunteerForm.addEventListener('submit', function(e) {
        // You can add form validation here
        console.log('Form submitted');
    });
}
