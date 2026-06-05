// Sets up a modal with the given button and modal IDs
function setupModal(buttonId, modalId) {
    const button = document.getElementById(buttonId);
    const modal = document.getElementById(modalId);
    const closeBtn = modal.querySelector(".close");

    // Open
    button.addEventListener("click", () => {
        modal.style.display = "block";
    });

    // Close via X
    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });

    // Close via outside click
    modal.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
}

// Sets up a slider to adjust the font size of a text element
function setupFontSize(sliderId, textId) {
    const slider = document.getElementById(sliderId);
    const text = document.getElementById(textId);

    text.style.fontSize = slider.value + "px";

    slider.addEventListener("input", () => {
        text.style.fontSize = slider.value + "px";
    });
}

setupModal("btnHelp", "modalHelp");
setupModal("btnSettings", "modalSettings");
setupFontSize("sldrFontSize","sampleText");