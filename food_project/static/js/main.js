document.addEventListener('DOMContentLoaded', function() {
    function food_club() {
        const userName = prompt("Welcome to the Food Club! Please enter your name:");
        if (userName) {
            alert(`Thank you, ${userName}, for joining the Food Club! Stay tuned for delicious updates.`);
        } else {
            alert("You did not enter a name. Please try again to join the Food Club.");
        }
    }
    const joinButton = document.getElementById('join-food-club');
    if (joinButton) {
        joinButton.addEventListener('click', food_club);
    }

    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        alert('Thank you for your donation!');
    });
});
