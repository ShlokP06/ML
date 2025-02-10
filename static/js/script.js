document.getElementById('recommendationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const user_id = document.getElementById('user_id').value;
    const title = document.getElementById('title').value;

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: user_id, title: title }),
    })
    .then(response => response.json())
    .then(data => {
        const recommendationsList = document.getElementById('recommendations-list');
        recommendationsList.innerHTML = ''; // Clear previous recommendations
        data.forEach(movie => {
            const movieElement = document.createElement('li');
            movieElement.textContent = movie;
            recommendationsList.appendChild(movieElement);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
