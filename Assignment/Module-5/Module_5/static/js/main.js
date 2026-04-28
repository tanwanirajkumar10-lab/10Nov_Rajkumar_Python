document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    
    // Stagger animation delays
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.05}s`;
    });

    // Optional: Subtle parallax effect on hover
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const deltaX = (x - centerX) / centerX;
            const deltaY = (y - centerY) / centerY;
            
            card.style.transform = `translateY(-8px) perspective(1000px) rotateX(${deltaY * -2}deg) rotateY(${deltaX * 2}deg)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0) perspective(1000px) rotateX(0) rotateY(0)';
        });

        // Make entire card clickable
        card.addEventListener('click', (e) => {
            // Check if the click was directly on an <a> tag
            const clickedLink = e.target.closest('a');
            
            // If the user clicked a link directly, let the browser handle it
            if (clickedLink) return;

            // Otherwise, find the first link in the card
            const firstLink = card.querySelector('a');
            if (firstLink) {
                console.log(`Card clicked! Redirecting to: ${firstLink.href}`);
                window.location.assign(firstLink.href);
            }
        });
    });
});
