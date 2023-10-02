const champinones = [
    { name: "Vit flugsvamp", description: "Beskrivning:vit, rund, gift", image: "static/pics/vit_flugsvamp.jpg" },
    { name: "Lömsk flugsvamp", description: "Beskrivning:rund, lång", image: "static/pics/lomsk_flugsvamp.jpg"  },
    // Lägg till fler champijoner här. 
];

function displayChampinones(champinonesToDisplay) {
    const champinonesList = document.getElementById("champinonesList");
    champinonesList.innerHTML = ""; // Rengöra över listan 

    champinonesToDisplay.forEach(champinon => {
        const champinonDiv = document.createElement("div");
        champinonDiv.innerHTML = `
            <h2>${champinon.name}</h2>
            <img src="${champinon.image}" alt="${champinon.name}" />
            <p>${champinon.description}</p>
        `;
        champinonesList.appendChild(champinonDiv);
    });
}

function search() {
    const searchInput = document.getElementById("searchInput").value.toLowerCase();
    const filteredChampinones = champinones.filter(champinon => champinon.description.toLowerCase().includes(searchInput));
    displayChampinones(filteredChampinones);
}

// Ladda upp champijoner-bilder när man laddar sidan. 
displayChampinones(champinones);
