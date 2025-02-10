document.getElementById("method").addEventListener("change", function () {
    const method = this.value;
    document.getElementById("userIdInput").style.display = method === "Content" ? "none" : "block";
    document.getElementById("titleInput").style.display = method === "CF" ? "none" : "block";
});

document.getElementById("recommendationForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const method = document.getElementById("method").value;
    const userId = document.getElementById("userId").value;
    const title = document.getElementById("title").value;

    fetch("/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ method, userId, title }),
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "<h2>Recommendations:</h2>";
        data.forEach(movie => {
            console.log(movie);
            resultsDiv.innerHTML += `<p>${movie.Title} (${movie.Genres})</p>`;
        });
    });
});