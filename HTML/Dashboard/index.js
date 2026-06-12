// Dashboard JavaScript

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
        var textScale = slider.value/16;
    });
}
// Toggles between light and dark themes by changing CSS variables
function toggleTheme() {
    const drop = document.getElementById("drpTheme");

    const applyTheme = (theme) => {
        const root = document.documentElement;
        if (theme === "Dark") {
            root.style.setProperty('--background', 'var(--background-dark)');
            root.style.setProperty('--surface', 'var(--surface-dark)');
            root.style.setProperty('--shadow', 'var(--shadow-dark)');
            root.style.setProperty('--text', 'var(--text-dark)');
            root.style.setProperty('--accent', 'var(--accent-dark)');
            root.style.setProperty('--accent-hover', 'var(--accent-hover-dark)');
            root.style.setProperty('--slider-track', 'var(--slider-track-dark)');
            
        } else {
            root.style.setProperty('--background', 'var(--background-light)');
            root.style.setProperty('--surface', 'var(--surface-light)');
            root.style.setProperty('--shadow', 'var(--shadow-light)');
            root.style.setProperty('--text', 'var(--text-light)');
            root.style.setProperty('--accent', 'var(--accent-light)');
            root.style.setProperty('--accent-hover', 'var(--accent-hover-light)');
            root.style.setProperty('--slider-track', 'var(--slider-track-light)');
        }
    };

    if (!drop) return;

    drop.addEventListener("change", () => {
        applyTheme(drop.value);
    });

}

function resetSettings() {
    const btnReset = document.getElementById("btnResetSett");
    btnReset.addEventListener("click", () => {
        // Reset theme to default (Light)
        const drop = document.getElementById("drpTheme");
        drop.value = "Light";
        toggleTheme();


        // Reset font size to default (16px)
        const slider = document.getElementById("sldrFontSize");
        if (slider) {
            slider.value = 16;
            setupFontSize("sldrFontSize", "sampleText");
        }
    });
}

function applySettings() {
    const drop = document.getElementById("drpTheme");
    const slider = document.getElementById("sldrFontSize");
    const btnApply = document.getElementById("btnApplySett");

    btnApply.addEventListener("click", () => {

        document.documentElement.style.setProperty(
            '--base-font-size', 
            `${slider.value}px`);
        
        
    });
}

// Initialize modals and font size slider
setupModal("btnHelp", "modalHelp");
setupModal("btnSettings", "modalSettings");
setupFontSize("sldrFontSize","sampleText");
toggleTheme();
resetSettings();